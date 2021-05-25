from collections import deque
import random
from string import ascii_uppercase


class Graph:
    def goFromVertex(self, vertex, visited, result, graph):
        visited[vertex] = True
        result.append(vertex)
        for i in graph[vertex]:
            if visited[i] == False:
                self.goFromVertex(i, visited, result, graph)

    def dfs(self, graph):
        visitedLength = len(graph)
        visited = {x: y for x, y in zip([*graph], [False]*(visitedLength))}
        result = list()
        for i in visited.keys():
            if visited[i] == False:
                self.goFromVertex(i, visited, result, graph)
        return result
    
    def bfs(self, graph):
        distance = {x: y for x, y in zip([*graph], [None]*len(graph))}
        vertex = 1
        distance[vertex] = 1
        queue = deque([vertex])
        visitedLength = len(graph)
        visited = {x: y for x, y in zip([*graph], [False]*(visitedLength))}
        result =list()
        
        while queue:
            visit = queue.popleft()
            for vert in graph[visit]:
                if  distance[vert] is None:
                    distance[vert] = distance[visit] +1
                    queue.append(vert)
                    for i in visited.keys():                        
                        if visited[i] == False:
                            self.goFromVertex(i, visited, result, graph)
        return result                    

    
    def Cruscal(self, graph):
        D = list()
        Result = list()
        graph.sort()
        for i in range(1, 8):
            D.append(i)
        for weight, a, b in graph:
            if D[a-1] != D[b-1]:
                Result.append((a, b))
                temp = D[a-1]
                for j in range(len(D)):
                    if D[j] == temp:
                        D[j] = D[b-1]
                print(f'Соединяем вершину {a} с вершиной {b}')
        return Result

    def dijekstra(self, graph, start, finish):
        distance = {}
        predessor = {}        
        INF = float('INF')
        visited = []
        for node in graph:
            distance[node] = INF
            distance[start] = 0

        while graph:
            minNode = None
            for node in graph:
                if minNode is None:
                    minNode = node
                elif distance[node] < distance[minNode]:    					
                    minNode = node

            for childNode, weight in graph[minNode].items():
                    if weight + distance[minNode] < distance[childNode]:
                            distance[childNode] = weight + distance[minNode] 
                            predessor[childNode] = minNode

            graph.pop(minNode)
        
        actualNode = finish
        while actualNode != start:
            try:
                visited.insert(0, actualNode)
                actualNode = predessor[actualNode]
            except KeyError:
                print('Невозможно найти путь')
                break

        visited.insert(0, start)	
        if distance[finish] != INF:
                return'Длина:' + str(distance[finish]) + ' ' + str(visited)

    def floydWarshall(self, graph):
        graph = graph
        v = len(graph)
        

        for k in range(0, v):
            for i in range(0, v):
                for j in range(0, v):
                    if graph[i][j]> graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        return graph

    


    def prima(self, graph, label = None):
        INF = float('INF')
        countNode = len(graph)        
        for weights in graph:
            assert len(weights) == countNode

        if not label:
            label = [x for x in range(1,8)]

        assert countNode <= len(label)
        freeVertexes = list(range(0, len(label)))
        startVertex = random.choice(freeVertexes)
        tied = [startVertex]
        freeVertexes.remove(startVertex)      
        lenPath = 0        
        while freeVertexes:
            minVert = None 
            minGeneralPath = INF   
            for actualVert in tied:
                weights = graph[actualVert]
                minPath = INF
                minFrVertex = actualVert
                for vertex in range(countNode):
                    vertexPath = weights[vertex]
                    if vertexPath == 0:
                        continue
                    if vertex in freeVertexes and vertexPath < minPath:
                        minFrVertex = vertex
                        minPath = vertexPath
                if minFrVertex != actualVert:
                    if minGeneralPath > minPath:
                        minVert = (actualVert, minFrVertex)
                        minGeneralPath = minPath
            try:
                lenPath = graph[minVert[0]][minVert[1]]
            except TypeError:
                
                return('Невозможно найти путь')

            print('Соединяем вершину %s с вершиной %s [%s]' % (label[minVert[0]], label[minVert[1]], lenPath))

            lenPath += lenPath
            freeVertexes.remove(minVert[1])
            tied.append(minVert[1])

        return('Длина пути: %s' % lenPath)                