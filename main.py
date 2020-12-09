# Decimal to binary convertor
from time import sleep
l = []
def run2(n):
    n = int(n)
    if n > 1:
        run2(n//2)
    rem = (n%2)
    if str(rem) == '1':
        l.append(1)
    elif str(rem) == '0':
        l.append(0)
    length = len(str(n))
    sleep(length)
    print(l,"\n",  end='')

n = input("Enter the number to be converted to binary: ")
print("Converting...")
try:
    run2(n)
except ValueError:
    print("Please Keep Correct Value of Decimal")

sleep(2)
print("\nPress any Key to Continue \nOr You can Exit by Typing 'exit' here: ")
asktocontinue = input()

while asktocontinue == '' or asktocontinue == ' ':
    l.clear()
    n = input("Enter the number to be converted to binary: ")
    print("Converting...")
    try:
        run2(n)
    except ValueError:
        print("Please Keep Correct Value of Decimal")
    sleep(2)
    print("\n\nPress any Key to Continue \nOr You can Exit by Typing 'exit' here: ")
    asktocontinue = input()
