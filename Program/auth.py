# Login Function (Ghina)

from data import user

def login(user):
    print("=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in user and user[username]["password"]==password:
        print("Login berhasil!")
        return username, user[username]["role"]
    else:
        print("Username atau password salah.")
        return None, None
    
def register(user):
    print("=== Register ===")
    username = input("Masukkan username baru: ")

    if username in user:
        print("Username sudah terdaftar.")
        return
    
    password = input("Masukkan password baru: ")
    role = input("Masukkan role (superadmin/admin/user): ")

    user[username] = {
        "username": username,
        "password": password,
        "role": role
    }
    print("Registrasi berhasil!")
        
        