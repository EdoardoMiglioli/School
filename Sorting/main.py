def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

x, y, z = map(int, input('Enter three numbers separated by spaces: ').split())
sorted_numbers = sort_three_numbers(x, y, z)
print('Sorted numbers: ', sorted_numbers)

"""
array_ = list(map(int, input('Enter three numbers separated by spaces: ').split()))
array_.sort()
print(array_)
"""