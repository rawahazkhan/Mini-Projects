numeralInput = input("> Please enter a Roman numeral (in uppercase letters only):: ")

def roman_to_int(numeral):
    convertedValue = 0
    
    if "CM" in numeral:
        convertedValue += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        convertedValue += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        convertedValue += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        convertedValue += 9
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        convertedValue += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        convertedValue += 4
        numeral = numeral.replace("IV", "")
    
    for i in numeral:
        if i == "M":
            convertedValue += 1000
        elif i == "D":
            convertedValue += 500
        elif i == "C":
            convertedValue += 100
        elif i == "L":
            convertedValue += 50
        elif i == "X":
            convertedValue += 10
        elif i == "V":
            convertedValue += 5
        elif i == "I":
            convertedValue += 1
    print("> Entered roman numeral translates to: " + str(convertedValue))

roman_to_int(numeralInput)
