from prettytable import PrettyTable
from utils import clear


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
            print("=== MENU MOD ===")
            print("1. Lihat daftar mod")
            print("2. Tambah mod")
            print("3. Edit mod")
            print("4. Hapus mod")
            print("5. Kembali")
            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                clear()
                tableMod(users[usernameLogin]["mods"])
                input("\nTekan Enter untuk kembali...")

            elif pilihan == "2":
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

                    print("Mod berhasil ditambahkan!")
                    input("Tekan Enter...")

                except Exception as e:
                    print("Gagal menambah mod:", e)
                    input("Tekan Enter...")

            elif pilihan == "3":
                clear()
                print("\n=== EDIT MOD ===")
                tableMod(users[usernameLogin]["mods"])
                nama_mod = input("\nNama mod yang mau diedit: ").strip()

                if nama_mod not in users[usernameLogin]["mods"]:
                    print("Mod tidak ditemukan!")
                    input("Tekan Enter...")
                    continue

                try:
                    mod = users[usernameLogin]["mods"][nama_mod]
                    print("Tekan Enter untuk skip (tidak mengubah).")

                    versi = input(f"Versi baru ({mod.get('versi','-')}): ").strip() or mod["versi"]
                    kategori = input(f"Kategori baru ({mod.get('kategori','-')}): ").strip() or mod["kategori"]
                    ukuran = input(f"Ukuran baru ({mod.get('ukuran','-')}): ").strip() or mod["ukuran"]
                    deskripsi = input(f"Deskripsi baru ({mod.get('deskripsi','-')}): ").strip() or mod["deskripsi"]
                    review = input(f"Review baru ({mod.get('review','-')}): ").strip() or mod["review"]

                    users[usernameLogin]["mods"][nama_mod] = {
                        "versi": versi,
                        "kategori": kategori,
                        "ukuran": ukuran,
                        "deskripsi": deskripsi,
                        "review": review
                    }

                    print("Mod berhasil diperbarui!")
                    input("Tekan Enter...")

                except Exception as e:
                    print("Gagal mengedit mod:", e)
                    input("Tekan Enter...")

            elif pilihan == "4":
                clear()
                print("\n=== HAPUS MOD ===")
                tableMod(users[usernameLogin]["mods"])
                nama_mod = input("\nNama mod yang ingin dihapus: ").strip()

                if nama_mod not in users[usernameLogin]["mods"]:
                    print("Mod tidak ditemukan!")
                else:
                    try:
                        del users[usernameLogin]["mods"][nama_mod]
                        print("Mod berhasil dihapus!")
                    except Exception as e:
                        print("Gagal menghapus mod:", e)

                input("Tekan Enter...")

            elif pilihan == "5":
                print("Kembali ke menu sebelumnya...")
                break

            else:
                print("Pilihan tidak valid.")
                input("Tekan Enter...")

        except KeyboardInterrupt:
            print("\nKembali ke menu.")
            break

        except Exception as e:
            input("Terjadi kesalahan:", e,"Tekan Enter...")
