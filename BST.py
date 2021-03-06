class BinarySearchTree:
    class Node:
        def __init__(self,key):
            self.key=key
            self.left=self.right=None
    def __init__(self):
        self.root=None
                    
    def insert(self, key):
        def rec_insert(key, v):
            if v.key == key:
                w=v
            elif key < v.key:
                if v.left is None:
                    w = v.left = BinarySearchTree.Node(key)
                else:
                    w = rec_insert(key,v.left)
            else:
                if v.right is None:
                    w = v.right = BinarySearchTree.Node(key)
                else:
                    w = rec_insert(key,v.right)
            return w
        if self.root is None:
            self.root=BinarySearchTree.Node(key)
            return self.root
        return rec_insert(key,self.root)
        
b=BinarySearchTree()
assert b.root is None
b.insert(2)
assert b.root.key == 2
v=b.insert(1)
three=b.insert(3)
four20=b.insert(420)
forty_two=b.insert(42)
"""
        2
    1       3
                  420
                42
"""
assert b.root.key ==2
assert b.root.left.key ==1
assert b.root.right.key==3
assert v is b.root.left
assert four20.left is forty_two
assert three.right is four20