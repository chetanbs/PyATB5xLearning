from abc import ABC, abstractmethod

class GearBox(ABC):

    @abstractmethod
    def set_gear(self):
        pass


class Engine(GearBox):

    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        super().set_gear()
        pass

class Car(Engine):

    def start(self):
        print("Starting the Car")

    def stop(self):
        print("Stopping the Car")

    def set_gear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.set_gear()
        self.stop()

c = Car()
c.drive()

