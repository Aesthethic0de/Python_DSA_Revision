class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
            
class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp_list = []
        temp = self.head
        while temp is not None:
            temp_list.append(temp.value)
            temp = temp.next
        if self.head == None:
            temp_list.append(None)
        print(temp_list)
        print(self.length)
    
    def append_end(self,value):
        new_node = Node(value=value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_end(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            temp  = self.head
            if temp.next is not None:
                while temp.next.next is not None:
                    temp = temp.next
                self.tail = temp
                self.tail.next = None
                self.length -= 1
            else:
                self.head = None
                self.tail = None
                self.length -= 1
        return True
    
    def pre_append(self,value):
        if self.length == 0:
            new_node = Node(value=value)
            self.head = new_node
            self.tail = new_node
        else:
            if self.head.next is not None:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node               
            else:
                new_node = Node(value=value)
                self.head = new_node
                self.head.next = self.tail
            self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head.next
            self.head = temp
        self.length -= 1
        return True
    
    def get_from_ll(self, index):
        if self.length == 0:
            return None
        else:
            if index < self.length:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                return temp.value
            else:
                return None
                
                
        
            
                
                    

if __name__ == "__main__":
    my_linked_list = LinkedList(6)
    # my_linked_list.pre_append(5)
    # my_linked_list.pre_append(7)
    # my_linked_list.append_end(7)
    my_linked_list.print_list()
    # my_linked_list.pop_end()
    # my_linked_list.print_list()
    # my_linked_list.pop_end()
    # my_linked_list.print_list()
    my_linked_list.append_end(1)
    my_linked_list.append_end(2)
    my_linked_list.append_end(3)
    my_linked_list.print_list()
    my_linked_list.pre_append(5)
    my_linked_list.pre_append(10)
    # my_linked_list.pop_end()
    my_linked_list.print_list()
    my_linked_list.pre_append(1010)
    my_linked_list.print_list()
    my_linked_list.pop_first()
    my_linked_list.print_list()
    my_linked_list.pop_first()
    my_linked_list.print_list()
    print(my_linked_list.get_from_ll(4))