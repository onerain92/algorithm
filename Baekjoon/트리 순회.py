class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def pre_order(tree, start_node):
    current_node = tree[start_node]
    print(current_node.value, end='')
    if current_node.left_node != '.':
        pre_order(tree, tree[current_node.left_node].value)
    if current_node.right_node != '.':
        pre_order(tree, tree[current_node.right_node].value)


def in_order(tree, start_node):
    current_node = tree[start_node]
    if current_node.left_node != '.':
        in_order(tree, tree[current_node.left_node].value)
    print(current_node.value, end='')
    if current_node.right_node != '.':
        in_order(tree, tree[current_node.right_node].value)


def post_order(tree, start_node):
    current_node = tree[start_node]
    if current_node.left_node != '.':
        post_order(tree, tree[current_node.left_node].value)
    if current_node.right_node != '.':
        post_order(tree, tree[current_node.right_node].value)
    print(current_node.value, end='')


def solution(trees):
    tree = {}

    for tree_info in trees:
        value, left_node, right_node = tree_info
        tree[value] = Node(value, left_node, right_node)

    pre_order(tree, 'A')
    print()
    in_order(tree, 'A')
    print()
    post_order(tree, 'A')


solution([['A', 'B', 'C'], ['B', 'D', '.'], ['C', 'E', 'F'], [
    'E', '.', '.'], ['F', '.', 'G'], ['D', '.', '.'], ['G', '.', '.']])
