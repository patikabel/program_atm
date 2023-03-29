import getpass
class Atm:
    def pilih_menu():
        saldo = 10000000
        print("="*36)
        print("             ATM BERSAMA       ")
        print(" Jl.S Parman No.14 Balikpapan Tengah")
        print("           Telp.0542-48215")
        print("=========== MENU PILIHAN ===========")
        print("[1] Informasi Saldo")
        print("[2] Bayar")
        print("[3] Transfer")
        print("[4] Ambil Uang")
        print("[5] Exit")
        print("="*36)
        pilih = int(input("Masukkan Menu Pilihan [1/2/3/4/5]: "))
        if(pilih == 1):
            n = 1
            while(n == 1):
                print("Menu: INFORMASI SALDO")
                print("Informasi Rekening Tabungan")
                print("Informasi Giro")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue  
        elif(pilih == 2):
            n = 1
            while(n == 1):
                print("Menu: BAYAR")
                print("[1] BPJS\t[3] PDAM")
                print("[2] PLN\t[4] PULSA PASCABAYAR")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue  
        elif(pilih == 3):
            n = 1
            while(n == 1):
                print("Menu: TRANSFER")
                print("[1] Transfer Antar Bank")
                print("[2] Transfer Sesama Bank")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue            
        elif(pilih == 4):
            n = 1
            while(n == 1):
                print("Menu: AMBIL UANG")
                print("[1] Rp. 1.000.000,-")
                print("[2] Rp. 500.000,-")
                print("[3] Rp. 300.000,-")
                print("[4] Nominal Lain")
                print("="*36)
                ambil = int(input("Masukkan nilai uang yang akan di ambil [1/2/3/4]: "))
                uang1 = 1000000
                uang2 = 500000
                uang3 = 300000
                if(ambil == 1):
                    saldo = saldo - uang1
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 2):
                    saldo = saldo - uang2
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 3):
                    saldo = saldo - uang3
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 4):
                    uanglain = int(input("Masukkan nominal uang yang di ambil: Rp. "))
                    saldo = saldo - uanglain
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi baru [y/t]: ") 
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                else :
                    print("Maaf saldo anda tidak cukup")
                    kembali = input("Masukkan Transaksi baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                            
        elif(pilih == 5):
            print("Terima kasih silahkan ambil kartu anda")
            exit()  

                 
def menu_utama():
    pin = "12345"
    print("="*36)
    print("             ATM BERSAMA       ")
    print(" Jl.S Parman No.14 Balikpapan Tengah")
    print("           Telp.0542-48215")
    print("=========== MENU PILIHAN ===========")   
    for i in range(3) :
        sandi = getpass.getpass("Masukkan PIN Anda\t: ")
        if (sandi == pin):
            Atm.pilih_menu()
        else : 
            print('Pin anda salah!')
            if i == 2 :
                print("Anda telah melakukan 3x percobaan")
                print("Kartu ATM terblokir")
                exit() 
menu_utama()
   
        