from random import choice

class Node:
    def __init__(self, name):
        self.name = name
        self.d = float('inf')
        self.pi = None

    def __lt__(self, other):
        return self.d < other.d
    
    def __repr__(self):
        return f"Node({self.name})"

class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.adj = {}

def approx_vertex_cover(G):
    C = set()
    E0 = G.E[:]
    while E0:
        u, v = choice(E0)
        C.add(u)
        C.add(v)
        
        E0 = [e for e in E0 if u not in e and v not in e]
    
    return C

def main():
    G = Graph()
    while True:
        v_name = input('Enter vertice name:')
        if v_name == 'exit':
            break
        if not any(node.name == v_name for node in G.V):
            u = Node(v_name)
            G.V.append(u)
            G.adj[u] = []
        else:
            print('Node already exists')
            continue
    while True:
        edge = input("Enter edge source, target and weight:")
        if edge == 'exit':
            break
        u, v= edge.split()
        U = next((i for i in G.V if i.name == u), None)
        V = next((i for i in G.V if i.name == v), None)
        if not U or not V:
            print('Node doesnt exist')
            exit()
        if (U, V) in G.E:
            print('Edge already exists, do you want to update weight?')
            choice = input()
            if choice == 'n':
                continue
        G.E.append((U, V))
        G.adj[U] = G.adj[U] + [V]
        G.E.append((V, U))
        G.adj[V] = G.adj[V] + [U]
    cover_vertices = approx_vertex_cover(G)
    print(f"Vertex Cover solution: {cover_vertices}")
    print(f"Size of vertex cover: {len(cover_vertices)}")

if __name__ == '__main__':
    main()
