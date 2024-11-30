class PyATB:

    name = None
    Batch = None
    Time = None
    Duration = None
    Location = None

    def __init__(self, name, Batch, Time, Duration, Location):
        self.name = name
        self.Batch = Batch
        self.Time = Time
        self.Duration = Duration
        self.Location = Location

    def print_student_info(self):
        print("Student Name is: ", self.name)
        print("Batch is: ", self.Batch)
        print("Time is: ", self.Time)
        print("Duration is: ", self.Duration)
        print("Location is: ", self.Location)

    def Student_Detail(self):
        pass

student_information1 = PyATB ("Pat", "Python", "Morning","3 Months", "KA" )
student_information2 = PyATB("Matt", "API", "Afternoon","1 Months", "DL" )
student_information3 = PyATB("Paul", "Automation", "Evening","2 Months", "CH" )


print("Student_Information1: ")
student_information1.print_student_info()
print("******========******")
print("Student_Information2: ")
student_information2.print_student_info()
print("******========******")
print("Student_Information3: ")
student_information3.print_student_info()