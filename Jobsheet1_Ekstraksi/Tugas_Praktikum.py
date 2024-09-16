corpus = open("corpus.txt", "r")

from sklearn.feature_extraction.text import TfidfVectorizer

#Inisiasi Obyek TF-IDF Vectorizer
vect = TfidfVectorizer(stop_words='english')

#Pembobotan TF-IDF
resp = vect.fit_transform(corpus)

#Cetak Hasil
print(resp)
print(vect.get_feature_names_out())

