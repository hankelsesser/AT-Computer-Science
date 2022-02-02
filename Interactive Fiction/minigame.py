import keyboard, random

def space(number):
    for i in range(number):
        print("")

class Screen:
    def __init__(self):
        self.rows = []
    def create(self):
        top = "/---------------------\ "
        self.rows.append(top)
        for i in range (10):
            self.rows.append(Line(i))
            self.rows[-1].build()
        bottom = "\---------------------/ "
        self.rows.append(bottom)
    def display(self):
        print(self.rows[0])
        for i in range(1, len(self.rows)-1):
            self.rows[i].show()
        print(self.rows[-1])
    def move(self, x, y, icon):
        self.rows[y].line[(x*2)-1] = icon

class Line:
    def __init__(self, number):
        self.number = number
        self.line = []
    def build (self):
        self.line.append("|")
        for i in range(10):
            self.line.append("-")
            self.line.append(" ")
        self.line.append("-")
        self.line.append("|")
    def show(self):
        stringline = ""
        for item in (self.line):
            stringline += item
        print(stringline)

class Player:
    def __init__(self, screen, job):
        self.x = 6
        self.y = 10
        self.screen = screen
        self.job = job
    #def get_coords(self):
        #return self.x,self.y,"^"
    def place(self):
        self.screen.move(self.x, self.y, "^")
    def move(self):
        self.screen.move(self.x, self.y, "-")
        print("Which way would you like to move? \n  W: Up\n  A: Left\n  S:Down\n  D:Right")
        choice = input('  ').upper()
        if choice == "W":
            if self.y != 1:
                self.y -= 1
            else:
                print("You can't move any higher!")
                self.move()
        elif choice == "A":
            if self.x != 1:
                self.x -= 1
            else:
                print("You can't move any farther left!")
                self.move()
        elif choice == "S":
            if self.y != 10:
                self.y += 1
            else:
                print("You can't move any lower!")
                self.move()
        elif choice == "D":
            if self.x != 10:
                self.x += 1
            else:
                print("You can't move any farther right!")
                self.move()
        else:
            print("Please enter W, A, S, or D.")
            self.move()
        self.screen.move(self.x, self.y, "^")
    def check(self, obstacles):
        for obj in obstacles:
            if self.x == obj.x and self.y == obj.y or self.x == obj.x and self.y+1 == obj.y:
                if self.y >2:
                    print ("You have",self.job["crash"])
                    return [False, False]
        if self.y == 1:
            return [False, True]
        else:
            return[True]


class Obstacle:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
    def place(self):
        self.screen.move(self.x, self.y, "0")
    def move(self):
        self.screen.move(self.x, self.y, "-")
        if self.y != 10:
            self.y+=1
            self.screen.move(self.x, self.y, "0")
        else:
            del self



class Game:
    def __init__(self, job):
        self.round = 0
        self.screen = Screen()
        self.job = job.mg_info
        self.player = Player(self.screen, self.job)
        self.running = False
        self.obstacles = []

    def run(self):
        space(10)
        print(self.job["prompt"], "\n")
        print("     ^ : You")
        print("     0 : "+self.job["obstacle"])
        self.running = True
        self.screen.create()
        self.place_obstacles()
        self.player.place()
        while self.running == True:
            self.round += 1
            self.screen.display()
            self.player.move()
            for obj in self.obstacles:
                obj.move()
            if self.round % 3 == 0: self.place_obstacles()
            self.gamestatus = self.player.check(self.obstacles)
            space(15)
            self.running = self.gamestatus[0]
        if self.gamestatus[1] == True: #game is won
            self.win()
        else: self.lose()
        return(self.gamestatus[1])
    def place_obstacles(self):
        for i in range(4):
            self.obstacles.append(Obstacle(random.randint(1,10), 1, self.screen))
        for obj in self.obstacles:
            obj.place()
    def win(self):
        print(self.job["win"]+"\n\n\n\n")
    def lose(self):
        print(self.job["lose"]+"\n\n\n\n")








    #hah
