#Write a program to ind those numbers which are divisible by 7 and mutiple of 5, between 1500 and 2700(both included).

new_list = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        new_list.append(str(x))
print(",".join(new_list))