import random

count = 1

while True:
    knife = random.randrange(0, 401)
    input("Hit enter to open a case: ")

    if knife == 400:
        print(f"Case: #{count}: ", end="")
        print("YOUJUSTGOTAKNIFE")
    else:
        print(f"Case: #{count}", end="")
        print("~~~")
    count += 1
