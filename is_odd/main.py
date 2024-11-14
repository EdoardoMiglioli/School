def is_even(a):
    if (a % 2 == 0) :
        return 'even'
    return 'odd'

a = int(input('Enter a number: '))

print(f'{a} is {is_even(a)}')
