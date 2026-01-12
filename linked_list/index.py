class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __is_not_null(self):
        if self.head == None:
            print("List has no elements")
            return False
        else:
            return True
    
    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node                                #type: ignore
        return

    def unshift(self, value):
        new_node = Node(value)
        new_node.next = self.head                                   #type: ignore
        self.head = new_node
    
    def length(self) -> int: 
        if self.head == None:
            return 0
        
        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next

        return total
  
    def to_list(self) -> list:
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.value)
            current_node = current_node.next

        return node_data

    def display(self):
        contents = self.head

        if not self.__is_not_null():
            return False
        
        while contents:
            print(contents.value)
            contents = contents.next
        print('---------------')

    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next = current_node.next
            current_node.next = previous_node                       #type: ignore
            previous_node = current_node
            current_node = next
        self.head = previous_node 

    def pop(self):
        if not self.__is_not_null():
            return False
        
        current_node = self.head
        while current_node.next.next:                               #type: ignore
                current_node = current_node.next                    #type: ignore
        current_node.next = None                                    #type: ignore

    def shift(self):
        if not self.__is_not_null():
            return False
        
        if self.length() == 1:
            self.head = None

        
        self.head = self.head.next                                  #type: ignore

    def remove_by_value(self, value):
        if not self.__is_not_null():
            return False
        
        current_node = self.head

        if current_node != None:
            if current_node.value == value:
                self.head = current_node.next
                current_node = None
                return

        while current_node.next:                                    #type: ignore
            if current_node.next.value == value:                    #type: ignore
                current_node.next = current_node.next.next          #type: ignore
            current_node = current_node.next                        #type: ignore

        if current_node == None:
            print("Value is not in list")
            return

    def get(self, index):
        if index > self.length() or index < 0:
            print("Index out of range")
            return
        current_index = 0
        current_node = self.head

        while current_node:
            if current_index == index:
                return current_node.value
            current_node = current_node.next
            current_index += 1
        return current_node.value                                   #type: ignore

    def get_by_value(self, value):
        if not self.__is_not_null():
            return False
        
        current_node = self.head

        while current_node:
            if current_node.value == value:
                print("Item Found")
                return True
            current_node = current_node.next
        print("Item Not Found")
        return False
        
    def insert_at_index(self, index, value):
        if index == 0:
            self.unshift(value)
    
        i = 0
        current_node = self.head
        while i < index-1 and current_node is not None:
            current_node = current_node.next
            i += 1

        if current_node is None:
            print("Index out of range!")
        else:
            new_node = Node(value)
            new_node.next = current_node.next
            current_node.next = new_node                            #type: ignore

l1 = LinkedList()

l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)

# l1.reverse_linkedlist()

l1.display()
l1.shift()
l1.insert_at_index(1, 10)
l1.unshift(45)
l1.insert_at_index(3, 25)
l1.pop()
l1.display()