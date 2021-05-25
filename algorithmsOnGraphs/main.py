import Graph as gh

def main():
    gr = gh.Graph()
    menu(gr)

def menu(gr):
    print('\nВыберите номер нужного вам алгоритма:\n',
    '1 - Алгоритм поиска в глубину\n',
    '2 - Алгоритм поиска в ширину\n',
    '3 - Алгоритм Дейкстры\n',
    '4 - Алгоритм Крускала\n',
    '5 - Алгоритм Прима\n',
    '6 - Алгоритм Флойда-Уоршалла\n',
    '7 - Выход')
    nomer = int(input())
    if nomer == 1:
        graph = {1:[2,3], 2:[5,4], 3:[4], 4:[2], 5:[4]}
        print('Список вершин графа: ') 
        print(gr.dfs(graph))
        menu(gr)
    elif nomer == 2:
        graph = {1:[2,3], 2:[5,4], 3:[4], 4:[2], 5:[4]}
        print('Список вершин графа: ') 
        print(gr.bfs(graph))
        menu(gr)
    elif nomer == 3:
        graph = {'a':{'b':10, 'c':3}, 'b':{'c':1, 'd':2}, 'c':{'b':4, 'd':8, 'e':11}, 'd':{'e':7}, 'e':{'d':9}}
        print('кратчайший путь между вершинами:')
        print(gr.dijekstra(graph,'a','e'))
        menu(gr)
    elif nomer == 4:
        graph = [[2, 1, 2], [1, 1, 3], [6, 1, 6], [3, 1, 4],
        [3, 3, 6], [2, 3, 4], [7, 6, 7], [1, 4, 7], [3, 2, 5], [1, 2, 4], [4, 5, 7]]
        print(gr.Cruscal(graph))
        menu(gr)
    elif nomer == 5:
        INF = float('INF')
        graph = [
                
                [0, 1, 2, 4, INF, INF, INF], 
                [1, 0, INF, 2, 5, INF, INF], 
                [2, INF, 0, 7, INF, 4, 1], 
                [4, 2, 7, 0, 1, INF, 1], 
                [INF, 5, INF, 1, 0, INF, INF], 
                [INF, INF, 4, INF, INF, 0, INF], 
                [INF, INF, 1, 1, INF, INF, 0], 
            ]
        print(gr.prima(graph))
        menu(gr)
    elif nomer == 6:
        INF = float('INF')
        graph = [
                
                [0, 1, 2, 4, INF, INF, INF], 
                [1, 0, INF, 2, 5, INF, INF], 
                [2, INF, 0, 7, INF, 4, 1], 
                [4, 2, 7, 0, 1, INF, 1], 
                [INF, 5, INF, 1, 0, INF, INF], 
                [INF, INF, 4, INF, INF, 0, INF], 
                [INF, INF, 1, 1, INF, INF, 0], 
            ]
        print(gr.floydWarshall(graph))
        menu(gr)
    elif nomer == 7:
        pass
    else:
        menu(gr)
    
if __name__ == "__main__":    
    main()