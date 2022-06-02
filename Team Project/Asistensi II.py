from ast import Return
import datetime as dt
from tkinter import END

while True: 
    x = "T" 
    print("==================================================")
    print("=Selamat Datang di Program Pemesanan Paket Travel=")
    print("==================================================")
    def menu ():
        print("[1] Register")
        print("[2] Validasi")
        print("[3] Refund")
    menu ()
    Menu = int(input("Masukkan pilihan menu Anda = ")) 
    print("==================================================")
    while Menu != 3:
        if Menu == 1:
            Nama_pemesan = str(input("Nama          = "))
            umur_pemesan = int(input("Umur          = "))
            if umur_pemesan < 17:
                print("=================================================================================")
                print("Mohon Maaf Umur Anda Belum Mencukupi")
                print("=================================================================================")
                menu ()
                Menu = int(input("Masukkan pilihan menu Anda = ")) 
                print("=================================================================================")
            else:
                nomer = int(input("Nomor Telepon = "))
                print("=========================================================================================")
                def kota ():
                    print("Kota Tujuan Wisata")
                    print("[1] Bali")
                    print("[2] Lombok")
                    print("[3] Jogjakarta")
                    print("[4] Jakarta - Bandung")
                    print("[5] Labuan Bajo")
                kota ()
                Kota = int(input("Kota yang dipilih = ")) 
                print("=========================================================================================")
                while kota != 5:
                    if Kota == 1:
                        jk = 1
                        nk = "BALI"
                        No = 6
                        PaketWisata1_Bali = ("3 hari 2 Malam", "Favehotel Kuta Kartika Plaza", "7X makan", "Mobil Avanza","7 Destinasi " , "Rp 2.800.000")
                        PaketWisata2_Bali = ["5 hari 4 Malam ", "Aston Hotel Kuta", "12X makan", "Mobil Innova", "16 Destinasi ", "Rp 5.500.000"]
                        print("\n                                    Daftar Paket Wisata Bali")
                        print("""
                    ----------------------------------------------------------
                    |No |        Paket Wisata 1         |   Paket Wisata 2   |
                    ----------------------------------------------------------""")
                        for i in range (No):
                            kolom_1 = str (i+1)
                            kolom_2 = str(PaketWisata1_Bali[i])
                            kolom_3 = str(PaketWisata2_Bali[i])
                            print('                    |' + kolom_1 + (3-len(kolom_1))*' '
                                + '| ' + kolom_2 + (30-len(kolom_2))*' '
                                + '| ' + kolom_3 + (17-len(kolom_3))*' '+ '  |')
                        print(110*"-")
                        print("Deskripsi Paket Wisata I Bali")
                        print("-----------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Bali menginap 3 hari 2 malam di hotel bintang tiga, 
dengan destinasi wisata yang terdiri dari Pantai Pandawa, Pantai Luhur Uluwatu, Pantai Kuta, 
Tegallalang Rice Terrace, Kintamani,  Desa Panglipuran, Tanah Lot, Joger dan mengelilingi 
exoticnya pulau Bali untuk lebih mengenal suku, budaya, dan alamnnya.""")
                        print(110*"-")
                        print("Deskripsi Paket Wisata II Bali")
                        print("------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Bali menginap 5 hari 4 malam di hotel bintang empat, 
dengan destinasi wisata yang terdiri dari Watersport Tanjung Benoa, Nusa Dua , Pulau Penyu, 
Garuda Wisnu Kencana, Pura Luhur Uluwatu, Pantai Pandawa, Tegallalang Rice Terrace, Kintamani,Toya Devasya, 
Desa Penglipuran,Pura Ulun Danu Beratan,Jatiluwih Rice Terrace, Pura Tanah Lot,Bali Zoo,Krisna Oleh Oleh, 
Joger Kuta, dan mengelilingi exoticnya pulau Bali untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        break
                    elif Kota == 2 :
                        jk = 2
                        nk = "LOMBOK"
                        No = 6
                        PaketWisata1_Lombok = [" 3 hari 2 Malam", "Hotel Svarga Resort", "7X makan", "Mobil Avanza","9 Destinasi " , "Rp 3.000.000"]
                        PaketWisata2_Lombok = [" 5 hari 4 Malam ", "Hotel Svarga Resort", "12x makan", "Mobil Innova", "15 Destinasi", "Rp. 5.500.000 "]
                        print("\n                                   Daftar Paket Wisata Lombok")
                        print("""
                    ----------------------------------------------------
                    | No |   Paket Wisata 1    |     Paket Wisata 2    | 
                    ----------------------------------------------------""")
                        for i in range (No):
                            kolom_1 = str (i+1)
                            kolom_2 = str(PaketWisata1_Lombok[i])
                            kolom_3 = str(PaketWisata2_Lombok[i])
                            print('                    |' + kolom_1 + (4-len(kolom_1))*' '
                                + '| ' + kolom_2 + (20-len(kolom_2))*' '
                                + '| ' + kolom_3 + (20-len(kolom_3))*' '+ '  |')
                        print(110*"-")
                        print("Deskripsi Paket Wisata I Lombok")
                        print("-------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Lombok menginap 3 hari 2 malam di hotel bintang empat, 
dengan destinasi wisata yang terdiri dari  Desa Sukarara, Pantai Kuta Mandalika Lombok,  Bukit Merese,
Gili Trawangan,cBukit Malaka/ Malimbu, Pusat Oleh-oleh,Pelabuhan Teluk Nare, Monkey Forest, Pura Taman 
Narmada, dan mengelilingi exoticnya pulau Lombok untuk lebih mengenal suku,budaya, dan alamnya.""")
                        print(110*"-")
                        print("Deskripsi Paket Wisata II Lombok")
                        print("--------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Lombok menginap 5 hari 4 malam di hotel bintang empat, 
dengan destinasi wisata yang terdiri dari Desa Sukarara, Pantai Kuta Mandalika Lombok, Pantai Tanjung Aan, 
Bukit Merese, I Monkey Forest, Pelabuhan Teluk Nare, Gili Trawangan,  Bukit Malaka/ Malimbu, 
Desa Senaru, Air Terjun Sendang Gile, Pusat  Oleh – Oleh, Pelabuhan Tanjung Luar, 
Pantai Pink (pink 1 & pink 2), Gili Petelu, Pura Taman Narmada, 
dan mengelilingi exoticnya pulau Lombok untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        break
                    elif Kota == 3 :
                        jk = 3
                        nk = "JOGJA"
                        No = 6
                        PaketWisata1_Jogja = [" 3 hari 2 Malam", "Hotel Grand Sarila", "7X makan", "Mobil Avanza","7 Destinasi " , "Rp 2.100.000"]
                        PaketWisata2_Jogja = [" 5 hari 4 Malam", "Hotel Grand Sarila", "12x makan", "Mobil Innova", "11 Destinasi", "Rp. 4.000.000"]
                        print("\n                                Daftar Paket Wisata Jogjakarta")
                        print("""
                    ----------------------------------------------------
                    | No |   Paket Wisata 1    |     Paket Wisata 2    |
                    ----------------------------------------------------""")
                        for i in range (No):
                            kolom_1 = str (i+1)
                            kolom_2 = str(PaketWisata1_Jogja[i])
                            kolom_3 = str(PaketWisata2_Jogja[i])
                            print('                    |' + kolom_1 + (4-len(kolom_1))*' '
                                + '| ' + kolom_2 + (20-len(kolom_2))*' '
                                + '| ' + kolom_3 + (20-len(kolom_3))*' '+ '  |')
                        print(110*"-")
                        print("Deskripsi Paket Wisata I Jogjakarta")
                        print("-----------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Yogyakarta menginap 5 hari 3 malam di hotel bintang 
tiga, dengan destinasi wisata yang terdiri dari Keraton Kasultanan Yogyakarta, Istana Taman Sari, 
Candi Borobudur, Desa Wisata Bukit Teletubbies, Taman Lampion Pelangi, Alun-Alun Kota Jogja, 
Candi Prambanan, Gunung Kidul, Museum Gunung Merapi, Pabrik Batik, Bukit Kali Kuning, dan 
mengelilingi exoticnya Kota Yogyakarta untuk lebih mengenal suku, budaya, dan alamnya. """)
                        print(110*"-")
                        print("Deskripsi Paket Wisata II Jogjakarta")
                        print("------------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Yogyakarta menginap 5 hari 3 malam di hotel bintang tiga, 
dengan destinasi wisata yang terdiri dari Keraton Kasultanan Yogyakarta, Istana Taman Sari, 
Candi Borobudur, Desa Wisata Bukit Teletubbies, Taman Lampion Pelangi, Alun-Alun Kota Jogja, 
Candi Prambanan, Gunung Kidul, Museum Gunung Merapi, Pabrik Batik, Bukit Kali Kuning, dan 
mengelilingi exoticnya Kota Yogyakarta untuk lebih mengenal suku, budaya, dan alamnya. """)
                        print(110*"-")
                        break
                    elif Kota == 4 :
                        jk = 4
                        nk = "JAKARTA-BANDUNG"
                        No = 6
                        PaketWisata1_JB = [" 3 hari 2 Malam", "Hotel Atlantic City", "5X makan", "Mobil Avanza"," 7 Destinasi " , "Rp 2.400.000"]
                        PaketWisata2_JB = [" 5 hari 4 Malam ", "Hotel Meize Bandung", "12x makan", " Mobil Avanza", " 10 Destinasi", "Rp. 3.650.000"]
                        print("\n                               Daftar Paket Wisata Jakarta - Bandung")
                        print("""
                        ----------------------------------------------------
                        | No |   Paket Wisata 1    |     Paket Wisata 2    |
                        ----------------------------------------------------""")
                        for i in range (No):
                            kolom_1 = str (i+1)
                            kolom_2 = str(PaketWisata1_JB[i])
                            kolom_3 = str(PaketWisata2_JB[i])
                            print('                        |' + kolom_1 + (4-len(kolom_1))*' '
                                + '| ' + kolom_2 + (20-len(kolom_2))*' '
                                + '| ' + kolom_3 + (20-len(kolom_3))*' '+ '  |')
                        print(110*"-")
                        print("Deskripsi Paket Wisata I Jakarta-Bandung")
                        print("----------------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata  Jakarta-Bandung menginap 3 hari 2 malam di hotel bintang tiga
dengan destinasi wisata yang terdiri dari Tangkuban Perahu, Floating Market, Orchid Forest, 
Kawah Putih, Glamping Lakeside, Kebun Teh Rancabali, Bandung City Tour dan Cibaduyut, dan mengelilingi
exoticnya Kota Jakarta-Bandung untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        print("Deskripsi Paket Wisata II Jakarta-Bandung")
                        print("-----------------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata Jakarta-Bandung menginap 5 hari 4 malam di hotel bintang tiga 
dengan destinasi wisata yang terdiri dari Factory Outlet, Lembang, Tangkuban Perahu, Ciwalk, 
Primasari, Cibaduyut, Kawah Putih, Monas, Thamrin City, Pantai Indah Kapuk 2 (PIK-2), dan 
mengelilingi exoticnya Kota Jakarta-Bandung untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        break
                    elif Kota == 5 :
                        jk = 5
                        nk = "LABUAN BAJO"
                        No = 6
                        PaketWisata1_LB = [" 3 hari 2 Malam", "Hotel Ende", "7X makan", "Mobil Innova"," 11 Destinasi " , "Rp 1.700.000"]
                        PaketWisata2_LB = [" 4 hari 3 Malam ", "Hotel Twin Share", "9x makan", "Mobil Innova", "14 Destinasi", "Rp.3.000.000"]
                        print("\n                                   Daftar Paket Wisata Labuan Bajo")
                        print("""
                        ----------------------------------------------------
                        | No |   Paket Wisata 1    |     Paket Wisata 2    |
                        ----------------------------------------------------""")
                        for i in range (No):
                            kolom_1 = str (i+1)
                            kolom_2 = str(PaketWisata1_LB[i])
                            kolom_3 = str(PaketWisata2_LB[i])
                            print('                        |' + kolom_1 + (4-len(kolom_1))*' '
                                + '| ' + kolom_2 + (20-len(kolom_2))*' '
                                + '| ' + kolom_3 + (20-len(kolom_3))*' '+ '  |')
                        print(110*"-")
                        print("Deskripsi Paket Wisata I Labuan Bajo")
                        print("------------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Labuan Bajo menginap 3 hari 2 malam di hotel bintang tiga,
dengan destinasi wisata yang terdiri dari Kampung Adat Bena, Pemandian Air Panas Soa, Kawasan Riung 17, 
Kalong Hill, Pulau Ontoloe, Pulau Rutong, Pulau Tiga, Pulau Tembang, Kelimutu, Tempat Pengasingan Bung Karno, 
Pasar Ende ,dan mengelilingi exoticnya pulau Lombok untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        print("Deskripsi Paket Wisata II Labuan Bajo")
                        print("-------------------------------------")
                        print("""Kami menyiapkan jadwal standar kegiatan wisata di Labuan Bajo menginap 4 hari 3 malam di hotel bintang tiga, 
dengan destinasi wisata yang terdiri dari Kampung Adat Ratenggaro, Pantai Bawana, Pantai Mandorak, 
Danau Weekuri, Kampung Adat Praijing, Sunset Bukit Wairinding, Savana Puru Kambera, Pantai Puru Kambera, 
Air Terjun Waimarang, Sunset Pantai Walakiri, Milky Way dan Sunrise Bukit Tenau,Tenun Ikat, Toko Souvenir
di Sumba Timur , dan mengelilingi exoticnya pulau Lombok untuk lebih mengenal suku, budaya, dan alamnya.""")
                        print(110*"-")
                        break
                    else:
                        END
                x = str(input("Konfirmasi pemesanan, jika Lanjut ketik L/l, jika tidak ketik T/t = "))
                if x== "L" or x == "l":
                    print("==================================================")
                    jp = int(input('[1] Jenis Paket Wisata = '))

                    
                    #jk = int(input('[2] Kota = '))
                    jo = int(input('[2] Jumlah Orang = '))
                    if jk == 1 and jp == 1:
                        kota = "BALI"
                        harga = 2800000
                    elif jk == 1 and jp == 2:
                        kota = "BALI"
                        harga = 5500000
                    elif jk == 2 and jp == 1:
                        kota = "LOMBOK"
                        harga = 3500000
                    elif jk == 2 and jp == 2:
                        kota = "LOMBOK"
                        harga = 5500000
                    elif jk == 3 and jp == 1:
                        kota = "JOGJA"
                        harga = 2100000
                    elif jk == 3 and jp == 2:
                        kota = "JOGJA"
                        harga = 4000000
                    elif jk == 4 and jp == 1:
                        kota = "JAKARTA-BANDUNG"
                        harga = 2400000
                    elif jk == 4 and jp == 2:
                        kota = "JAKARTA-BANDUNG"
                        harga = 3650000
                    elif jk == 5 and jp == 1:
                        kota = "LABUAN BAJO"
                        harga = 1700000
                    elif jk == 5 and jp == 2:
                        kota = "LABUAN BAJO"
                        harga = 2300000
                    else:
                        print('EROR')
                    total = harga * jo
                    #print(f'{kota}, harga total : Rp. {total:,} ,-')
                    print('[4] Silahkan Masukkan = ')
                    tanggal = int(input("    Tanggal \t      = "))
                    bulan = int(input("    Bulan \t      = "))
                    tahun = int(input("    Tahun \t      = "))
                    tanggalkeberangkatan = dt.date(tahun,bulan,tanggal)
                    print(f"Tanggal Keberangkatan = {tanggalkeberangkatan}")
                    print("==================================================")
                    menu ()
                    Menu = int(input("Masukkan pilihan menu Anda = ")) 
                    print("==================================================")
                    while Menu != 3:
                        if Menu == 2:
                            print("Validasi Data")
                            print("------------------------------------")
                            print("Nama Pemesan = ", Nama_pemesan)
                            print("Nomor Telepon = ", nomer)
                            print("------------------------------------")
                            print("Jenis Paket Wisata    = ", jp,"Kota", nk)
                            print("Jumlah Orang          = ", jo)
                            print("Tanggal Keberangkatan = ", tanggalkeberangkatan)
                            print("------------------------------------")
                            v = input("Apakah data sudah valid (Sudah/Belum) ? ")
                            if v.lower() == "belum":
                                Return (Menu)
                                break
                            elif v.lower() == "sudah":
                                print("WELCOME TO SISTEM PEMBAYARAN")
                                print("")
                                #print("Pilihan metode (Transfer via Bank, E-wallet)")
                                print('''
                                Pilihan metode :

                                Kode 1 : Transfer via Bank
                                Kode 2 : E-wallet
                                ''')
                                metode = int(input("Sistem Pembayaran : "))
                                if metode == 1:
                                    metodes = "TRANSFER VIA BANK"
                                    print(metodes)
                                    print("")
                                    print('''
Silakan transfer ke rekening berikut

NO REK : 122811802120
ATAS NAMA : RUBY

                                    ''')
                                elif metode == 2:
                                    metodes = "TRANSFER VIA E-WALLET"
                                    print(metodes)
                                    print("")
                                    print('''

1.  Gopay
    Nomor : 08124248188
    Atas Nama : Ruby
2.  Dana
    Nomor : 08124248188
    Atas Nama : Ruby
3.  OVO
    Nomor : 08124248188
    Atas Nama : Ruby
                                    ''')
                                print(f'''

NAMA PEMESAN : {Nama_pemesan}
TUJUAN       : {kota}
PAKET WISATA : {jp}
TOTAL HARGA  : Rp. {total:,} ,-
METODE BAYAR : {metodes}
                                
TERIMA KASIH

                                ''')
                                break
                            else:
                                print("Data yang anda masukkan salah")
                                break
                        else:
                            break
                    break
                break