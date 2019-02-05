def count_a(seq):
    #counting the number of A's in the sequence

    #Counter for the A's
    result = 0
    for b in seq:
        if b == 'A':
            result += 1
    # return the result
    return result

#Main program

s = input('PLease introduce the sequence: ')
na = count_a(s)
print('The number of As in the sequence is: {}'.format(na))

#calculate the total sequence length
tl = len(s)

#calculate the percentage of As in the sequence
if tl > 0:
    perc = round(100.0 * na / tl,1)
else:
    perc = 0
print('The total length is: {}'.format(tl))
print('The total percentage of As is: {}%'.format(perc))