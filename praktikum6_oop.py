class User:
    daftar_user = []  # List untuk menyimpan semua user (Admin dan Customer)

    def __init__(self, nama):
        self.nama = nama

    def tambah(self):
        """Menambahkan user ke daftar_user."""
        self.__class__.daftar_user.append(self)

    def hapus(self):
        """Menghapus user dari daftar_user."""
        if self in self.__class__.daftar_user:
            self.__class__.daftar_user.remove(self)
            return f"User {self.nama} berhasil dihapus."
        return f"User {self.nama} tidak ditemukan."

    @classmethod
    def tampilkan_user(cls):
        """Menampilkan semua user dalam daftar_user."""
        print("\nDaftar User:")
        for i, user in enumerate(cls.daftar_user, start=1):
            if isinstance(user, Admin):
                print(f"{i}. [Admin] Nama: {user.nama}, Bidang: {user.bidang}")
            elif isinstance(user, Customer):
                print(f"{i}. [Customer] Nama: {user.nama}, Poin: {user.poin}")
        print()


class Admin(User):
    def __init__(self, nama, bidang):
        super().__init__(nama)
        self.bidang = bidang

    def hapus(self):
        """Menghapus admin dari daftar_user."""
        hasil = super().hapus()
        return f"[Admin] {hasil}"


class Customer(User):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def hapus(self):
        """Menghapus customer dari daftar_user."""
        hasil = super().hapus()
        return f"[Customer] {hasil}"


# Program utama
def main():
    while True:
        print("Menu:")
        print("1. Tambah Admin")
        print("2. Tambah Customer")
        print("3. Hapus User")
        print("4. Tampilkan User")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            # Tambah Admin
            nama = input("Masukkan nama admin: ")
            bidang = input("Masukkan bidang admin: ")
            admin = Admin(nama, bidang)
            admin.tambah()
            print("Admin berhasil ditambahkan.\n")

        elif pilihan == "2":
            # Tambah Customer
            nama = input("Masukkan nama customer: ")
            poin = int(input("Masukkan poin customer: "))
            customer = Customer(nama, poin)
            customer.tambah()
            print("Customer berhasil ditambahkan.\n")

        elif pilihan == "3":
            # Hapus User
            User.tampilkan_user()
            indeks = int(input("Masukkan nomor user yang ingin dihapus: ")) - 1
            if 0 <= indeks < len(User.daftar_user):
                user = User.daftar_user[indeks]
                print(user.hapus())
            else:
                print("Indeks tidak valid.\n")

        elif pilihan == "4":
            # Tampilkan User
            User.tampilkan_user()

        elif pilihan == "5":
            # Keluar
            print("Program dihentikan.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


# Jalankan program
if __name__ == "__main__":
    main()
