from .assassin import solution

def main():
    print(solution(['X.....>', '..v..X.', '.>..X..', 'A......']) == False)
    print(solution(['...Xv', 'AX..^', '.XX..']) == True)
    print(solution(['...', '>.A']) == False)
    print(solution(['A.v', '...']) == False)


if __name__ == "__main__":
    main()