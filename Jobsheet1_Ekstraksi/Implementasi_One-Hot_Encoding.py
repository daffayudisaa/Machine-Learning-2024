from sklearn.preprocessing import OneHotEncoder

#inisialisasi obyek odinal encoder
ohe = OneHotEncoder()

#definisikan data dalam bentuk 2d
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang'],
]

#Transformasi One-Hot Encoder
transform_ohe = ohe.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi Ordinal Encoder')
print(transform_ohe.toarray())