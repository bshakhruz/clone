from __future__ import division, print_function, unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_UZ(Num2Word_EU):
    CURRENCY_FORMS = {"UZS": (("so'm", "сўм"), ("tiyin", "тийин"))}

    GIGA_SUFFIX = {"latin": "illiard", "cyrillic": "иллиард"}
    MEGA_SUFFIX = {"latin": "illion", "cyrillic": "иллион"}

    def __init__(self, script="latin"):
        self.script = script
        super(Num2Word_UZ, self).__init__()

    def setup(self):
        super(Num2Word_UZ, self).setup()

        self.negword = "minus" if self.script == "latin" else "минус"
        self.pointword = "nuqta" if self.script == "latin" else "нуқта"
        self.exclude_title = (
            ["va", "nuqta", "minus"]
            if self.script == "latin"
            else ["ва", "нуқта", "минус"]
        )

        self.mid_numwords = self._get_mid_numwords()
        self.low_numwords = self._get_low_numwords()
        self.ords = self._get_ords()
        self.large_numwords = self._get_large_numwords()

    def _get_mid_numwords(self):
        return [
            (1000, "ming" if self.script == "latin" else "минг"),
            (100, "yuz" if self.script == "latin" else "йуз"),
            (90, "to'qson" if self.script == "latin" else "тўқсон"),
            (80, "sakson" if self.script == "latin" else "саксон"),
            (70, "etmish" if self.script == "latin" else "етмиш"),
            (60, "oltmish" if self.script == "latin" else "олтмиш"),
            (50, "ellik" if self.script == "latin" else "эллик"),
            (40, "qirq" if self.script == "latin" else "қирқ"),
            (30, "o'ttiz" if self.script == "latin" else "ўттиз"),
        ]

    def _get_low_numwords(self):
        return (
            [
                "yigirma",
                "o'n to'qqiz",
                "o'n sakkiz",
                "o'n yetti",
                "o'n olti",
                "o'n besh",
                "o'n to'rt",
                "o'n uch",
                "o'n ikki",
                "o'n bir",
                "o'n",
                "to'qqiz",
                "sakkiz",
                "yetti",
                "olti",
                "besh",
                "to'rt",
                "uch",
                "ikki",
                "bir",
                "nol",
            ]
            if self.script == "latin"
            else [
                "йигирма",
                "ўн тўққиз",
                "ўн саккиз",
                "ўн етти",
                "ўн олти",
                "ўн беш",
                "ўн тўрт",
                "ўн уч",
                "ўн икки",
                "ўн бир",
                "ўн",
                "тўққиз",
                "саккиз",
                "етти",
                "олти",
                "беш",
                "тўрт",
                "уч",
                "икки",
                "бир",
                "нол",
            ]
        )

    def _get_ords(self):
        return (
            {
                "bir": "birinchi",
                "ikki": "ikkinchi",
                "uch": "uchinchi",
                "to'rt": "to'rtinchi",
                "besh": "beshinchi",
                "olti": "oltinchi",
                "yetti": "yettinchi",
                "sakkiz": "sakkizinchi",
                "to'qqiz": "to'qqizinchi",
                "o'n": "o'ninchi",
                "o'n bir": "o'n birinchi",
                "o'n ikki": "o'n ikkinchi",
            }
            if self.script == "latin"
            else {
                "бир": "биринчи",
                "икки": "иккинчи",
                "уч": "учинчи",
                "тўрт": "тўртинчи",
                "беш": "бешинчи",
                "олти": "олтинчи",
                "етти": "еттинчи",
                "саккиз": "саккизинчи",
                "тўққиз": "тўққизинчи",
                "ўн": "ўнинчи",
                "ўн бир": "ўн биринчи",
                "ўн икки": "ўн иккинчи",
            }
        )

    def _get_large_numwords(self):
        return [
            (10**33, "decillion"),
            (10**30, "nonillion"),
            (10**27, "oktillion"),
            (10**24, "septillion"),
            (10**21, "sextillion"),
            (10**18, "kvintillion"),
            (10**15, "kvadrillion"),
            (10**12, "trillion"),
            (10**9, "milliard"),
            (10**6, "million"),
            (1000, "ming" if self.script == "latin" else "минг"),
        ]

    def set_high_numwords(self, high):
        cap = 3 + 6 * len(high)
        for word, n in zip(high, range(cap, 3, -6)):
            suffix = self.GIGA_SUFFIX if n == 9 else self.MEGA_SUFFIX
            self.cards[10**n] = word + suffix[self.script]

    def to_cardinal(self, number):
        if number < 0:
            return self.negword + " " + self.to_cardinal(-number)
        if number < 20:
            return self.low_numwords[number]
        if number < 100:
            div, mod = divmod(number, 10)
            return self.mid_numwords[div - 2][1] + (
                "" if mod == 0 else " " + self.low_numwords[mod]
            )
        for divisor, name in self.large_numwords:
            if number < divisor * 10:
                div, mod = divmod(number, divisor)
                return (
                    self.to_cardinal(div)
                    + " "
                    + name
                    + ("" if mod == 0 else " " + self.to_cardinal(mod))
                )
        raise ValueError("Number out of range")

    def to_ordinal(self, number):
        if number < 0:
            return self.negword + " " + self.to_ordinal(-number)
        words = self.to_cardinal(number).split()
        suffix = "inchi" if self.script == "latin" else "инчи"
        words[-1] = self.ords.get(words[-1], words[-1] + suffix)
        return " ".join(words)

    def to_ordinal_num(self, number):
        return f"{number}-{self.to_ordinal(number)}"

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return rtext, rnum
        elif 100 > lnum > rnum:
            return f"{ltext}-{rtext}", lnum + rnum
        elif lnum >= 100 > rnum:
            return f"{ltext} va {rtext}", lnum + rnum
        elif rnum > lnum:
            return f"{ltext} {rtext}", lnum * rnum
        return f"{ltext}, {rtext}", lnum + rnum

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = "miloddan avval" if not suffix else suffix
        high, low = divmod(val, 100)
        if high == 0 or (high % 10 == 0 and low < 10) or high >= 100:
            valtext = self.to_cardinal(val)
        else:
            hightext = self.to_cardinal(high)
            if low == 0:
                lowtext = "yuz" if self.script == "latin" else "йуз"
            elif low < 10:
                lowtext = (
                    f"nol-{self.to_cardinal(low)}"
                    if self.script == "latin"
                    else f"нол-{self.to_cardinal(low)}"
                )
            else:
                lowtext = self.to_cardinal(low)
            valtext = f"{hightext} {lowtext}"
        return f"{valtext} {suffix}" if suffix else valtext

    def to_currency(
        self, val, currency="UZS", cents=True, separator=" va ", adjective=False
    ):
        if currency in self.CURRENCY_FORMS:
            units, subunits = self.CURRENCY_FORMS[currency]
            unit = units[0] if self.script == "latin" else units[1]
            subunit = subunits[0] if self.script == "latin" else subunits[1]
            return self._to_currency(val, unit, subunit, separator, cents)
        return super(Num2Word_UZ, self).to_currency(
            val,
            currency=currency,
            cents=cents,
            separator=separator,
            adjective=adjective,
        )

    def _to_currency(self, val, unit, subunit, separator, cents):
        s = separator.strip()
        result = self.to_cardinal(val)
        if val == 1:
            result += f" {unit}"
        else:
            result += f" {unit}{s}"
        if cents:
            val = int(round(val * 100)) % 100
            if val > 0:
                result += f"{separator}{self.to_cardinal(val)} {subunit}"
        return result