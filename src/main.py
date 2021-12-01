from .assassin import Assassin
from .groupDivision import GroupDivision
from .warehouse import Warehouse

def main():
    assassin()
    groupDivision()
    warehouse()

def assassin():
    assert Assassin(['X.....>', '..v..X.', '.>..X..', 'A......']) == False
    assert Assassin(['...Xv', 'AX..^', '.XX..']) == True
    assert Assassin(['...', '>.A']) == False
    assert Assassin(['A.v', '...']) == False

def groupDivision():
    assert GroupDivision([1, 4, 7, 3, 4], 2) == 3
    assert GroupDivision([1, 7, 3], 2) == 2
    assert GroupDivision([5, 4, 1, 2, 5, 3], 0) == 5

def warehouse():
    assert Warehouse([[1, 1, 0, 1], [1, 1, 1, 1]]).sol() == 2
    assert Warehouse([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]).sol() == 10

if __name__ == "__main__":
    main()