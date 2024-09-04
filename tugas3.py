import socket
import platform

def get_service_by_port():
    try:
        port = int(input("Masukkan port protokol: "))
        service_name = socket.getservbyport(port)
        print(f"Port: {port} => service name: {service_name}")
    except OSError:
        print(f"Port: {port} tidak memiliki service name yang terdaftar.")
    except ValueError:
        print("Input harus berupa angka.")

def get_ip_address():
    try:
        website = input("Masukkan alamat web: ")
        ip_address = socket.gethostbyname(website)
        local_ip = socket.gethostbyname(socket.gethostname())
        computer_name = platform.node()
        print(f"Anda mengakses {website} dengan alamat IP {ip_address} dari komputer {computer_name} dengan alamat IP {local_ip}")
    except socket.gaierror:
        print("Alamat web tidak valid.")

def main():
    while True:
        print("\nMENU PILIHAN:")
        print("1. MENGETAHUI SERVICE DAN PROTOKOL PADA JARINGAN")
        print("2. MENGETAHUI ALAMAT IP DARI SEBUAH WEBSITE")
        
        choice = input("Pilih opsi (1/2): ")

        if choice == '1':
            get_service_by_port()
        elif choice == '2':
            get_ip_address()
        else:
            print("Pilihan tidak valid.")

        repeat = input("ANDA INGIN MENGULANG (Y/T)? ").upper()
        if repeat != 'Y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
