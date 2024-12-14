from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import close_browser


def test_case():
    start_browser()
    print("Running the TC")
    close_browser()

tc = test_case()