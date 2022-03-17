from typing import Any

balanced_sequences = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
open_brackets = ['(', '[', '{']
closed_brackets = [')', ']', '}']


class StackItem:

    def __init__(self, value: Any, prev_stack_item: 'StackItem' = None):
        self.value = value
        self.prev_stack_item = prev_stack_item


class Stack:

    def __init__(self):
        self.tail = None
        self.size_stack = 0

    def isEmpty(self):
        if self.tail is None:
            return True
        return False

    def push(self, value: Any):
        new_stack_item = StackItem(value, self.tail)
        self.tail = new_stack_item
        self.size_stack += 1

    def pop(self):
        value = self.tail.value
        self.tail = self.tail.prev_stack_item
        self.size_stack -= 1
        return value

    def peek(self):
        return self.tail.value

    def size(self):
        return self.size_stack


def check_sequence(bracket, mystack_peek):
    if bracket == ')':
        if mystack_peek == '(': return True
        else: return False
    elif bracket == ']':
        if mystack_peek == '[': return True
        else: return False
    elif bracket == '}':
        if mystack_peek == '{': return True
        else: return False


def main():
    mystack = Stack()
    for balanced_sequence in balanced_sequences:
        not_balance = True
        for bracket in balanced_sequence:
            if bracket in open_brackets:
                mystack.push(bracket)
            elif bracket in closed_brackets:
                if mystack.size() != 0 and check_sequence(bracket, mystack.peek()):
                    mystack.pop()
                else:
                    print(f'Последовательность {balanced_sequence} - несбалансированная')
                    not_balance = False
                    break
        if not_balance:
            print(f'Последовательность {balanced_sequence} - сбалансированная')


if __name__ == '__main__':
    main()
