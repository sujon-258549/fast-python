# ============================================
# BUILDER DESIGN PATTERN in Python
# ============================================
# Builder Pattern = Complex object ke STEP BY STEP banano
# Ekta object er onek part/option thakle, builder use kori
#
# Real life: Burger banano - bun, patty, cheese, sauce, veggies
#            sob ek shathe na, step by step add koro
#
# Use case: Object er onek optional parameter, complex construction,
#           Same construction process diye different objects
# ============================================


# ============================================
# 1. PROBLEM WITHOUT BUILDER
# Onek parameter wala constructor - ugly!
# ============================================
print("=== 1. PROBLEM WITHOUT BUILDER ===")

class BadPizza:
    def __init__(self, size, cheese, pepperoni, mushroom,
                 olives, onion, sauce, crust, extra_cheese):
        # Onek parameter - confusing, hard to remember order!
        self.size = size
        self.cheese = cheese
        # ... etc

# Ugly call - kon parameter ki bujha jay na
bad = BadPizza("large", True, False, True, False, True, "tomato", "thin", True)
print("Bad pizza created - but hard to read!")


# ============================================
# 2. BASIC BUILDER PATTERN
# Step by step object banano
# ============================================
print("\n=== 2. BASIC BUILDER ===")

class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.sauce = None
        self.cheese = False

    def show(self):
        print(f"Pizza: {self.size}, {self.crust} crust")
        print(f"  Sauce: {self.sauce}")
        print(f"  Cheese: {'Yes' if self.cheese else 'No'}")
        print(f"  Toppings: {self.toppings}")

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self          # IMPORTANT: return self for chaining!

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def build(self):
        return self.pizza

# METHOD CHAINING - sundor look!
pizza = (PizzaBuilder()
         .set_size("large")
         .set_crust("thin")
         .set_sauce("tomato")
         .add_cheese()
         .add_topping("mushroom")
         .add_topping("olives")
         .add_topping("pepperoni")
         .build())

pizza.show()


# ============================================
# 3. BUILDER FOR BURGER
# Real world example
# ============================================
print("\n=== 3. BURGER BUILDER ===")

class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = False
        self.lettuce = False
        self.tomato = False
        self.sauce = []
        self.extras = []

    def show(self):
        print(f"Burger:")
        print(f"  Bun: {self.bun}")
        print(f"  Patty: {self.patty}")
        print(f"  Cheese: {self.cheese}")
        print(f"  Lettuce: {self.lettuce}")
        print(f"  Tomato: {self.tomato}")
        print(f"  Sauce: {self.sauce}")
        print(f"  Extras: {self.extras}")

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def set_bun(self, bun_type):
        self.burger.bun = bun_type
        return self

    def set_patty(self, patty_type):
        self.burger.patty = patty_type
        return self

    def add_cheese(self):
        self.burger.cheese = True
        return self

    def add_lettuce(self):
        self.burger.lettuce = True
        return self

    def add_tomato(self):
        self.burger.tomato = True
        return self

    def add_sauce(self, sauce):
        self.burger.sauce.append(sauce)
        return self

    def add_extra(self, item):
        self.burger.extras.append(item)
        return self

    def build(self):
        return self.burger

# Customer 1: Beef burger with everything
print("--- Customer 1: Full Beef Burger ---")
burger1 = (BurgerBuilder()
           .set_bun("sesame")
           .set_patty("beef")
           .add_cheese()
           .add_lettuce()
           .add_tomato()
           .add_sauce("mayo")
           .add_sauce("ketchup")
           .add_extra("bacon")
           .build())
burger1.show()

# Customer 2: Simple chicken burger
print("\n--- Customer 2: Simple Chicken Burger ---")
burger2 = (BurgerBuilder()
           .set_bun("plain")
           .set_patty("chicken")
           .add_lettuce()
           .add_sauce("mustard")
           .build())
burger2.show()


# ============================================
# 4. COMPUTER BUILDER
# Different specs for different needs
# ============================================
print("\n=== 4. COMPUTER BUILDER ===")

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None
        self.peripherals = []

    def show(self):
        print(f"Computer Specs:")
        print(f"  CPU: {self.cpu}")
        print(f"  RAM: {self.ram}")
        print(f"  Storage: {self.storage}")
        print(f"  GPU: {self.gpu}")
        print(f"  OS: {self.os}")
        print(f"  Peripherals: {self.peripherals}")

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_os(self, os):
        self.computer.os = os
        return self

    def add_peripheral(self, item):
        self.computer.peripherals.append(item)
        return self

    def build(self):
        return self.computer

# Gaming PC
print("--- Gaming PC ---")
gaming_pc = (ComputerBuilder()
             .set_cpu("Intel i9")
             .set_ram("32GB DDR5")
             .set_storage("2TB SSD")
             .set_gpu("RTX 4090")
             .set_os("Windows 11")
             .add_peripheral("Gaming Mouse")
             .add_peripheral("Mechanical Keyboard")
             .build())
gaming_pc.show()

# Office PC
print("\n--- Office PC ---")
office_pc = (ComputerBuilder()
             .set_cpu("Intel i5")
             .set_ram("8GB DDR4")
             .set_storage("256GB SSD")
             .set_os("Windows 11")
             .build())
office_pc.show()


# ============================================
# 5. BUILDER WITH DIRECTOR
# Director knows the construction steps for common types
# ============================================
print("\n=== 5. BUILDER WITH DIRECTOR ===")

class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.color = None
        self.features = []

    def show(self):
        print(f"{self.color} {self.brand} {self.model}")
        print(f"  Engine: {self.engine}")
        print(f"  Features: {self.features}")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def add_feature(self, feature):
        self.car.features.append(feature)
        return self

    def build(self):
        return self.car

class CarDirector:
    """Director knows how to build standard cars"""

    @staticmethod
    def build_sports_car():
        return (CarBuilder()
                .set_brand("Ferrari")
                .set_model("488 GTB")
                .set_engine("V8 Twin-Turbo")
                .set_color("Red")
                .add_feature("Sport Mode")
                .add_feature("Carbon Fiber")
                .add_feature("Racing Seats")
                .build())

    @staticmethod
    def build_family_car():
        return (CarBuilder()
                .set_brand("Toyota")
                .set_model("Camry")
                .set_engine("2.5L Hybrid")
                .set_color("White")
                .add_feature("AC")
                .add_feature("Auto Transmission")
                .add_feature("7 Seater")
                .build())

    @staticmethod
    def build_economy_car():
        return (CarBuilder()
                .set_brand("Suzuki")
                .set_model("Alto")
                .set_engine("800cc")
                .set_color("Silver")
                .add_feature("AC")
                .build())

# Client just says what type, director handles details
print("--- Sports Car ---")
CarDirector.build_sports_car().show()

print("\n--- Family Car ---")
CarDirector.build_family_car().show()

print("\n--- Economy Car ---")
CarDirector.build_economy_car().show()


# ============================================
# 6. REAL WORLD - HTTP Request Builder
# ============================================
print("\n=== 6. HTTP REQUEST BUILDER ===")

class HttpRequest:
    def __init__(self):
        self.url = None
        self.method = "GET"
        self.headers = {}
        self.params = {}
        self.body = None
        self.timeout = 30

    def show(self):
        print(f"{self.method} {self.url}")
        print(f"  Headers: {self.headers}")
        print(f"  Params: {self.params}")
        print(f"  Body: {self.body}")
        print(f"  Timeout: {self.timeout}s")

class HttpRequestBuilder:
    def __init__(self):
        self.request = HttpRequest()

    def url(self, url):
        self.request.url = url
        return self

    def method(self, method):
        self.request.method = method
        return self

    def header(self, key, value):
        self.request.headers[key] = value
        return self

    def param(self, key, value):
        self.request.params[key] = value
        return self

    def body(self, body):
        self.request.body = body
        return self

    def timeout(self, seconds):
        self.request.timeout = seconds
        return self

    def build(self):
        return self.request

# Build API request with fluent interface
api_request = (HttpRequestBuilder()
               .url("https://api.example.com/users")
               .method("POST")
               .header("Authorization", "Bearer xyz123")
               .header("Content-Type", "application/json")
               .param("page", "1")
               .body({"name": "Sujon", "age": 22})
               .timeout(60)
               .build())

api_request.show()


# ============================================
# WHY BUILDER PATTERN?
# ============================================
print("\n=== WHY USE BUILDER? ===")
print("1. Readable - method chaining sundor")
print("2. Flexible - optional parameters easy")
print("3. Step by step - complex object banano shoja")
print("4. Same builder, different products")
print("5. No giant constructor with many parameters")

print("\n=== WHEN TO USE? ===")
print("- Object er onek (5+) parameter ache")
print("- Onek parameter optional")
print("- Same construction process, different output")
print("- Immutable object banate")
print("- Method chaining chaile (.set().set().build())")

print("\n=== KEY COMPONENTS ===")
print("1. Product    - final object (Pizza, Burger, Car)")
print("2. Builder    - step by step build kore")
print("3. Director   - (optional) common patterns banaye")
print("4. build()    - final object return kore")
