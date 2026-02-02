# Aplikasi Pengelola Uang Saku

Aplikasi berbasis command-line (CLI) untuk mengelola uang saku pribadi dengan fitur pencatatan pemasukan dan pengeluaran.

## Fitur Utama

✅ **Tambah Pemasukan** - Mencatat setiap pemasukan uang dengan keterangan
✅ **Tambah Pengeluaran** - Mencatat setiap pengeluaran dengan validasi saldo
✅ **Lihat Saldo** - Menampilkan saldo terkini dan riwayat transaksi
✅ **Menu Utama** - Interface user-friendly untuk navigasi

## Cara Menjalankan

```bash
python main.py
```

## Cara Penggunaan

1. Pilih menu dengan mengetik angka 1-4
2. **Menu 1**: Masukkan jumlah pemasukan dan keterangan
3. **Menu 2**: Masukkan jumlah pengeluaran dan keterangan
4. **Menu 3**: Lihat saldo dan riwayat transaksi
5. **Menu 4**: Keluar aplikasi

## Contoh Penggunaan

```
=== Aplikasi Pengelola Uang Saku ===
1. Tambah pemasukan
2. Tambah pengeluaran
3. Lihat saldo
4. Keluar
Pilih menu: 1
Masukkan jumlah pemasukan: Rp 50000
Masukkan keterangan (opsional): Gaji minggu ke-1
✓ Pemasukan Rp 50,000 berhasil ditambahkan!
```

## Persyaratan

- Python 3.6+

## Fitur Tambahan

- Validasi input untuk memastikan data yang benar
- Riwayat transaksi lengkap dengan keterangan
- Format tampilan uang dengan pemisah ribuan
- Pesan error yang informatif