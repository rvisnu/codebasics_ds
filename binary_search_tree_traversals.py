"""
Add following methods to BinarySearchTreeNode class created in main video tutorial

1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
"""

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_member(self,data):
        if self.data == data:
            return
        elif self.data > data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.add_member(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.add_member(data)
    
    def search(self,data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.search(data) 
            else:
                return False
        elif self.data < data:
            if self.right:
                return self.right.search(data) 
            else:
                return False
                
    def in_order_traversal(self):
        elem = []
        if self.left:
            elem+=self.left.in_order_traversal()
        elem.append(self.data)
        if self.right:
            elem+=self.right.in_order_traversal()
        return elem

    def post_order_traversal(self):
        elem = []
        if self.left:
            elem+=self.left.in_order_traversal()
        if self.right:
            elem+=self.right.in_order_traversal()
        elem.append(self.data)
        return elem

    def pre_order_traversal(self):
        elem = []
        elem.append(self.data)
        if self.left:
            elem+=self.left.in_order_traversal()
        if self.right:
            elem+=self.right.in_order_traversal()
        return elem
        
    def find_min(self):
        sorted = self.in_order_traversal()
        return sorted[0]
    
    def find_max(self):
        sorted = self.in_order_traversal()
        return sorted[-1]
    
    def find_sum(self):
        elem = 0
        if self.left:
            elem+=self.left.find_sum()
        elem+=self.data
        if self.right:
            elem+=self.right.find_sum()
        return elem

def build_tree(elements):
    my_tree = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        my_tree.add_member(elements[i])
    return my_tree
    
if __name__ == "__main__":
    elem = [30,3,41,16,79,100]
    new_elem = build_tree(elem)
    
    print(new_elem.search(100))
    print(new_elem.search(3))
    print(new_elem.search(1))
    print(f"In order traversal:\n{new_elem.in_order_traversal()}")

    print(f"min: {new_elem.find_min()}")
    print(f"max: {new_elem.find_max()}")
    print(f"sum: {new_elem.find_sum()}")
    
    print(f"post order traversal:\n{new_elem.post_order_traversal()}")
    print(f"pre order traversal:\n{new_elem.pre_order_traversal()}")
        
        
            
