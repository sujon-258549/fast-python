# ============================================
# FACTORY DESIGN PATTERN in Python
# ============================================
# Factory Pattern = Object create korar jonno ekta SEPARATE method/class
# Client direct object banay na, factory ke bole "amake ei type er object dao"
#
# Real life: Car factory - tumi bolba "SUV chai", factory SUV banaye debe
#            tumi engine, body etc nije banate hobe na
#
# Use case: Object creation logic complex hole, multiple types of objects,
#           Loose coupling chaile
# ============================================


# ============================================
# 1. SIMPLE FACTORY (Most Common)
# Ekta method object create kore type onujayi
# ============================================
print("=== 1. SIMPLE FACTORY ===")

class Dog:
    def speak(self):
        return "Ghew Ghew!"

class Cat:
    def speak(self):
        return "Meow Meow!"

class Cow:
    def speak(self):
        return "Hamba!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal: {animal_type}")

# Client code - direct Dog(), Cat() banay na
animal1 = AnimalFactory.create_animal("dog")
animal2 = AnimalFactory.create_animal("cat")
animal3 = AnimalFactory.create_animal("cow")

print(animal1.speak())
print(animal2.speak())
print(animal3.speak())


# ============================================
# 2. FACTORY METHOD (Class based)
# Subclass decide kore kon object create hobe
# ============================================
print("\n=== 2. FACTORY METHOD ===")

class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car on road"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class Truck(Vehicle):
    def drive(self):
        return "Driving a heavy truck"

class VehicleFactory:
    def create_vehicle(self, type):
        vehicles = {
            "car": Car,
            "bike": Bike,
            "truck": Truck
        }
        vehicle_class = vehicles.get(type.lower())
        if vehicle_class:
            return vehicle_class()
        raise ValueError(f"Unknown vehicle: {type}")

factory = VehicleFactory()
v1 = factory.create_vehicle("car")
v2 = factory.create_vehicle("bike")
v3 = factory.create_vehicle("truck")

print(v1.drive())
print(v2.drive())
print(v3.drive())


# ============================================
# 3. ABSTRACT FACTORY (Advanced)
# Factory of factories - related objects together
# ============================================
print("\n=== 3. ABSTRACT FACTORY ===")

from abc import ABC, abstractmethod

# Product interfaces
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Window(ABC):
    @abstractmethod
    def open(self):
        pass

# Windows OS products
class WindowsButton(Button):
    def click(self):
        return "Windows button clicked"

class WindowsWindow(Window):
    def open(self):
        return "Windows window opened"

# Mac OS products
class MacButton(Button):
    def click(self):
        return "Mac button clicked"

class MacWindow(Window):
    def open(self):
        return "Mac window opened"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    def create_window(self):
        return WindowsWindow()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_window(self):
        return MacWindow()

# Client code
def build_app(factory):
    button = factory.create_button()
    window = factory.create_window()
    print(button.click())
    print(window.open())

print("--- Windows App ---")
build_app(WindowsFactory())

print("--- Mac App ---")
build_app(MacFactory())


# ============================================
# 4. REAL WORLD - Pizza Ordering System
# ============================================
print("\n=== 4. REAL WORLD: PIZZA SHOP ===")

class Pizza:
    def __init__(self):
        self.toppings = []
        self.size = None
        self.price = 0

    def show(self):
        print(f"Pizza: {self.__class__.__name__}")
        print(f"  Size: {self.size}")
        print(f"  Toppings: {self.toppings}")
        print(f"  Price: {self.price} tk")

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.toppings = ["cheese", "tomato", "basil"]
        self.size = "medium"
        self.price = 350

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.toppings = ["cheese", "pepperoni", "olives"]
        self.size = "large"
        self.price = 550

class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.toppings = ["cheese", "capsicum", "mushroom", "corn"]
        self.size = "medium"
        self.price = 400

class PizzaFactory:
    @staticmethod
    def order_pizza(pizza_type):
        pizzas = {
            "margherita": MargheritaPizza,
            "pepperoni": PepperoniPizza,
            "veggie": VeggiePizza,
        }
        pizza_class = pizzas.get(pizza_type.lower())
        if not pizza_class:
            raise ValueError(f"Sorry, {pizza_type} not in menu!")
        return pizza_class()

# Customer orders
print("--- Order 1 ---")
pizza1 = PizzaFactory.order_pizza("margherita")
pizza1.show()

print("\n--- Order 2 ---")
pizza2 = PizzaFactory.order_pizza("pepperoni")
pizza2.show()

print("\n--- Order 3 ---")
pizza3 = PizzaFactory.order_pizza("veggie")
pizza3.show()


# ============================================
# 5. REAL WORLD - Payment Gateway
# ============================================
print("\n=== 5. REAL WORLD: PAYMENT GATEWAY ===")

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class BkashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} tk via bKash"

class NagadPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} tk via Nagad"

class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} tk via Credit/Debit Card"

class CashPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} tk in Cash"

class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        methods = {
            "bkash": BkashPayment,
            "nagad": NagadPayment,
            "card": CardPayment,
            "cash": CashPayment,
        }
        payment_class = methods.get(method.lower())
        if not payment_class:
            raise ValueError(f"Payment method '{method}' not supported!")
        return payment_class()

# Use cases
p1 = PaymentFactory.get_payment_method("bkash")
print(p1.pay(500))

p2 = PaymentFactory.get_payment_method("nagad")
print(p2.pay(1200))

p3 = PaymentFactory.get_payment_method("card")
print(p3.pay(3000))

p4 = PaymentFactory.get_payment_method("cash")
print(p4.pay(150))


# ============================================
# 6. REAL WORLD - Notification System
# ============================================
print("\n=== 6. REAL WORLD: NOTIFICATION ===")

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"PUSH: {message}")

class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"WHATSAPP: {message}")

class NotificationFactory:
    @staticmethod
    def create(channel):
        channels = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification,
            "whatsapp": WhatsAppNotification,
        }
        notif_class = channels.get(channel.lower())
        if not notif_class:
            raise ValueError(f"Unknown channel: {channel}")
        return notif_class()

# Send via different channels
message = "Your order is confirmed!"

for channel in ["email", "sms", "push", "whatsapp"]:
    notif = NotificationFactory.create(channel)
    notif.send(message)


# ============================================
# WHY FACTORY PATTERN?
# ============================================
print("\n=== WHY USE FACTORY? ===")
print("1. Loose Coupling - client doesn't depend on concrete classes")
print("2. Easy to add new types - just add new class in factory")
print("3. Code organization - object creation logic in one place")
print("4. Flexibility - change object type without changing client code")
print("5. Single Responsibility - factory handles creation only")

print("\n=== FACTORY TYPES ===")
print("1. Simple Factory  - static method create kore")
print("2. Factory Method  - subclass decide kore which to create")
print("3. Abstract Factory - factory of factories")

print("\n=== WHEN TO USE? ===")
print("- Multiple types of related objects")
print("- Object creation logic complex")
print("- Hide creation details from client")
print("- Future e new types add hobe")
