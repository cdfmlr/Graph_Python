from graph_class import *

def traverse(node):
    node.visited = True

    stack = []
    stack.append(node)

    while stack:
        node = stack.pop()
        print(node.name)
        for link in node.links:
            if not link.nodes[1].visited:
                link.nodes[1].visited = True
                stack.append(link.nodes[1])


if __name__ == '__main__':
    g = Graph('tinyG.txt')
    print('-' * 10, '0:')
    traverse(g.nodes[0])
    print('-' * 10, '9:')
    traverse(g.nodes[9])
