from prettytable import PrettyTable
from InquirerPy import inquirer
from utils import clear, catat_log

def menu_akun(usernameLogin, users):
    role_login = users[usernameLogin]["role"]

    while True:
        clear()
        menu_akun = inquirer.select(message="=== MANAJEMEN AKUN ===",
                                    choices=["Lihat daftar user", 
                                            "Tambah user baru",
                                            "Edit user",
                                            "Hapus user",
                                            "Kembali"],
                                    pointer="->",
                                    qmark=" ",
                                    amark=" "
                                    ).execute()

        if menu_akun == "Lihat daftar user":
            clear()  
            print("\n=== LIST USER ===")
            tabel = PrettyTable()
            tabel.field_names = ["Username", "Password", "Role"]
            for username, data in users.items():
                tabel.add_row([username, data["password"], data["role"]])
            print(tabel)

            catat_log(usernameLogin, "Melihat daftar user", "-")
            input("\nEnter...")

        elif menu_akun == "Tambah user baru":
            clear()
            print("\n=== TAMBAH USER ===")
            usn_baru = inquirer.text(
                            message="Masukkan Username baru: ",
                            qmark="->",
                            amark="->"
                            ).execute()
            if usn_baru in users:
                print("User sudah ada!")
                input("\nEnter...")
                continue

            pw_baru = inquirer.secret(
                            message="Masukkan Password baru: ",
                            qmark="->",
                            amark="->"
                            ).execute()

            if role_login == "admin":
                role_baru = "user"
                print("Role otomatis: user")
            else:
                role_baru = inquirer.select(
                            message="Masukkan role (superadmin/admin/user): ",
                            choices=["superadmin", "admin", "user"],
                            pointer="->",
                            qmark="->",
                            amark="->"
                            ).execute()

            users[usn_baru] = {
                "password": pw_baru,
                "role": role_baru,
                "mods": {}
            }
            catat_log(usernameLogin, "Menambah user baru", usn_baru)

            print("User berhasil dibuat!")
            input("\nEnter...")

        elif menu_akun == "Edit user":
            clear()
            print("\n=== EDIT USER ===" "\n")
            tabel = PrettyTable()
            tabel.field_names = ["Username", "Password", "Role"]
            for username, data in users.items():
                tabel.add_row([username, data["password"], data["role"]])
            print(tabel)

            usn_edit = input("\nMasukkan username yang ingin diedit: ")
            if usn_edit not in users:
                print("User tidak ditemukan!")
                input("\nEnter...")
                continue

            if role_login == "admin" and users[usn_edit]["role"] != "user":
                print("Admin tidak dapat edit user non-user!")
                input("\nEnter...")
                continue

            print("Kosongkan untuk tidak mengubah.")
            pw_edit = inquirer.secret(
                            message="Masukkan Password baru: ",
                            qmark="->",
                            amark="->"
                            ).execute()
            role_edit = inquirer.select(
                            message="Masukkan role: ",
                            choices=["superadmin", "admin", "user"],
                            pointer="->",
                            qmark="->",
                            amark="->"
                            ).execute() if role_login == "superadmin" else None

            if pw_edit:
                users[usn_edit]["password"] = pw_edit
            if role_edit:
                users[usn_edit]["role"] = role_edit

            catat_log(usernameLogin, "Mengedit user", usn_edit)

            print("User berhasil diperbarui!")
            input("\nEnter...")

        elif menu_akun == "Hapus user":
            clear()
            print("\n=== HAPUS USER ===" "\n")
            tabel = PrettyTable()
            tabel.field_names = ["Username", "Password", "Role"]
            for username, data in users.items():
                tabel.add_row([username, data["password"], data["role"]])
            print(tabel)

            user_hapus = inquirer.text(
                            message="Masukkan Username: ",
                            qmark=" ",
                            amark=" "
                            ).execute()
            if user_hapus not in users:
                print("User tidak ditemukan!")
                input("\nEnter...")
                continue

            if role_login == "admin" and users[user_hapus]["role"] != "user":
                print("Admin tidak dapat menghapus user non-user!")
                input("\nEnter...")
                continue

            konfirmasi = inquirer.select(message="Yakin ingin Mengapus User?",
                                                choices=["YA", "TIDAK"],
                                                pointer="->",
                                                qmark="?",
                                                amark=" "
                                                ).execute()
            if konfirmasi == "YA":
                del users[user_hapus]

                catat_log(usernameLogin, "Menghapus user", user_hapus)
                
                print("User berhasil dihapus.")
                input("\nEnter...")
            else:
                print("Dibatalkan.")
                input("\nEnter...")

        elif menu_akun == "Kembali":
            break

