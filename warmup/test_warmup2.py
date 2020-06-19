from unittest import TestCase

from warmup.Warmup2 import WarmUp2


class MyTestCase(TestCase):
    def setUp(self):
        self.warmup2 = WarmUp2()

    def test_string_times(self):
        self.assertEqual(self.warmup2.string_times('Hi', 2), "HiHi")
        self.assertEqual(self.warmup2.string_times('Hi', 3), "HiHiHi")
        self.assertEqual(self.warmup2.string_times('Hi', 1), "Hi")

    def test_front_times(self):
        self.assertEqual(self.warmup2.front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(self.warmup2.front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(self.warmup2.front_times('Abc', 3), 'AbcAbcAbc')

    def test_string_bits(self):
        self.assertEqual(self.warmup2.string_bits('Hello'), 'Hlo')
        self.assertEqual(self.warmup2.string_bits('Hi'), 'H')
        self.assertEqual(self.warmup2.string_bits('Heeololeo'), 'Hello')

    def test_string_splosion(self):
        self.assertEqual(self.warmup2.string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(self.warmup2.string_splosion('abc'), 'aababc')
        self.assertEqual(self.warmup2.string_splosion('ab'), 'aab')

    def test_last2(self):
        self.assertEqual(self.warmup2.last2('hixxhi'), 1)
        self.assertEqual(self.warmup2.last2('xaxxaxaxx'), 1)
        self.assertEqual(self.warmup2.last2('axxxaaxx'), 2)

    def test_array_count(self):
        self.assertEqual(self.warmup2.array_count([1, 2, 9]), 1)
        self.assertEqual(self.warmup2.array_count([1, 9, 9]), 2)
        self.assertEqual(self.warmup2.array_count([1, 9, 9, 3, 9]), 3)

    def test_array_front9(self):
        self.assertEqual(self.warmup2.array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(self.warmup2.array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(self.warmup2.array_front9([1, 2, 3, 4, 5]), False)

    def test_array123(self):
        self.assertEqual(self.warmup2.array123([1, 1, 2, 3, 1]), True)
        self.assertEqual(self.warmup2.array123([1, 1, 2, 4, 1]), False)
        self.assertEqual(self.warmup2.array123([1, 1, 2, 1, 2, 3]), True)

    def test_string_match(self):
        self.assertEqual(self.warmup2.string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(self.warmup2.string_match('abc', 'abc'), 2)
        self.assertEqual(self.warmup2.string_match('abc', 'axc'), 0)