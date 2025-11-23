# Login Function (Ghina)
from InquirerPy import inquirer
from data import user

def login(user):
    print("=== Login ===")
    username = inquirer.text(
                            message="Masukkan Username: ",
                            qmark=" ",
                            amark=" "
                            ).execute()
    password = inquirer.secret(
                            message="Masukkan Password baru: ",
                            qmark=" ",
                            amark=" "
                            ).execute()

    if username in user and user[username]["password"]==password:
        print("Login berhasil!")
        return username, user[username]["role"]
    else:
        print("Username atau password salah.")
        return None, None
    
def register(user):
    print("=== Register ===")
    username = inquirer.text(
                            message="Masukkan Username baru: ",
                            qmark="📝",
                            amark="📝"
                            ).execute()

    if username in user:
        print("Username sudah terdaftar.")
        return
    
    password = inquirer.secret(
                            message="Masukkan Password baru: ",
                            qmark="📝",
                            amark="📝"
                            ).execute()
    role = inquirer.select(
                            message="Masukkan role (superadmin/admin/user): ",
                            choices=["superadmin", "admin", "user"],
                            pointer="👉",
                            qmark="📝",
                            amark="📝"
                            ).execute()

    user[username] = {
        "username": username,
        "password": password,
        "role": role
    }
    print("Registrasi berhasil!")
        
        