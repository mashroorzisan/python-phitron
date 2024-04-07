import pyautogui as p
from time import *

n = int(input())
sleep(1)

for i in range(n):
    p.write('#'*(i+1))
    p.write("\n")
#
##
###
####
#####
