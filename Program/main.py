import os
from auth import login
os.system('cls')

while True:
    os.system('cls')
    print("=== Menu Utama ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihanMenu = input("Pilih menu (1/2/3): ")
    
    #if pilihanMenu == '1':
        #login()
    # while True:
    #     os.system('cls')
    #     if roleLogin == 'superadmin':
    #         # Menu Superadmin 
    #     elif roleLogin == 'admin':
    #         # Menu Admin
    #     elif roleLogin == 'user':
    #         # Menu User
    #     else:
    #         print("Role tidak dikenali.")
    #         break
    #elif pilihanMenu == '2':
        #register()
    
    if pilihanMenu == '3':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        continue