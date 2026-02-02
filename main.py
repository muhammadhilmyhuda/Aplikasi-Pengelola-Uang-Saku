from datetime import datetime
import json
import os

saldo = 0
riwayat_transaksi = []
FILE_DATA = "data_keuangan.json"

def load_data():
    """Membaca data dari file JSON"""
    global saldo, riwayat_transaksi
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, 'r') as file:
                data = json.load(file)
                saldo = data.get("saldo", 0)
                riwayat_transaksi = data.get("riwayat_transaksi", [])
                print("✓ Data berhasil dimuat dari file!")
        except Exception as e:
            print(f"⚠ Error membaca file: {e}")
    else:
        print("ℹ File data tidak ditemukan, memulai dengan data baru.")

def save_data():
    """Menyimpan data ke file JSON"""
    try:
        data = {
            "saldo": saldo,
            "riwayat_transaksi": riwayat_transaksi
        }
        with open(FILE_DATA, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"✗ Error menyimpan file: {e}")

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: Rp "))
        if jumlah > 0:
            saldo += jumlah
            keterangan = input("Masukkan keterangan: ").strip()
            tanggal = input("Masukkan tanggal transaksi (DD-MM-YYYY) atau tekan Enter untuk hari ini: ").strip()
            
            if not tanggal:
                tanggal = datetime.now().strftime("%d-%m-%Y")
            
            riwayat_transaksi.append({
                "jenis": "Pemasukan",
                "jumlah": jumlah,
                "keterangan": keterangan,
                "tanggal": tanggal
            })
            save_data()
            print(f"✓ Pemasukan Rp {jumlah:,.0f} berhasil ditambahkan!")
        else:
            print("✗ Jumlah harus lebih dari 0!")
    except ValueError:
        print("✗ Input tidak valid! Masukkan angka.")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: Rp "))
        if jumlah > 0:
            if saldo >= jumlah:
                saldo -= jumlah
                keterangan = input("Masukkan keterangan: ").strip()
                tanggal = input("Masukkan tanggal transaksi (DD-MM-YYYY) atau tekan Enter untuk hari ini: ").strip()
                
                if not tanggal:
                    tanggal = datetime.now().strftime("%d-%m-%Y")
                
                riwayat_transaksi.append({
                    "jenis": "Pengeluaran",
                    "jumlah": jumlah,
                    "keterangan": keterangan,
                    "tanggal": tanggal
                })
                save_data()
                print(f"✓ Pengeluaran Rp {jumlah:,.0f} berhasil dicatat!")
            else:
                print(f"✗ Saldo tidak cukup! Saldo saat ini: Rp {saldo:,.0f}")
        else:
            print("✗ Jumlah harus lebih dari 0!")
    except ValueError:
        print("✗ Input tidak valid! Masukkan angka.")

def lihat_saldo():
    print("\n" + "="*40)
    print(f"Saldo Saat Ini: Rp {saldo:,.0f}")
    print("="*40 + "\n")

def laporan_keuangan():
    print("\n" + "="*60)
    print("LAPORAN KEUANGAN".center(60))
    print("="*60)
    print(f"Saldo Saat Ini: Rp {saldo:,.0f}".center(60))
    print("="*60)
    
    if riwayat_transaksi:
        total_pemasukan = 0
        total_pengeluaran = 0
        
        print("\nDETAIL TRANSAKSI:")
        print("-"*60)
        print(f"{'No':<4} {'Tanggal':<12} {'Jenis':<12} {'Jumlah':<15} {'Keterangan':<15}")
        print("-"*60)
        
        for i, transaksi in enumerate(riwayat_transaksi, 1):
            jenis = transaksi['jenis']
            jumlah = transaksi['jumlah']
            tanggal = transaksi['tanggal']
            keterangan = transaksi['keterangan'][:12] if transaksi['keterangan'] else "-"
            
            print(f"{i:<4} {tanggal:<12} {jenis:<12} Rp {jumlah:>12,.0f}  {keterangan:<15}")
            
            if jenis == "Pemasukan":
                total_pemasukan += jumlah
            else:
                total_pengeluaran += jumlah
        
        print("-"*60)
        print(f"{'TOTAL PEMASUKAN':<28} Rp {total_pemasukan:>12,.0f}")
        print(f"{'TOTAL PENGELUARAN':<28} Rp {total_pengeluaran:>12,.0f}")
        print("="*60)
    else:
        print("Belum ada transaksi.")
        print("="*60)
    print()

def menu():
    print("\n" + "="*40)
    print("=== MENU UTAMA ===".center(40))
    print("="*40)
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Laporan Keuangan")
    print("5. Keluar")
    print("="*40)

load_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        laporan_keuangan()
    elif pilihan == "5":
        save_data()
        print("\nTerima kasih telah menggunakan Aplikasi Pengelola Uang Saku!")
        break
    else:
        print("✗ Pilihan tidak valid! Silakan pilih 1-5.")
