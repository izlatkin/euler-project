import collections


class Stack:
    ElementWithCachedMax = []

    def __init__(self) -> None:
        self._elementWithCachedMax: list[Stack.ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._elementWithCachedMax) == 0

    def pop(self) -> int:
        return self._elementWithCachedMax.pop()

    def push(self, x: int) -> None:
        self._elementWithCachedMax.append(x)


def evaluate(expression: str) -> int:
    intermediate_result: list[int] = []
    operator = ['+', '-', '*', '/']

    for token in expression.split():
        if token in operator:
            if token == '+':
                intermediate_result.append(intermediate_result.pop() + intermediate_result.pop())
            if token == '-':
                intermediate_result.append(intermediate_result.pop() - intermediate_result.pop())
            if token == '*':
                intermediate_result.append(intermediate_result.pop() * intermediate_result.pop())
            if token == '/':
                intermediate_result.append(intermediate_result.pop() // intermediate_result.pop())
        else:
            intermediate_result.append(int(token))
    return intermediate_result[-1]


def evaluate_reverse(expression: str) -> int:
    #result: list[int] = []
    result = Stack()
    #operator_stack: list[int] = []
    operator_stack = Stack()
    operator = ['+', '-', '*', '/']
    last_op = False

    for token in expression.split():
        if token in operator:
            operator_stack.push(token)
            last_op = True
        else:
            if not result.empty() and not operator_stack.empty() and not last_op:
                opt = operator_stack.pop()
                if opt == '+':
                    result.push(result.pop() + int(token))
                if opt == '-':
                    result.push(result.pop() - int(token))
                if opt == '*':
                    result.push(result.pop() * int(token))
                if opt == '/':
                    result.push(result.pop() // int(token))
            else:
                result.push(int(token))
            last_op = False
    while not operator_stack.empty():
        opt = operator_stack.pop()
        if opt == '+':
            result.push(result.pop() + result.pop())
        if opt == '-':
            result.push(result.pop() - result.pop())
        if opt == '*':
            result.push(result.pop() * result.pop())
        if opt == '/':
            result.push(result.pop() // result.pop())


    return result.pop()




def main():
    print(evaluate("1798"))
    print(evaluate("3 4 + 2 * 1 +"))
    print(evaluate("1 1 +  -2  *"))
    print(evaluate("-644 6 / 28 /"))
    print(evaluate_reverse("1798"))
    print(evaluate_reverse("+ + 1 2 3"))
    print(evaluate_reverse("+ + 1 2 / 18 3"))


if __name__ == '__main__':
    main()