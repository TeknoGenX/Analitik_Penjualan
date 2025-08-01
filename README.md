## 📊 Analitik Penjualan

Proyek ini adalah aplikasi web **Analitik Penjualan** berbasis **Django** yang memungkinkan pengguna untuk mengelola portofolio proyek, analisis data penjualan, dashboard interaktif, form kontak, dan blog sederhana. Dibangun dengan prinsip modular dan terstruktur, proyek ini cocok untuk pembelajaran dan pengembangan sistem analitik internal perusahaan.

---

### 🚀 Fitur Utama

* 📁 **Manajemen Proyek Portofolio**
  CRUD proyek dengan kategori dan gambar.

* 💬 **Komentar Proyek**
  Pengunjung dapat meninggalkan komentar pada setiap proyek.

* 📈 **Dashboard UI**
  Tampilan dashboard analitik berbasis template dengan integrasi data dari model.

* 📊 **Sales Analytics**
  Analisis data penjualan sederhana melalui `sales_analytics` app.

* ✉️ **Form Kontak**
  Kirim pesan ke admin dengan validasi form.

* 📝 **Blog**
  Artikel blog untuk berbagi berita atau informasi.

---

### 🧱 Struktur Aplikasi Django

```bash
Analitik_Penjualan/
├── manage.py
├── db.sqlite3
├── myproject/            # Konfigurasi utama Django
├── portfolio/            # Manajemen proyek & komentar
├── contact/              # Form kontak
├── blog/                 # Sistem blog
├── dashboard_ui/         # Dashboard interaktif
├── sales_analytics/      # App analitik penjualan
├── templates/            # Template global
├── static/               # Aset statis global
└── media/                # Upload gambar
```

---

### 🛠️ Cara Menjalankan Proyek

1. **Klon repositori:**

   ```bash
   git clone https://github.com/TeknoGenX/Analitik_Penjualan.git
   cd Analitik_Penjualan
   ```

2. **Aktifkan virtual environment (jika belum):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # di Linux/macOS
   venv\Scripts\activate     # di Windows
   ```

3. **Install dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasi database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Jalankan server lokal:**

   ```bash
   python manage.py runserver
   ```

6. **Akses di browser:**

   ```
   http://127.0.0.1:8000/
   ```

---

### 👤 Admin & Login

Untuk login admin:

```bash
python manage.py createsuperuser
```

---

### 📂 Lisensi

Proyek ini berada di bawah lisensi [MIT License](LICENSE) — silakan digunakan dan dikembangkan lebih lanjut!

---

### 🙌 Kontribusi

Pull Request dan Issue sangat dipersilakan! Jangan lupa beri bintang ⭐ kalau kamu suka proyek ini.

---

> Dibuat oleh **[TeknoGenX](https://github.com/TeknoGenX)**

---

