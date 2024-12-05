base = float(input('Enter the base: '))
exponent = float(input('Enter the exponent: '))
power = 1

while exponent > 0:
    power *= base 
    exponent -= 1

print(f'The result is {power}')