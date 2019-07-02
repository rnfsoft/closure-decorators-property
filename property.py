# Tutorial from https://www.programiz.com/python-programming/property

class Celsis:
    def __init__(self, temperature=0):
        self._temperature = temperature
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


    # def __init__(self, temperature=0):
    #     self.temperature = temperature

    # def to_fahrenheit(self):
    #     return (self.temperature * 1.8) - 32

    # def get_temperature(self):
    #     print("Getting value")
    #     return self._temperature
    
    # def set_temperature(self, value):
    #     if value < -273:
    #         raise ValueError("Temperature below -273 is not possible")
    #     print("Setting value")
    #     self._temperature = value
    
    # temperature = property(get_temperature, set_temperature)
    
    
    
    # def __init__(self, temperature = 0):
    #     self.set_temperature(temperature)
    
    # def set_temperature(self, value):
    #     if value < -273:
    #         raise ValueError("Temperature below -273 is not possible")
    #     self._temperature = value
    
    # def get_temperature(self):
    #     return self._temperature

    # def to_fahrenheit(self):
    #     return (self.get_temperature() * 1.8) + 32
    
    
    # def __init__(self, temperature=0):
    #     self.temperature = temperature

    # def to_fahrenheit(self):
    #     return (self.temperature * 1.8) + 32

c = Celsis()
c.temperature = 37

print(c.to_fahrenheit())
# c = Celsis(37)
# print(c.get_temperature())
# c.set_temperature(10)
# print(c.get_temperature())


# man = Celsis()

# man.temperature = 37

# print(man.temperature)
# print(man.__dict__['temperature'])
# print(man.to_fahrenheit())

# print(man.__dict__)