# ============================================
# Python File Handling - Complete Example
# ============================================

# 1. READ - Read file
print("=== READ FILE ===")
file = open("sujon.txt", "r")
print(file.read())
file.close()


# 2. WRITE - Write to file (old data will be erased)
print("\n=== WRITE FILE ===")
file = open("sujon.txt", "w")
file.write("I am a student\n")
file.write("I am learning Python\n")
file.close()
print("Written to file!")


# 3. APPEND - Add at the end of file
print("\n=== APPEND FILE ===")
file = open("sujon.txt", "a")
file.write("This is a new line\n")
file.close()
print("Added to file!")


# 4. READ LINE BY LINE
print("\n=== READ LINE BY LINE ===")
file = open("sujon.txt", "r")
for line in file:
    print(line.strip())
file.close()


# 5. READLINES - All lines in a list
print("\n=== READLINES (list) ===")
file = open("sujon.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# 6. WITH STATEMENT - Best practice (auto close)
print("\n=== WITH STATEMENT ===")
with open("sujon.txt", "r") as file:
    content = file.read()
    print(content)


# 7. TRY-EXCEPT - Error handling
print("\n=== ERROR HANDLING ===")
try:
    with open("sujon.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error: {e}")
