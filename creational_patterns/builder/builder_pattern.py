"""
An exanded example of a Builder Pattern implemented in Python. Original example 
is from the book "Mastering Python Design Patterns" from Packt Publishing. 
"""

# This class and the next are the end-goal objects of this Builder Pattern
class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.ram = None
        self.gpu = None
        self.hd = None

    def __str__(self):
        info = (
            f"RAM: {self.ram}GB",
            f"Hard Drive: {self.hd}GB",
            f"GPU Model: {self.gpu}",
        )
        return "\n".join(info)


class Tablet:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.screen = None
        self.storage = None

    def __str__(self):
        info = (
            f"Screen Size: {self.screen} inches",
            f"Storage Size: {self.storage}GB",
        )
        return "\n".join(info)

# This class and the next are the Builder components of the Builder Pattern
class ComputerBuilder:
    def __init__(self):
        # Hardcoded serial for demo
        self.computer = Computer("A5221482")

    def config_ram(self, amount):
        self.computer.ram = amount

    def config_hd(self, amount):
        self.computer.hd = amount

    def config_gpu(self, model):
        self.computer.gpu = model


class TabletBuilder:
    def __init__(self):
        # Hardcoded serial for demo
        self.tablet = Tablet("A54138462")

    def config_screen(self, size):
        self.tablet.screen = size

    def config_storage(self, amount):
        self.tablet.storage = amount

# This class is the Director component of the Builder Pattern
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, ram, hd, gpu):
        self.builder = ComputerBuilder()

        # Steps
        self.builder.config_ram(ram)
        self.builder.config_hd(hd)
        self.builder.config_gpu(gpu)

    def construct_tablet(self, screen_size, storage_amount):
        self.builder = TabletBuilder()

        # Steps
        self.builder.config_screen(screen_size)
        self.builder.config_storage(storage_amount)

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet(self):
        return self.builder.tablet


# Example
if __name__ == "__main__":
    # The Director
    engineer = HardwareEngineer()

    # Computer Builder
    engineer.construct_computer(ram=2, hd=500, gpu="1080Ti")
    computer = engineer.computer
    print("Computer Specs")
    print(computer)

    # Tablet Builder
    engineer.construct_tablet(screen_size=10, storage_amount=64)
    tablet = engineer.tablet
    print("\nTablet Specs")
    print(tablet)