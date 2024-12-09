


def converToRoman(num):
    roman_chart = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    # Process each number in tht input list
    results = []
    for n in num:
        roman = ""
        for value, symbol in roman_chart:
            while n >= value:
                roman += symbol
                n -= value
        results.append(roman)
    return results

print(converToRoman([60, 80, 30, 112, 50]))
