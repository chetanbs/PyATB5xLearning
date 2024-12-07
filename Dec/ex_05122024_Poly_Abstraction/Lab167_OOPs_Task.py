from abc import ABC, abstractmethod

class PC:

    def __init__(self, name):
        self.name = name

class MotherBoard(ABC):

    @abstractmethod
    def start_MotherBoard(self):
        pass

class RAM(ABC):

    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):

    @abstractmethod
    def start_processor(self):
        pass

class Storage(Processor):

    @abstractmethod
    def storage_data(self):
        pass

    def start_MotherBoard(self):
        #self.start_processor()
        print("MotherBoard is Started")

    def start_ram(self):
        #self.start_ram()
        print("RAM is started")

    def start_processor(self):
        #self.start_processor()
        print("Processor is started")

    def storage_data(self):
        print("Data is stored")

    @staticmethod
    def loadOS():
        print("OS is loaded")

    def start_mouse(self):
        print("Mouse is ready to use")

    def use_HeadPhone(self):
        print("Headphone is plugged in")

    def runTC(self):
        self.start_MotherBoard()
        self.start_ram()
        self.start_processor()
        self.storage_data()
        self.loadOS()
        self.start_mouse()
        self.use_HeadPhone()


obj = Storage()
obj.runTC()






