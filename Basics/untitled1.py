line = str(input('Enter the line: '))
new_line = line[-1:] + line[1:-1] + line[:1]
print(new_line)