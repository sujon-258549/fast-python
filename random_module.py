# ============================================
# RANDOM MODULE - Complete Guide
# ============================================
# Random module = random (jhok mok) number generate kore
# Use case: game, password generator, lottery, shuffle, etc.
# ============================================

import random


# ============================================
# 1. random() - 0 to 1 er moddhe float
# ============================================
print("=== 1. random() ===")
print(random.random())          # 0.0 to 1.0 (float)
print(random.random())


# ============================================
# 2. randint(a, b) - Integer between a and b (both inclusive)
# ============================================
print("\n=== 2. randint() ===")
print(random.randint(1, 10))    # 1 to 10 (both included)
print(random.randint(1, 100))   # 1 to 100

# Dice roll
dice = random.randint(1, 6)
print(f"Dice rolled: {dice}")


# ============================================
# 3. randrange(start, stop, step) - Range theke random
# ============================================
print("\n=== 3. randrange() ===")
print(random.randrange(0, 100))         # 0 to 99
print(random.randrange(0, 100, 5))      # 0, 5, 10, 15, ... 95
print(random.randrange(10))             # 0 to 9


# ============================================
# 4. uniform(a, b) - Random FLOAT between a and b
# ============================================
print("\n=== 4. uniform() ===")
print(random.uniform(1.0, 10.0))        # float between 1.0 and 10.0
print(random.uniform(0, 1))


# ============================================
# 5. choice(sequence) - List/tuple theke ekta random select
# ============================================
print("\n=== 5. choice() ===")

fruits = ["apple", "banana", "mango", "orange", "grape"]
print(random.choice(fruits))

colors = ("red", "green", "blue", "yellow")
print(random.choice(colors))

# Random letter
letter = random.choice("PYTHON")
print(f"Random letter: {letter}")


# ============================================
# 6. choices(sequence, k=n) - K number er random items (REPEAT ALLOWED)
# ============================================
print("\n=== 6. choices() ===")

result = random.choices(fruits, k=3)
print(result)    # 3 items, repeat hote pare

# With weights (probability)
items = ["common", "rare", "legendary"]
weights = [70, 25, 5]    # common 70%, rare 25%, legendary 5%
print(random.choices(items, weights=weights, k=10))


# ============================================
# 7. sample(sequence, k=n) - K UNIQUE items (NO repeat)
# ============================================
print("\n=== 7. sample() ===")

lottery = random.sample(range(1, 100), 6)    # 6 unique numbers
print(f"Lottery: {lottery}")

cards = random.sample(fruits, 3)             # 3 unique fruits
print(cards)


# ============================================
# 8. shuffle(list) - List ke shuffle kore (in-place)
# ============================================
print("\n=== 8. shuffle() ===")

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before:", deck)
random.shuffle(deck)
print("After:", deck)

# Card shuffle
cards = ["A", "K", "Q", "J", "10", "9", "8"]
random.shuffle(cards)
print(cards)


# ============================================
# 9. seed() - Same random number repeat korar way
# ============================================
print("\n=== 9. seed() ===")

random.seed(42)
print(random.randint(1, 100))    # always same with seed 42

random.seed(42)
print(random.randint(1, 100))    # same again!

# Without seed, different result each time
random.seed()    # reset


# ============================================
# 10. gauss(mu, sigma) - Gaussian (normal) distribution
# ============================================
print("\n=== 10. gauss() ===")

# mean=0, standard deviation=1
print(random.gauss(0, 1))
print(random.gauss(100, 15))    # mean=100, std=15


# ============================================
# REAL WORLD EXAMPLES
# ============================================

# Example 1: Random Password Generator
print("\n=== Example 1: PASSWORD GENERATOR ===")

import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(random.choices(chars, k=length))
    return password

print(generate_password())
print(generate_password(12))
print(generate_password(16))


# Example 2: OTP Generator
print("\n=== Example 2: OTP GENERATOR ===")

def generate_otp(length=6):
    return "".join(random.choices("0123456789", k=length))

print(f"Your OTP: {generate_otp()}")
print(f"Your OTP: {generate_otp(4)}")


# Example 3: Rock Paper Scissors
print("\n=== Example 3: ROCK PAPER SCISSORS ===")

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
print(f"Computer chose: {computer}")


# Example 4: Coin Toss
print("\n=== Example 4: COIN TOSS ===")

for i in range(5):
    print(f"Toss {i+1}: {random.choice(['Heads', 'Tails'])}")


# Example 5: Lottery Number Generator
print("\n=== Example 5: LOTTERY ===")

def lottery():
    return sorted(random.sample(range(1, 50), 6))

print(f"This week's lottery: {lottery()}")
print(f"Next week's lottery: {lottery()}")


# Example 6: Random Quiz Questions
print("\n=== Example 6: QUIZ ===")

questions = [
    "What is 2+2?",
    "Capital of Bangladesh?",
    "Who wrote Hamlet?",
    "What is Python?",
    "Which planet is red?"
]

selected = random.sample(questions, 3)
print("Today's quiz:")
for i, q in enumerate(selected, 1):
    print(f"{i}. {q}")


# Example 7: Dice Game
print("\n=== Example 7: DICE GAME ===")

player_dice = random.randint(1, 6)
computer_dice = random.randint(1, 6)
print(f"Player: {player_dice}, Computer: {computer_dice}")

if player_dice > computer_dice:
    print("Player wins!")
elif computer_dice > player_dice:
    print("Computer wins!")
else:
    print("Tie!")


# ============================================
# SUMMARY TABLE
# ============================================
print("\n=== SUMMARY ===")
print("random()         - float 0 to 1")
print("randint(a, b)    - int a to b (both inclusive)")
print("randrange(a, b)  - int a to b-1")
print("uniform(a, b)    - float a to b")
print("choice(seq)      - one random item")
print("choices(seq, k)  - k items WITH repeat")
print("sample(seq, k)   - k UNIQUE items")
print("shuffle(list)    - shuffle in-place")
print("seed(n)          - reproducible random")
