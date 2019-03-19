import json
import termcolor
f = open('person.json','r')
person = json.load(f)
print()
termcolor.cprint('Name:','green',end='')
print(person['Firstname'],person['Lastname'])
termcolor.cprint('Age:', 'green', end='')
print(person['age'])

for num in enumerate(person['Phonenumber']):
    termcolor.cprint("Phone:",'blue',end='')
    print(num)