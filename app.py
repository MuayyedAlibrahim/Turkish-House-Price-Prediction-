import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Sayfa yapılandırması
st.set_page_config(
    page_title="Türk Ev Fiyat Tahmini",
    page_icon="🏠",
    layout="wide"
)

# Başlık ve açıklama
st.title("Türk Ev Fiyat Tahmini Projesi")
st.markdown("Bu uygulama, Türkiye'deki ev fiyatlarını tahmin etmek için makine öğrenmesi modelini kullanmaktadır.")

# Veri yükleme fonksiyonu
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('processed_turkish_house_sales.csv')
        return df
    except Exception as e:
        st.error(f"Veri yüklenirken hata oluştu: {e}")
        return None

# Model eğitme fonksiyonu
@st.cache_resource
def train_model(df):
    # Oda sayısını sayısala çevir
    def parse_oda_sayisi(oda_str):
        try:
            return sum([float(x) for x in str(oda_str).split("+")])
        except:
            return None
    
    df["Oda_Sayisi"] = df["Oda_Sayisi"].apply(parse_oda_sayisi)
    
    # Eksik verileri temizle
    df.dropna(subset=["Metrekare", "Oda_Sayisi", "il", "Ilce", "fiyat"], inplace=True)
    
    # Tarih sütununu kaldır (eğer varsa)
    if "Tarih" in df.columns:
        df = df.drop(columns=["Tarih"])
    
    # Özellikleri ve hedef değişkeni seç
    X = df[["Metrekare", "Oda_Sayisi", "il", "Ilce", "Mahalle", "satici_tip"]]
    y = df["fiyat"]
    
    # Kategorik değişkenleri sayısallaştır
    X = pd.get_dummies(X, columns=["il", "Ilce", "Mahalle", "satici_tip"], drop_first=True)
    
    # Sadece sayısal kolonları ölçekle
    scaler = StandardScaler()
    X_scaled = X.copy()
    X_scaled[["Metrekare", "Oda_Sayisi"]] = scaler.fit_transform(X[["Metrekare", "Oda_Sayisi"]])
    
    # Modeli oluştur ve eğit
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)
    
    return model, scaler, X.columns, df

# Veriyi yükle
df = load_data()

if df is not None:
    # Yan panel için benzersiz değerleri al
    iller = sorted(df["il"].unique())
    
    # Model eğitimi
    with st.spinner("Model eğitiliyor..."):
        model, scaler, columns, processed_df = train_model(df)
    
    # Yan panel oluştur
    st.sidebar.header("Ev Özellikleri")
    
    # Satıcı tipi seçimi
    satici_tip = st.sidebar.selectbox(
        "Satıcı Tipi",
        options=sorted(df["satici_tip"].unique()),
        index=0
    )
    
    # İl seçimi
    selected_il = st.sidebar.selectbox(
        "İl",
        options=iller,
        index=0
    )
    
    # Seçilen ile göre ilçeleri filtrele
    ilceler = sorted(df[df["il"] == selected_il]["Ilce"].unique())
    selected_ilce = st.sidebar.selectbox(
        "İlçe",
        options=ilceler,
        index=0
    )
    
    # Seçilen ilçeye göre mahalleleri filtrele
    mahalleler = sorted(df[(df["il"] == selected_il) & (df["Ilce"] == selected_ilce)]["Mahalle"].unique())
    selected_mahalle = st.sidebar.selectbox(
        "Mahalle",
        options=mahalleler,
        index=0
    )
    
    # Metrekare ve oda sayısı girişi
    metrekare = st.sidebar.number_input(
        "Metrekare",
        min_value=30,
        max_value=500,
        value=100,
        step=1
    )
    
    oda_sayisi = st.sidebar.number_input(
        "Oda Sayısı",
        min_value=1.0,
        max_value=10.0,
        value=3.0,
        step=0.5
    )
    
    # Tahmin butonu
    if st.sidebar.button("Fiyat Tahmini Yap"):
        # Yeni veri oluştur
        new_data = pd.DataFrame({
            "satici_tip": [satici_tip],
            "Metrekare": [metrekare],
            "Oda_Sayisi": [oda_sayisi],
            "il": [selected_il],
            "Ilce": [selected_ilce],
            "Mahalle": [selected_mahalle]
        })
        
        # One-hot encoding uygula
        new_data_encoded = pd.get_dummies(new_data, columns=["il", "Ilce", "Mahalle", "satici_tip"], drop_first=True)
        
        # Eksik sütunları ekle
        for col in columns:
            if col not in new_data_encoded.columns:
                new_data_encoded[col] = 0
        
        # Sütun sırasını düzenle
        new_data_encoded = new_data_encoded[columns]
        
        # Sayısal özellikleri ölçekle
        new_data_encoded[["Metrekare", "Oda_Sayisi"]] = scaler.transform(new_data_encoded[["Metrekare", "Oda_Sayisi"]])
        
        # Tahmin yap
        fiyat_tahmin = model.predict(new_data_encoded)[0]
        
        # Sonucu göster
        st.success(f"Tahmin edilen fiyat: {fiyat_tahmin:,.2f} TL")
        
        # Benzer evleri göster
        st.subheader("Benzer Evler")
        similar_houses = df[
            (df["il"] == selected_il) & 
            (df["Ilce"] == selected_ilce) & 
            (df["Mahalle"] == selected_mahalle) & 
            (df["Metrekare"].between(metrekare * 0.8, metrekare * 1.2))
        ].sort_values(by="fiyat").head(5)
        
        if not similar_houses.empty:
            st.dataframe(similar_houses[["Metrekare", "Oda_Sayisi", "fiyat"]])
        else:
            st.info("Seçilen kriterlere uygun benzer ev bulunamadı.")
    
    # Veri analizi sekmesi
    st.header("Veri Analizi")
    tabs = st.tabs(["Fiyat Dağılımı", "İllere Göre Fiyatlar", "Metrekare-Fiyat İlişkisi"])
    
    with tabs[0]:
        st.subheader("Fiyat Dağılımı")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df["fiyat"], bins=50, kde=True, ax=ax)
        ax.set_xlabel("Fiyat (TL)")
        ax.set_ylabel("Frekans")
        st.pyplot(fig)
    
    with tabs[1]:
        st.subheader("İllere Göre Ortalama Fiyatlar")
        il_fiyat = df.groupby("il")["fiyat"].mean().sort_values(ascending=False).reset_index()
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x="il", y="fiyat", data=il_fiyat, ax=ax)
        ax.set_xlabel("İl")
        ax.set_ylabel("Ortalama Fiyat (TL)")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)
    
    with tabs[2]:
        st.subheader("Metrekare-Fiyat İlişkisi")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x="Metrekare", y="fiyat", hue="il", data=df.sample(1000), ax=ax)
        ax.set_xlabel("Metrekare")
        ax.set_ylabel("Fiyat (TL)")
        st.pyplot(fig)

else:
    st.error("Veri yüklenemedi. Lütfen 'processed_turkish_house_sales.csv' dosyasının mevcut olduğundan emin olun.")