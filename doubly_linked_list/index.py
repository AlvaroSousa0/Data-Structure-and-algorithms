class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __is_not_null(self):
        if self.head == None:
            print("List has no elements")
            return False
        else:
            return True

    def append(self, value):
        new_node = DoubleNode(value)


        new_node.next = None
        if self.head == None:
            new_node.previous = None
            self.head = new_node
            return
       
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node                                   #type: ignore

        new_node.previous = last_node                               #type: ignore
        return
    
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

    def reverse_linked_list(self):
        if not self.__is_not_null():
            return False
        
        current_node = self.head
        new_node = current_node.next                                #type: ignore
        current_node.next = None                                    #type: ignore
        new_node.previous = current_node                            #type: ignore
        while new_node:
            new_node.previous = new_node.next
            new_node.next = current_node
            current_node = new_node
            new_node = new_node.previous
        self.head = current_node

    def unshift(self, value):
        if not self.head:
            new_node = DoubleNode(value)
            self.head = new_node
            return
        new_node = DoubleNode(value)
        self.head.previous = new_node                               #type: ignore
        self.head = new_node

    def shift(self):
        if not self.__is_not_null:
            return False
 
        if self.length() == 1:
            self.head = None
            return

        self.head.next.previous = None                              #type: ignore
        self.head = self.head.next                                  #type: ignore

    def pop(self):
        if not self.__is_not_null():
            return False
        
        if self.length() == 1:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:                               #type: ignore
                current_node = current_node.next                    #type: ignore
        current_node.next = None                                    #type: ignore

    def remove_by_value(self, value):
        if not self.__is_not_null():
            return False
        
        current_node = self.head

        if current_node != None:
            if current_node.value == value:
                self.head = current_node.next
                current_node = None
                self.head.previous = None                           #type: ignore
                return

        while current_node.next:                                    #type: ignore
            if current_node.next.value == value:                    #type: ignore
                current_node.next = current_node.next.next          #type: ignore
                current_node.next.next.previous = current_node      #type: ignore
            current_node = current_node.next                        #type: ignore

        if current_node == None:
            print("Value is not in list")
            return
        

l1 = DoublyLinkedList()

l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)

l1.display()

l1.reverse_linked_list()

l1.display()