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

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
Jawab : **Teori Relevan**

Cipher klasik adalah metode lama dalam kriptografi yang digunakan untuk menyembunyikan isi pesan supaya tidak mudah dibaca oleh orang lain. Cara kerjanya cukup sederhana, yaitu dengan mengganti huruf-huruf pada teks asli (*plaintext*) menjadi huruf lain sesuai pola tertentu sehingga membentuk teks sandi (*ciphertext*). Contohnya adalah **Caesar Cipher**, yang mengganti setiap huruf dengan huruf lain yang berjarak beberapa langkah di alfabet. Misalnya, jika pergeserannya tiga huruf, maka huruf A akan menjadi D, huruf B menjadi E, dan seterusnya. Meskipun tergolong sederhana dan mudah dipecahkan dengan teknologi sekarang, cipher klasik ini menjadi dasar dari banyak teknik enkripsi modern yang lebih rumit.

Selain itu, ada juga konsep penting yang disebut **aritmetika modular**, yaitu cara menghitung dengan sistem sisa bagi. Misalnya, dalam sistem alfabet yang terdiri dari 26 huruf, angka 27 akan dianggap sama dengan 1 karena 27 mod 26 = 1. Konsep ini digunakan untuk membantu proses penggantian huruf dalam cipher. Misalnya, saat kita ingin menggeser huruf dengan jumlah tertentu, kita bisa memakai perhitungan modular agar hasilnya tetap berada dalam jangkauan alfabet. Dalam kriptografi modern seperti RSA, prinsip aritmetika modular juga digunakan untuk menjaga keamanan data dengan perhitungan angka yang jauh lebih besar dan rumit.
---


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
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


## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Adelya Ayu Virnanda <adelyavirnanda@gmail.com>
Date:   2025-14-10

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
