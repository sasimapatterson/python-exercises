#Print the following number pattern using Python's range() and for loop.
#1
#22
#333

for num in range(4):
    for i in range(num):
        print(num, end=" ")
    print() #print new line after each row