import networkx as nx

if __name__ == '__main__':
    # 创建一个DAG
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 3), (1, 4), (4, 3)])

    # 进行拓扑排序
    topological_order = list(nx.topological_sort(G))
    print(topological_order)
