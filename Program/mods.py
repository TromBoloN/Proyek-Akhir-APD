from prettytable import PrettyTable
from utils import clear, catat_log
from InquirerPy import inquirer

def tableMod(mods):
    clear()
    print("=== DAFTAR MOD ===")

    if not mods:
        print("Belum ada mod.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Nama Mod", "Versi", "Kategori", "Ukuran", "Deskripsi", "Review"]

    for nama, data in mods.items():
        tabel.add_row([
            nama,
            data.get("versi", "-"),
            data.get("kategori", "-"),
            data.get("ukuran", "-"),
            data.get("deskripsi", "-"),
            data.get("review", "-")
        ])

    print(tabel)


def menu_mod(usernameLogin, users):
    if "mods" not in users[usernameLogin]:
        users[usernameLogin]["mods"] = {}

    while True:
        try:
            clear()
            
            pilihan = inquirer.select(message="=== MENU MOD ===",
                                      choices=["Lihat daftar mod", 
                                               "Tambah mod",
                                               "Edit mod",
                                               "Hapus mod",
                                               "Kembali",],
                                      pointer="->",
                                      qmark=" ",
                                      amark=" ",
                                      ).execute()



            if pilihan == "Lihat daftar mod":
                clear()
                tableMod(users[usernameLogin]["mods"])
                catat_log(usernameLogin, "Melihat daftar mod", "-")
                input("\nTekan Enter untuk kembali...")

            elif pilihan == "Tambah mod":
                clear()
                print("\n=== TAMBAH MOD ===")
                nama_mod = input("Nama mod baru: ").strip()

                if not nama_mod:
                    print("Nama mod tidak boleh kosong!")
                    input("Tekan Enter...")
                    continue

                if nama_mod in users[usernameLogin]["mods"]:
                    print("Mod sudah ada!")
                    input("Tekan Enter...")
                    continue

                try:
                    versi = input("Versi: ").strip()
                    kategori = input("Kategori: ").strip()
                    ukuran = input("Ukuran: ").strip()
                    deskripsi = input("Deskripsi: ").strip()
                    review = input("Review: ").strip()

                    users[usernameLogin]["mods"][nama_mod] = {
                        "versi": versi or "-",
                        "kategori": kategori or "-",
                        "ukuran": ukuran or "-",
                        "deskripsi": deskripsi or "-",
                        "review": review or "-"
                    }
                    catat_log(usernameLogin, "Menambah mod", nama_mod)

                    print("Mod berhasil ditambahkan!")
                    input("Tekan Enter...")

                except Exception as e:
                    print("Gagal menambah mod:", e)
                    input("Tekan Enter...")
            
            elif pilihan == "Edit mod":
                clear()
                print("\n=== EDIT MOD ===")
                tableMod(users[usernameLogin]["mods"])

                nama_mod = input("\nPilih nama mod yang mau diedit: ").strip()

                if nama_mod not in users[usernameLogin]["mods"]:
                    print("Mod tidak ditemukan!")
                    input("Tekan Enter...")
                    continue

                mod = users[usernameLogin]["mods"][nama_mod]

                while True:
                    clear()
                    print(f"=== EDIT MOD: {nama_mod} ===")
                    print("Pilih bagian yang ingin diubah:")

                    menuEdit = inquirer.select(
                        message="Bagian yang ingin diubah:",
                        choices=[
                            "Versi",
                            "Kategori",
                            "Ukuran",
                            "Deskripsi",
                            "Review",
                            "Kembali"
                        ],
                        pointer="->",
                        qmark=" ",
                        amark=" "
                    ).execute()

                    if menuEdit == "Kembali":
                        break

                    dataEdit = {
                        "Versi": "versi",
                        "Kategori": "kategori",
                        "Ukuran": "ukuran",
                        "Deskripsi": "deskripsi",
                        "Review": "review"
                    }

                    key = dataEdit[menuEdit]

                    print(f"Nilai sekarang: {mod.get(key, '-')}")
                    valueBaru = input(f"Masukkan {menuEdit} baru (kosong untuk batal): ").strip()

                    if not valueBaru:
                        print("Tidak ada perubahan.")
                        input("Enter...")
                        continue

                    # lakukan edit
                    users[usernameLogin]["mods"][nama_mod][key] = valueBaru
                    catat_log(usernameLogin, f"Mengedit {key}", nama_mod)

                    print(f"{menuEdit} berhasil diperbarui!")
                    input("Enter...")


            elif pilihan == "Hapus mod":
                clear()
                print("\n=== HAPUS MOD ===")
                tableMod(users[usernameLogin]["mods"])
                nama_mod = input("\nNama mod yang ingin dihapus: ").strip()

                if nama_mod not in users[usernameLogin]["mods"]:
                    print("Mod tidak ditemukan!")
                else:
                    try:
                        del users[usernameLogin]["mods"][nama_mod]
                        catat_log(usernameLogin, "Menghapus mod", nama_mod)
                        print("Mod berhasil dihapus!")
                    except Exception as e:
                        print("Gagal menghapus mod:", e)

                input("Tekan Enter...")

            elif pilihan == "Kembali":
                print("Kembali ke menu sebelumnya...")
                break

            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter...")

        except KeyboardInterrupt:
            print("\nKembali ke menu.")
            break

        except Exception as e:
                print("Terjadi kesalahan:", e)
                input("Tekan Enter...")
