import types

class Node:
    pass

class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                print('before: ', stack)
                if isinstance(last, types.GeneratorType):
                    print('1')
                    # stack.append(next(last))
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    print('2')
                    stack.append(self._visit(stack.pop()))
                else:
                    print('3')
                    last_result = stack.pop()

                print('after: ', stack)
            except StopIteration:
                stack.pop()
            print('---------------')

        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield (yield node.operand)

if __name__ == '__main__':
    # t1 = Sub(Number(3), Number(4))
    # t2 = Mul(Number(2), t1)
    # t3 = Div(t2, Number(5))
    # t4 = Add(Number(1), t3)
    # e = Evaluator()
    # print(e.visit(t4))
    a = Number(0)
    for n in range(1, 3):
        a = Add(a, Number(n))

    e = Evaluator()
    print(e.visit(a))
