# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase
from num2words import num2words


class Num2WordsUZTest(TestCase):

    def test_cardinal_latin(self):
        self.assertEqual(num2words(0, lang='uz', script='latin'), "nol")
        self.assertEqual(num2words(1, lang='uz', script='latin'), "bir")
        self.assertEqual(num2words(12, lang='uz', script='latin'), "o'n ikki")
        self.assertEqual(num2words(23, lang='uz', script='latin'), 
                         "yigirma uch")
        self.assertEqual(num2words(105, lang='uz', script='latin'), "yuz besh")
        self.assertEqual(num2words(1000, lang='uz', script='latin'), 
            "ming")
        self.assertEqual(
            num2words(1000000, lang='uz', script='latin'), 
            "million"
        )

    def test_cardinal_cyrillic(self):
        self.assertEqual(num2words(0, lang='uz', script='cyrillic'), "нол")
        self.assertEqual(num2words(1, lang='uz', script='cyrillic'), "бир")
        self.assertEqual(num2words(12, lang='uz', script='cyrillic'), "ўн икки")
        self.assertEqual(num2words(23, lang='uz', script='cyrillic'), "йигирма уч")
        self.assertEqual(num2words(105, lang='uz', script='cyrillic'), "йуз беш")
        self.assertEqual(
            num2words(1000, lang='uz', script='cyrillic'), 
            "минг"
        )
        self.assertEqual(
            num2words(1000000, lang='uz', script='cyrillic'), 
            "миллион"
        )

    def test_ordinal_latin(self):
        self.assertEqual(
            num2words(1, lang='uz', to='ordinal', script='latin'), 
            "birinchi"
        )
        self.assertEqual(
            num2words(5, lang='uz', to='ordinal', script='latin'), 
            "beshinchi"
        )
        self.assertEqual(
            num2words(21, lang='uz', to='ordinal', script='latin'), 
            "yigirma birinchi"
        )
        self.assertEqual(
            num2words(100, lang='uz', to='ordinal', script='latin'), 
            "yuzinchi"
        )
        self.assertEqual(
            num2words(1000, lang='uz', to='ordinal', script='latin'), 
            "minginchi"
        )

    def test_ordinal_cyrillic(self):
        self.assertEqual(
            num2words(1, lang='uz', to='ordinal', script='cyrillic'), 
            "биринчи"
        )
        self.assertEqual(
            num2words(5, lang='uz', to='ordinal', script='cyrillic'), 
            "бешинчи"
        )
        self.assertEqual(
            num2words(21, lang='uz', to='ordinal', script='cyrillic'), 
            "йигирма биринчи"
        )
        self.assertEqual(
            num2words(100, lang='uz', to='ordinal', script='cyrillic'), 
            "йузинчи"
        )
        self.assertEqual(
            num2words(1000, lang='uz', to='ordinal', script='cyrillic'), 
            "мингинчи"
        )

    def test_ordinal_num_latin(self):
        self.assertEqual(
            num2words(1, lang='uz', to='ordinal_num', script='latin'), 
            "1-birinchi"
        )
        self.assertEqual(
            num2words(5, lang='uz', to='ordinal_num', script='latin'), 
            "5-beshinchi"
        )
        self.assertEqual(
            num2words(21, lang='uz', to='ordinal_num', script='latin'), 
            "21-yigirma birinchi"
        )

    def test_ordinal_num_cyrillic(self):
        self.assertEqual(
            num2words(1, lang='uz', to='ordinal_num', script='cyrillic'), 
            "1-биринчи"
        )
        self.assertEqual(
            num2words(5, lang='uz', to='ordinal_num', script='cyrillic'), 
            "5-бешинчи"
        )
        self.assertEqual(
            num2words(21, lang='uz', to='ordinal_num', script='cyrillic'), 
            "21-йигирма биринчи"
        )

    def test_to_currency_latin(self):
        self.assertEqual(
            num2words(2000.00, lang='uz', to='currency', script='latin'), 
            "ikki ming so'm va nol tiyin"
        )
        self.assertEqual(
            num2words(1001.01, lang='uz', to='currency', script='latin'), 
            "bir ming bir so'm va bir tiyin"
        )
        self.assertEqual(
            num2words(158.30, lang='uz', to='currency', script='latin'), 
            "yuz ellik sakkiz so'm va o'ttiz tiyin"
        )

    def test_to_currency_cyrillic(self):
        self.assertEqual(
            num2words(2000.00, lang='uz', to='currency', script='cyrillic'), 
            "икки минг сўм ва нол тийин"
        )
        self.assertEqual(
            num2words(1001.01, lang='uz', to='currency', script='cyrillic'), 
            "бир минг бир сўм ва бир тийин"
        )
        self.assertEqual(
            num2words(158.30, lang='uz', to='currency', script='cyrillic'), 
            "йуз эллик саккиз сўм ва ўттиз тийин"
        )

    def test_to_year_latin(self):
        self.assertEqual(
            num2words(2023, lang='uz', to='year', script='latin'), 
            "ikki ming yigirma uch"
        )
        self.assertEqual(
            num2words(-44, lang='uz', to='year', script='latin', suffix='miloddan avval'), 
            "qirq to'rt miloddan avval"
        )

    def test_to_year_cyrillic(self):
        self.assertEqual(
            num2words(2023, lang='uz', to='year', script='cyrillic'), 
            "икки минг йигирма уч"
        )
        self.assertEqual(
            num2words(-44, lang='uz', to='year', script='cyrillic', suffix='милоддан аввал'), 
            "қирқ тўрт милоддан аввал"
        )