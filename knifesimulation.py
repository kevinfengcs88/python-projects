import random
import time

count = 1

while True:
    knife = random.randrange(0, 401)
    if knife == 400:
        print(f"Case #{count}: ", end = "")
        print("KNIFE!!!!!!!!!!!!!!!!!!!")
    else:
        print(f"Case #{count}: ", end="")
        print("~~~")
    count += 1
    time.sleep(0.01)
