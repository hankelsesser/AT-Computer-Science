members = []

class member:
    def __init__ (self, info):
        self.name = info[0]
        self.ID = str(info[1])
        self.birthday = info[2]
    def show_info(self):
        print("Name: "+ self.name)
        print("ID Number: "+ self.ID)
        print("Birthday: "+ self.birthday)
    def get_age(self):
        year = 2020
        print(self.name + " is " + str(int(year - (2000 + int(self.birthday[-2:])))))

def new():
    info = []
    print("Name:")
    name = str(input())
    info.append(name)
    print("ID Number")
    ID = int(input())
    info.append(ID)
    print("Birthday:")
    birthday = str(input())
    info.append(birthday)
    return info


hank = member(new())
print(hank.name)
print(hank.get_age())
print(hank.show_info())
