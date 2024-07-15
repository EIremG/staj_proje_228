# staj_proje_228
--------------------------

# Bitki Büyüme Veri Seti Analizi
--------------------------

Bu proje, bitki büyüme veri setini inceleyerek, bitkilerin büyüme koşullarını anlamak ve analiz etmek amacıyla gerçekleştirilmiştir. Python programlama dili ve pandas, seaborn, matplotlib gibi kütüphaneler kullanılmıştır.

## İçindekiler
--------------------------

- [Projenin Amacı](#projenin-amacı)
- [Giriş](#giriş)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Adım Adım Proje Açıklaması](#adım-adım-proje-açıklaması)
  - [1. Veri Yükleme ve Temizleme](#1-veri-yükleme-ve-temizleme)
  - [2. Eksik Değerlerin Kontrolü](#2-eksik-değerlerin-kontrolü)
  - [3. Temel İstatistiklerin Hesaplanması](#3-temel-istatistiklerin-hesaplanması)
  - [4. Kategorik Verilerin Görselleştirilmesi](#4-kategorik-verilerin-görselleştirilmesi)
  - [5. Sayısal Verilerin Görselleştirilmesi](#5-sayısal-verilerin-görselleştirilmesi)
  - [6. Korelasyon Analizi](#6-korelasyon-analizi)
- [Sonuçlar ve Öneriler](#sonuçlar-ve-öneriler)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Projenin Amacı
--------------------------

Bu projenin amacı, bitki büyüme koşullarını etkileyen faktörleri anlamak ve bu faktörler arasındaki ilişkileri görsel ve istatistiksel olarak analiz etmektir. Bu analizler, tarımsal uygulamalar ve bitki yetiştiriciliği üzerine daha derinlemesine çalışmalar için temel oluşturabilir.

## Giriş
--------------------------

Veri seti, bitki büyüme süreçlerini takip eden parametreleri içermektedir. `plant_growth_data.csv` dosyasından yüklenen veri seti, toprak türü, sulama sıklığı, gübre türü, güneş saatleri, sıcaklık, nem gibi çeşitli faktörleri içermektedir.

## Kurulum
--------------------------

Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Gerekli Kütüphaneleri Yükleyin:
   ```bash
   pip install pandas seaborn matplotlib
   
2. Veri Setini İndirin: 
   plant_growth_data.csv dosyasını projenizin kök dizinine yerleştirin.

## Kullanım
--------------------------

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Python Betiğini Çalıştırın:
   ```bash
   python analyze_plant_growth.py

2. Sonuçları İnceleyin:
   Grafikler ve analiz sonuçları görüntülenecektir.

## Adım Adım Proje Açıklaması
--------------------------

1. Veri Yükleme ve Temizleme
   Veri seti, pandas kullanılarak yüklenir ve temizlenir.

   ```python
   import pandas as pd

   file_path = 'plant_growth_data.csv'
   data = pd.read_csv(file_path)

  `import pandas as pd`: Pandas kütüphanesini pd takma adıyla içe aktarır.
  
  `file_path = 'plant_growth_data.csv'`: Veri setinin dosya yolunu belirtir.
  
  `data = pd.read_csv(file_path)`: Belirtilen dosya yolundan CSV dosyasını okur ve bir DataFrame'e yükler.

2. Eksik Değerlerin Kontrolü
   Veri setindeki eksik değerler kontrol edilir.

   ```python 
   missing_values = data.isnull().sum()
   print("Missing values in each column:")
   print(missing_values)

  `missing_values = data.isnull().sum()`: Her sütundaki eksik değerlerin sayısını hesaplar.
  
  `print("Missing values in each column:")`: Kolonlardaki eksik değerlerin sayısını ekrana yazdırır.
  
  `print(missing_values)`: Eksik değerlerin sayısını ekrana yazdırır.

3. Temel İstatistiklerin Hesaplanması
   Veri setinin temel istatistikleri hesaplanır.

   ```python  
   basic_stats = data.describe(include='all')
   print("\nBasic statistics of the dataset:")
   print(basic_stats)

  `basic_stats = data.describe(include='all')`: Tüm sütunların temel istatistiklerini hesaplar ve bir DataFrame döndürür.
  
  `print("\nBasic statistics of the dataset:")`: Temel istatistiklerin başlığını ekrana yazdırır.
  
  `print(basic_stats)`: Temel istatistikleri ekrana yazdırır.

4. Kategorik Verilerin Görselleştirilmesi
   Kategorik verilerin dağılımı görselleştirilir.

   ```python 
   import seaborn as sns
   import matplotlib.pyplot as plt

   plt.figure(figsize=(10, 6))
   sns.countplot(x='Soil_Type', data=data)
   plt.title('Soil Type Distribution')
   plt.show()

   plt.figure(figsize=(10, 6))
   sns.countplot(x='Water_Frequency', data=data)
   plt.title('Water Frequency Distribution')
   plt.show()

   plt.figure(figsize=(10, 6))
   sns.countplot(x='Fertilizer_Type', data=data)
   plt.title('Fertilizer Type Distribution')
   plt.show()

  `import seaborn as sns`: Seaborn kütüphanesini sns takma adıyla içe aktarır.
  
  `import matplotlib.pyplot as plt`: Matplotlib kütüphanesini plt takma adıyla içe aktarır.
  
  `plt.figure(figsize=(10, 6))`: Grafik boyutlarını ayarlar.
  
  `sns.countplot(x='Soil_Type', data=data)`: Soil_Type sütununun frekans dağılımını çubuk grafiği olarak çizer.
  
  `plt.title('Soil Type Distribution')`: Grafiğe başlık ekler.
  
  `plt.show()`: Grafiği görüntüler.
  
   Aynı adımlar Water_Frequency ve Fertilizer_Type sütunları için de tekrarlanır.

5. Sayısal Verilerin Görselleştirilmesi
   Sayısal verilerin dağılımı görselleştirilir.

   ```python 
   plt.figure(figsize=(10, 6))
   sns.histplot(data['Sunlight_Hours'], bins=10, kde=True)
   plt.title('Distribution of Sunlight Hours')
   plt.show()
 
   plt.figure(figsize=(10, 6))
   sns.histplot(data['Temperature'], bins=10, kde=True)
   plt.title('Distribution of Temperature')
   plt.show()

   plt.figure(figsize=(10, 6))
   sns.histplot(data['Humidity'], bins=10, kde=True)
   plt.title('Distribution of Humidity')
   plt.show()

  `plt.figure(figsize=(10, 6))`: Grafik boyutlarını ayarlar.
  
  `sns.histplot(data['Sunlight_Hours'], bins=10, kde=True)`: Sunlight_Hours sütununun histogramını çizer ve KDE (yoğunluk tahmin eğrisi) ekler.
  
  `plt.title('Distribution of Sunlight Hours')`: Grafiğe başlık ekler.
  
  `plt.show()`: Grafiği görüntüler
  
   Aynı adımlar Temperature ve Humidity sütunları için de tekrarlanır.

6. Korelasyon Analizi
   Korelasyon matrisi hesaplanır ve görselleştirilir.

   ```python 
   numeric_data = data[['Sunlight_Hours', 'Temperature', 'Humidity', 'Growth_Milestone']]
   correlation_matrix = numeric_data.corr()

   plt.figure(figsize=(10, 6))
   sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
   plt.title('Correlation Matrix')
   plt.show()

  `numeric_data = data[['Sunlight_Hours', 'Temperature', 'Humidity', 'Growth_Milestone']]`: Sayısal sütunları seçer.
  
  `correlation_matrix = numeric_data.corr()`: Seçilen sütunların korelasyon matrisini hesaplar.
  
  `plt.figure(figsize=(10, 6))`: Grafik boyutlarını ayarlar.
  
  `sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')`: Korelasyon matrisini ısı haritası olarak çizer ve değerleri ekler.
  
  `plt.title('Correlation Matrix')`: Grafiğe başlık ekler.
  
  `plt.show()`: Grafiği görüntüler.

Sonuçlar ve Öneriler
--------------------------

Bu proje, bitki büyüme koşullarını analiz etmek için kapsamlı bir başlangıç noktası sağlamaktadır. Elde edilen bulgular, tarım endüstrisinde bitki yetiştirme tekniklerinin geliştirilmesi ve optimize edilmesi için önemli bir temel oluşturabilir. İleriye yönelik çalışmalarda, daha fazla parametrenin dikkate alınması ve farklı büyüme koşullarının analiz edilmesi önerilmektedir.

Katkıda Bulunma
--------------------------

Projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir sorun bildirin.
