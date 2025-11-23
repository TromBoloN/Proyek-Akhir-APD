import os
import csv
from datetime import datetime

def clear():
    os.system("cls||clear")

def catat_log(username, action, nama_item):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log_aktivitas.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([waktu, username, action, nama_item])

def tampilkan_log():
    print("=== LOG AKTIVITAS ===")

    try:
        with open("log_aktivitas.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) == 0:
                print("Belum ada aktivitas.")
                return
            
            for row in data:
                waktu, username, action, nama_item = row
                print(f"{waktu} | {username} | {action} | {nama_item}")
    except FileNotFoundError:
        print("Belum ada aktivitas.")