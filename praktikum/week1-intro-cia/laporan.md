# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: [Sejarah Kriptografi]  
Nama: [Adelya Ayu Virnanda]  
NIM: [230202796]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
Jawab : – Kerahasiaan
Tujuan dasar penggunaan kriptografi yaitu kerahasiaan yang terkait layanan yang memiliki fungsi untuk menjaga isi suatu informasi. Kerahasiaan ini berlaku untuk siapa saja. Selain Anda yang memiliki kunci rahasia maupun otoritas dalam membuka informasi yang berhubungan dengan penggunaan kata sandi tepat. 

– Integritas data
Kedua berhubungan dengan penjagaan mengubah data tidak sah. Contohnya penjagaan dari hacker yang tak bertanggung jawab. 

Diperlukan sistem yang bisa mendeteksi data manipulation dari pihak lain dalam mempertahankan integritas data. Manipulasi ini dapat berupa penyisipan, penghapusan atau pensubstitusian data lain pada data asli. 

– Autentikasi
Autentikasi berhubungan dengan pengenalan serta identifikasi. Mengenai hal ini kedua belah pihak akan saling berkomunikasi dan wajib memperkenalkan diri. 

Adapun informasi diri dibagikan melalui kanal harus diautentikasi kebenarannya. Informasi tersebut termasuk isi data ataupun waktu pengiriman serta lainnya. 

– Non repudiasi
Terakhir yaitu non repudiasi atau anti penyangkalan. Non repudiasi adalah upaya yang perlu dilakukan untuk mencegah terjadinya penyangkalan pengiriman informasi yang dilakukan pihak pengirim. Repudiasi atau penyangkalan terhadap pesan pihak yang ditunjuk. 

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
Jawab : **Teori Relevan**

Cipher klasik adalah metode lama dalam kriptografi yang digunakan untuk menyembunyikan isi pesan supaya tidak mudah dibaca oleh orang lain. Cara kerjanya cukup sederhana, yaitu dengan mengganti huruf-huruf pada teks asli (*plaintext*) menjadi huruf lain sesuai pola tertentu sehingga membentuk teks sandi (*ciphertext*). Contohnya adalah **Caesar Cipher**, yang mengganti setiap huruf dengan huruf lain yang berjarak beberapa langkah di alfabet. Misalnya, jika pergeserannya tiga huruf, maka huruf A akan menjadi D, huruf B menjadi E, dan seterusnya. Meskipun tergolong sederhana dan mudah dipecahkan dengan teknologi sekarang, cipher klasik ini menjadi dasar dari banyak teknik enkripsi modern yang lebih rumit.

**aritmetika modular**, yaitu cara menghitung dengan sistem sisa bagi. Misalnya, dalam sistem alfabet yang terdiri dari 26 huruf, angka 27 akan dianggap sama dengan 1 karena 27 mod 26 = 1. Konsep ini digunakan untuk membantu proses penggantian huruf dalam cipher. Misalnya, saat kita ingin menggeser huruf dengan jumlah tertentu, kita bisa memakai perhitungan modular agar hasilnya tetap berada dalam jangkauan alfabet. Dalam kriptografi modern seperti RSA, prinsip aritmetika modular juga digunakan untuk menjaga keamanan data dengan perhitungan angka yang jauh lebih besar dan rumit.

Sejarah Kriptografi :

Kriptografi berasal dari bahasa Yunani, yaitu kryptos yang berarti “rahasia” dan graphia yang berarti “tulisan”. Jadi, kriptografi bisa diartikan sebagai seni atau teknik menulis pesan rahasia agar hanya orang yang berhak yang bisa membacanya.

Perkembangan kriptografi terbagi menjadi beberapa zaman:

Masa Kuno (Sandi Klasik)

Pada masa ini, orang menggunakan cara sederhana untuk menyembunyikan pesan.

Contohnya:

Caesar Cipher (Sandi Caesar) yang menggeser huruf alfabet beberapa langkah, misalnya huruf A diganti jadi D.

Vigenère Cipher, sandi yang menggunakan kunci berupa kata untuk menyandikan pesan.

Masa Perang Dunia

Kriptografi digunakan untuk strategi militer.

Contoh terkenalnya adalah mesin Enigma yang dipakai Jerman pada Perang Dunia II untuk mengenkripsi pesan rahasia.

Mesin ini akhirnya berhasil dipecahkan oleh Alan Turing dan timnya di Inggris, yang kemudian menjadi cikal bakal komputer modern.

Masa Modern (Era Digital)

Kriptografi berkembang pesat seiring kemajuan komputer.

Sistem sandi berubah menjadi algoritma matematis yang sangat rumit.

Contohnya: RSA, AES, dan SHA yang digunakan untuk mengamankan data di internet, transaksi online, dan komunikasi digital.

Prinsip CIA dalam Keamanan Informasi :

Dalam dunia keamanan data, dikenal prinsip utama yang disebut CIA Triad, yaitu:

Confidentiality (Kerahasiaan)
Artinya data harus dijaga agar hanya orang yang berhak yang bisa mengaksesnya.
➤ Contohnya: pesan WhatsApp yang terenkripsi end-to-end supaya tidak bisa disadap.

Integrity (Keutuhan Data)
Data harus tetap asli dan tidak diubah tanpa izin.
➤ Contohnya: tanda tangan digital atau checksum yang memastikan file tidak diubah saat dikirim.

Availability (Ketersediaan)
Data dan sistem harus selalu tersedia bagi pengguna yang berhak kapan pun dibutuhkan.
➤ Contohnya: server website harus tetap aktif agar bisa diakses pengguna kapan saja.

---

## 3. Alat dan Bahan
Jawab : Alat & Bahan Kriptografi )
1) Untuk memahami konsep dasar / klasik
Kertas, pulpen, penggaris — untuk enkripsi manual (Caesar, Vigenère, transposition).
Kartu/cerdas (index cards) — buat kunci, tabel substitusi, latihan one-time pad.
Whiteboard / spidol — visualisasi matriks, transformasi.

2) Perangkat lunak pembelajaran & eksperimen
Python + library: cryptography, PyCryptodome, hashlib — untuk implementasi cipher, hash, KDF.
SageMath atau SageCell — untuk teori bilangan, kurva eliptik, dan eksperimen kriptografi matematis.
OpenSSL — praktek TLS, pembuatan sertifikat, enkripsi simetris/asimetris.
GnuPG (GPG) — enkripsi email/file (OpenPGP), tanda tangan digital.
VeraCrypt / LUKS — enkripsi disk untuk praktek sistem file aman.
Wireshark — menganalisis protokol, melihat handshake TLS (untuk tujuan edukasi).
Hashcat / John the Ripper — pemahaman serangan password / cracking (gunakan secara etis dan legal).
VirtualBox / Docker — lingkungan terisolasi untuk eksperimen.

3) Perangkat keras & token keamanan
Raspberry Pi (atau mini-PC) — buat server kripto, HSM ringan, atau laboratorium PKI.
USB security tokens / YubiKey — praktek autentikasi berbasis kunci publik.
Smartcard / reader — latihan PKI dan token berbasis kartu.
TPM (Trusted Platform Module) — jika perlu eksperimen dengan secure boot / penyimpanan kunci.
Hardware Security Module (HSM) — untuk penelitian/produksi jika tersedia (mahal).

4) Bahan untuk pengujian & evaluasi
Dataset password (publik/anonimisasi) atau wordlists — untuk latihan kekuatan password (hanya dataset legal/public).
File sample (dokumen, gambar) — untuk menguji enkripsi, steganografi.
Skenario lab / tugas — contoh: membangun CA, TLS server-client, tanda tangan digital.

5) Literatur & referensi praktis
Buku pengantar (contoh yang biasa direkomendasikan): Applied Cryptography (Schneier), Introduction to Modern Cryptography (Katz & Lindell).
Dokumentasi resmi: OpenSSL, GnuPG, libs yang dipakai.
RFC penting: TLS, PKCS, X.509 (untuk konfigurasi jaringan/protokol).

6) Praktik keamanan & etika
Aturan etika & izin — jangan mencoba cracking atau penyerangan tanpa izin eksplisit.
Lingkungan terisolasi (VM, jaringan lab) — hindari eksperimen di jaringan produksi.
Backup & kunci recovery plan — saat bereksperimen dengan enkripsi nyata.

---

## 4. Langkah Percobaan
Jawab :Langkah-langkah percobaan kriptografI
  > Langkah-langkah Percobaan**

1. **Menentukan pesan asli (plaintext)**
   Tulis pesan sederhana, misalnya:

   > “BELAJAR KRIPTOGRAFI ITU SERU”

2. **Menentukan kunci pergeseran (key)**
   Pilih angka untuk pergeseran huruf, misalnya:

   > Kunci = 3 (berarti setiap huruf digeser 3 huruf ke kanan dalam alfabet)

3. **Melakukan proses enkripsi (penyandian)**
   Geser setiap huruf sesuai kunci.
   Contoh:

   * B → E
   * E → H
   * L → O
     Jadi pesan baru menjadi:

   > “EHOAODM NULSWRJUDI LWX VHUX”

4. **Mencatat hasil enkripsi**
   Tulis hasil pesan rahasia (ciphertext) di kertas atau di aplikasi yang digunakan.

5. **Melakukan proses dekripsi (membuka sandi)**
   Gunakan kunci yang sama (3) untuk menggeser huruf ke arah kiri agar pesan kembali ke bentuk aslinya.

   > “EHOAODM NULSWRJUDI LWX VHUX” → “BELAJAR KRIPTOGRAFI ITU SERU”

6. **Membandingkan hasilnya**
   Pastikan pesan setelah didekripsi sama dengan pesan awal (plaintext). Jika sama, berarti proses kriptografinya berhasil.

7. **Menyimpulkan hasil percobaan**
   Tuliskan bahwa kriptografi bekerja dengan cara **mengubah pesan menjadi bentuk lain yang tidak mudah dibaca**, dan hanya bisa dikembalikan dengan **kunci yang tepat**.

---

## 7. Jawaban Pertanyaan Quizz
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
- Jawab : Tokoh yang dianggap sebagai bapak kriptografi modern adalah Claude Shannon. Ia adalah seorang ilmuwan Amerika yang dikenal sebagai pelopor teori informasi dan kriptografi modern. Pada tahun 1949, Shannon menulis sebuah makalah berjudul "Communication Theory of Secrecy Systems", yang menjelaskan dasar-dasar matematis tentang bagaimana sistem enkripsi bekerja dan bagaimana keamanan sebuah cipher bisa diukur secara ilmiah.
  
- Pertanyaan 2: Sebutkan algoritma kunci publik yang populer digunakan saat ini.
- Jawab : > ECC (Elliptic Curve Cryptography), yang menggunakan matematika kurva eliptik untuk menghasilkan keamanan tinggi dengan ukuran kunci yang lebih kecil dan efisien.
          > Diffie–Hellman, yang digunakan untuk pertukaran kunci secara aman di jaringan.
          > ElGamal, yang menjadi dasar dari beberapa sistem tanda tangan digital modern.
  
- Pertanyaan 3: Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
- Jawab : 
---Perbedaan utama antara kriptografi klasik dan kriptografi modern terletak pada cara kerja, tingkat keamanan, dan penggunaan matematikanya.

Cara Kerja:
Kriptografi klasik menggunakan metode yang sederhana seperti penggantian huruf (substitution) atau pergeseran huruf (transposition). Contohnya Caesar Cipher atau Vigenère Cipher, yang hanya mengubah huruf-huruf dalam pesan berdasarkan pola tertentu. Sedangkan kriptografi modern menggunakan algoritma kompleks yang melibatkan operasi matematis, bilangan besar, dan komputer untuk melakukan enkripsi dan dekripsi.

Tingkat Keamanan:
Cipher klasik mudah dipecahkan dengan teknik analisis frekuensi atau percobaan manual karena jumlah kombinasi kuncinya relatif sedikit. Sebaliknya, kriptografi modern jauh lebih aman karena menggunakan kunci yang sangat panjang dan sulit ditebak. Bahkan komputer pun membutuhkan waktu sangat lama untuk memecahkannya tanpa kunci yang benar.

Penggunaan Kunci:
Kriptografi klasik umumnya menggunakan satu kunci yang sama untuk enkripsi dan dekripsi (disebut kunci simetris). Sedangkan kriptografi modern memiliki dua jenis sistem: simetris dan asimetris (kunci publik), di mana enkripsi dan dekripsi dilakukan dengan kunci yang berbeda.

---


## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Adelya Ayu Virnanda <adelyavirnanda@gmail.com>
Date:   2025-14-10

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
