class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"Name: {self.name} | Price: ${self.price:.2f} | "
                f"Stock: {self.stock} | Warranty: {self.warranty_period} months")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
        else:
            print("Not enough stock available!")

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return (super().__str__() +
                f" | Screen: {self.screen_size}\" | Battery: {self.battery_life}h")

    def make_call(self):
        print(f"{self.name} is making a call...")

    def install_app(self):
        print(f"Installing app on {self.name}...")

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return (super().__str__() +
                f" | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz")

    def run_program(self):
        print(f"{self.name} is running a program...")

    def use_keyboard(self):
        print(f"Typing on {self.name}'s keyboard...")


class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return (super().__str__() +
                f" | Resolution: {self.screen_resolution} | Weight: {self.weight}g")

    def browse_internet(self):
        print(f"{self.name} is browsing the internet...")

    def use_touchscreen(self):
        print(f"Using touchscreen on {self.name}...")

class Cart:
    def __init__(self):
        self.items = [] 
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            print(f"Added {amount} x {device.name} to cart.")
        else:
            print("Not enough stock available!")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if amount <= item[1]:
                    self.items.remove(item)
                    self.total_price -= device.price * amount
                    print(f"Removed {amount} x {device.name} from cart.")
                else:
                    print("Invalid amount to remove.")
                return
        print("Device not found in cart.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return
        for device, amount in self.items:
            print(f"{device.name} x {amount} = ${device.price * amount:.2f}")
        print(f"Total: ${self.total_price:.2f}")

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
            return

        for device, amount in self.items:
            if not device.is_available(amount):
                print(f"{device.name} does not have enough stock.")
                return

        for device, amount in self.items:
            device.reduce_stock(amount)

        print("\n===== RECEIPT =====")
        self.print_items()
        print("Thank you for your purchase!")
        self.items.clear()
        self.total_price = 0



def create_devices():
    devices = []

    # Smartphones
    devices.append(Smartphone("iPhone 13", 999, 10, 24, 6.1, 20))
    devices.append(Smartphone("Samsung S22", 850, 15, 24, 6.2, 22))
    devices.append(Smartphone("Google Pixel 7", 700, 8, 24, 6.3, 24))
    devices.append(Smartphone("OnePlus 11", 650, 12, 24, 6.7, 25))
    devices.append(Smartphone("Xiaomi 13", 600, 20, 24, 6.5, 23))

    # Laptops
    devices.append(Laptop("MacBook Pro", 2000, 5, 36, 16, 3.2))
    devices.append(Laptop("Dell XPS 13", 1500, 7, 24, 16, 3.0))
    devices.append(Laptop("HP Spectre", 1400, 10, 24, 16, 2.8))
    devices.append(Laptop("Lenovo ThinkPad", 1300, 6, 24, 8, 2.5))
    devices.append(Laptop("Asus ROG", 1800, 4, 24, 32, 3.5))

    # Tablets
    devices.append(Tablet("iPad Pro", 1100, 9, 24, "2048x1536", 470))
    devices.append(Tablet("Samsung Tab S8", 900, 14, 24, "2560x1600", 500))
    devices.append(Tablet("Surface Go", 800, 6, 24, "1920x1280", 520))
    devices.append(Tablet("Lenovo Tab P12", 600, 11, 24, "2000x1200", 480))
    devices.append(Tablet("Huawei MatePad", 550, 13, 24, "2560x1600", 450))

    # Add 5 more mixed devices
    devices.append(Smartphone("Sony Xperia 5", 780, 7, 24, 6.1, 21))
    devices.append(Laptop("Acer Swift 3", 900, 8, 24, 8, 2.6))
    devices.append(Tablet("Amazon Fire HD", 300, 25, 12, "1280x800", 400))
    devices.append(Smartphone("Motorola Edge", 720, 9, 24, 6.6, 22))
    devices.append(Laptop("MSI Modern 14", 1000, 6, 24, 16, 3.1))

    return devices


def main():
    devices = create_devices()
    cart = Cart()

    while True:
        print("\n===== Electronic Store =====")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            for i, device in enumerate(devices):
                print(f"{i + 1}. {device}")

            selection = int(input("Select device number to add to cart (0 to cancel): "))
            if selection > 0 and selection <= len(devices):
                amount = int(input("Enter quantity: "))
                cart.add_device(devices[selection - 1], amount)

        elif choice == "2":
            cart.print_items()

        elif choice == "3":
            cart.checkout()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
