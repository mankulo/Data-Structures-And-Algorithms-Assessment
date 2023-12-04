def is_balanced(expression):
    # Define a dictionary to store the mapping of opening and closing brackets
    brackets_map = {')': '(', '}': '{', ']': '['}

    # Create an empty stack to store opening brackets
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        if char in brackets_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in brackets_map.keys():  # If it's a closing bracket
            # Check if the stack is empty or if the top of the stack doesn't match the expected opening bracket
            if not stack or stack.pop() != brackets_map[char]:
                return False

    # After iterating through the entire expression, the stack should be empty for a balanced expression
    return len(stack) == 0

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False