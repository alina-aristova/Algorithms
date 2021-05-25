
class Tariana:
    def goFromVertex(self, vertex, visited, result, graph):
            visited[vertex] = True
            result.append(vertex)

            for i in graph[vertex]:
                if visited[i] == False:
                    self.goFromVertex(i, visited, result, graph)
            result.append(vertex)

    def dfs(self, graph):
            visitedLength = len(graph)
            visited = {x: y for x, y in zip([*graph], [False]*(visitedLength))}
            result = list()
            for i in visited.keys():
                if visited[i] == False:
                    self.goFromVertex(i, visited, result, graph)
            return result

class Fleury:
    def __init__(self, graph, vertices):
        self.vertices = vertices
        self.graph = graph
        self.result = list()

    def addEdge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph.update({v1:[v2]})
        if v2 in self.graph:
            self.graph[v2].append(v1)
        else:
            self.graph.update({v2:[v1]})

    def numberOfVertices(self, vertex, visited):
        count = 1
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                count += self.numberOfVertices(i, visited)
        return count

    def removeEdge(self, v1, v2):
        for idx, value in enumerate(self.graph[v1]):
            if v2 == value:
                self.graph[v1].pop(idx)
        for idx, value in enumerate(self.graph[v2]):
            if v1 == value:
                self.graph[v2].pop(idx)

    def isCorrectPath(self, v1, v2):
        if len(self.graph[v1]) == 1:
            return True
        else:
            visited = [False] * (self.vertices)
            countBefore = self.numberOfVertices(v1, visited)
            self.removeEdge(v1, v2)
            visited = [False] * (self.vertices)
            countAfter = self.numberOfVertices(v1, visited)
            self.addEdge(v1, v2)
            if countBefore <= countAfter:
                return True
            else:
                return False

    def getResult(self, v1):
        for i in self.graph[v1]:
            if self.isCorrectPath(v1, i):
                self.result.append(v1)
                self.result.append(i)
                self.removeEdge(v1, i)
                self.getResult(i)
        return self.result

class GraphFor:
    def __init__(self, graph):
        self.result = list()
        self.graph = graph

    def removeEdge(self, v1, v2):
        for idx, value in enumerate(self.graph[v1]):
            if v2 == value:
                self.graph[v1].pop(idx)
        for idx, value in enumerate(self.graph[v2]):
            if v1 == value:
                self.graph[v2].pop(idx)

    def findEulerPath(self, v):
        for i in self.graph[v]:
            self.removeEdge(v, i)
            self.findEulerPath(i)
        self.result.append(v)
        return self.result

class Cosaraju:
    def __init__(self, graph):
        self.stack = list()
        self.graph = graph
        self.result = list()

    def dfsInv(self, x, visited):
        visited[x] = True
        for y in self.graph[x]:
            if visited[y] == False:
                self.dfsInv(y, visited)
        self.stack.append(x)

    def gT(self):
        visitedLen = len(self.graph)
        visited = {x: y for x, y in zip([*self.graph], [False] * (visitedLen))}
        for v in self.graph:
            if visited[v] == False:
                self.dfsInv(v, visited)
        

    def goFromVertex(self, v, visited):
        visited[v] = True
        self.result.append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.goFromVertex(i, visited)

    def dfs(self):
        visitedLen = len(self.graph)
        visited = {x: y for x, y in zip([*self.graph], [False] * (visitedLen))}
        self.stack.reverse()
        for idx, value in enumerate(self.stack):
            v = value
            self.stack.pop(idx)
            if visited[v] == False:
                self.goFromVertex(v, visited)
        return self.result
