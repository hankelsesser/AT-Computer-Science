class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.head = None
  def push(self, data):
    item = Node(data, self.head)
    self.head = item
  def pop(self):
    item = self.head
    self.head = item.next
    return(item.data)
  def create(self, string):
      for character in string:
          self.push(character)

bracket_count= {
    "curly" : 0,
    "square" : 0,
    "parenthesis" : 0,
}

brackets = {
    "curly" : ["{","}"],
    "square" : ["[","]"],
    "parenthesis" : ["(",")"]
}

opening = ["{","[","("]
closing = ["}","]",")"]

def parse(character):
    bracket_type = ""
    if character in brackets["curly"]:
        bracket_type = "curly"
    elif character in brackets["square"]:
        bracket_type = "square"
    elif character in brackets["parenthesis"]:
        bracket_type = "parenthesis"


    if character in opening:
        bracket_count[bracket_type] += 1
    if character in opening:
        bracket_count[bracket_type] -= 1

def check(data):
    if data["curly"] == 0 and data["square"] == 0 and data["parenthesis"] == 0:
        print("VALID")
    else:
        print("INVALID")

def main(string):
    stack = Stack()
    stack.create(string)
    for i in range(len(string)):
        parse(stack.pop())
    check(bracket_count)

main(input())
