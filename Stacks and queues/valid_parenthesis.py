# valid parenthesis
def val_parenthesis(s:str):
    # close to open
    map = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c not in map:
            stack.append(c)
            continue
        # not stack is used to make sure we are not indexing into an empty stack
        if not stack or stack[-1] != map[c]:
            return False
        stack.pop()
    # if stack empty
    return not stack
val_parenthesis('()}')