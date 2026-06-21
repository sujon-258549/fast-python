number = 0
while number < 5:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")
