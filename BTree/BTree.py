import copy

class BNode: 
    def __init__(self, t, leaf):
        self.t = t
        self.keys = list()
        self.count = 0
        self.sons = list()
        self.leaf = leaf
        self.parent = None

    def __repr__(self):
        return str(self.keys)

class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "".join(['Key: ', str(self.key), ' ; Value: ', str(self.value)])

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def insert(self, key, value):
        if self.root == None:
            self.root = BNode(self.t, True)
            self.root.keys.append(KeyValue(key, value))
            self.root.count = 1
        else:
            if self.root.count == 2 * self.t - 1:
                node = BNode(self.t, False)
                node.sons.append(self.root)

                self.splitChild(0, self.root, node)

                i = 0
                if node.keys[0].key < key:
                    i += 1
                self.insertNonFull(node.sons[i], key, value)
                self.root = node
            else:
                self.insertNonFull(self.root, key, value)

    def insertNonFull(self, node, key, value):
        i = node.count - 1

        if node.leaf == True:
            while i >= 0 and node.keys[i].key > key:
                i -= 1

            node.keys.insert(i + 1, KeyValue(key, value))
            node.count += 1
        else:
            while i >= 0 and node.keys[i].key > key:
                i -= 1

            if node.sons[i + 1].count == 2 * self.t - 1:
                self.splitChild(i + 1, node.sons[i + 1], node)

                if node.keys[i + 1].key < key:
                    i += 1

            self.insertNonFull(node.sons[i + 1], key, value)

    def splitChild(self, i, node1, node2):
        newNode = BNode(node1.t, node1.leaf)
        newNode.count = self.t - 1

        for j in range(self.t - 1):
            newNode.keys.append(node1.keys[j + self.t])

        if node1.leaf == False:
            for j in range(self.t):
                newNode.sons.append(node1.sons[j + self.t])

        node1.count = self.t - 1
        node2.sons.insert(i + 1, newNode)
        node2.keys.insert(i, node1.keys[self.t - 1])
        node2.count = len(node2.keys)
        del node1.keys[-self.t:]

    def isEmty(self):
        if self.root == None:
            return True

    def delAll(self):
        self.root = None
        
    def search(self, key, node=None):
        if node == None:
            node = self.root

        try:
            if node.keys[-1].key < key:
                self.search(key, node.sons[-1])

            for i in range(len(node.keys)):
                if node.keys[i].key > key:
                    self.search(key, node.sons[i])
                    break

                if node.keys[i].key == key:
                    print(node.keys[i])
                    return
                    
        except:
            print('Ключ не найден')


    def check(self, node=None):
        if node == None:
            node = self.root
        for i in range(len(node.keys)):
            if node.leaf == False:
                self.check(node.sons[i])

            if self.root.count > 2 * self.t - 1 or self.root.count < 1:
                print('Кол-во ключей в корне не соответствует нужному кол-ву')
                return 
            if len(self.root.sons) > 2 * self.t or len(self.root.sons) < 2:
                print('Кол-во потомков корня не соотвествует')
                return 

            if node != self.root and node.leaf != True :
                if self.t > len(node.sons) or 2 * self.t < len(node.sons):
                    print('Кол-во потомков  не соотвествует')
                    return 

            if node != self.root  :
                if node.count > 2 * self.t - 1 or node.count < self.t - 1:
                    print('Кол-во ключей в узле не соответствует нужному кол-ву')
                    return 
            else:
                print('дерево выполнено верно')

    def _copy(self): 
        return copy.deepcopy(self)
    
    