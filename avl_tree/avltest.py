import avltree as av
import random
if __name__ == "__main__": 
    tree = av.avltree()
    n = 0
    while n!= 10000:
        tree.insert(random.randint(1,1000),chr(random.randint(ord("а"),ord("я"))))
        n=n+1
    for key in [2]:
           tree.delete(key)
        
    #print (tree.inorder_traverse())
    tree.isEmty()
    tree.search_balance()
