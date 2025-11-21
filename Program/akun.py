from prettytable import PrettyTable
from utils import clear

clear()

def menu_akun(usernameLogin, users):
    role_login = users[usernameLogin]["role"]
    while True:
        print("\n=== MANAJEMEN AKUN ===")
        print("1. Lihat daftar user")
        print("2. Tambah user baru")
        print("3. Edit user")
        print("4. Hapus user")
        print("5. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            clear()
            print("\n=== LIST USER ===")
            tabel = PrettyTable()
            tabel.field_names = ["Username", "Password", "Role"]
            for username, data in users.items():
                tabel.add_row([username, data["password"], data["role"]])
            print(tabel)

        elif pilihan == "2":
            clear()
            print("\n=== TAMBAH USER ===")
            usn_baru = input("Masukkan username baru: ")
            if usn_baru in users:
                print("User sudah ada!")
                continue
            pw_baru = input("Masukkan password: ")
            if role_login == "admin":
                role_baru = "user"
                print("Role diset otomatis ke 'user'")
            else:
                role_baru = input("Masukkan role (user/admin/superadmin): ")
            users[usn_baru] = {
                "password": pw_baru,
                "role": role_baru,
                "mods": {}
            }
            print("User berhasil dibuat!")

        elif pilihan == "3":
            clear()
            print("\n=== EDIT USER ===")
            usn_edit = input("Masukkan username yang ingin diedit: ")
            if usn_edit not in users:
                print("User tidak ditemukan!")
                continue
            if role_login == "admin" and users[usn_edit]["role"] != "user":
                print("Admin tidak dapat edit user non-user!")
                continue
            print("Kosongkan jika tidak ingin diubah.")
            pw_edit = input("Password baru: ")
            role_edit = None

            if role_login == "superadmin":
                role_edit = input("Role baru (biarkan kosong jika tidak diubah): ")
            if pw_baru:
                users[usn_edit]["password"] = pw_edit
            if role_edit:
                users[usn_edit]["role"] = role_edit
            print("User berhasil diperbarui!")

        elif pilihan == "4":
            print("\n=== HAPUS USER ===")
            user_hapus = input("Masukkan username yang ingin dihapus: ")
            if user_hapus not in users:
                print("User tidak ditemukan!")
                continue
            if role_login == "admin" and users[user_hapus]["role"] != "user":
                print("Admin tidak boleh hapus user non-user!")
                continue
            konfirmasi = input(f"Yakin ingin menghapus {user_hapus}? (y/n): ")
            if konfirmasi.lower() == "y":
                del users[user_hapus]
                print("User berhasil dihapus!")
            else:
                print("Dibatalkan.")

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid!")