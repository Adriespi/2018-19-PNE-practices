dna = input('Please introduce a dna sequence: ')
dna = dna.lower()
a = 0
c = 0
g = 0
t = 0
for i in dna:
    if i == 'a':
        a += 1
    elif i == 'c':
        c += 1
    elif i == 'g':
        g += 1
    elif i == 't':
        t += 1

print('The length of the sequence is',len(dna))
print('A =',a,'\nC =',c,'\nG =',g,'\nT =',t)