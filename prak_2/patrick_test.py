import unittest
import miller_rabin

class TestCryptoMethods(unittest.TestCase):

    def test_miller_rabin(self):
        self.assertTrue(miller_rabin.miller_rabin(32416190071, 300))
        self.assertTrue(miller_rabin.miller_rabin(7, 3))
        self.assertFalse(miller_rabin.miller_rabin(-1, 1))
        self.assertFalse(miller_rabin.miller_rabin(6, 3))

        self.assertTrue(miller_rabin.miller_rabin(99377, 300))
        self.assertFalse(miller_rabin.miller_rabin(3434264727117317381232123, 300))
        self.assertTrue(miller_rabin.miller_rabin(999979, 300))
        self.assertFalse(miller_rabin.miller_rabin(999980, 300))



    def test_next_prime_mil_rab(self):
        self.assertEqual(miller_rabin.next_prime_mil_rab(17, 5), 17)
        self.assertEqual(miller_rabin.next_prime_mil_rab(32, 5), 37)
        self.assertEqual(miller_rabin.next_prime_mil_rab(10**100, 10), 10**100 + 267)


    def test_anz_zeugen(self):
        self.assertEqual(miller_rabin.anz_zeugen(9), 6)
        self.assertEqual(miller_rabin.anz_zeugen(325), 306)

if __name__ == '__main__':
    unittest.main()
