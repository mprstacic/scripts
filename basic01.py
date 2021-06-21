import re

char_list = [ char for char in "linuxhint" ]
print(char_list)

# Define a tuple of websites
websites = ("google.com","yahoo.com", "ask.com", "bing.com")

# Define a list
websites = ["google.com","yahoo.com", "ask.com", "bing.com"]
print(type(websites))
websites.append('yahoo.ie')

for index, value in enumerate(websites):
    websites[index] = value.upper()

with open('list.txt', 'w') as f:
    for value in websites:
        f.write(value+"\n")
f.close()

a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
r=set(a) & set(b)
print(r)
print( set(a).intersection(b) )

string = "i am walking away right away"
if re.search('in', string):
    print("True")
else:
    print("False")

if string.startswith("I"):
    print("True")
else:
    print("False")