# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: [09 Digital Signature RSA/DSA]  
Nama: [Adelya Ayu Virnanda]  
NIM: [230202796]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2.Memverifikasi keaslian tanda tangan digital.
3.Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.


## 2. Dasar Teori
1.Program Python untuk pembuatan dan verifikasi tanda tangan digital.
2.Demo hasil verifikasi tanda tangan digital.
3.Laporan singkat yang menjelaskan implementasi, hasil uji coba, serta manfaat tanda tangan digital.
4.Commit Git dengan format week9-digital-signature.



## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `signature.py` di folder `praktikum/week-9 digital-signature/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python signature.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
    # Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
)


---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?  
Jawab : Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuan penggunaan serta urutan pemanfaatan kunci publik dan privat. Enkripsi RSA bertujuan untuk menjaga kerahasiaan pesan, di mana pengirim menggunakan kunci publik penerima untuk mengenkripsi pesan sehingga hanya pemilik kunci privat penerima yang dapat mendekripsinya dan membaca isi pesan tersebut. Sebaliknya, tanda tangan digital RSA digunakan untuk membuktikan autentisitas dan integritas pesan, di mana pengirim menghitung hash dari pesan kemudian mengenkripsinya menggunakan kunci privat miliknya sendiri; penerima kemudian dapat memverifikasi tanda tangan tersebut dengan mendekripsinya menggunakan kunci publik pengirim dan membandingkan hasil hash-nya dengan hash pesan yang diterima. Dengan kata lain, enkripsi RSA melindungi isi pesan agar tidak dibaca orang lain, sedangkan tanda tangan digital RSA memastikan bahwa pesan benar-benar berasal dari pengirim yang sah dan tidak diubah selama pengiriman, meskipun algoritma matematis RSA yang mendasari keduanya sama, hanya urutan kunci yang digunakan yang dibalik.
2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan? 
Jawab : Tanda tangan digital dapat menjamin integritas dan otentikasi pesan karena prosesnya menggabungkan fungsi hash kriptografis yang aman dengan enkripsi asimetris. Pengirim terlebih dahulu menghitung nilai hash (digest) dari pesan asli menggunakan algoritma hash seperti SHA-256, di mana nilai hash ini unik dan akan berubah secara drastis meskipun hanya ada sedikit perubahan pada pesan. Kemudian, hash tersebut dienkripsi menggunakan kunci privat pengirim untuk menghasilkan tanda tangan digital yang dikirim bersama pesan asli. Saat penerima memverifikasi, ia menghitung ulang hash dari pesan yang diterima dan mendekripsi tanda tangan dengan kunci publik pengirim untuk mendapatkan hash asli. Jika kedua hash tersebut identik, maka terbukti bahwa pesan tidak mengalami perubahan apa pun (integritas terjaga) dan benar-benar dibuat oleh pemilik kunci privat yang sah (otentikasi terjamin), karena hanya pemilik kunci privat tersebut yang mampu menghasilkan tanda tangan yang valid. Selain itu, mekanisme ini juga memberikan non-repudiation, sehingga pengirim tidak dapat menyangkal telah mengirim pesan tersebut. 
3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?  
Jawab : Certificate Authority (CA) memainkan peran krusial dalam sistem tanda tangan digital modern sebagai pihak ketiga tepercaya yang mengeluarkan **sertifikat digital**. Sertifikat ini mengikat identitas seseorang (atau entitas) dengan pasangan kunci publik-privat mereka melalui tanda tangan digital CA sendiri. Saat seseorang membuat tanda tangan digital pada dokumen atau pesan, mereka menggunakan kunci privatnya untuk mengenkripsi hash dokumen, sementara penerima memverifikasi tanda tangan tersebut dengan kunci publik dari sertifikat yang dikeluarkan CA.

Kunci publik ini dipercaya karena CA telah memverifikasi identitas pemiliknya secara ketat sebelum menerbitkan sertifikat, sehingga menjamin otentikasi (bahwa tanda tangan benar-benar dari pemilik yang sah) dan non-repudiation (pemilik tidak dapat menyangkal telah menandatangani). Selain itu, CA mengelola siklus hidup sertifikat, termasuk penerbitan, pembaruan, dan pencabutan (revocation) jika kunci privat bocor atau identitas tidak lagi valid, sering melalui Certificate Revocation List (CRL) atau OCSP. Dalam Public Key Infrastructure (PKI) modern, CA membentuk rantai kepercayaan (chain of trust) yang menjadi fondasi keamanan aplikasi seperti e-signature berkualitas tinggi (qualified electronic signatures di eIDAS), penandatanganan dokumen PDF, code signing, serta protokol seperti SSL/TLS, memastikan tanda tangan digital memiliki nilai hukum dan keamanan yang setara dengan tanda tangan basah.

---

## 8. Kesimpulan
Digital Signature dengan algoritma RSA dan DSA berperan penting dalam menjamin keaslian, keutuhan, dan non-repudiation suatu pesan atau dokumen digital. RSA lebih fleksibel karena dapat digunakan untuk enkripsi dan tanda tangan digital, sedangkan DSA dirancang khusus untuk proses penandatanganan dengan tingkat keamanan yang kuat dan efisiensi yang baik. Keduanya mengandalkan kriptografi kunci publik sehingga hanya pemilik kunci privat yang dapat membuat tanda tangan, dan pihak lain dapat memverifikasinya menggunakan kunci publik. Dengan penerapan yang benar, RSA dan DSA mampu meningkatkan kepercayaan dan keamanan dalam sistem komunikasi serta transaksi elektronik.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit 2808dbb588200631d6d335079767aa0d81c16b79 (HEAD -> main, origin/main, origin/HEAD)
Author: AdelyaAv <adelya@gmail.com>
Date:   Sat Jan 17 13:39:17 2026 +0700

    week9-digital-signature
```
