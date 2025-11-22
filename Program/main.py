import os
from data import user
from auth import login, register
from mods import menu_mod
from akun import menu_akun
from utils import clear


while True:
    clear()
    print("=== Menu Utama ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihanMenu = input("Pilih menu (1/2/3): ").strip()

    if pilihanMenu == "2":
        register()
        input("Tekan Enter untuk kembali...")
        continue

    if pilihanMenu == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    if pilihanMenu == "1":
        hasiLogin = login(user)
        if not hasiLogin:
            input("Login gagal. Tekan Enter...")
            continue
        usernameLogin, roleLogin = hasiLogin
        while True:
            clear()

            if roleLogin == "superadmin":
                print("=== MENU SUPERADMIN ===")
                print("1. Menu Akun")
                print("2. Menu Mod")
                print("3. Logout")

                pilihSA = input("Pilih menu: ").strip()

                if pilihSA == "1":
                    menu_akun(usernameLogin, user)
                    input("Tekan Enter...")
                    continue
                elif pilihSA == "2":
                    menu_mod(usernameLogin, user)
                    continue
                elif pilihSA == "3":
                    print("Logout berhasil.")
                    break 
                else:
                    print("Pilihan tidak valid.")
                    input("Enter...")
                    continue

            elif roleLogin == "admin":
                print("=== MENU ADMIN ===")
                print("1. Menu Akun")
                print("2. Logout")
                pilihanA = input("Pilih menu: ").strip()

                if pilihanA == "1":
                    menu_akun(usernameLogin, user)
                    continue
                    
                elif pilihanA == "2":
                    print("Logout berhasil.")
                    break

                else:
                    input("Pilihan tidak valid. Tekan enter...")
                    continue

            elif roleLogin == "user":
                print("=== MENU USER ===")
                print("1. Menu Mod ")
                print("2. Logout")

                pilihanU = input("Pilih menu: ").strip()

                if pilihanU == "1":
                    menu_mod(usernameLogin, user)
                    continue

                elif pilihanU == "2":
                    print("Logout berhasil.")
                    break

                else:
                    print("Pilihan tidak valid.")
                    input("Enter...")
                    continue

            else:
                print("Role tidak dikenali!")
                input("Tekan Enter...")
                break

    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter...")
        continue
