numbers = 0
for i in range(0, 1001):
    if i % 17 == 0 and i % 2 == 0:
        numbers += 1
        print(i)
print("The total number of numbers that are divisible by 17 and 2:", numbers)