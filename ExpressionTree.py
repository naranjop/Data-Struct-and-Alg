#  File: ExpressionTree.py

#  Description: BST Practice

#  Date Created: 11/12/2020

#  Date Last Modified: 11/12/2020


import sys

class Stack (object):
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    # add and item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]
    
    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)

class Tree (object):
    def __init__ (self):
        self.root = Node(None)

    def create_tree (self, expr):
        
        expStack = Stack()
        currentNode = self.root
        operators = ['+', '-', '*', '/', '//', '%', '**']
        
        # loop through the expression string
        for ch in expr:
            # ( ( 8 + 3 ) * ( 7 - 2 ) )

            # beginning of the parentheses
            if ch == '(':
                left = Node(None)
                currentNode.lchild = left
                expStack.push(currentNode)
                currentNode = currentNode.lchild 

            # operators
            elif ch in operators:
                currentNode.data = ch
                expStack.push(currentNode)
                currentNode.rchild = Node(None)
                currentNode = currentNode.rchild
            
            elif ch == ')':
                if not expStack.is_empty():
                    currentNode = expStack.pop()

            else:
                currentNode.data = ch
                currentNode = expStack.pop()


    def evaluate (self, aNode):
        operators = ['+', '-', '*', '/', '//', '%', '**']
        if aNode.data not in operators:
            return aNode.data        
        elif aNode.data in operators: 
            return operate(self.evaluate(aNode.lchild), self.evaluate(aNode.rchild), aNode.data)

    
    def pre_order (self, aNode):
        if (aNode != None):
            print (aNode.data, end= ' ')
            self.pre_order (aNode.lchild)
            self.pre_order (aNode.rchild)

      
    def post_order (self, aNode):
        if (aNode != None):
            self.post_order (aNode.lchild)
            self.post_order (aNode.rchild)
            print (aNode.data, end= ' ')

def operate(oper1, oper2, token):
        expr = str(oper1) + token + str(oper2)
        return eval(expr)


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    
    # initialize
    exprTree = Tree()
    exprTree.create_tree(expr.split())

    # evaluate the expression and print the result
    result = exprTree.evaluate(exprTree.root)
    print(expr, '=' , float(result))

    # get the prefix version of the expression and print
    print('Prefix Expression:', end =' ')
    exprTree.pre_order(exprTree.root)
    print()

    # get the postfix version of the expression and print
    print('Postfix Expression:', end =' ')
    exprTree.post_order(exprTree.root)

if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    main()