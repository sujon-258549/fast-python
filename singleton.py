# ============================================
# SINGLETON DESIGN PATTERN in Python
# ============================================
# Singleton = Ekta class er SHUDHU EKTA object tairi hobe
# Jotobar object create korar try korbe, same object return korbe
#
# Use case: Database connection, Logger, Configuration,
#           Cache, Thread pool, etc.
# ============================================


# ============================================
# 1. BASIC SINGLETON (using __new__ method)
# Most common way
# ============================================
print("=== 1. BASIC SINGLETON ===")

class Singleton:
    _instance = None    # class variable - shared by all

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("New object created!")
        else:
            print("Returning existing object")
        return cls._instance

# Test
obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()

print(f"obj1 id: {id(obj1)}")
print(f"obj2 id: {id(obj2)}")
print(f"obj3 id: {id(obj3)}")
print(f"Same object? {obj1 is obj2 is obj3}")   # True


# ============================================
# 2. SINGLETON WITH __init__ (with data)
# ============================================
print("\n=== 2. SINGLETON WITH DATA ===")

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name="DefaultApp", version="1.0"):
        self.name = name
        self.version = version

config1 = Config("MyApp", "2.0")
print(f"Config1: {config1.name} v{config1.version}")

config2 = Config("AnotherApp", "3.0")
print(f"Config2: {config2.name} v{config2.version}")

# Both are same object! __init__ overwrite kore
print(f"Same object? {config1 is config2}")   # True
print(f"Config1 name now: {config1.name}")    # AnotherApp (overwritten!)


# ============================================
# 3. SINGLETON USING DECORATOR
# Clean and reusable way
# ============================================
print("\n=== 3. SINGLETON USING DECORATOR ===")

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")

    def show_logs(self):
        print("All logs:", self.logs)

log1 = Logger()
log1.log("App started")

log2 = Logger()
log2.log("User logged in")

print(f"Same logger? {log1 is log2}")   # True
log1.show_logs()   # Shows BOTH logs (same object)


# ============================================
# 4. SINGLETON USING METACLASS
# Advanced way - most "pythonic"
# ============================================
print("\n=== 4. SINGLETON USING METACLASS ===")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Database connection created!")
        self.connection = "Connected to DB"

    def query(self, sql):
        print(f"Running: {sql}")

# Test - "Database connection created!" prints only ONCE
db1 = Database()
db2 = Database()
db3 = Database()

print(f"Same DB? {db1 is db2 is db3}")
db1.query("SELECT * FROM users")


# ============================================
# 5. REAL WORLD EXAMPLE - Database Connection
# Why Singleton? Multiple connections = waste of resources
# ============================================
print("\n=== 5. REAL WORLD: DATABASE ===")

class DatabaseConnection:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize only once
        if not DatabaseConnection._initialized:
            self.host = "localhost"
            self.port = 5432
            self.connection_id = "DB-001"
            print(f"Connecting to {self.host}:{self.port}...")
            DatabaseConnection._initialized = True

    def execute(self, query):
        print(f"[{self.connection_id}] Executing: {query}")

# User module uses DB
user_db = DatabaseConnection()
user_db.execute("SELECT * FROM users")

# Product module uses DB
product_db = DatabaseConnection()
product_db.execute("SELECT * FROM products")

# Order module uses DB
order_db = DatabaseConnection()
order_db.execute("SELECT * FROM orders")

print(f"All same connection? {user_db is product_db is order_db}")


# ============================================
# 6. REAL WORLD EXAMPLE - Application Settings
# ============================================
print("\n=== 6. REAL WORLD: APP SETTINGS ===")

class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {
                "theme": "dark",
                "language": "english",
                "notifications": True
            }
        return cls._instance

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings[key] = value

    def show_all(self):
        print(self.settings)

# Different parts of app access same settings
settings_a = AppSettings()
settings_a.set("theme", "light")

settings_b = AppSettings()
print(f"Theme in B: {settings_b.get('theme')}")   # light (same instance!)

settings_b.show_all()


# ============================================
# WHY SINGLETON?
# ============================================
print("\n=== WHY USE SINGLETON? ===")
print("1. Resource saving - one DB connection, not many")
print("2. Global access - one config for whole app")
print("3. Consistency - same data everywhere")
print("4. Memory efficient - only one object in memory")
print("5. Coordination - shared state across modules")

print("\n=== COMMON USE CASES ===")
print("- Database Connection")
print("- Logger")
print("- Configuration Manager")
print("- Cache Manager")
print("- Thread Pool")
print("- Print Spooler")
print("- File Manager")
