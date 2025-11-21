from prettytable import PrettyTable

def menu_mod(usernameLogin, users):
    if "mods" not in users[usernameLogin]:
        users[usernameLogin]["mods"] = {}

    while True:
        print("\n=== MENU MOD ===")
        print("1. Lihat daftar mod")
        print("2. Tambah mod")
        print("3. Edit mod")
        print("4. Hapus mod")
        print("5. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\n=== DAFTAR MOD ===")
            mods = users[usernameLogin]["mods"]

            if not mods:
                print("Belum ada mod.")
            else:
                tabel = PrettyTable()
                tabel.field_names = ["Nama Mod", "Versi", "Kategori", "Ukuran", "Deskripsi", "Review"]

                for nama, data in mods.items():
                    tabel.add_row([
                        nama,
                        data["versi"],
                        data["kategori"],
                        data["ukuran"],
                        data["deskripsi"],
                        data["review"]
                    ])

                print(tabel)
                
        elif pilihan == "2":
            print("\n=== TAMBAH MOD ===")
            nama_mod = input("Nama mod baru: ")

            if nama_mod in users[usernameLogin]["mods"]:
                print("Mod sudah ada!")
                continue

            versi = input("Versi: ")
            kategori = input("Kategori: ")
            ukuran = input("Ukuran: ")
            deskripsi = input("Deskripsi: ")
            review = input("Review: ")

            users[usernameLogin]["mods"][nama_mod] = {
                "versi": versi,
                "kategori": kategori,
                "ukuran": ukuran,
                "deskripsi": deskripsi,
                "review": review
            }

            print("Mod berhasil ditambahkan!")

        elif pilihan == "3":
            print("\n=== EDIT MOD ===")
            nama_mod = input("Nama mod yang mau diedit: ")

            if nama_mod not in users[usernameLogin]["mods"]:
                print("Mod tidak ditemukan!")
                continue

            mod = users[usernameLogin]["mods"][nama_mod]

            print("Tekan Enter untuk skip (tidak mengubah).")

            versi = input(f"Versi baru ({mod['versi']}): ") or mod["versi"]
            kategori = input(f"Kategori baru ({mod['kategori']}): ") or mod["kategori"]
            ukuran = input(f"Ukuran baru ({mod['ukuran']}): ") or mod["ukuran"]
            deskripsi = input(f"Deskripsi baru ({mod['deskripsi']}): ") or mod["deskripsi"]
            review = input(f"Review baru ({mod['review']}): ") or mod["review"]

            users[usernameLogin]["mods"][nama_mod] = {
                "versi": versi,
                "kategori": kategori,
                "ukuran": ukuran,
                "deskripsi": deskripsi,
                "review": review
            }

            print("Mod berhasil diperbarui!")

        elif pilihan == "4":
            print("\n=== HAPUS MOD ===")
            nama_mod = input("Nama mod yang ingin dihapus: ")

            if nama_mod not in users[usernameLogin]["mods"]:
                print("Mod tidak ditemukan!")
            else:
                del users[usernameLogin]["mods"][nama_mod]
                print("Mod berhasil dihapus!")

        elif pilihan == "5":
            print("Kembali ke menu sebelumnya...")
            break

        else:
            print("Pilihan tidak valid.")
            
print("Tekan Enter untuk melanjutkan...")
