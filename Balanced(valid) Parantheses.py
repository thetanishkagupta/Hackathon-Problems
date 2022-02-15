# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isMatching(openingBracket, closingBracket):
    if (openingBracket == '{' and closingBracket == '}'):
        return True
    if (openingBracket == '(' and closingBracket == ')'):
        return True
    if (openingBracket == '[' and closingBracket == ']'):
        return True
    return False
class Solution(object):
    def isValid(self, expression):
        stack = []    
        for i in range(len(expression)):
            if (expression[i] == '{' or expression[i] == '(' or expression[i] == '['):    # if any openingBracket is present in the expression
                stack.append(expression[i])         # push it into the stack
            else:
                if(len(stack) == 0):     # if stack is empty   
                    return False
                if (isMatching(stack.pop(), expression[i] ) is not True):     #fetching top element of stack and comapring it with current element
                    return False
        if (len(stack) == 0):
            return True
        return False
