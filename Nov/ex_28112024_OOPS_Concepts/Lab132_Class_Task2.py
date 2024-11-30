# Create a Class Name API - RestfulBooker
# Name, list_of_api, links{}
# print_apis, print_set()

class RestfulBooker:

    name = None
    list_of_api = []
    links = {}

    def __init__(self, name, list_of_api, Links):
        self.name = name
        self.list_of_api = list_of_api
        self.Links = Links

    def name(self):
        print("RestfulBooker")


    def api(self):
        print("List of APIs: ")
        print(self.list_of_api)


    def links(self):
        #print("List of Links is: ")
        print(self.links())


method = RestfulBooker("RestfulBooker",["GET"], {"https//www.sdet.qa"})
print(method.api())
print(method.links())


