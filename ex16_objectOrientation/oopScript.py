from oopClasses import Car
from oopClasses import Dog
from oopClasses import GoldenRetriever

car1 = Car("blue", 20000)
car2 = Car("red", 30000)

for car in (car1, car2):
    print(car)

hershey = GoldenRetriever("Hershey", 7)
print(hershey.speak())