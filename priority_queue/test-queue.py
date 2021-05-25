import Priority_queue as pq

def menu(binary):
    print("1 - добавление элемента\n2 - удаление элемента\n",
        "3 - доступ к максимальному элементу\n",
        "4 - получение числа элементов в очереди\n 5 - выход") 
    nomer = int(input('-->'))
    
    if nomer == 1:
        while True:
            element = input('Введите элемент, введите stop для остановки ')
            if element == "stop":
                print(binary.heapList)
                menu(binary)
                break
            else:
                try:
                    binary.add(int(element))
                except:
                    print("ошибка ввода")
                

    elif nomer == 2: 
        if binary.isEmty() == True:
            print(" очереди нет элементов")
        else:
            binary.deleteMax()
            print(binary.heapList)
        menu(binary)  
    elif nomer == 3:
        if binary.isEmty():
            print("в очереди нет элементов")

        else:
            print("максимальный элемент: ", binary.getMax())
        menu(binary)
    elif nomer == 4:
        print("число элементов в очереди: ", binary.getSize())
        menu(binary)
    elif nomer == 5:
        pass    
    else:
        menu(binary)

    

if __name__ == "__main__":
    binary = pq.binary()
    menu(binary)
