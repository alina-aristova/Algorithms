import graphB as gh


def main():

    print('\nВыберите номер нужного вам алгоритма:\n',
    '1 - Алгоритм Тарьяна\n',
    '2 - Алгоритм Флери\n',
    '3 - Алгоритм на основе циклов\n',
    '4 - Алгоритм Косарайю\n',    
    '5 - Выход')
    nomer = int(input())
    
    if nomer == 1:
        gr = gh.Tariana()
        graph = {6:[3,5], 5:[2,4], 3:[2], 2:[1], 7:[4], 4:[1], 1:[]}
        print(gr.dfs(graph))
        main()
        
    elif nomer == 2:
        gra = {0:[1,2,3,4],1:[0,2,3,4], 2:[0,1,3,5],3:[0,1,2,4],4:[0,1,3,5],5:[2,4]}
        s = gh.Fleury(gra,6)
        print(s.getResult(5))
        main()
        
    elif nomer == 3:
        gr = {1:[2,5,4,3], 2:[5,4,3,1], 3:[1, 2, 4, 6], 
            4:[2,1,3,5], 5:[6,4,1,2], 6:[3, 5]}
        g = gh.GraphFor(gr)
        print(g.findEulerPath(6))
        main()

    elif nomer == 4:
        g = {1:[4], 2:[1], 3:[7,5,2], 4:[1, 5],
            5:[2,  8], 6:[3, 5], 7:[8,6,2,3
            ], 8:[5, 7]}
        cs = gh.Cosaraju(g)
        cs.gT()
        print(cs.dfs())
        main()

    elif nomer == 5:
        pass
    else:
        main()

    
if __name__ == "__main__":    
    main()