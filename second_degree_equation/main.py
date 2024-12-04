import math

def second_deg_equation(a, b, c):
    delta = b**2 - 4*a*c

    if a == 0:
        if b == 0:
            return "Identity" if c == 0 else "Impossible"
        return f"X is {-c / b}"

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"X1 is {x1}, X2 is {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"X is {x}"
    else:
        return "Impossible (no real solutions)"

a = float(input("Insert a: "))
b = float(input("Insert b: "))
c = float(input("Insert c: "))

print(second_deg_equation(a, b, c))
