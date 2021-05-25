import copy

class HashTable:
    def __init__(self, m):
        self.hashTable = [[] for i in range (m)]
        self.m = m
        self.load = 2

    def add(self, key, value):
        hashCode = self.getHash(key)

        try:
            if self.search(key, True)[2] is True:
                return
        except:
            if self.hashTable[hashCode] == None:
                self.hashTable[hashCode].append([key,value])
                
                if len(self.hashTable[hashCode]) > self.load:
                    self.updateHashTable()
            else: 
                self.hashTable[hashCode].append([key,value])   
                
                if len(self.hashTable[hashCode]) > self.load:
                    self.updateHashTable()

    def getHash(self, key):
        hashget = hash(key)%self.m
        return hashget

    def view(self):
        print(self.hashTable)

    def removeAll(self):
        self.hashTable.clear()

    def updateHashTable(self):
        self.m = 2*self.m + 1
        hashTableCopy = copy.deepcopy(self.hashTable)
        self.removeAll()
        self.hashTable = [[] for i in range (self.m)]
        
        for i in range(len(hashTableCopy)-1):            
            for key in range(len(hashTableCopy[i])):
                value = hashTableCopy[i][key][1]
                key =  hashTableCopy[i][key][0]
                self.add(key,value)
        
    def search(self, key, flagRem=False):  
        flag = False 
        for i in range(len(self.hashTable)-1):         
            for k in range(len(self.hashTable[i])):
                if key == self.hashTable[i][k][0]:
                    flag = True
                    value = self.hashTable[i][k][1]
                    if flagRem is False:
                        print('key = ', key,'value = ', value)
                    return [i, k, True]
                else:
                    flag = False
                    
        if flag is False and flagRem is False:
            print('Ключ не найден!')  
        
        
    def remove(self,key):
        try:
            idxKeyValue = self.search(key, True)
            del self.hashTable[idxKeyValue[0]][idxKeyValue[1]]
            print('Ключ и значение удалены')
        except:
            print('Неверный ключ')

    def factorLoad(self, load2):
        self.load = load2
        

            