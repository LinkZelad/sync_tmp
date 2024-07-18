from typing import Set

if __name__ == "__main__":
    a: Set[int] = set()
    a.add(1)
    a.add(1)
    print(len(a))
    print(a)