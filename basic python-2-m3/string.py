name = 'sakib\'s khan'  # escape character
name2 = "sakib khan"

# multiline string
name3 = """
    sakib khna
    number one
"""

print(name)
# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])  # reverse


# mutable means changable
# immutable means unchangeable
# string is immutable
# name2[0]= 'R'
if 'khan' in name2:
    print('exists')

print(name2.upper())
