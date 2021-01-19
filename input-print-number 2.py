number = int(input("Please enter the number to be divided: "))

list_range = list(range(1, number+1))

divisor_list = []

for num in list_range:
    if number % num == 0:
        divisor_list.append(num)
print(divisor_list)