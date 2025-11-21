import os
from data import user
from auth import login, register
from mods import menu_mod
os.system('cls')

while True:
    os.system('cls')
    print("=== Menu Utama ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihanMenu = input("Pilih menu (1/2/3): ")
    
    if pilihanMenu == '1':
        usernameLogin, roleLogin = login()
        while True:
            os.system('cls')
            if roleLogin == 'superadmin':
                print("=== MENU SUPERADMIN ===")
                print("1. Kelola Akun")
                print("2. Kelola Mod")
                print("3. Keluar")
                pilihanSuperAdmin = input("Pilih menu: ")
                if pilihanSuperAdmin == '1':
                    print("Fitur Kelola Akun belum tersedia.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                elif pilihanSuperAdmin == '2':
                    menu_mod(usernameLogin, user)
                elif pilihanSuperAdmin == '3':
                    break
            elif roleLogin == 'admin':
                print("Fitur untuk admin belum tersedia.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            elif roleLogin == 'user':
                menu_mod(usernameLogin, user)
            else:
              print("Role tidak dikenali.")
              break
    elif pilihanMenu == '2':
        print("Fitur Register belum tersedia.")
        input("Tekan Enter untuk melanjutkan...")
        continue
    
    if pilihanMenu == '3':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        continue
    

print("Tekan Enter untuk keluar...")