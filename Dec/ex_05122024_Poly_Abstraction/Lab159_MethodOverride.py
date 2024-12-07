class OldBrowser:

    def start_browser(self):
        print("IE Browser is Starting")

    def stop_browser(self):
        print("IE Browser is Closing")


class Chrome(OldBrowser):

    def start_browser(self):
        super().start_browser()
        print("Chrome browser is starting")

    def stop_browser(self):
        print("Chrome browser is closing")


obj = Chrome()
obj.start_browser()
obj.stop_browser()