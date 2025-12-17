"""
abstract class - abstract + non-abstract methods
abstract methods -> don't have any implementation in the abstract class but must be overridden in the child class
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    # non-abstract method -> it is not mandatory to override this in the child class
    def msg(self):
        print('I am a vehicle')

    @abstractmethod
    def type(self):
        pass

    def start(self):
        pass

    def acc(self):
        pass

    def brake(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):

    def type(self):
        print('I am a car')

    def start(self):
        print('Car engine started')

    def acc(self):
        print('Car is accelerating')

    def brake(self):
        print('Car braking')

    def stop(self):
        print('Car engine stopped')

obj1 = Car()
obj1.msg()
obj1.type()
obj1.start()
obj1.acc()
obj1.brake()
obj1.stop()


