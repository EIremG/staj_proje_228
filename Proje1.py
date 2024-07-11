
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veri kümesini yükleyelim
file_path = '/content/drive/MyDrive/plant_growth_data.csv'  # CSV dosyasının yolu
data = pd.read_csv(file_path)  # CSV dosyasını pandas DataFrame'e yükleme

# Eksik değerleri kontrol edelim
missing_values = data.isnull().sum()  # Her sütundaki eksik değerleri say
print("Missing values in each column:")
print(missing_values)
print("\n")

# Temel istatistikler
basic_stats = data.describe(include='all')  # Tüm sütunlar için temel istatistikleri al
print("\nBasic statistics of the dataset:")
print(basic_stats)
print("\n")

# Kategorik verilerin dağılımını inceleyelim
plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.countplot(x='Soil_Type', data=data)  # Soil_Type sütunundaki değerlerin sayımını görselleştir
plt.title('Soil Type Distribution')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.countplot(x='Water_Frequency', data=data)  # Water_Frequency sütunundaki değerlerin sayımını görselleştir
plt.title('Water Frequency Distribution')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.countplot(x='Fertilizer_Type', data=data)  # Fertilizer_Type sütunundaki değerlerin sayımını görselleştir
plt.title('Fertilizer Type Distribution')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

# Sayısal verilerin dağılımını inceleyelim
plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.histplot(data['Sunlight_Hours'], bins=10, kde=True)  # Sunlight_Hours sütununu histogram ve KDE ile görselleştir
plt.title('Distribution of Sunlight Hours')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.histplot(data['Temperature'], bins=10, kde=True)  # Temperature sütununu histogram ve KDE ile görselleştir
plt.title('Distribution of Temperature')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.histplot(data['Humidity'], bins=10, kde=True)  # Humidity sütununu histogram ve KDE ile görselleştir
plt.title('Distribution of Humidity')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

# Korelasyon matrisini hesaplayalım
numeric_data = data[['Sunlight_Hours', 'Temperature', 'Humidity', 'Growth_Milestone']]  # Sadece sayısal sütunları seç
correlation_matrix = numeric_data.corr()  # Korelasyon matrisini hesapla
print("\n")

# Korelasyon matrisini görselleştirme
plt.figure(figsize=(10, 6))  # Grafik boyutunu ayarlama
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Korelasyon matrisini ısı haritası ile görselleştir
plt.title('Correlation Matrix')  # Grafiğe başlık ekle
plt.show()  # Grafiği göster
print("\n")

