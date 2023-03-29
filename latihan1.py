import getpass

while (True) :
    print("""\tApeVac (aplikasi Pencatatan Vaksinasi Covid-19)
------------------------------------------------------------------
[1] Data Warga Gang Sahabat RT.16
[2] Pencatatan Data Vaksinasi Covid-19
[3] Untuk Keluar
------------------------------------------------------------------""")

    menu = int(input("Pilih menu 1-3 : "))

    if menu == 1:
        print("\nDATA VAKSINASI WARGA")
        print("=========================================================")

        database = open("data_baru.txt", "r")
        data = database.readlines()
        for text in data:
            print (text)

        enter = input("\n\n\nTekan tombol apa saja untuk kembali...")
        print()

    elif menu == 2:
        print("\nArea Administrator")
        print("=========================================================")

        pass_idm = getpass.getpass('Masukan Password\t: ')
        konfirm = getpass.getpass('Konfirmasi Ulang Password\t: ')

        if pass_idm == konfirm:
            with open ("data_baru.txt", "a") as f:
                print('\nPencatatan Data Baru')

                nama = input("Nama = ")
                alamat = input("Alamat = ")
                vaksin = input("vaksin = ") 

                f.write(f"\nNama : {nama}|Alamat :{alamat}|Vaksin : {vaksin}")
                print()

        else :
            print("Password anda salah!!!\n")
            enter = ("\nTekan tombol apa saja untuk kembali...")
            print()
                
    elif menu == 3:
        print("\nProgram selesai...... \n")
        break