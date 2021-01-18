#Printing current and previous number sum in a given range(10)
#Current Number 0 Previous Number 0 Sum: 0
#Current Number 1 Previous Number 0 Sum: 1
#Current Number 2 Previous Number 1 Sum: 3


def sum_number(num):
    previous_num = 0
    for i in range(num):
        sum = previous_num + i
        print("Current Number", i, "Previous Number", previous_num, "Sum", sum)
        previous_num = i

sum_number(10)