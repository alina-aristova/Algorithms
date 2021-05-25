from math import floor

class binary():  
    def __init__(self):
        self.heapList=[]
        
    def parent(self, i):
        return floor(((i-1)/2))

    def leftChild(self, i):
        return (2*i+1)

    def rightChild(self, i):
        return(2*i+2)    
    
    def up(self, i):
        while (i != 0 and self.heapList[i] > self.heapList[self.parent(i)]):
            self.heapList[i], self.heapList[self.parent(i)] = self.heapList[self.parent(i)], self.heapList[i]
            i = self.parent(i)

    def down(self, i):
        while(i < floor(len(self.heapList) / 2)):
            maxI = self.leftChild(i)
            if (self.rightChild(i) < len(self.heapList) and self.heapList[self.rightChild(i)] > self.heapList[self.leftChild(i)] ):
                maxI = self.rightChild(i)
            if (self.heapList[i] >=self.heapList[maxI] ):
                return
                
            self.heapList[i], self.heapList[maxI] = self.heapList[maxI], self.heapList[i]
            i = maxI

    def add (self, element):
        self.heapList.append(element)
        self.up(len(self.heapList)-1)

    def deleteMax (self):
        self.heapList[0], self.heapList[len(self.heapList)-1] = self.heapList[len(self.heapList)-1], self.heapList[0]
        del self.heapList[len(self.heapList)-1]
        self.down(0)

    def getSize(self):
        return len(self.heapList)

    def isEmty(self):
        if len(self.heapList) == 0:
            return True
    def getMax(self):
        return self.heapList[0]    












 
