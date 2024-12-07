class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("Reading from Excel")


class MYSQLDBConnection:

    @staticmethod
    def readMYSQLFile():
        print("Reading from MYSQL")

class TC1:

    def testcase(self):
        MYSQLDBConnection.readMYSQLFile()
        ExcelReader.read_from_excel()

obj = TC1()
obj.testcase()


# if we are able to call with class name the we need to think that as static
