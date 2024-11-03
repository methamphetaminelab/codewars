class RomanNumerals:
    constants = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    
    @staticmethod
    def to_roman(val : int) -> str:
        result = ""
        for symbol, value in RomanNumerals.constants.items():
            while val >= value:
                result += symbol
                val -= value
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        result = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in RomanNumerals.constants:
                result += RomanNumerals.constants[roman_num[i:i+2]]
                i += 2
            else:
                result += RomanNumerals.constants[roman_num[i]]
                i += 1
        return result