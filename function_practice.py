# Chicken Monkey Exercise
def chicken_monkey(range_of_nums):
    for num in range_of_nums:
        if num % 7 == 0 and num % 5 == 0:
            print(num, "ChickenMonkey")
        elif num % 5 == 0:
            print(num, "Chicken")
        elif num % 7 == 0:
            print(num, "Monkey")

chicken_monkey(range(1, 100))

# Activities for Kids Exercise


# Running kids: Pam, Sam, Andrea, Will
# Swinging kids: Marybeth, Ariel, Kevin, Courtney
# Sliding kids: Mike, Jack, Jennifer, Earl
# Hiding kids: Henry, Heather, Hayley, Hugh

def run(*kids):
    for kid in kids:
        print(f'{kid} ran like a bat out of hell!')

def swing(*kids):
    for kid in kids:
        print(f'{kid} swung really high!')

def slide(*kids):
    for kid in kids:
        print(f'{kid} slid really fast!')

def hide_and_seek(*kids):
    for kid in kids:
        print(f'{kid} hid from the cops!')

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh") 