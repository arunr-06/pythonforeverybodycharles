file_name = input('Enter a file name')
file = open(file_name)
for line in file:
    b = line.strip().upper()
    print(b)





