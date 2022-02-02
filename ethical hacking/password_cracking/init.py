import crypt
import getpass

def test_pass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print ("[+] Found Password: "+word+"\n")
            return
    print("[-] Password Not Found.")


def main():
    print("hello!")
    username = input('username: ')
    #Password = (getpass.getpass(prompt = "password: "),"HX")
    password = crypt.crypt(getpass.getpass(prompt = "password: "),"HX")
    users = open('passwords.txt','a')
    users.write(username+":"+password+"\n")
    users.close()
    a = input()
    crack()

def crack():
    passFile = open("passwords.txt")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip("\n")
            print("cracking password for",user)
            test_pass(cryptPass)
        else:
            print("ol")
main()
