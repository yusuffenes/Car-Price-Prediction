# Car Price Prediction :car: :arrow_forward: :dollar:
Bu proje, makine öğrenimi kullanarak otomobil fiyatlarını tahmin etmek için geliştirilmiş bir uygulamadır.

## Proje Açıklaması
Bu uygulama, kullanıcıların otomobil markası, modeli, üretim yılı, kilometre, motor özellikleri, renk, montaj yeri, gövde tipi, şanzıman türü ve kayıt durumu gibi özellikleri seçerek bir otomobilin tahmini fiyatını öğrenmelerine olanak tanır.

## Proje Linki 

[Proje Linki !](https://huggingface.co/spaces/yusufenes/CarPricePredict)

## Kullanılan Teknolojiler
- Python
- Pandas, NumPy: Veri işleme ve manipülasyonu için kullanıldı.
- Scikit-learn: Makine öğrenimi modelinin oluşturulması ve eğitilmesi için kullanıldı.
- Streamlit: Web uygulaması arayüzünün oluşturulması için kullanıldı.
- HistGradientBoostingRegressor: Tahmin modeli olarak kullanıldı.
## Kurulum
### Projeyi klonlamak için aşağıdaki komutu kullanabilirsiniz:


'''
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
'''
Gerekli Python kütüphanelerini yüklemek için:

'''
pip install -r requirements.txt
'''

## Nasıl Kullanılır?
Proje dizininde Streamlit uygulamasını başlatın:
'''
streamlit run app.py
'''
Web tarayıcınızda localhost:8501 adresine gidin.
Form üzerinde otomobil özelliklerini seçin ve "Predict" butonuna tıklayarak tahmini fiyatı gözlemleyin.
