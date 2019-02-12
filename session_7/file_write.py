# Example of reading a file located in our local file system

NAME = 'mynotes'

#open the file
myfile = open(NAME, 'r')

print('File opened: {}'.format(myfile.name))
contents = myfile.read()

print('The file contents are: {}'.format(contents))

myfile.close()

f = open(NAME, 'a')

f.write('THIS IS A TEXT EXAMPLE ADDED TO MY FILE')

#close the file
f.close()
print('The end')