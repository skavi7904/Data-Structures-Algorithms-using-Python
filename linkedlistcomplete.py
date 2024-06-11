class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return (True)
        else:
            return (False)

    def append(self, v):  # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode #newnode's next is None as it is created by Node()
        else:
            self.next.append(v) #recursively called by next
        return

    def insert(self, v):
        if self.isempty():
            self.value = v #its next is None only as it is empty previously
            return

        newnode = Node(v)

        # Evchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)

        return

    def delete(self, v):  # delete, recursive
        if self.isempty():
            return

        if self.value == v:
            self.value = None #it is for, what if it is singleton; the next line will be false
            if self.next != None:  #if to del first val, replace first by second ,then unlink second
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v) #recursive call
                if self.next.value == None:
                    self.next = None #terminates from deleted node
        return

    def __str__(self):
        selflist = []
        if self.value == None:
            return (str(selflist))

        temp = self
        selflist.append(temp.value)

        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return (str(selflist))

l = Node(2)
for i in range(3,9):
    l.append(i)
l.delete(2)
l.append(2)
print(l)