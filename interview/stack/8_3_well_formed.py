class Stack:
    def __init__(self) -> None:
        self._elementWithCachedMax: list[Stack.ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._elementWithCachedMax) == 0

    def pop(self) -> int:
        return self._elementWithCachedMax.pop()

    def push(self, x: int) -> None:
        self._elementWithCachedMax.append(x)


def well_fromed(s: str) -> bool:
    result = Stack()
    open = ['{', '[', '(']
    close = ['}', ']', ')']
    for c in s:
        if c in open:
            result.push(c)
        elif c in close:
            if result.empty():
                return False
            if open.index(result.pop()) != close.index(c):
                return False
        else:
            return False
    return result.empty()




def main():
    print(well_fromed("{[]}"))
    print(well_fromed("{{[]}"))
    print(well_fromed("()(())"))
    print(well_fromed("[()[]{()()}]"))
    print(well_fromed("{)"))


if __name__ == '__main__':
    main()