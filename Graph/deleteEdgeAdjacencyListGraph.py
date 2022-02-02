def add_node(v):
    if v in graph:
        print(v, 'is already present in graph')
    else:
        graph[v] = []

graph = {}

def add_edge(v1, v2):

    if v1 not in graph:
        print(v1, 'is not present in the graph')
    elif v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        #list1 = [v2, cost]
        #list2 = [v1, cost]
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete_node(v):
    if v not in graph:
        print(v, 'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    elif v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)





add_node('A')
add_node('B')
add_node('C')
add_edge('A', 'B')
add_edge('A', 'C')
delete_edge('A', 'B')
print(graph) 