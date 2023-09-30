class RomanNumeralConverter:
    def __init__(self):
        self.numeral_map = (
            ("M", 1000), ("CM", 900), ("D", 500),
            ("CD", 400), ("C", 100),  ("XC", 90),
            ("L", 50),   ("XL", 40),  ("X", 10),
            ("IX", 9),   ("V", 5),    ("IV", 4),
            ("I", 1))

    def convert_to_roman(self, n):
        result = ""
        for r, num in self.numeral_map:
            while n >= num:
                result += r
                n -= num
        return result

number=int(input("Enter a number:"))
print(RomanNumeralConverter().convert_to_roman(number))