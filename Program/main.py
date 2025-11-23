from InquirerPy import inquirer
from data import user
from auth import login, register
from mods import menu_mod
from akun import menu_akun
from utils import clear


while True:
    clear()
    pilihanMenu = inquirer.select(message="=== MENU UTAMA ===",
                                choices=["Login", 
                                        "Register",
                                        "Keluar",],
                                pointer="👉",
                                qmark=" ",
                                amark=" "
                                ).execute()

    if pilihanMenu == "Register":
        register(user)
        input("Tekan Enter untuk kembali...")
        continue

    if pilihanMenu == "Keluar":
        print("Terima kasih telah menggunakan program ini.")
        break

    if pilihanMenu == "Login":
        hasiLogin = login(user)
        if not hasiLogin:
            input("Login gagal. Tekan Enter...")
            continue
        usernameLogin, roleLogin = hasiLogin
        while True:
            clear()

            if roleLogin == "superadmin":
                pilihSA = inquirer.select(message="=== MENU SUPERADMIN ===",
                                            choices=["Menu Akun", 
                                                    "Menu Mod",
                                                    "Logout",],
                                            pointer="👉",
                                            qmark=" ",
                                            amark=" "
                                            ).execute()

                if pilihSA == "Menu Akun":
                    menu_akun(usernameLogin, user)
                    continue
                elif pilihSA == "Menu Mod":
                    menu_mod(usernameLogin, user)
                    continue
                elif pilihSA == "Logout":
                    konfirmasi = inquirer.select(message="Yakin ingin Logout?",
                                                choices=["YA", "TIDAK"],
                                                pointer="👉",
                                                qmark="❓",
                                                amark="☑️"
                                                ).execute()
                    if konfirmasi == "YA":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Logout dibatalkan")
                        input("Enter...")

            elif roleLogin == "admin":
                pilihanA = inquirer.select(message="=== MENU ADMIN ===",
                                            choices=["Menu Akun", 
                                                    "Logout",
                                                    ],
                                            pointer="👉",
                                            qmark=" ",
                                            amark=" "
                                            ).execute()

                if pilihanA == "Menu Akun":
                    menu_akun(usernameLogin, user)
                    continue
                    
                elif pilihanA == "Logout":
                    konfirmasi = inquirer.select(message="Yakin ingin Logout?",
                                                choices=["YA", "TIDAK"],
                                                pointer="👉",
                                                qmark="❓",
                                                amark=" "
                                                ).execute()
                    if konfirmasi == "YA":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Logout dibatalkan")
                        input("Enter...")

            elif roleLogin == "user":
                pilihanU = inquirer.select(message="=== MENU USER ===",
                                            choices=["Menu Mod", 
                                                    "Logout",
                                                    ],
                                            pointer="👉",
                                            qmark=" ",
                                            amark=" "
                                            ).execute()

                if pilihanU == "Menu Mod":
                    menu_mod(usernameLogin, user)
                    continue

                elif pilihanU == "Logout":
                    konfirmasi = inquirer.select(message="Yakin ingin Logout?",
                                                choices=["YA", "TIDAK"],
                                                pointer="👉",
                                                qmark="❓",
                                                amark=" "
                                                ).execute()
                    if konfirmasi == "YA":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Logout dibatalkan")
                        input("Enter...")

            else:
                print("Role tidak dikenali!")
                input("Tekan Enter...")
                break
