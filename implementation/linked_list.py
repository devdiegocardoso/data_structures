class Node:
    def __init__(self,value) -> None:
        self.next = None
        self.value = value

    def __str__(self) -> str:
        return self.value
    

class List:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, element) -> None:
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
    
    def remove(self,element) -> bool:
        if self.head == None:
            return False
        else:
            pointer = self.head
            if pointer.value == element:
                self.remove_beginning()
                return True
            while pointer.next:
                current = pointer
                pointer = pointer.next
                if pointer.value == element:
                    self.remove_after(current)
                    return True
        return False

    def remove_beginning(self):
        to_remove = self.head
        self.head = self.head.next
        del to_remove
   
    def remove_after(self,node):
        to_remove = node.next
        node.next = node.next.next
        del to_remove

    def get_list(self):
        pointer = self.head
        list_str = ""
        if pointer == None:
            return ""
        while(pointer.next):
            list_str += str(pointer.value) + " -> "
            pointer = pointer.next
        list_str += str(pointer.value)
        return list_str

    def print_list(self) -> None:
        pointer = self.head
        if pointer == None:
            return
        while(pointer.next):
            print(pointer.value,"-> ", end="")
            pointer = pointer.next
        print(pointer.value)
    
