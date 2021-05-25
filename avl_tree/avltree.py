    
class avlnode(object):
    
    def __init__(self, key, value):
        "Construct."
        self.value = value
        self.key = key
        self.left = None
        self.right = None
 
    
 
    def __repr__(self):
        
        return f"(key: {self.key} ; value: {self.value})"

class avltree(object):    

    def __init__(self):
        
        self.node = None
        self.height = -1
        self.balance = 0
        
    def insert(self, key, value):
    
        n = avlnode(key,value)
 
        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        
        elif key < self.node.key:
            self.node.left.insert(key,value)
     
        elif key > self.node.key:
            self.node.right.insert(key,value)
        
        self.rebalance()
        
    def rebalance(self):
    
        self.update_heights(recursive=False)
        self.update_balances(False)
 
        while self.balance < -1 or self.balance > 1: 
            
            if self.balance > 1:
 
                if self.node.left.balance < 0:
                    
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()
 
                self.rotate_right()
                self.update_heights()
                self.update_balances()
           
            if self.balance < -1:
                
                
                if self.node.right.balance > 0:
                 
                    self.node.right.rotate_right() 
                    self.update_heights()
                    self.update_balances()
 
                self.rotate_left()
                self.update_heights()
                self.update_balances()
 
    def update_heights(self, recursive=True):
        
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1
 
    def update_balances(self, recursive=True):
        
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()
 
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0 
 
            
    def rotate_right(self):
        
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node
 
        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root
 
    def rotate_left(self):
        
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node
 
        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root
 
    def delete(self, key):
        
        if self.node != None:
            if self.node.key == key:
                
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                
                elif not self.node.left.node:                
                    self.node = self.node.right.node
                
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                   
                    successor = self.node.right.node  
                    while successor and successor.left.node:
                        successor = successor.left.node
 
                    if successor:
                        self.node.key = successor.key
 
                        self.node.right.delete(successor.key)
 
            elif key < self.node.key:
                self.node.left.delete(key)
 
            elif key > self.node.key:
                self.node.right.delete(key)
 
            self.rebalance()
 
    def inorder_traverse(self):
        
        result = []
 
        if not self.node:
            return result
        
        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())
 
        return result
        
    def isEmty(self):
        if self.node == None:
            print("список пуст") 

    def search_balance(self):
        print("Баланс дерева = ", self.balance)

        

