class Bank :
    def __init__(self, norek, nama, saldo):
        self.norek = norek
        self.nama = nama
        self.saldo = saldo

class Bca(Bank) :
    def __init__(self, norek, nama, saldo):
        super().__init__(norek, nama, saldo)
        self.j_b = "BCA"
        self.b_b = 0.05
        self.potongan_bulanan = 5000

    def setor_tunai(self, tambahan) :
        self.saldo += tambahan

    def tarik_tunai(self, tarikan) :
        self.saldo -= tarikan

    def cek_saldo(self) :
        return self.saldo

class Bni(Bank) :
    def __init__(self, norek, nama, saldo):
        super().__init__(norek, nama, saldo)
        self.j_b = "BNI"
        self.b_b = 0.06
        self.potongan_bulanan = 7000

    def setor_tunai(self, tambahan) :
        self.saldo += tambahan

    def tarik_tunai(self, tarikan) :
        self.saldo -= tarikan

    def cek_saldo(self) :
        return self.saldo

def buat_rekening(daftar_rekening):
    while True:
        norek = input('Masukkan no. rekening: ')
        if any(rekening.norek == norek for rekening in daftar_rekening):
            print('Nomor rekening telah terdaftar!')
        else:
            break

    nama = input('Masukkan nama: ')
    print('1. BCA\n2. BNI')

    while True:
        jenis_bank = int(input('Masukkan jenis bank (1/2): '))
        if jenis_bank in [1, 2]:
            break
        else:
            print('Jenis bank tidak valid!')

    saldo = float(input('Masukkan saldo: '))
    if jenis_bank == 1:
        rekening_baru = Bca(norek, nama, saldo)
    else:
        rekening_baru = Bni(norek, nama, saldo)

    daftar_rekening.append(rekening_baru)
    print("Rekening berhasil dibuat!")

def setor_tunai(daftar_rekening):
    norek = input('Masukkan no. rekening: ')
    rekening = next((x for x in daftar_rekening if x.norek == norek), None)

    if rekening:
        saldo_tambahan = float(input('Masukkan nilai setor tunai: '))
        rekening.setor_tunai(saldo_tambahan)
        print("Setor tunai berhasil")
    else:
        print("Rekening tidak ditemukan!")

def tarik_tunai(daftar_rekening):
    norek = input('Masukkan no. rekening: ')
    rekening = next((x for x in daftar_rekening if x.norek == norek), None)

    if rekening:
        saldo_tarikan = float(input('Masukkan nilai tarik tunai: '))
        if saldo_tarikan > rekening.saldo:
            print("Saldo tidak mencukupi untuk melakukan penarikan.")
            return

        if rekening.saldo - saldo_tarikan < 0:
            print("Penarikan tidak dapat dilakukan karena saldo akan menjadi kurang dari 0.")
            return

        print(f'Anda yakin?\nSisa saldo anda: {rekening.saldo}\nJika ditarik: {rekening.saldo - saldo_tarikan}')
        pilihan_tarik = input('Y/N: ').lower()

        if pilihan_tarik == 'y':
            rekening.tarik_tunai(saldo_tarikan)
            print("Tarik tunai berhasil")
        else:
            print('Batal melakukan tarik tunai')
    else:
        print("Rekening tidak ditemukan!")

def cek_saldo(daftar_rekening):
    norek = input('Masukkan no. rekening: ')
    rekening = next((x for x in daftar_rekening if x.norek == norek), None)

    if rekening:
        print(f'Sisa saldo anda: {rekening.saldo}')
    else:
        print("Rekening tidak ditemukan!")

def main():
    daftar_rekening = []

    while True:
        print('\nMenu:\n1. Buat Rekening\n2. Setor Tunai\n3. Tarik Tunai\n4. Cek Saldo\n5. Keluar')
        try:
            pilihan = int(input('Masukkan pilihan: '))
        except ValueError:
            print("Pilihan harus berupa angka!")
            continue

        if pilihan == 1:
            buat_rekening(daftar_rekening)
        elif pilihan == 2:
            setor_tunai(daftar_rekening)
        elif pilihan == 3:
            tarik_tunai(daftar_rekening)
        elif pilihan == 4:
            cek_saldo(daftar_rekening)
        elif pilihan == 5:
            print('\nTerima kasih!')
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
