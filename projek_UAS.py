# Data awal
pemesan = set()  
pesanan_tiket = []
gerbong_kursi = {}  

# Kamus singkatan
kereta_dict = {'CLD': 'Commuter Line Dhoho', 'DP': 'Dhoho Panataran'}
kelas_dict = {'E': 'Ekonomi', 'B': 'Bisnis', 'V': 'VIP'}
kode_kereta = ('CLD', 'DP')
kode_kelas = ('E', 'B', 'V')

# Fungsi untuk mencatat gerbong dan kursi
def add_gerbong_kursi(gerbong, kursi):
    if gerbong not in gerbong_kursi:
        gerbong_kursi[gerbong] = set()  
    if kursi in gerbong_kursi[gerbong]:
        print(f"Kursi {kursi} di gerbong {gerbong} sudah terpesan. Silakan pilih kursi lain.")
        return False
    else:
        gerbong_kursi[gerbong].add(kursi)  
        return True

# Fungsi untuk membuat pemesanan baru
def Pemesanan_Baru():
    jumlah_tiket = int(input("Berapa tiket yang ingin dipesan? "))
    for i in range(jumlah_tiket):
        print(f"Pemesanan tiket ke-{i+1}")
        while True:
            nama_pemesan = input('Masukkan nama pemesan: ')
            if nama_pemesan == "":
                print("Tidak boleh kosong")
            else:
                break
        while True:
            nik = input('Masukkan NIK pemesan: ')
            if nik == "":
                print("Tidak boleh kosong")
            else:
                break

    
    # Cek apakah NIK sudah ada (menggunakan set untuk memastikan NIK unik)
        if nik in pemesan:
            print(f"Pemesan dengan NIK {nik} sudah terdaftar.")
            return

    # Memilih kode kereta dan kelas dari pilihan yang tersedia
        kode_kereta = input("Masukkan kode kereta CLD(Commuter Line Dhoho) | DP(Dhoho Panataran): ")
        if kode_kereta not in kode_kereta:
            print("Kode kereta tidak valid! Pilih dari CLD(Commuter Line Dhoho) | DP(Dhoho Panataran)!")
            return
    
        kode_kelas = input('Masukkan kode kelas kereta E(Ekonomi) | B(Bisnis) | V(VIP) : ')
        if kode_kelas not in kode_kelas:
            print("Kode kelas tidak valid! Pilih dari E(Ekonomi) | B(Bisnis) | V(VIP) !")
            return

    # Pemilihan Gerbong dan Kursi
        gerbong = input("Masukkan kode gerbong (1, 2, 3): ")
        kursi = input(f"Masukkan nomor kursi di {gerbong} (misal A1-A20):")
        
                    
    # Mengecek apakah kursi tersedia
        if not add_gerbong_kursi(gerbong, kursi):
            return  # Jika kursi sudah terpesan, keluar dari fungsi create_pesanan

        pemesan.add(nik)  # Menambahkan NIK ke set pemesan

        if kode_kereta == 'CLD':
            nama_kereta = kereta_dict['CLD']
            harga = {'E': 12000, 'B': 24000, 'V': 50000}[kode_kelas]
        else:
            nama_kereta = kereta_dict['DP']
            harga = {'E': 24000, 'B': 50000, 'V': 80000}[kode_kelas]

    # Menambahkan pesanan tiket ke list
        pesanan_tiket.append({
            'Nama Pemesan': nama_pemesan,
            'NIK': nik,
            'Kereta': nama_kereta,
            'Kelas Kereta': kode_kelas,
            'Harga': harga,
            'Gerbong': gerbong,
            'Kursi': kursi
        })
        print("Pemesanan berhasil!")

# Fungsi untuk menampilkan daftar pemesanan
def Daftar_pemesanan():
    # Menampilkan semua pemesanan dalam bentuk tabel
    if not pesanan_tiket:
        print("Tidak ada pemesanan.")
        return
    print(pesanan_tiket)

# Fungsi untuk mengupdate pemesanan
def Update_Pemesanan():
    nik = input("Masukkan NIK pemesan yang ingin diupdate: ")
    for pesanan in pesanan_tiket:
        if pesanan['NIK'] == nik:
            print("Data ditemukan! Silahkan masukkan update data:")
            pesanan['Nama Pemesan'] = input('Masukkan nama pemesan baru: ')
            pesanan['Kereta'] = input("Masukkan kode kereta baru CLD(Commuter Line Dhoho) | DP(Dhoho Panataran): ")
            pesanan['Kelas Kereta'] = input('Masukkan kode kelas kereta baru E(Ekonomi) | B(Bisnis) | V(VIP): ')
            pesanan['Gerbong'] = input('Masukkan gerbong baru (1, 2, 3): ')
            pesanan['Kursi'] = input(f"Masukkan nomor kursi baru di gerbong {pesanan['Gerbong']}: ")
            print("Pesanan berhasil diperbarui!")
            return
    print("Pesanan dengan NIK tersebut tidak ditemukan!")

# Fungsi untuk menghapus pemesanan
def Menghapus_Pemesanan():
    nik = input("Masukkan NIK pemesan yang ingin dihapus: ")
    for pesanan in pesanan_tiket:
        if pesanan['NIK'] == nik:
            pesanan_tiket.remove(pesanan)
            pemesan.remove(nik)  # Menghapus NIK dari set pemesan
            print(f"Pesanan dengan NIK {nik} berhasil dihapus.")
            return
    print("Pesanan tidak ditemukan!")

# Fungsi untuk memproses pembayaran
def Proses_Pembayaran():
    total = sum(pesanan['Harga'] for pesanan in pesanan_tiket)
    print(f"Total harga: {total}")
    if total > 30000:
        diskon = total * 0.05  # 5% diskon
    else:
        diskon = 0
    total_bayar = total - diskon
    print(f"Diskon: {diskon}")
    print(f"Total bayar: {total_bayar}")

    # Memeriksa apakah uang yang dibayar cukup
    uang_bayar = int(input("Masukkan uang pembayaran: "))
    total_bayar_sementara = uang_bayar
    
    while total_bayar_sementara < total_bayar:
        print(f"Uang Anda kurang! Anda masih perlu membayar {total_bayar - total_bayar_sementara}.")
        tambahan = int(input("Masukkan uang tambahan: "))
        total_bayar_sementara += tambahan  # Menambahkan uang yang dibayar lagi

    kembalian = total_bayar_sementara - total_bayar
    print(f"Kembalian: {kembalian}")


# Fungsi untuk mencetak tiket dalam format tabel
def Cetak_Tiket():
    # Menampilkan header tabel
    print("="*120)
    print(f"{'No':<5} {'Nama Pemesan':<20} {'NIK':<15} {'Kereta':<30} {'Kelas':<15} {'Gerbong':<10} {'Kursi':<10} {'Harga':<10}")
    print("="*120)

    # Menampilkan data setiap pemesanan tiket
    for i, pesanan in enumerate(pesanan_tiket):
        print(f"{i:<5} {pesanan['Nama Pemesan']:<20} {pesanan['NIK']:<15} {pesanan['Kereta']:<30} {pesanan['Kelas Kereta']:<15} {pesanan['Gerbong']:<10} {pesanan['Kursi']:<10} {pesanan['Harga']:<10}")
    
    print("="*120)
    
    # Menghitung total harga dari semua tiket
    total = sum(pesanan['Harga'] for pesanan in pesanan_tiket)
    print(f"{'Total Harga':<113} {total:<10}")
    print("="*120)

# Menu
while True:
    print("1. Pemesanan Baru")
    print("2. Daftar Pemesanan")
    print("3. Update Pemesanan")
    print("4. Menghapus Pemesanan")
    print("5. Proses Pembayaran")
    print("6. Cetak Tiket")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == '1':
       Pemesanan_Baru()
    elif pilihan == '2':
        Daftar_pemesanan()
    elif pilihan == '3':
        Update_Pemesanan()
    elif pilihan == '4':
        Menghapus_Pemesanan()
    elif pilihan == '5':
        Proses_Pembayaran()
    elif pilihan == '6':
        Cetak_Tiket()
    elif pilihan == '7':
        print("Terima kasih telah menggunakan program kami🙏!")
        break
    else:
        print("Pilihan tidak valid!")