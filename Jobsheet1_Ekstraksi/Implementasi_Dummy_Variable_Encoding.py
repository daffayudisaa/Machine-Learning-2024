from sklearn.preprocessing import OneHotEncoder

#Inisiasi Objek Ordinal Encoder
de = OneHotEncoder(drop='first')

#Definisikan data dalam bentuk 2D
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang'],
]

#Transformasi Ordinal Encoder
transform_de = de.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi Dummy Encoder')
print(transform_de.toarray())