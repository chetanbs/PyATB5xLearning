class BaseTest:

    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from Excel")

    def close_browser(self):
        print("Close browser")


class TestCase1(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test Case P1 Executed")
        self.read_from_excel()
        self.close_browser()


    def test_negative(self):
        self.open_browser()
        print("Test Case N1 Executed")
        self.close_browser()


class TestCase2(BaseTest):

    def test_2(self):
        self.open_browser()
        print("Test Case P2 Executed")
        self.close_browser()


p = TestCase1()
p.test_positive()
