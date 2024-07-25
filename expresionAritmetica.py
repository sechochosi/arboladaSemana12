class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def construct_tree(self, postfix):
        stack = []
        for char in postfix:
            if char.isdigit():
                stack.append(ExpressionNode(char))
            else:
                node = ExpressionNode(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    def evaluate(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return int(node.value)
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

# Ejemplo de uso
et = ExpressionTree()
postfix_expression = "325*+"
et.construct_tree(postfix_expression)
print("Evaluación de la expresión:", et.evaluate(et.root))
