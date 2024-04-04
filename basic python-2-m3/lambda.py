from math import *

# normal functions


def square(num):
    return (num*num)


def root(num):
    return (sqrt(num))


def add(num1, num2):
    return (num1+num2)


def sub(num1, num2):
    return num1-num2


sq = square(5)
# print(sq)

rt = int(root(sq))
# print(rt)

ad = add(sq, rt)
# print(ad)

sb = sub(rt, sq)
# print(sb)


# equivalent lambda function

sq_lam = lambda x : x*x
# result = sq_lam
# print(result)

# 1.
numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])

# 2.
numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)

# 3.
# string and tuples are immutable
# lists are not

# 4.
person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)

# 5.
student = { 
  "name": "Amir", 
  "class": 10, 
  "marks": 85 
}
student.pop("marks")
for k, v in student.items():
    print(k,v)

# 6
try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")

# 7. 
from math import *
result=ceil(5.00001)
print(result)

# 8. 
num = lambda a:a*a
print(num(2**2))

# 9. Dictionary is mutable in Python 