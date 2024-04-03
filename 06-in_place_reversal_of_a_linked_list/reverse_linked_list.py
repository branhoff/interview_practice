"""
## Reverse Linked List
Given the head of a singly linked list, reverse the linked list and return its
updated head.

**Constraints**

Let $n$ be the number of nodes in a linked list.
- $1 \leq n \leq 500$
- $−5000 \leq$ `Node.value` $\leq 5000$
"""

"""
Template
"""
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

"""
Template
"""
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_node_at_head(self, node):
    if self.head:
      node.next = self.head
      self.head = node
    else:
      self.head = node


  def create_linked_list(self, lst):
    for x in reversed(lst):
      new_node = Node(x)
      self.insert_node_at_head(new_node)

  def __str__(self):
    result = ""
    temp = self.head
    while temp:
      result += str(temp.data)
      temp = temp.next
      if temp:
        result += ", "
    result += ""
    return result

"""
Helper method for display
"""
def print_list_with_forward_arrow(linked_list_node):
  temp = linked_list_node
  while temp:
    print(temp.data, end=" ")  # print node value

    temp = temp.next
    if temp:
      print("→", end=" ")
    else:
      # if this is the last node, print null at the end
      print("→ null", end=" ")

"""
Solution
"""
def reverse(head):
  prev_node = None
  curr_node = head
  next_node = None

  while curr_node:
    next_node = curr_node.next
    curr_node.next = prev_node
    prev_node = curr_node
    curr_node = next_node

  head = prev_node
  return head

def main():
  input = (
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
    [3, 2, 1],
    [10],
    [1, 2],
  )

  for i in range(len(input)):
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input[i])
    print(i + 1, ".\tInput linked list: ", sep="", end="")
    print_list_with_forward_arrow(input_linked_list.head)
    print("\n\tReversed linked list: ", end="")
    print_list_with_forward_arrow(reverse(input_linked_list.head))
    print("\n", "-" * 100)


if __name__ == "__main__":
  main()