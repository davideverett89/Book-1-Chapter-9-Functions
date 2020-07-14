# Chicken Monkey Exercise
def chicken_monkey(range_of_nums):
    statement = ''
    for num in range_of_nums:
        if num % 7 == 0 and num % 5 == 0:
            statement += f"{num}: ChickenMonkey, "
        elif num % 5 == 0:
            statement += f"{num}: Chicken, "
        elif num % 7 == 0:
            statement += f"{num}: Monkey, "
    return statement

print(chicken_monkey(range(1, 100)))

# Activities for Kids Exercise


# Running kids: Pam, Sam, Andrea, Will
# Swinging kids: Marybeth, Ariel, Kevin, Courtney
# Sliding kids: Mike, Jack, Jennifer, Earl
# Hiding kids: Henry, Heather, Hayley, Hugh
