saldo= 10000000
nrp = "12345"
    

def transaksi(id_menu):
    global saldo
    id_menu = int(id_menu)
    print("--"*50)
    if id_menu == 1:
        print("anda memilih untuk cek saldo")
    elif id_menu == 2:
        print ("anda memilih untuk tarik tunai:")
        nilai = input ("Masukkan jumlah yang akan diambil: ")
        if nilai.isnumeric():
            nilai = int(nilai)
           
            if saldo>nilai:
                print("Anda menarik tunai sebesar Rp : {0:,}".format(nilai))
                saldo -= int(nilai)
            else:
                print(" Maaf Saldo anda tidak cukup")  
      
        else:
            print("Anda tidak memasukkan jumlah yang benar.")
    elif id_menu ==3:
        print("anda memilih untuk setor tunai")
        nilai = input ("Masukkan nilai yang akan dideposit: ")
        if nilai.isnumeric():
            nilai = int(nilai)
            print("Anda sudah mendepositkan sebesar Rp : {0:,}".format(nilai))
            saldo+=nilai
        else:
            print("Anda belum memasukkan angka deposit.")
    else:
        print("Terima kasih dan sampai jumpa")
        exit()
        return 0;
        
        
    print("Nilai saldo anda sekarang Rp {0:,}".format(saldo))
    print("--"*50)
    print()
    penutup()

def mainmenu():
    print()
    print()
    print("Pilih menu transaksi:")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor tunai")
    print("4. Keluar sistem")
    print()
    print()
    pilihan_menu = input ("Menu yang dipilih (1,2,3,4):  ")
    if pilihan_menu.isnumeric():
        transaksi(pilihan_menu)
    else:
        print("ada kesalahan dalam pemilihan menu")
        penutup()
    

def penutup():
    closing = input("Apakah anda ingin melakukan transaksi yang lain? (Y atau N):  ")
    if (closing.upper()=="Y"):
        mainmenu()
    elif (closing.upper()=="N"):
        #break
        print("Terima kasih sudah memakai layanan ATM sederhana")
    else:
        print("Terima kasih sudah memakai layanan ATM sederhana")
        exit()

print("="*25)
print()
print("SELAMAT DATANG DI ATM SEDERHANA")
print()
print("="*25)

norek = input("Masukkan Nomor Rekening: ")

while (norek == nrp):
    print("-"*40)
    print("saldo anda saat ini sebesar Rp {0:,}".format(saldo))
    print("-"*40)
    mainmenu()
else:
    print("Nomor Rekening yang anda masukkan salah.")
    print("Keluar dari sistem dan ulangi lagi")