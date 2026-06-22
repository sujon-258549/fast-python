# ============================================
# COLLECTIONS MODULE - Complete Guide
# ============================================
# collections = built-in list/dict/tuple er upgraded version
# More powerful, specialized data structures
#
# Main classes:
# 1. Counter      - count korar jonno
# 2. namedtuple   - tuple but with names
# 3. OrderedDict  - order preserve kore (3.7+ regular dict o kore)
# 4. defaultdict  - default value diye dict
# 5. deque        - double-ended queue (fast)
# 6. ChainMap     - multiple dict ek shathe
# ============================================

from collections import (
    Counter, namedtuple, OrderedDict,
    defaultdict, deque, ChainMap
)


# ============================================
# 1. Counter - Element count kore
# ============================================
print("=== 1. Counter ===")

# String e letter count
text = "programming"
counter = Counter(text)
print(counter)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

# List e item count
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
fruit_count = Counter(fruits)
print(fruit_count)
# Counter({'apple': 3, 'banana': 2, 'mango': 1})

# Most common items
print(fruit_count.most_common(2))    # top 2: [('apple', 3), ('banana', 2)]

# Counter methods
print(fruit_count["apple"])          # 3
print(fruit_count["grape"])          # 0 (no error!)

# Add more
fruit_count.update(["apple", "grape"])
print(fruit_count)

# Word count from sentence
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
print(Counter(words))


# ============================================
# 2. namedtuple - Tuple with names (mini class)
# ============================================
print("\n=== 2. namedtuple ===")

# Define namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)
print(p1)              # Point(x=10, y=20)
print(p1.x, p1.y)      # 10 20
print(p1[0], p1[1])    # 10 20 (still works as tuple)

# Real example - Student
Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student("Sujon", 22, "A")
s2 = Student("Karim", 21, "B")

print(s1)
print(f"{s1.name} is {s1.age} years old with grade {s1.grade}")

# Convert to dict
print(s1._asdict())

# Replace value (new tuple)
s1_new = s1._replace(age=23)
print(s1_new)


# ============================================
# 3. OrderedDict - Insertion order preserve
# Note: Python 3.7+ regular dict o order maintain kore
# ============================================
print("\n=== 3. OrderedDict ===")

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)            # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move to end
od.move_to_end("a")
print(od)            # 'a' goes to end

# Move to beginning
od.move_to_end("c", last=False)
print(od)

# Pop from end/beginning
od.popitem()          # last item remove
od.popitem(last=False)  # first item remove
print(od)


# ============================================
# 4. defaultdict - Auto default value
# ============================================
print("\n=== 4. defaultdict ===")

# Regular dict problem
regular = {}
# regular["x"] += 1    # KeyError!

# defaultdict solution
dd = defaultdict(int)    # default = 0
dd["a"] += 1
dd["b"] += 5
dd["a"] += 2
print(dd)                # defaultdict(<class 'int'>, {'a': 3, 'b': 5})

# Group items by letter
words = ["apple", "ant", "banana", "berry", "cat", "car"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(grouped)
# {'a': ['apple', 'ant'], 'b': ['banana', 'berry'], 'c': ['cat', 'car']}

# Count with defaultdict
count = defaultdict(int)
text = "hello world"
for ch in text:
    count[ch] += 1
print(dict(count))


# ============================================
# 5. deque - Double Ended Queue (FAST!)
# Both ends e add/remove O(1)
# ============================================
print("\n=== 5. deque ===")

dq = deque([1, 2, 3, 4, 5])
print(dq)

# Add at right
dq.append(6)
print(dq)            # deque([1, 2, 3, 4, 5, 6])

# Add at left
dq.appendleft(0)
print(dq)            # deque([0, 1, 2, 3, 4, 5, 6])

# Remove from right
dq.pop()
print(dq)            # deque([0, 1, 2, 3, 4, 5])

# Remove from left
dq.popleft()
print(dq)            # deque([1, 2, 3, 4, 5])

# Rotate
dq.rotate(2)         # right rotate
print(dq)            # deque([4, 5, 1, 2, 3])

dq.rotate(-2)        # left rotate
print(dq)

# Limited deque (last N items)
recent = deque(maxlen=3)
for i in range(10):
    recent.append(i)
print(recent)        # deque([7, 8, 9], maxlen=3)


# ============================================
# 6. ChainMap - Multiple dict combine
# ============================================
print("\n=== 6. ChainMap ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "a": 100}    # 'a' will be from dict1

cm = ChainMap(dict1, dict2, dict3)
print(cm)
print(cm["a"])       # 1 (first dict wins)
print(cm["c"])       # 3
print(cm["e"])       # 5

# All keys
print(list(cm.keys()))

# Useful for configuration layers
defaults = {"theme": "light", "lang": "english"}
user_settings = {"theme": "dark"}
final_config = ChainMap(user_settings, defaults)
print(final_config["theme"])    # dark (user_settings priority)
print(final_config["lang"])     # english (from defaults)


# ============================================
# REAL WORLD EXAMPLES
# ============================================

# Example 1: Most common words in text
print("\n=== Example 1: WORD FREQUENCY ===")

text = """python is great python is easy python is powerful
          learning python is fun"""
words = text.split()
top_words = Counter(words).most_common(3)
print(top_words)


# Example 2: Student records using namedtuple
print("\n=== Example 2: STUDENT RECORDS ===")

Student = namedtuple("Student", "name roll marks")
students = [
    Student("Sujon", 1, 85),
    Student("Karim", 2, 92),
    Student("Rahim", 3, 78),
]

# Top scorer
top = max(students, key=lambda s: s.marks)
print(f"Top: {top.name} with {top.marks}")


# Example 3: Browser History using deque
print("\n=== Example 3: BROWSER HISTORY ===")

history = deque(maxlen=5)
sites = ["google.com", "youtube.com", "github.com",
         "stackoverflow.com", "python.org", "claude.ai", "anthropic.com"]

for site in sites:
    history.append(site)

print("Last 5 sites:", list(history))


# Example 4: Word grouping by length
print("\n=== Example 4: GROUP BY LENGTH ===")

words = ["cat", "dog", "bird", "fish", "elephant", "ant", "lion"]
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)

for length, items in sorted(groups.items()):
    print(f"Length {length}: {items}")


# Example 5: Config Manager with ChainMap
print("\n=== Example 5: CONFIG MANAGER ===")

system_default = {"timeout": 30, "retries": 3, "debug": False}
env_settings = {"timeout": 60}
user_settings = {"debug": True}

config = ChainMap(user_settings, env_settings, system_default)
print(f"timeout: {config['timeout']}")    # 60 (from env)
print(f"retries: {config['retries']}")    # 3 (from default)
print(f"debug:   {config['debug']}")      # True (from user)


# ============================================
# SUMMARY
# ============================================
print("\n=== SUMMARY ===")
print("Counter      - count items, most_common()")
print("namedtuple   - tuple with field names")
print("OrderedDict  - dict with order operations")
print("defaultdict  - dict with default value")
print("deque        - fast double-ended queue")
print("ChainMap     - combine multiple dicts")
