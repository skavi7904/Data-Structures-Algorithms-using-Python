class Tree:

    # Empty node has self.value, self.left, self.right = None
    # Leaf has self.value != None, and self.left, self.right point to empty node

    # Constructor: create an empty node or a leaf node, depending on initval
    def __init__(self, initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    # Only empty node has value None
    def isempty(self):
        return (self.value == None)

    # Leaf nodes have both children empty
    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

    # Convert a leaf node to an empty node
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    # Copy right child values to current node
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    # Check if value v occurs in tree
    def find(self, v):
        if self.isempty():
            return (False)

        if self.value == v:
            return (True)

        if v < self.value:
            return (self.left.find(v))

        if v > self.value:
            return (self.right.find(v))

    # Insert value v in tree
    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            return

        if v > self.value:
            self.right.insert(v)
            return

    # Find maximum value in a nonempty tree
    def maxval(self):
        if self.right.isempty():
            return (self.value)
        else:
            return (self.right.maxval())

    # Delete value v from tree
    def delete(self, v):
        if self.isempty():
            return

        if v < self.value:
            self.left.delete(v)
            return

        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    # Inorder traversal
    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())

    # Display Tree as a string
    def __str__(self):
        return (str(self.inorder()))
# class Tree:
#     def __init__(self,initval = None): #create empty node of empty list or | one node with right and left points to empty node;
#         self.val = initval
#         if self.val:
#             self.left = Tree()
#             self.right = Tree()
#         else:
#             self.left = None
#             self.right = None
#         return
#     def makeempty(self):
#         self.val = None
#         self.left = None
#         self.right = None
#         return
#     def isempty(self):
#         return (self.val == None)
#     def inorder(self):
#         if self.isempty():
#             return ([])
#         else:
#             return (self.left.inorder() + [self.val] + self.right.inorder())
#     def __str__(self):
#         return (str(self.inorder()))
#     def find(self,v):
#         if self.isempty():
#             return (False)
#         if self.val == v:
#             return (True)
#         if v < self.val:
#             return (self.left.find(v))
#         if v > self.val:
#             return (self.right.find(v))
#     def minval(self):
#         if self.left == None:
#             return (self.val)
#         else:
#             return (self.left.minval())
#     def maxval(self):
#         if self.right == None:
#             return (self.val)
#         else:
#             return (self.right.maxval())
#     def insert(self,v):
#         if self.isempty():   #add v as leaf, since lastnode's left and right nodes are None only; EMPTY
#             self.val = v
#             self.left = Tree()
#             self.right = Tree()
#         if self.val == v: #value found, do nothing
#             return
#         if v < self.val:
#             self.left.insert(v)
#             return
#         if v > self.val:
#             self.right.insert(v)
#             return
#     def delete(self,v):
#         if self.isempty():
#             return
#         if v < self.val:
#             self.left.delete(v)
#             return
#         if v > self.val:
#             self.right.delete(v)
#             return
#         if v == self.val:
#             if self.isleaf():
#                 self.makeempty()
#             elif self.left.isempty():
#                 self.copyright()
#             else:
#                 self.val = self.left.maxval()
#                 self.left.delete(self.left.maxval())
#             return
#     def copyright(self):
#         self.val = self.right.val
#         self.left = self.right.left
#         self.right = self.right.right
#         return
#     def isleaf(self):
#         return (self.left.isempty() and self.right.isempty())

t = Tree()
for i in [1,7,99,5,4,8,34,21,9,5,3]:
    t.insert(i)

print(t)
t.insert(4.5)
t.delete(99)
print(t)



