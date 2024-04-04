from time import sleep
# write
# with open('sample.txt', 'w')as file:
#     sleep(1)
#     for i in range(6):
#         sleep(1)
#         file.write("i love python!\n")

# append
# with open('sample.txt', 'a')as file:
#     file.write('Ilovepython dobara')


# read
with open('sample.txt', 'r')as file:
    txt = file.read()
    print(txt)
