# Directory -> Folder
# Special file used in Python to defie packages and initialize -> __init__.py
# It marks the directory as a Python Package


from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import close_browser

class TestCase:

    def test_case(self):
        start_browser()
        print("Running the TC")
        close_browser()

obj = TestCase()
obj.test_case()