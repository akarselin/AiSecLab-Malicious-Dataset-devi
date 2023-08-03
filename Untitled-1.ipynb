import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Veri Kümesini Yükleme
data = pd.read_csv('veri_kumesi.csv')

# 2. Veri Keşfi
print(data.head())
print(data.describe())
print(data.isnull().sum())
print(data['target_column'].value_counts())

# 3. Eksik Veri Doldurma
data.fillna(data.mean(), inplace=True)

# 4. Kategorik Verileri Dönüştürme (One-Hot Encoding)
data_encoded = pd.get_dummies(data, columns=['categorical_column'])

# 5. Özellik Ölçeklendirme (Min-Max Scaling)
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data_encoded)

# 6. Veri Bölünmesi
X = data_scaled.drop(columns=['target_column'])
y = data_scaled['target_column']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Oluşturma ve Eğitim
model = LogisticRegression()
model.fit(X_train, y_train)

# Model Doğrulama ve Değerlendirme
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluğu:", accuracy)
print(classification_report(y_test, y_pred))
