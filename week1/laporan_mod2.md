# LAPORAN PRAKTIKUM MODUL 2

Nama: Glory Leonthine Angi
NIM: 103072400058

## Tujuan Praktikum
Menggunakan wireshark untuk mengamati dan menganalisis paket data dalam jaringan komputer.

## Menjalankan Wireshark
1. Jalankan aplikasi wireshark

2. Pada tampilan awal, dibawah capture terdapat daftar interface, klik dua kali pada interface **"Wi-Fi"**.
![tampilan awal](../assets/image/mod2.png)
wireshark akan langsung mulai menangkap paket data yang lewat melalui koneksi Wi-Fi.
![melalukan capture](../assets/image/mod2(1).png)

3. Setelah memulai pengambilan paket data, kita dapat menghentikannya dengan cara mengklik ikon **"kotak merah"** disebelah sirip wireshark.
![menghentikan](../assets/image/mod(2).png)

4. Untuk menjalankan kembali, klik ikon **"sirip wireshark"** dan pilih **"continue without saving"** jika tidak ingin menyimpan hasil sebelumnya.
![menjalankan kembali](../assets/image/mod(3).png)

### **Catatan:** 
Jika komputer tidak terhubung ke koneksi Wi-Fi, proses capture akan otomatis berhenti. Jika koneksi WI-Fi tersambung kembali, wireshark akan melanjutkan penangkapan paket tanpa perlu memulai ulang.
![tanpa koneksi Wi-Fi](../assets/image/mod(4).png)
![terhubung kembali ke Wi-Fi](../assets/image/mod(5).png)

5. Untuk menghasilkan lalu lintas jaringan, buka browser dan masukkan URL: http://gaia.cs.umass.edu/wireshark
labs/INTRO-wireshark-file1.html 

### **Catatan:**
- Jika URL otomatis berubah menjadi **"https"**, halaman tidak akan menampilkan pesan **"Congratulations! You've downloaded the first Wireshark lab file!"**. Pastikan huruf **"s"** dihapus sehingga tetap menggunakan "**http**".
![https error](../assets/image/mod2(6).png)

- Jika sudah diubah ke http tetapi masih error, lakukan langkah ini:
    1. Klik kanan di browser > pilih **"Inspect"**.
    ![inspect](../assets/image/mod2(11).png)

    2. Masuk ke menu **"Application"** > **"Cookies"**.

    3. Klik kanan pada cookies browser yang ada, lalu pilih **"Clear"**.
    ![Application & clear cookies](../assets/image/mod2(7).png)

    4. Refresh halaman.
    ![error berhasil teratasi](../assets/image/mod2(8).png)

- Jika masih error, coba gunakan aplikasi lain untuk membuka.

6. Setelah halaman berhasil ditampilkan di browser, kembali ke aplikasi wireshark dan hentikan proses capture agar data tidak terus bertambah.

7. Ketik **"http"** di kolom display filter lalu tekan enter. Wireshark akan menampilan paket HTTP saja.

8. Cari alamat URL yang sebelumnya dimasukkan muncul di daftar paket. Jika terbaca, berarti proses berhasil.
![paket HTTP & URL muncul](../assets/image/mod2(9).png)

9. Cari paket dengan info bertulisan **"HTTP/1.1 200 OK (text/html)"** dan length sekitar 499.
![HTTP/1.1 200 OK (text/html)](../assets/image/mod2(12).png)

10. Klik paket tersebut, lalu pada detail protokol HTTP akan menampilkan pesan “Congratulations! You've downloaded the first Wireshark lab file!” seperti pada browser yang telah kita buka tadi.
![menampilkan pesan](../assets/image/mod2(10).png)

11. Running berhasil dan keluar dari wireshark.