def sum_n(num):
    total = 0
    for i in range(num + 1):
        total = total + i
    return total

num = int(input('PLease introduce an integer number:'))
print(sum_n(num))

