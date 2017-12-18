#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from ttdc.office_extract import content_extract as ex


class TestContentExtract(TestCase):
    def test_get_filename(self):
        testpair = ex.FileProp('w_T_EXT_PROJ_No.3.ppt')

        self.assertEqual(testpair.header, 'T_EXT_PROJ_No.3')
        self.assertEqual(testpair.lang, 'ja')

        testpair = ex.FileProp('e_EPS-IPA要求仕様書.doc')

        self.assertEqual(testpair.header, 'EPS-IPA要求仕様書')
        self.assertEqual(testpair.lang, 'en')

