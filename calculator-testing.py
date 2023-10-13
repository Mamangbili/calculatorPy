import unittest
from Calculator import tambah, kali, bagi, kurang, log


class OperatorTest(unittest.TestCase):
    def test_tipeDataAngka(self):
        n = 2
        b = 8

        hasilTambah = tambah(n, b)
        hasilKurang = kurang(b, n)
        hasilBagi = bagi(b, n)
        hasilKali = kali(b, n)
        hasilLog = log(b, n)

        self.assertEqual(hasilTambah, 10)
        self.assertEqual(hasilKurang, 6)
        self.assertEqual(hasilBagi, 4)
        self.assertEqual(hasilKali, 16)
        self.assertEqual(hasilLog, 3)

    def test_tipeDataCampuran(self):
        n = 2
        b = "8"

        with self.assertRaises(TypeError):
            hasilTambah = tambah(n, b)
        with self.assertRaises(TypeError):
            hasilKurang = kurang(b, n)
        with self.assertRaises(TypeError):
            hasilBagi = bagi(b, n)
        with self.assertRaises(TypeError):
            hasilKali = kali(b, n)
        with self.assertRaises(TypeError):
            hasilLog = log(b, n)

    def test_logBase1(self):
        base = 1
        n = 8

        with self.assertRaises(ValueError):
            log(n, base)

    def test_logBaseNegatif(self):
        base = -2
        n = 8

        with self.assertRaises(ValueError):
            log(n, base)

    def test_bagi0(self):
        denum = 0
        enum = 10

        with self.assertRaises(ValueError):
            bagi(10, 0)


if __name__ == "__main__":
    unittest.main()
