# Ev Fiyat Tahmini Projesi

Bu proje, Türkiye'deki ev fiyatlarını tahmin etmek için makine öğrenmesi modelini kullanan interaktif bir Streamlit uygulamasıdır. Kullanıcılar, il, ilçe, mahalle, metrekare ve oda sayısı gibi özellikleri belirleyerek potansiyel ev fiyatlarını tahmin edebilir ve kapsamlı veri analizlerini inceleyebilirler.

## 📋 Proje Özeti

Türk Ev Fiyat Tahmini Projesi, Türkiye'deki konut piyasasında fiyat tahminleri yapmak için geliştirilmiş bir veri bilimi uygulamasıdır. Proje, gerçek emlak verilerini kullanarak Random Forest algoritması ile eğitilmiş bir makine öğrenmesi modeli içermektedir. Kullanıcı dostu arayüzü sayesinde, gayrimenkul yatırımcıları, ev almak isteyenler ve emlak profesyonelleri için değerli bir araç olarak tasarlanmıştır.

## ✨ Özellikler

### Tahmin Özellikleri
- **Konum Bazlı Tahmin**: İl, ilçe ve mahalle bazında detaylı fiyat tahmini
- **Özellik Bazlı Tahmin**: Metrekare ve oda sayısına göre özelleştirilmiş fiyat tahmini
- **Satıcı Tipi Analizi**: Farklı satıcı tiplerine göre fiyat değişimlerini analiz etme

### Veri Analizi ve Görselleştirme
- **Fiyat Dağılımı**: Türkiye genelinde ev fiyatlarının dağılımını gösteren histogramlar
- **İl Bazlı Karşılaştırma**: İllere göre ortalama ev fiyatlarını karşılaştıran bar grafikleri
- **Metrekare-Fiyat İlişkisi**: Metrekare ve fiyat arasındaki ilişkiyi gösteren scatter plot grafikler

### Benzer Ev Analizi
- **Benzer Evlerin Tespiti**: Seçilen kriterlere göre benzer özellikteki evlerin listelenmesi
- **Fiyat Karşılaştırması**: Benzer evlerin fiyatlarını karşılaştırma imkanı

## 🧠 Model Detayları

### Kullanılan Algoritma
- **Random Forest Regresyon**: Yüksek doğruluk ve gürbüzlük sağlayan ensemble öğrenme algoritması
- **Hiperparametreler**: n_estimators=100, random_state=42

### Model Özellikleri
- **Özellik Mühendisliği**: Kategorik değişkenler için one-hot encoding
- **Veri Ön İşleme**: Eksik verilerin temizlenmesi ve sayısal özelliklerin ölçeklendirilmesi
- **Özellik Önem Derecesi**: Model, hangi özelliklerin fiyat üzerinde daha etkili olduğunu belirleyebilir

## 📊 Veri Seti

Uygulama, `processed_turkish_house_sales.csv` dosyasındaki verileri kullanmaktadır. Bu veri seti aşağıdaki özellikleri içermektedir:

- **satici_tip**: Ev satıcısının tipi (Sahibinden, Emlak Ofisi vb.)
- **Metrekare**: Evin metrekare cinsinden büyüklüğü (30-500 m² aralığında)
- **Oda_Sayisi**: Evin oda sayısı (1+0, 1+1, 2+1, 3+1 vb. formatında)
- **il**: Evin bulunduğu il
- **Ilce**: Evin bulunduğu ilçe
- **Mahalle**: Evin bulunduğu mahalle
- **Tarih**: İlan tarihi
- **fiyat**: Evin satış fiyatı (TL cinsinden)

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler
- **Streamlit**: İnteraktif web uygulaması geliştirme
- **Pandas & NumPy**: Veri manipülasyonu ve analizi
- **Scikit-learn**: Makine öğrenmesi modeli geliştirme
- **Matplotlib & Seaborn**: Veri görselleştirme

### Veri İşleme Adımları
1. Veri yükleme ve temizleme
2. Oda sayısı formatını sayısal değerlere dönüştürme
3. Eksik verilerin filtrelenmesi
4. Kategorik değişkenlerin one-hot encoding ile dönüştürülmesi
5. Sayısal özelliklerin StandardScaler ile ölçeklendirilmesi

## 🚀 Kurulum

### Gereksinimler
Projeyi çalıştırmak için aşağıdaki kütüphanelere ihtiyacınız vardır:

```bash
pip install -r requirements.txt
```

Gerekli kütüphaneler:
- streamlit
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

### Kurulum Adımları

1. Projeyi bilgisayarınıza klonlayın veya indirin
2. Proje dizinine gidin
3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. Uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```
   veya Windows için:
   ```bash
   run_app.bat
   ```

## 📱 Kullanım Kılavuzu

### Tahmin Yapma
1. Yan panelden ev özelliklerini seçin:
   - **Satıcı Tipi**: Evin satıcı tipini seçin
   - **İl**: Evin bulunduğu ili seçin
   - **İlçe**: Seçilen ile göre filtrelenmiş ilçelerden birini seçin
   - **Mahalle**: Seçilen ilçeye göre filtrelenmiş mahallelerden birini seçin
   - **Metrekare**: Evin metrekare değerini girin (30-500 m²)
   - **Oda Sayısı**: Evin oda sayısını girin (1-10 arası, 0.5 artışlarla)

2. "Fiyat Tahmini Yap" butonuna tıklayın

3. Tahmin sonuçlarını inceleyin:
   - Tahmin edilen fiyat
   - Benzer özellikteki evlerin fiyat karşılaştırması

### Veri Analizi
1. "Veri Analizi" bölümündeki sekmeleri kullanarak farklı analizleri inceleyin:
   - **Fiyat Dağılımı**: Türkiye genelinde ev fiyatlarının dağılımını gösteren histogram
   - **İllere Göre Fiyatlar**: İllere göre ortalama ev fiyatlarını gösteren bar grafik
   - **Metrekare-Fiyat İlişkisi**: Metrekare ve fiyat arasındaki ilişkiyi gösteren scatter plot

## 🔍 Kullanım Senaryoları

- **Ev Alıcıları**: Belirli bir bölgedeki ev fiyatlarını tahmin ederek bütçe planlaması yapabilir
- **Gayrimenkul Yatırımcıları**: Farklı bölgelerdeki fiyat trendlerini analiz ederek yatırım fırsatlarını değerlendirebilir
- **Emlak Profesyonelleri**: Müşterilerine daha doğru fiyat tahminleri sunabilir
- **Veri Analistleri**: Türkiye'deki konut piyasası hakkında detaylı analizler yapabilir

## 📈 Gelecek Geliştirmeler

- Daha fazla özellik ekleme (bina yaşı, kat sayısı, vb.)
- Zaman serisi analizi ile fiyat trend tahminleri
- Farklı makine öğrenmesi modellerinin karşılaştırılması
- Harita tabanlı görselleştirmeler
- Mobil uygulama desteği

## 📄 Lisans

Bu proje açık kaynaklıdır ve eğitim amaçlı kullanılabilir.

##  İletişim

Proje hakkında sorularınız veya önerileriniz için lütfen iletişime geçin.
meil : Muayyedalibrahim@gmail.com

---

*Not: Bu uygulama, gerçek emlak verileri üzerinde eğitilmiş bir makine öğrenmesi modeli kullanmaktadır. Tahminler, gerçek piyasa koşullarına göre farklılık gösterebilir.*
