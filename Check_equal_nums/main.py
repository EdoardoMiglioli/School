def check_equals(x, y, z):
    if (x == y) or (x == z) or (y == z):
        return True
    return False

x, y, z = map(int, input('Enter three numbers separated by spaces: ').split())
print(check_equals(x, y, z))