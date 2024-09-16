from sklearn.preprocessing import OrdinalEncoder

#inisialisasi obyek odinal encoder
oe = OrdinalEncoder()

#definisikan data dalam bentuk 2d
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang'],
]

#Transformasi Ordinal Encoder
transform_oe = oe.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi Ordinal Encoder')
print(transform_oe)