from datetime import datetime
import shelve, hashlib

class Message:
    def __init__(self, user, text, time):
        self.user = user
        self.text = text
        self.time = time
    def show(self):
        print(self.user.get_username()+ ' said "' + self.text + '" at ' + str(self.time))

class User:
    def __init__(self, username, password):
        self.name = username
        self.password = password
    def logout(self):
        main()
    def get_username(self):
        return(self.name)
    def change_password(self):
        hasher = hashlib.sha256()
        hasher.update(str.encode(input('What is your current password? ')))
        password = hasher.digest()
        if password == self.password:
            hasher = hashlib.sha256()
            hasher.update(str.encode(input('What would you like your new password to be? ')))
            new_password = hasher.digest()
            self.password = new_password
            with shelve.open('users') as users:
                    users[self.name] = self
            print("Password set!")

        else:
            print("Password is incorrect. Please try again.")
            space(1)
            self.change_password()


class Menu:
    def __init__(self, user):
        self.user = user
    def show(self):
        print('Menu Choices')
        print('1: post a message')
        print('2: display messages')
        print('3: logout')
        print('4: change password')
        print('5: quit')
        choice = input('What would you like to do? ')
        space(1)
        if choice == '1': # post a message
            self.new_message()
        elif choice == '2': # display messages
            self.show_messages()
        elif choice == '3': # display messages
            self.user.logout()
        elif choice == '4': # display messages
            self.user.change_password()
            self.show()
        elif choice == '5': # display messages
            print("Bye Bye!")
        else:
            print('please enter a valid choice')
        print()
    def new_message(self):
        messages=[]
        text = input('What would you like you message to say? ')
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        messages.append(Message(self.user, text, time))
        with shelve.open('messages') as msg:
                msg[time] = messages[-1]
        print("Message Posted.")
        self.show()
    def show_messages(self):
        with shelve.open('messages') as msg:
                for key in msg:
                    msg[key].show()
        space(2)
        self.show()


class Login:
    def __init__(self):
        self.username = ""
    def start(self):
        self.username = input('What is your username? ')
        user_found = self.user_in_db()
        if user_found == False:
            print('Username not found')
            print(" 1: create new account")
            print(" 2: try again")
            choice = int(input(" "))
            if choice == 1: return(self.new_user())
            elif choice == 2: self.start()
            else:
                print("choice not valid")
                self.start()
        else:
            return(self.returning_user())

    def user_in_db(self):
        with shelve.open('users') as users:
                for key in users:
                    if key == self.username:
                        return True
                return False
    def new_user(self):
        print("You will be registered as a new user.")
        hasher = hashlib.sha256()
        hasher.update(str.encode(input('What would you like your password to be? ')))
        password = hasher.digest()
        with shelve.open('users') as users:
                users[self.username] = User(self.username, password)
                print("Account Created!")
                return [True, users[self.username]]
    def returning_user(self):
        hasher = hashlib.sha256()
        hasher.update(str.encode(input('What is your password? ')))
        password = hasher.digest()
        with shelve.open('users') as users:
            if users[self.username].password == password:
                space(1)
                print("Login Complete!")
                space(1)
                return [True, users[self.username]]
            else:
                print ("Wrong password")
                return [False]

def space(number):
    for i in range(number):
        print("")

def main():
    login = Login()
    space(1)
    print('Welcome to PACKER MICROBLOG')
    space(1)
    login_result = login.start()
    if login_result[0] == True:
        user = login_result[1]
        menu = Menu(user)
        menu.show()
    else:
        print("Password not found")
        login_result = login.start()

main()
