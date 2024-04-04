# list --> []
# tuple --> ()
# set--> {}
# set : unique collection of items and no duplicates

nombres = [12, 12, 12, 54, 12, 22, 33, 22]
print(nombres)

# order maintain korbena

nombre_set = set(nombres)
print(nombre_set)

nombre_set.add(44)
print(nombre_set)

nombre_set.remove(44)
print(nombre_set)


a = {1, 2, 3, 6, 7, 3}
b = {3, 2, 4, 1, 5}
print(a, b)

c = a & b
print(c)
print(a | b)
