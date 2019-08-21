"""
A bracket is any of the following: (), {}, [].
Write a function which takes a sequence of n brackets, return
whether or not the sequence is balanced
"""

def isBalanced(s):
    stack = []
    stack_size = 0
    n = len(s)
    if n % 2 == 1:
        return False

    brackets = '([{}])'
    mapper = {brackets[i]: brackets[len(brackets) - i - 1]
              for i in range(len(brackets) // 2)}

    for bracket in s:
        if bracket in mapper:
            stack.append(bracket)
            stack_size += 1
        else:
            pop_val = stack[-1]
            if bracket != mapper[pop_val]:
                return False
            del stack[-1]
            stack_size -= 1
    if stack_size == 0:
        return True
    return False

if __name__ == '__main__':
    s = '{[(])}'
    print(isBalanced(s))
