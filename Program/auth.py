# Login Function (Ghina)

from data import user

def login(user):
    print("=== LOGIN ====")
    username = input("Masukkan username:")
    password = input("Masukkan password:")

    if username == "" or password == "":
        print("Input tidak boleh kosong!")
        return None, None
    
    if username in user and user[username]["password"] == password:
        print("Login berhasil!")
        return username, user[username]["role"]
    else:
        print("Username atau password salah!")
        return None, None
    
def register(user):
    print("=== REGISTER ====")
    username = input("Masukkan username baru:")

    if username == "":
        print("Username tidak boleh kosong!")
        return
    
    if username in user:
        print("Username sudah terdaftar!")
        return
    
    password = input("Masukkan password baru:")

    if password == "":
        print("Password tidak boleh kosong!")
        return
    
    role = input("Masukkan role (superadmin/admin/user): ")

    if role == "":
        print("Role tidak boleh kosong!")
        return
    
    if role not in ["superadmin", "admin", "user"]:
        print("Role tidak valid! Pilihan role: superadmin, admin, user")
        return
    
    user[username] = {
        "password": password,
        "role": role
    }

    print("Registrasi berhasil!")