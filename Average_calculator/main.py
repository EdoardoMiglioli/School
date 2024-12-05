inputs_num = int(input('How many numbers do you want to enter? '))
i = inputs_num
sum = 0

while i > 0:
    num = float(input('Enter a number: '))
    sum += num
    i -= 1

print(sum / inputs_num)