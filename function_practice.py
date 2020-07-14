nums_1_to_100 = range(1, 100)

for num in nums_1_to_100:
    if num % 7 == 0 and num % 5 == 0:
        print(num, 'ChickenMonkey')
    elif num % 5 == 0:
        print(num, 'Chicken')
    elif num % 7 == 0:
        print(num, 'Monkey')