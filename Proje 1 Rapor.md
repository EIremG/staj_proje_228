# Veri Analizi Raporu

## Problemi Anlama ve Veri Analizi Süreci

### 1. Problem Tanımı
Bitki büyümesi üzerine çalışırken, farklı değişkenlerin bitki büyümesini nasıl etkilediğini anlamak istiyoruz. Özellikle toprağın türü, sulama sıklığı, gübre türü, gün ışığı saatleri, sıcaklık ve nem gibi faktörlerin bitki büyümesi üzerindeki etkilerini analiz etmek istiyoruz.

### 2. Veri Setinin Yapısı
Veri setimiz, bitki büyümesine etki eden çeşitli faktörleri içeren bir tabloyu temsil eder. Bu tabloyu anlamak için, her sütunun ne anlama geldiğini ve hangi tür veriler içerdiğini bilmemiz gerekiyor:

- **Soil_Type (Toprak Türü):** Bitkinin yetiştiği toprak türünü belirtir. Kategorik bir değişkendir.
- **Water_Frequency (Sulama Sıklığı):** Bitkinin sulama sıklığını belirtir. Kategorik bir değişkendir.
- **Fertilizer_Type (Gübre Türü):** Kullanılan gübre türünü belirtir. Kategorik bir değişkendir.
- **Sunlight_Hours (Gün Işığı Saatleri):** Bitkinin günlük olarak aldığı gün ışığı saatlerini belirtir. Sayısal bir değişkendir.
- **Temperature (Sıcaklık):** Bitkinin yetiştiği ortamın sıcaklığını belirtir. Sayısal bir değişkendir.
- **Humidity (Nem):** Ortamın nem oranını belirtir. Sayısal bir değişkendir.
- **Growth_Milestone (Büyüme Dönemi):** Bitkinin büyüme durumunu veya dönüm noktalarını belirtir. Bu değişken bitkinin büyüme performansını ölçmek için kullanılabilir. Sayısal bir değişkendir.

## Veri Analizi ve Neden Bu Adımları Attık?

### 1. Veri Kümesini Yükleme ve Eksik Değerleri Kontrol Etme
Veri setini yükledikten sonra eksik değerleri kontrol ettik. Eksik değerler analiz sonuçlarını olumsuz etkileyebileceğinden, bu adım çok önemlidir. Eksik değerlerin varlığı, bazı sütunlarda bilgi eksikliği olduğunu ve bu durumun analiz sürecinde dikkate alınması gerektiğini gösterir.

### 2. Temel İstatistiklerin Hesaplanması
Veri setinin temel istatistiklerini hesaplamak, her sütunun genel özelliklerini anlamamıza yardımcı olur. Bu adımda, sütunların ortalama, medyan, minimum ve maksimum değerleri gibi istatistiksel özelliklerini inceledik. Bu, veri setinin genel dağılımını ve aykırı değerleri anlamak için önemlidir.

### 3. Kategorik Verilerin Dağılımının İncelenmesi
Kategorik değişkenlerin (toprak türü, sulama sıklığı, gübre türü) dağılımını görselleştirerek, her kategorinin veri setinde ne kadar yaygın olduğunu anladık. Bu, hangi kategorilerin daha sık gözlemlendiğini ve analiz sürecinde hangi kategorilerin dikkate alınması gerektiğini anlamamıza yardımcı olur.

### 4. Sayısal Verilerin Dağılımının İncelenmesi
Sayısal değişkenlerin (gün ışığı saatleri, sıcaklık, nem) dağılımını incelemek, bu değişkenlerin veri setindeki genel davranışlarını anlamamızı sağlar. Histogram ve KDE (Kernel Density Estimation) kullanarak, sayısal değişkenlerin dağılımlarını görselleştirdik. Bu, veri setinin genel dağılımı hakkında daha derin bir anlayış sağlar ve olası aykırı değerleri belirlememize yardımcı olur.

### 5. Korelasyon Matrisinin Hesaplanması ve Görselleştirilmesi
Son olarak, sayısal değişkenler arasındaki ilişkileri incelemek için korelasyon matrisini hesapladık. Korelasyon matrisi, değişkenler arasındaki doğrusal ilişkiyi gösterir. Bu, hangi değişkenlerin bitki büyümesi üzerinde daha fazla etkisi olduğunu belirlemek için kullanılır. Örneğin, gün ışığı saatleri ile bitki büyümesi arasında güçlü bir pozitif korelasyon varsa, bu iki değişkenin birbirine bağlı olduğunu gösterir.

## Sonuç
Bu adımların her biri, veri setimizin yapısını ve içeriğini daha iyi anlamamıza yardımcı oldu. Eksik değerlerin kontrol edilmesi, temel istatistiklerin hesaplanması, kategorik ve sayısal verilerin dağılımının incelenmesi ve korelasyon matrisinin görselleştirilmesi, bitki büyümesini etkileyen faktörleri daha iyi analiz etmemizi sağlar. Bu süreç, veriye dayalı kararlar almamıza ve bitki büyümesini optimize etmek için stratejiler geliştirmemize yardımcı olur.


