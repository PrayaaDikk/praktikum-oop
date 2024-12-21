class Akun_bank :
    def __init__(this, no_akun, nama, saldo_awal, jenis_akun) :
        this.no_akun = no_akun
        this.nama = nama
        this.saldo_awal = saldo_awal
        this.jenis_akun = jenis_akun

    def saldo_akhir(this) :
        pass

class Tabungan(Akun_bank) :
    def __init__(this, no_akun, nama, saldo_awal, jenis_akun, setoran_bul) :
        super().__init__(no_akun, nama, saldo_awal, jenis_akun)
        this.setoran_bul = setoran_bul

    def saldo_akhir(this) :
        return this.saldo_awal + this.setoran_bul*12
    
class Deposito(Akun_bank) :
    def __init__(this, no_akun, nama, saldo_awal, jenis_akun, bunga_tahunan) :
        super().__init__(no_akun, nama, saldo_awal, jenis_akun)
        this.bunga_tahunan = bunga_tahunan
    
    def saldo_akhir(this) :
        return this.saldo_awal + this.saldo_awal*this.bunga_tahunan
    
daftar_akun_bank = []
while True :
    print("\nMenu\n1. Input Data Bank\n2. Tampilkan Akun Bank\n3. Keluar")
    p1 = int(input("Masukkan Pilihan -> "))

    if p1 == 1:
        no_akun = input("Masukkan Nomor Akun -> ")
        nama = input("Masukkan Nama -> ")
        saldo_awal = float(input("Masukkan Saldo Awal -> "))
        print("Jenis Akun :")
        print("1. Tabungan")
        print("2. Deposito")
        p2 = int(input("Masukkan Pilihan Jenis Akun -> "))
        pilihan_jenis_akun = True
        while pilihan_jenis_akun == True :
            if p2 == 1 :
                jenis_akun = "Tabungan"
                setoran_bul = float(input("Masukkan Setoran Bulanan -> "))
                akun_bank_baru = Tabungan(no_akun, nama, saldo_awal, jenis_akun, setoran_bul)
                daftar_akun_bank.append(akun_bank_baru)
                pilihan_jenis_akun = False
            elif p2 == 2 :
                jenis_akun = "Deposito"
                bunga_tahunan = float(input("Masukkan Bunga Tahunan -> "))
                bunga_tahunan = bunga_tahunan / 100
                akun_bank_baru = Deposito(no_akun, nama, saldo_awal, jenis_akun, bunga_tahunan)
                daftar_akun_bank.append(akun_bank_baru)
                pilihan_jenis_akun = False
            else :
                print("Pilihan Jenis Akun Tidak Valid!")

    elif p1 == 2 :
        print()
        print("No. Akun\tNama\tJenis Akun\tSaldo Awal\tSaldo Akhir")
        for akun_bank in daftar_akun_bank :
            print(f"{akun_bank.no_akun}\t\t{akun_bank.nama}\t{akun_bank.jenis_akun}\t{akun_bank.saldo_awal}\t{akun_bank.saldo_akhir()}")

    else :
        print("\nTerima Kasih")
        break
