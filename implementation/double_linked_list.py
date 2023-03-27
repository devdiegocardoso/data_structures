class Node:
    def __init__(self,value) -> None:
        self.next = None
        self.value = value
        self.prev = None

    def __str__(self) -> str:
        return self.value
    

class DList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def search(self,elem):
        pointer = self.head
        while pointer != None:
            if pointer.value == elem:
                return pointer
            pointer = pointer.next
        return None

    def iterate_forward(self):
        pointer = self.head
        list_str = ""
        while pointer != None:
            list_str += str(pointer.value) + " -> "
            pointer = pointer.next
        return list_str[:-4]
    
    def iterate_backward(self):
        pointer = self.tail
        list_str = ""
        while pointer != None:
            list_str += str(pointer.value) + " -> "
            pointer = pointer.prev
        return list_str[:-4]

    def insert_after(self,node,newNode):
        newNode.prev = node
        if node.next == None:
            newNode.next = None
            self.tail = newNode
        else:
            newNode.next = node.next
            node.next.prev = newNode
        node.next = newNode
    
    def insert_before(self,node,newNode):
        newNode.next = node
        if node.prev == None:
            newNode.prev = None
            self.head = newNode
        else:
            newNode.prev = node.prev
            node.prev.next = newNode
        node.prev = newNode
            
    def insert_begin(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
        else:
            self.insert_before(self.head,node)

    def insert_end(self,node):
        if self.tail == None:
            self.insert_begin(node)
        else:
            self.insert_after(self.tail,node)
    
    def add(self,elem,type=2):
        node = Node(elem)
        if type == 1:
            self.insert_begin(node)
        else:
            self.insert_end(node)

    
    def remove_node(self,node):
        if node.prev == None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next == None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        del node

    def remove(self,elem):
        node = self.search(elem)
        if node != None:
            self.remove_node(node)

lista = DList()
lista.add(1)
lista.add(2,type=1)
lista.add(3,type=1)
lista.add(4)

print(lista.iterate_forward())
print(lista.iterate_backward())