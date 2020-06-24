from unittest import TestCase

from warmup.String1 import String1


class MyTestCase(TestCase):
    def setUp(self):
        self.string1 = String1()

    def test_hello_name(self):
        self.assertEqual(self.string1.hello_name('Bob'), 'Hello Bob!')
        self.assertEqual(self.string1.hello_name('Alice'), 'Hello Alice!')
        self.assertEqual(self.string1.hello_name('X'), 'Hello X!')

    def test_make_abba(self):
        self.assertEqual(self.string1.make_abba('Hi', 'Bye'), 'HiByeByeHi')
        self.assertEqual(self.string1.make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
        self.assertEqual(self.string1.make_abba('What', 'Up'), 'WhatUpUpWhat')

    def test_make_tags(self):
        self.assertEqual(self.string1.make_tags('I', 'Yay'), '<I>Yay</I>')
        self.assertEqual(self.string1.make_tags('I', 'Hello'), '<I>Hello</I>')
        self.assertEqual(self.string1.make_tags('cite', 'Yay'), '<cite>Yay</cite>')

    def test_make_out_word(self):
        self.assertEqual(self.string1.make_out_word('<<>>', 'Yay'), '<<Yay>>')
        self.assertEqual(self.string1.make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
        self.assertEqual(self.string1.make_out_word('[[]]', 'word'), '[[word]]')

    def test_extra_end(self):
        self.assertEqual(self.string1.extra_end('Hello'), 'lololo')
        self.assertEqual(self.string1.extra_end('ab'), 'ababab')
        self.assertEqual(self.string1.extra_end('Hi'), 'HiHiHi')

    def test_first_two(self):
        self.assertEqual(self.string1.first_two('Hello'), 'He')
        self.assertEqual(self.string1.first_two('abcdefg'), 'ab')
        self.assertEqual(self.string1.first_two('ab'), 'ab')

    def test_first_half(self):
        self.assertEqual(self.string1.first_half('Woohoo'), 'Woo')
        self.assertEqual(self.string1.first_half('HelloThere'), 'Hello')
        self.assertEqual(self.string1.first_half('abcdef'), 'abc')

    def test_without_end(self):
        self.assertEqual(self.string1.without_end('Hello'), 'ell')
        self.assertEqual(self.string1.without_end('java'), 'av')
        self.assertEqual(self.string1.without_end('coding'), 'odin')

    def test_combo_string(self):
        self.assertEqual(self.string1.combo_string('Hello', 'hi'), 'hiHellohi')
        self.assertEqual(self.string1.combo_string('hi', 'Hello'), 'hiHellohi')
        self.assertEqual(self.string1.combo_string('aaa', 'b'), 'baaab')

    def test_non_start(self):
        self.assertEqual(self.string1.non_start('Hello', 'There'), 'ellohere')
        self.assertEqual(self.string1.non_start('java', 'code'), 'avaode')
        self.assertEqual(self.string1.non_start('shotl', 'java'), 'hotlava')

    def test_left2(self):
        self.assertEqual(self.string1.left2('Hello'), 'lloHe')
        self.assertEqual(self.string1.left2('java'), 'vaja')
        self.assertEqual(self.string1.left2('Hi'), 'Hi')