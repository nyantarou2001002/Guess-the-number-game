import random
import sys

min,max = map(int, input("Please input two numbers like '2 8'.").split())

while min > max:
    min,max = map(int, input("Please input two numbers in the correct order.").split())
    if min < max:
        break

a = random.randint(min,max)

y = int(input("Please input the right number."))

while y != a:
    y = int(input("Please input the right number again."))
    if y == a:
        print("Congratulation!!")
        break

        



