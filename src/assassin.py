class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
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
        if isinstance(other, Field):
            return self.__key() == other.__key()
        return NotImplemented
        
    def isValid(self, maxX, maxY):
        return self.x < maxX and self.x >= 0 and self.y < maxY and self.y >= 0
            
    def adyacentFields(self, maxX, maxY):
        res = set()
        f = Field(self.x + 1, self.y)
        if f.isValid(maxX, maxY):
            res.add(f)
        f = Field(self.x - 1, self.y)
        if f.isValid(maxX, maxY):
            res.add(f)
        f = Field(self.x, self.y + 1)
        if f.isValid(maxX, maxY):
            res.add(f)
        f = Field(self.x, self.y - 1)
        if f.isValid(maxX, maxY):
            res.add(f)
        return res
        
class Guard(Field):
    def __init__(self, x, y, char):
        super().__init__(x, y)
        self.char = char
        
    def monitoredFields(self, obstacles, maxX, maxY):
        res = set()
        if self.char == '>':
            for x in range(self.x + 1, maxX):
                f = Field(x, self.y)
                if f in obstacles:
                    break
                res.add(f)
                
        elif self.char == '<':
            for x in reversed(range(self.x)):
                f = Field(x, self.y)
                if f in obstacles:
                    break
                res.add(f)
                
        elif self.char == '^':
            for y in reversed(range(self.y)):
                f = Field(self.x, y)
                if f in obstacles:
                    break
                res.add(f)
                
        elif self.char == 'v':
            for y in range(self.y + 1, maxY):
                f = Field(self.x, y)
                if f in obstacles:
                    break
                res.add(f)
                
        return res
            
class Board:
    def __init__(self, B):
        self.obstacles = set()
        self.guards = set()
        self.maxY = len(B)
        for y, row in enumerate(B):
            self.maxX = len(row)
            self.targetField = Field(len(row) - 1, len(B) - 1)
            for x, field in enumerate(row):
                if field == 'A':
                    self.assassin = Field(x, y)
                elif field == 'X':
                    self.obstacles.add(Field(x, y))
                elif field in ('>', '<', '^', 'v'):
                    self.guards.add(Guard(x, y, field))

            self.obstacles.update(self.guards)
                    
    def forbidenFields(self):
        res = set(self.guards)
        res.update(self.obstacles)
        for guard in self.guards:
            res.update(guard.monitoredFields(self.obstacles, self.maxX, self.maxY))
            
        return res
        
    def sol(self):
        self.forbFields = self.forbidenFields()
        availableFields = set()
        knownFields = {self.assassin}
        for field in self.assassin.adyacentFields(self.maxX, self.maxY):
            if field not in self.forbFields:
                knownFields.add(field)
                availableFields.add(field)
                
        while(self.targetField not in availableFields):
            aux = set()
            # toSearch = {field for avField in availableFields for field in avField.adyacentFields(self.maxX, self.maxY) if field not in self.forbFields}
            for avField in availableFields:
                for field in avField.adyacentFields(self.maxX, self.maxY):
                    if field not in self.forbFields and field not in knownFields:
                        knownFields.add(field)
                        aux.add(field)
                    
            if len(aux) == 0:
                return False
                
            availableFields = aux
        
        return True
        
def Assassin(B):
    # write your code in Python 3.6
    return Board(B).sol()
    