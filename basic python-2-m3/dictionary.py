number = [1, 2, 3, 3, 4, 5]
person = ['kaka', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlaps with set
person = {'name': 'kaka', 'adress': 'kalipur',
          'age': 23, 'position': 'student'}

print(person)
print(person['age'])
print(person.keys())  # returns a list of keys
print(person.values())  # returns a list of values


for key, values in person.items():
    print(key, values)
