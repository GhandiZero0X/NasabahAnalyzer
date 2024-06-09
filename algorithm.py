import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from ImageTree import show_tree_image

# Data pelatihan
data = [
    ['Baik', 'BPKB', 'Wiraswasta', 'Kelas Atas'],
    ['Bermasalah', 'BPKB', 'Wiraswasta', 'Kelas Mikro'],
    ['Baik', 'BPKB', 'PNS', 'Kelas Atas'],
    ['Bermasalah', 'BPKB', 'PNS', 'Kelas Sedang'],
    ['', 'BPKB', 'Swasta', 'Kelas Sedang'],
    ['', 'Logam Mulia', '', 'Kelas Mikro'],
    ['Baik', 'Sertifikat HM', 'Wiraswasta', 'Kelas Atas'],
    ['Bermasalah', 'Sertifikat HM', 'Wiraswasta', 'Kelas Sedang'],
    ['', 'Sertifikat HM', 'PNS', 'Kelas Atas'],
    ['', 'Sertifikat HM', 'Swasta', 'Kelas Atas dan Sedang']
]

# Pisahkan fitur dan label
X = np.array([row[:-1] for row in data])
y = np.array([row[-1] for row in data])

# LabelEncoder untuk mengonversi data kategori ke numerik
le_prestasi = LabelEncoder()
le_jaminan = LabelEncoder()
le_pekerjaan = LabelEncoder()
le_kelas = LabelEncoder()

X[:, 0] = le_prestasi.fit_transform(X[:, 0])
X[:, 1] = le_jaminan.fit_transform(X[:, 1])
X[:, 2] = le_pekerjaan.fit_transform(X[:, 2])
y = le_kelas.fit_transform(y)

# Inisialisasi dan latih DecisionTreeClassifier dengan kriteria 'entropy'
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# Fungsi untuk mendapatkan input manual
def get_user_input():
    prestasi = input("Masukkan prestasi (Baik/Bermasalah): ")
    jaminan = input("Masukkan jaminan (BPKB/Logam Mulia/Sertifikat HM): ")
    pekerjaan = input("Masukkan pekerjaan (Swasta/Wiraswasta/PNS): ")
    return prestasi, jaminan, pekerjaan

# Meminta input dari pengguna
prestasi, jaminan, pekerjaan = get_user_input()

# Kondisi khusus
if jaminan == 'BPKB' and pekerjaan == 'Swasta':
    prediksi = 'Kelas Sedang'
elif jaminan == 'Logam Mulia':
    prediksi = 'Kelas Mikro'
else:
    # Konversi input pengguna ke numerik
    prestasi_num = le_prestasi.transform([prestasi])[0]
    jaminan_num = le_jaminan.transform([jaminan])[0]
    pekerjaan_num = le_pekerjaan.transform([pekerjaan])[0]

    # Prediksi menggunakan model decision tree
    prediksi_num = clf.predict([[prestasi_num, jaminan_num, pekerjaan_num]])
    prediksi = le_kelas.inverse_transform(prediksi_num)[0]

print(f"Prestasi: {prestasi}, Jaminan: {jaminan}, Pekerjaan: {pekerjaan} -> Nasabah Tingkat : {prediksi}")

# Tambahkan baris berikut untuk menampilkan gambar decision tree dalam pop-up
show_tree_image(clf, ['Prestasi', 'Jaminan', 'Pekerjaan'], ['Kelas Mikro', 'Kelas Sedang', 'Kelas Atas', 'Kelas Atas dan Sedang'])
