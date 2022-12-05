# Car类
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('U can\'t roll back an odometer!')

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage

my_new_car = Car('Mitsubishi', 'EVO', '2017')
print(my_new_car.get_descriptive_name())

# 给属性指定默认值
my_new_car.read_odometer()

# 修改属性的值
# 1.直接修改
# 2.通过方法修改
# 3.通过方法对属性的值进行递增
my_new_car.odometer_reading = 100000
my_new_car.read_odometer()
my_new_car.update_odometer(200000)
my_new_car.read_odometer()




