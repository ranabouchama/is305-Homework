import random
count = 0
current_number = 0
while current_number != 68:
    current_number = random.randint(1, 100)
    count += 1
print("The number 68 was generated after {count} times.")
