from unittest import TestCase

from warmup.Warmup1 import WarmUp1


class TestWarmUp1(TestCase):
    def setUp(self):
        self.warmup1 = WarmUp1()

    def test_sleep_in(self):
        self.assertEqual(self.warmup1.sleep_in(False, True), True)
        self.assertEqual(self.warmup1.sleep_in(True, False), False)
        self.assertEqual(self.warmup1.sleep_in(False, True), True)

    def test_monkey_trouble(self):
        self.assertEqual(self.warmup1.monkey_trouble(True, True), True)
        self.assertEqual(self.warmup1.monkey_trouble(False, False), True)
        self.assertEqual(self.warmup1.monkey_trouble(True, False), False)

    def test_sum_double(self):
        self.assertEqual(self.warmup1.sum_trouble(1, 2), 3)
        self.assertEqual(self.warmup1.sum_trouble(3, 2), 5)
        self.assertEqual(self.warmup1.sum_trouble(2, 2), 8)

    def test_diff_21(self):
        self.assertEqual(self.warmup1.diff21(19), 2)
        self.assertEqual(self.warmup1.diff21(10), 11)
        self.assertEqual(self.warmup1.diff21(21), 0)

    def test_parrot_trouble(self):
        self.assertEqual(self.warmup1.parrot_trouble(True, 6), True)
        self.assertEqual(self.warmup1.parrot_trouble(True, 7), False)
        self.assertEqual(self.warmup1.parrot_trouble(False, 6), False)

    def test_makes_10(self):
        self.assertEqual(self.warmup1.makes10(9, 10), True)
        self.assertEqual(self.warmup1.makes10(9, 9), False)
        self.assertEqual(self.warmup1.makes10(1, 9), True)

    def test_near_hundred(self):
        self.assertEqual(self.warmup1.near_hundred(93), True)
        self.assertEqual(self.warmup1.near_hundred(90), True)
        self.assertEqual(self.warmup1.near_hundred(89), False)

    def test_pos_neg(self):
        self.assertEqual(self.warmup1.pos_nes(1, -1, False), True)
        self.assertEqual(self.warmup1.pos_nes(-1, 1, False), True)
        self.assertEqual(self.warmup1.pos_nes(-4, -5, True), True)

    def test_not_string(self):
        self.assertEqual(self.warmup1.not_string('candy'), 'not candy')
        self.assertEqual(self.warmup1.not_string('x'), 'not x')
        self.assertEqual(self.warmup1.not_string('not bad'), 'not bad')

    def test_missing_char(self):
        self.assertEqual(self.warmup1.missing_char('kitten', 1), 'ktten')
        self.assertEqual(self.warmup1.missing_char('kitten', 0), 'itten')
        self.assertEqual(self.warmup1.missing_char('kitten', 4), 'kittn')

    def test_front_back(self):
        self.assertEqual(self.warmup1.front_back('code'), 'eodc')
        self.assertEqual(self.warmup1.front_back('a'), 'a')
        self.assertEqual(self.warmup1.front_back('ab'), 'ba')

    def test_front_3(self):
        self.assertEqual(self.warmup1.front3('Java'), 'JavJavJav')
        self.assertEqual(self.warmup1.front3('Chocolate'), 'ChoChoCho')
        self.assertEqual(self.warmup1.front3('abc'), 'abcabcabc')
