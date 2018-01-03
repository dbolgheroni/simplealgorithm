#!/usr/bin/python3

def dfs_preorder(graph, node):
    dt = {}
    time = 0

    def _dfs(graph, node):
        nonlocal dt
        nonlocal time

        time += 1
        dt[node] = time

        for n in graph[node]: 
            if n and not dt.get(n):
                _dfs(graph, n)

    _dfs(graph, node)

    # sort dict by discovery time
    return sorted(dt, key=dt.get)

def dfs_postorder(graph, node):
    dt = {}
    ft = {}
    time = 0

    def _dfs(graph, node):
        nonlocal dt
        nonlocal ft
        nonlocal time

        time += 1
        dt[node] = time

        for n in graph[node]: 
            if n and not dt.get(n):
                _dfs(graph, n)

        ft[node] = time

    _dfs(graph, node)

    # sort dict by discovery time
    return sorted(ft, key=ft.get)

def main():
    # examples
    tree = {
            'A': ('B', 'E'),
            'B': ('C', 'D'),
            'C': (),
            'D': (),
            'E': (None, 'F'),
            'F': ('G'),
            'G': (),
    }

    graph = {
            'A': ('B', 'C'),
            'B': ('C', 'D'),
            'C': ('D',),
            'D': ('C'),
            'E': ('F'),
            'F': ('C',),
    }

    print("tree preorder")
    preorder_tree = dfs_preorder(tree, 'A')
    for t in preorder_tree:
        print(t)

    print("tree postorder")
    postorder_tree = dfs_postorder(tree, 'A')
    for t in postorder_tree:
        print(t)

    preorder_graph = dfs_preorder(graph, 'A')
    print("graph preorder")
    for t in preorder_graph:
        print(t)

    postorder_graph = dfs_postorder(graph, 'A')
    print("graph postorder")
    for t in postorder_graph:
        print(t)

if __name__ == '__main__':
    main()
