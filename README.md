# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama : Indri Meilani
NIM : 2225250141
Kelas : 3A

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan
Program ini digunakan untuk menentukan jenis sudut berdasarkan besar sudut yang dimasukkan. Setiap kondisi memiliki kategori dan batas nilai yang berbeda.

Kategori; Masukan ditolak,	Syarat; Sudut ≤ 0° atau ≥ 180°,	Contoh Masukan; 0°, -10°, 180°, 200°
Kategori; Sudut lancip,	Syarat; Sudut > 0° dan < 90°, Contoh Masukan;	30°, 45°, 75°
Kategori; Sudut siku-siku, Syarat;	Sudut = 90°, Contoh Masukan;	90°
Kategori; Sudut tumpul, Syarat;	Sudut > 90° dan < 180°, Contoh Masukan;	100°, 120°, 150°

Program akan memeriksa nilai sudut dari kondisi pertama hingga kondisi berikutnya. Jika nilai tidak berada di antara 0° dan 180°, maka masukan akan ditolak. Jika berada dalam rentang tersebut, program akan menentukan apakah sudut termasuk lancip, siku-siku, atau tumpul berdasarkan besar sudutnya.

## Hasil Pengujian
Hasil Pengujian

Pengujian dilakukan dengan memberikan beberapa contoh nilai sudut untuk memastikan program dapat memvalidasi masukan dan mengklasifikasikan jenis sudut dengan benar. Hasil yang diperoleh dibandingkan dengan keluaran yang seharusnya muncul.

No.	Masukan	Keluaran yang Diharapkan	                                              Keluaran Aktual  	Status
1 	-10°	  Masukan ditolak karena sudut harus lebih dari 0° dan kurang dari 180° 	Masukan ditolak 	Berhasil
2	   0°   	Masukan ditolak karena sudut harus lebih dari 0° dan kurang dari 180°	  Masukan ditolak 	Berhasil
3	  45°	    Sudut lancip karena nilainya lebih dari 0° dan kurang dari 90°	        Sudut lancip	    Berhasil
4  	90°   	Sudut siku-siku karena nilainya tepat 90°                             	Sudut siku-siku 	Berhasil
5 	120°   	Sudut tumpul karena nilainya lebih dari 90° dan kurang dari 180°      	Sudut tumpul	    Berhasil
6 	180°	  Masukan ditolak karena sudut harus lebih dari 0° dan kurang dari 180° 	Masukan ditolak  	Berhasil
7 	200°  	Masukan ditolak karena sudut harus lebih dari 0° dan kurang dari 180° 	Masukan ditolak	  Berhasil

Berdasarkan hasil pengujian, program dapat menerima masukan berupa besar sudut, melakukan validasi terhadap nilai tersebut, kemudian menentukan jenis sudut sesuai dengan kondisi yang telah ditentukan. Seluruh contoh pengujian menghasilkan keluaran yang sesuai dengan yang diharapkan.

## Refleksi
Refleksi

Salah satu masukan tidak valid yang semula terlewat adalah ketika pengguna memasukkan nilai sudut 0°. Awalnya, nilai tersebut belum ditangani dengan baik karena sudut yang valid harus lebih dari 0° dan kurang dari 180°.

Untuk mengatasinya, saya menambahkan kondisi validasi sudut <= 0 or sudut >= 180. Dengan kondisi tersebut, nilai 0° maupun nilai di luar rentang 0° sampai 180° akan ditolak oleh program dan diberikan keterangan bahwa masukan tidak valid.
