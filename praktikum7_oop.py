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

daftar_rekening = []
while True :
    print('\nMenu :\n1. Buat Rekening\n2. Setor Tunai\n3. Tarik Tunai\n4. Cek Saldo\n5. Keluar')
    pilihan = int(input('Masukkan pilihan : '))

    if pilihan == 1 :
        cek_norek = True
        val = 0
        while cek_norek :
            norek = input('Masukkan no. rekening : ')
            for x in daftar_rekening :
                if norek == x.norek :
                    val += 1
            if val > 0 :
                print('Nomor rekening telah terdaftar!')
            else :
                cek_norek = False
        nama = input('Masukkan nama : ')
        print('1. BCA\n2. BNI')
        pilihan_bank = True
        while pilihan_bank == True :
            j_b = int(input('Masukkan jenis bank(1/2) : '))
            if not 0 < j_b < 3 :
                print('Jenis bank tidak valid!')
            else :
                pilihan_bank = False
        if j_b == 1 :
            saldo = float(input('Masukkan saldo : '))
            bca_baru = Bca(norek, nama, saldo)
            daftar_rekening.append(bca_baru)
        else :
            saldo = float(input('Masukkan saldo : '))
            bni_baru = Bni(norek, nama, saldo)
            daftar_rekening.append(bni_baru)

    elif pilihan == 2 :
        norek = input('Masukkan no. rekening : ')
        for x in daftar_rekening :
            if x.norek == norek :
                saldo_tambahan = float(input('Masukkan nilai setor tunai : '))
                x.setor_tunai(saldo_tambahan)

    elif pilihan == 3 :
        norek = input('Masukkan no. rekening : ')
        for x in daftar_rekening :
            if x.norek == norek :
                saldo_tarikan = float(input('Masukkan nilai tarik tunai : '))
                print(f'Anda yakin?\nSisa saldo anda : {x.saldo}.\nJika ditarik : {x.saldo - saldo_tarikan}')
                pilihan_tarik = input('Y/N : ')
                if pilihan_tarik == 'y' or pilihan_tarik == 'Y' :
                    x.tarik_tunai(saldo_tarikan)
                    print("Tarik tunai berhasil")
                else :
                    print('Batal melakukan tarik tunai')

    elif pilihan == 4 :
        norek = input('Masukkan no. rekening : ')
        for x in daftar_rekening :
            if x.norek == norek :
                print(f'Sisa saldo anda : {x.saldo}')

    else :
        print('\nTerima kasih!')
        break
