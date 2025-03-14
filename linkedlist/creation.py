class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
node1 = Node(10)
node2 = Node(11)
node3 = Node(12)
node4 = Node(13)
node5 = Node(14)
node6 = Node(15)
node7 = Node(16)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
current_node = node1
while current_node:
  print(current_node.data,end="->")
  current_node = current_node.next
print("Null")