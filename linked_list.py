
# LinkedList Properties:
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
            self.length += 1
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
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            return None
        else:
            if index < self.length:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                return temp
            else:
                return False
            
    def set_value(self, index, value):
        if self.length == 0:
            return None
        else:
            if index < self.length:
                temp = self.get_from_ll(index=index)
                if temp:
                    temp.value = value
            return True
    
    def insert_node(self, index, value):
        if index == 0:
            return self.pre_append(value=value)
        if index == self.length:
            return self.append_end(value=value)
        if index < 0 or index > self.length:
            return False
        else:
            temp = self.head
            new_node = Node(1000)
            for i in range(index-1):
                temp = temp.next
                print(temp)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
            
    def remove_at_node(self,index):
        if self.length == 0:
            return None
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length:
            self.pop_end()
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
            return True
            
        
            
        
                            
if __name__ == "__main__":
    my_linked_list = LinkedList(6)
    my_linked_list.pre_append(5)
    my_linked_list.pre_append(7)
    my_linked_list.append_end(7)
    my_linked_list.print_list()
    # my_linked_list.pop_end()
    my_linked_list.print_list()
    my_linked_list.insert_node(index=2, value=1000)
    my_linked_list.print_list()
    # my_linked_list.insert_node(index=3, value=5)
    # my_linked_list.print_list()
    # my_linked_list.print_list()
    # my_linked_list.pop_end()
    # my_linked_list.print_list()
    # my_linked_list.append_end(1)
    # my_linked_list.append_end(2)
    # my_linked_list.append_end(3)
    # my_linked_list.print_list()
    # my_linked_list.pre_append(5)
    # my_linked_list.pre_append(10)
    # # my_linked_list.pop_end()
    # my_linked_list.print_list()
    # my_linked_list.pre_append(1010)
    # my_linked_list.print_list()
    # my_linked_list.pop_first()
    # my_linked_list.print_list()
    # my_linked_list.pop_first()
    # my_linked_list.print_list()
    # print(my_linked_list.get_from_ll(4))
    # my_linked_list.set_value(index=2, value=500)
    # my_linked_list.print_list()
    # my_linked_list.insert_node(index=3, value=4)
    # my_linked_list.print_list()
    # my_linked_list.insert_node(index=1, value=1000)
    # my_linked_list.print_list()
    # my_linked_list.remove_at_node(index=0)
    # my_linked_list.print_list()
    # my_linked_list.remove_at_node(index=4)
    my_linked_list.print_list()
    my_linked_list.remove_at_node(index=3)
    my_linked_list.print_list()
    my_linked_list.remove_at_node(index=2)
    my_linked_list.print_list()