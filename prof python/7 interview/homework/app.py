from stack import Stack


def main(some_string):
    if some_string == '':
        return 'Введена пустая строка'

    possibly_elements = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = Stack()
    for el in some_string:
        if el in possibly_elements.values():
            stack.push(el)
        elif el in possibly_elements.keys() and not stack.is_empty():
            if stack.peek() == possibly_elements[el]:
                stack.pop()
            else:
                break
        else:
            return 'Не сбалансировано'
    if stack.is_empty():
        return 'Сбалансировано'
    else:
        return 'Не сбалансировано'


if __name__ == '__main__':
    user_string = input('Введите строку со скобками: ')
    result = main(user_string)
    print(result)
