#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from ttdc.postprocess.parse_align_out import output_break


class TestParseAlign(TestCase):
    def test_standard_parse(self):
        input = '0.10030155 ||| automotive_pioneers ||| 1-1 ||| 黎明期のパイオニアたち ||| EARLY AUTOMOTIVE PIONEERS'
        result = output_break(input)

        self.assertTrue(result[2])

    def test_exception_parse(self):
        input = 'automotive_pioneers ||| 1-1 ||| 黎明期のパイオニアたち ||| EARLY AUTOMOTIVE PIONEERS'
        result = output_break(input)

        self.assertTrue(result[2])
        self.assertEqual(result[0], '黎明期のパイオニアたち')
        self.assertEqual(result[1], 'EARLY AUTOMOTIVE PIONEERS')
