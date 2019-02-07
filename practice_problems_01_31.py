# Get the string
s = input('Please enter a string: ')
s = list(s)
new_s =[]

for idx, char in enumerate(s):
    if idx % 2 == 0:
        new_s.append(char.lower())
    else:
        new_s.append(char.upper())

result = ''.join(new_s)

# Print the result
print(result)





# Example input() statement
s = input('Please enter a string: ')
i=0

for char in s:
    print(s[i].upper())
    #i += 2
