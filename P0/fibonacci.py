#Already defined n
n = 5

count = 0
n1 = 0
n2 = 1

if n == 1:
    print(n1)
else:
    while count < n:
        print(n1, end=' , ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

