from faker import Faker
from faker.providers import BaseProvider
import pandas as pd

class Computer:
    def __init__(self, code):
        self.code = code
        self.processor = None
        self.videocard = None
        self.ram = None
        self.screen = None
        self.inches = None
        self.hertz = None
        self.illumination = None
        self.price = None


    def __str__(self):
        info: str = f"Computer ID {self.code} \n" \
                    f"Processor {self.Processor} \n" \
                    f"Videocard {self.videocard} \n" \
                    f"Ram {self.ram} \n" \
                    f"Screen {self.screen} \n" \
                    f"Inches {self.inches} \n" \
                    f"Hertz: {self.hertz} \n" \
                    f"Illumination: {self.illumination} \n" \
                    f"Price {self.price} \n"
        return info


class ComputerProvider(BaseProvider):
    Processor = ["Intel Celeron", "Intel Pentium",
                 "Amd Ryzen 3", "Amd Ryzen 5", "Amd Ryzen 7",
                 "Amd Ryzen 9", "Intel Core i3", "Intel Core i5",
                 "Intel Core i7", "Intel Core i9"]

    Videocard = ["GeoForce GTX 1050", "GeoForce GTX 1650", "GeoForce GTX 1660 Ti",
                 "GeoForce GTX 2060", "GeoForce GTX 3050", "GeoForce GTX 3050 Ti",
                 "GeoForce GTX 3060", "GeoForce GTX 3070", "GeoForce GTX 3080",]

    Ram = ["2", "4", "8", "16", "32"]

    Inches = ["13", "14", "15"]

    Screen = ["Да", "нет"]

    Herts = ["144", "60"]

    Illumination = ["Да", "Нет"]

    fake_code = Faker("ru_RU")

    def create_fake_computer(self):
        computer = Computer(self.fake_code.bothify(text="???-###"))
        computer.processor = self.random_element(self.Processor)
        computer.videocard = self.random_element(self.Videocard)
        computer.ram = self.random_element(self.Ram)
        computer.inches = self.random_element(self.Inches)
        computer.screen = self.random_element(self.Screen)
        computer.hertz = self.random_element(self.Herts)
        computer.illumination = self.random_element(self.Illumination)
        computer.price = self.random_int(15000, 40000)
        return computer


my_faker = Faker()
my_faker.add_provider(ComputerProvider)
data = []
for i in range(1000):
    fak = my_faker.create_fake_computer()
    dat = {"Computer ID": fak.code,
           "Processor": fak.processor,
           "Videocard": fak.videocard,
           "Ram": fak.ram,
           "Inches": fak.inches,
           "Screen": fak.screen,
           "hertz": fak.hertz,
           "Illumination": fak.illumination,
           "Computer price": fak.price}
    data.append(dat)

df = pd.DataFrame(data=data)
print(df)
