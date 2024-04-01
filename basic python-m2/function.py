# python is a dynamically typed programming language
# function definition
# define


# function without return type
def double_it(num1):
    result = num1*2
    print(result)


double_it(34)
double_it(4)


# function with return type
def sum(num1, num2):
    result = num1 + num2
    return result

# meaning you can now save the
# returned value in some variable


total = sum(21, 11)
print(total)
