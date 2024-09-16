import numpy as np
from sklearn.preprocessing import StandardScaler

np.set_printoptions(precision=6) #Bulatkan 4 angka koma
np.set_printoptions(suppress=True) #Hilangkan nilai e

data = [
    [100, 0.0001],
    [50, 0.05],
    [30, 0.003]
]

#Kita akan membentuk data, hal ini karena scikit-learn hanya menerima input dalam bentuk n-dimensional array
data = np.asanyarray(data)
print("Data Asli")
print(data)

#Mendefinisikan Objek StandardScaler
scaler = StandardScaler()

# Transformasi Data
sclaed = scaler.fit_transform(data)
print("\nData Normalisasi")
print(sclaed)
