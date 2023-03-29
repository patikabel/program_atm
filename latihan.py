class BangunDatar :
    def segitiga(): #method/function
        n = 1
        while(n == 1):
            print("menghitung luas segitiga")
            print("="*40)
            alas = float(input("Masukkan alas\t: "))
            tinggi = float(input("Masukkan tinggi\t: "))
            luas = (alas * tinggi)/2
            print("luas segitiga adalah\t: ",luas, "cm")
            coba = input("apakah ingin menhitung lagi (y/t): ")
            if(coba == "t"):
                break
    def persegipanjang():
        n = 1
        while(n == 1):
            print("menghitung luas persegi panjang")
            print("="*40)
            panjang = float(input("Masukkan panjang\t: "))
            lebar = float(input("Masukkan lebar\t: "))
            luas = (panjang * lebar)
            print("luas persegi panjang adalah\t: ",luas, "cm")
            coba = input("apakah ingin menhitung lagi (y/t): ")
            if(coba == "t"):
                break
    def lingkaran():
        n = 1
        while(n == 1):
            print("menghitung luas lingkaran")
            print("="*40)
            r = float(input("Masukkan jari-jari\t: "))
            luas = (22/7)*r*r
            print("luas lingkaran adalah\t: ",luas, "cm")
            coba = input("apakah ingin menhitung lagi (y/t): ")
            if(coba == "t"):
                break
                
def menu_awal():
    while(True):
        print("="*40)
        print("Aplikasi Hitung Bangun Datar")
        print("="*40)
        print("pilihan rumus bangun datar :")
        print("[1] Hitung Luas Segitiga")
        print("[2] Hitung Luas Persegi Panjang")
        print("[3] Hitung Luas Lingkaran")
        print("[4] Keluar Dari apk")
        print("="*35)
        pil = int(input("Masukkan Pilihan Anda\t: "))
        if(pil == 1):
            BangunDatar.segitiga()
        elif (pil == 2):
            BangunDatar.persegipanjang()
        elif (pil == 3):
            BangunDatar.lingkaran()
        elif (pil == 4):
            print("Terimakaciwww")
            exit()
        else :
            print("masukkan pilihan dengan benar")
menu_awal()   



