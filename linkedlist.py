#single node ( empty or with val
class Node:
    def __init__(self,initval=None):
        self.value = initval
        self.next = None
    def isempty(self):
        return(self.value==None)
    def appendi(self,v):
        if self.isempty():
            self.value = v
            return()
        # elif self.next == None:
        #     newnode = Node(v)
        #     self.next = newnode
        # else:
        #     self.next.append(v)
        # return()
        temp = self
        while temp.next != None:
            temp = temp.next
        newnode = Node(v)
        temp.next = newnode
        return()
#creating 2 diff lists each of single and empty node
# l1 = Node()
# l2 = Node(7)
#
# print(l1.isempty())
# print(l2.isempty())
    def insert(self,v):
        if self.isempty():
            self.value = v
            return()
        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value,self.value)
        (self.next,newnode.next) = (newnode,self.next)
        return()
    def delete(self,x):
        if self.isempty():
            return()
        if self.value == x:
            #del first node
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return()
        # recursive
        else:
            if self.next != None:
                self.next.delete(x)
                if self.next.value == None:
                    self.next = self.next.next #None - above line's next as None|None - recursive call end's result
        return()
        #del another nodes non recursive
        temp = self
        while temp.next != None:
            if temp.next.value == x:
                temp.next = temp.next.next
                return()
            else:
                temp = temp.next
        return()
    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))
        temp = self
        selflist.append(temp.value)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        return(str(selflist))




