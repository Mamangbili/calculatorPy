import math


def kali(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Type bukan angka")
    return a * b


def bagi(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Type bukan angka")
    if b == 0:
        raise ValueError("denumerator tidak boleh 0")
    return a / b


def tambah(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Type bukan angka")
    return a + b


def kurang(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Type bukan angka")
    return a - b


def log(a, n):
    if not (isinstance(a, (int, float)) and isinstance(n, (int, float))):
        raise TypeError("Type bukan angka")
    if n < 0 or n == 1:
        raise ValueError("base tidak boleh 0 sampai 1")

    return math.log(a, n)


from enum import Enum


class Menu(Enum):
    TAMBAH = 1
    KURANG = 2
    KALI = 3
    BAGI = 4
    LOG = 5
    MENU = 6


class View:
    def menuAwal(self):
        print(
            """
             Calculator
        ====================
        1. Tambah
        2. Kurang
        3. Kali
        4. Bagi
        5. Log
        ====================
        """
        )

    def inputMenuAwal(self):
        try:
            Input = int(input("Pilih Operasi [1/2/3/4/5] : "))
            if not 0 < Input < 6:
                raise ValueError("tidak ada di menu")
            return Input
        except ValueError as err:
            raise ValueError("Tidak ada di menu")

    def inputKali(self):
        print("a x b")
        try:
            a = float(input("masukan a: "))
            b = float(input("masukan b: "))
            return [a, b]
        except ValueError as err:
            print(str(err))

    def inputBagi(self):
        print("a / b")
        try:
            a = float(input("masukan a: "))
            b = float(input("masukan b: "))
            return [a, b]
        except ValueError as err:
            ValueError("input harus angka")

    def inputTambah(self):
        print("a + b")
        try:
            a = float(input("masukan a: "))
            b = float(input("masukan b: "))
            return [a, b]
        except ValueError as err:
            print(str(err))

    def inputKurang(self):
        print("a - b")
        try:
            a = float(input("masukan a: "))
            b = float(input("masukan b: "))
            return [a, b]
        except ValueError as err:
            print(str(err))

    def inputLog(self):
        print("n log a")
        try:
            n = float(input("masukan n: "))
            a = float(input("masukan a: "))
            return [a, n]
        except ValueError as err:
            raise ValueError("input harus angka")

    def hasil(self, hasil):
        print("Hasil : ", hasil)

    def clearScreen(self):
        import os
        import time

        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")


class Controller:
    def __init__(self, view):
        self.currentPage = Menu.MENU
        while True:
            match self.currentPage:
                case Menu.MENU:
                    self.loopPage(self.tampilkanMenuAwal, view)
                case Menu.TAMBAH:
                    self.loopPage(
                        self.tampilkanMenuOperasi, view, view.inputTambah, tambah
                    )
                case Menu.KURANG:
                    self.loopPage(
                        self.tampilkanMenuOperasi, view, view.inputKurang, kurang
                    )
                case Menu.KALI:
                    self.loopPage(self.tampilkanMenuOperasi, view, view.inputKali, kali)
                case Menu.BAGI:
                    self.loopPage(self.tampilkanMenuOperasi, view, view.inputBagi, bagi)
                case Menu.LOG:
                    self.loopPage(self.tampilkanMenuOperasi, view, view.inputLog, log)

    def tampilkanMenuAwal(self, view):
        view.menuAwal()
        Input = view.inputMenuAwal()
        match Input:
            case 1:
                self.currentPage = Menu.TAMBAH
            case 2:
                self.currentPage = Menu.KURANG
            case 3:
                self.currentPage = Menu.KALI
            case 4:
                self.currentPage = Menu.BAGI
            case 5:
                self.currentPage = Menu.LOG

    def tampilkanMenuOperasi(self, view, viewInput, fungsiOperasi):
        a, b = viewInput()
        result = fungsiOperasi(a, b)
        view.hasil(result)
        view.clearScreen()
        self.currentPage = Menu.MENU

    def loopPage(self, viewPage, *args):
        loop = True
        while loop:
            try:
                loop = False
                viewPage(*args)
                return
            except Exception as Err:
                loop = True
                print(str(Err))
                args[0].clearScreen()


if __name__ == "__main__":
    view = View()
    controller = Controller(view)
