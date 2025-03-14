class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self.head = None
  def insert(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  def traverse(self):
    current_node = self.head
    while current_node:
      print(current_node.data,end='->')
      current_node = current_node.next
    print("Null")
linkedlist = LinkedList()
linkedlist.insert(30)
linkedlist.insert(40) 
linkedlist.insert(20) 
linkedlist.insert(70) 
linkedlist.insert(50) 
linkedlist.insert(60) 
linkedlist.traverse()