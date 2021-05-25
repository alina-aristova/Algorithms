import HashTable as ht
import random

def main():    
    hashtable = ht.HashTable(10)
    i = 0
    
    while i < 100:
        hashtable.add(random.randint(1,100000),chr(random.randint(ord("а"),ord("я"))))
        i = i + 1
    hashtable.add(21,'d')
    hashtable.add(21,'g')
    hashtable.search(21)
    hashtable.remove(21)
    hashtable.search(21)
    hashtable.factorLoad(5)
    print(len(hashtable.hashTable))
    print(hashtable.load)
    hashtable.view()

if __name__ == "__main__":
    main()
   