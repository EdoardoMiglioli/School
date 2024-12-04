def first_deg_equation(a, b):
    if a == 0:
        if b == 0:
            return "Identity"
        else:
            return "Impossible"
    
    return f"X is {-b / a}"

a = float(input("insert a: "))
b = float(input("insert b: "))

print(first_deg_equation(a, b))