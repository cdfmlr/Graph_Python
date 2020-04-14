from graph_class import *
from collections import deque

def traverse(node):
    node.visited = True

    queue = deque([])
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node.name)
        for link in node.links:
            if not link.nodes[1].visited:
                link.nodes[1].visited = True
                queue.append(link.nodes[1])


if __name__ == '__main__':
    g = Graph('/Users/c/Desktop/a.txt')
    print('-' * 10, '0:')
    traverse(g.nodes[0])
    
    # print('-' * 10, '9:')
    # traverse(g.nodes[9])
