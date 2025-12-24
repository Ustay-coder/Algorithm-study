import sys


def solve(sentence):
    stack = []
    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char) 
        elif char == ")":
            # 만약 비어 있을 경우, 그냥 더한다.
            if(len(stack) == 0):
                stack.append(char)
                continue 
            top = stack[-1]
            if top == "(":
                stack.pop()
            else:
                stack.append(char)
        elif char == "]":
            # 만약 비어 있을 경우, 그냥 더한다.
            if(len(stack) == 0):
                stack.append(char)
                continue 
            top = stack[-1]
            if top == "[":
                stack.pop()
            else:
                stack.append(char)
        else:
            continue 
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    while(True):
        text = input()
        if text == ".":
            break 
        solve(text)
