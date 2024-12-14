class Mahasiswa :
    def __init__(this, nim, nama, nilai_tugas, nilai_mid, nilai_uas) :
        this.nim = nim
        this.nama = nama
        this.nilai_tugas = nilai_tugas
        this.nilai_mid = nilai_mid
        this.nilai_uas = nilai_uas

    def nilai_akhir(this) :
        return 0.2*this.nilai_tugas+0.3*this.nilai_mid+0.5*this.nilai_uas
    

daftar_mahasiswa = []
while True :
    print()
    print("Menu :\n1. Input Data\n2. Tampilkan Data\n3. Keluar")
    p = int(input("Masukkan Pilihan -> "))
    print()

    if p == 1 :
        nim = input("Masukkan NIM -> ")
        nama = input("Masukkan Nama Mahasiswa -> ")
        nilai_tugas = float(input("Masukkan Nilai Tugas -> "))
        nilai_mid = float(input("Masukkan Nilai Mid -> "))
        nilai_uas = float(input("Masukkan Nilai UAS -> "))

        data_mahasiswa = Mahasiswa(nim, nama, nilai_tugas, nilai_mid, nilai_uas)
        daftar_mahasiswa.append(data_mahasiswa)
        print()

    elif p == 2 :
        print("NIM\t\tNAMA\t\tNA")
        for mahasiswa in daftar_mahasiswa :
            print(f"{mahasiswa.nim}\t{mahasiswa.nama}\t{mahasiswa.nilai_akhir()}")

    else :
        print("Terima Kasih")
        break
