def is_positive(a):
    if (a == 0): return 'neither'
    if (a > 0): return 'positive'
    return 'negative'

a = int(input('Enter a number: '))

print(f'{a} is {is_positive(a)}')