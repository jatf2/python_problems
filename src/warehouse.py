import math

class Node:
    def __init__(self, x, y, father = None):
        self.x = x
        self.y = y
        self.father = father
    
    # @property
    # def level(self):
    #     if self.father is None:
    #         return 0

    #     else:
    #         return self.father.level + 1

    def children(self, maxX, maxY, obstacles, end):
        res = set()
        for node in self.adyacentFields(maxX, maxY, obstacles):
            if node.distanceTo(end) < node.father.distanceTo(end):
                res.add(node)
        
        return res
        
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
        
    def __key(self):
        return (
            self.x, 
            self.y
        )

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.__key() == other.__key()
        return NotImplemented
        
    def isValid(self, maxX, maxY, obstacles):
        return self not in obstacles and self.x < maxX and self.x >= 0 and self.y < maxY and self.y >= 0
            
    def adyacentFields(self, maxX, maxY, obstacles):
        res = set()

        node = Node(self.x + 1, self.y, self)
        if node.isValid(maxX, maxY, obstacles):
            res.add(node)

        node = Node(self.x - 1, self.y, self)
        if node.isValid(maxX, maxY, obstacles):
            res.add(node)

        node = Node(self.x, self.y + 1, self)
        if node.isValid(maxX, maxY, obstacles):
            res.add(node)

        node = Node(self.x, self.y - 1, self)
        if node.isValid(maxX, maxY, obstacles):
            res.add(node)

        return res
         
    def distanceTo(self, node):
        return math.sqrt((node.x - self.x)**2 + (node.y - self.y)**2)

class Warehouse:
    def __init__(self, W):
        self.start = Node(x = 0, y = 0)
        self.maxY = len(W)
        self.obstacles = set()
        for y, row in enumerate(W):
            self.maxX = len(row)
            for x, field in enumerate(row):
                if field == 0:
                    self.obstacles.add(Node(x, y))

        self.end = Node(self.maxX - 1, self.maxY - 1)

    def sol(self):
        res = 0
        nodes = [self.start]
        while len(nodes) != 0:
            aux = []
            for node in nodes:
                for child in node.children(self.maxX, self.maxY, self.obstacles, self.end):
                    aux.append(child)
                    if child == self.end:
                        res += 1

            nodes = aux

        return res
