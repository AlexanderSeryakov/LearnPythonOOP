from collections import deque


def main():
    G = read_graph()
    start = input("С какой вершины начать?")
    while start not in G:
        start = input("Такой вершины нет. С какой вершины начать?")
    shortest_distance = dijcstra(G, start)  # Словарь с подсчитанными кратчайшими путями по типу: s = {'A': 0, 'B': 6.0}
    finish = input("В какую вершину нужно найти путь?")
    while finish not in G:
        finish = input("Такой вершины нет. С какой вершины начать?")
    shortest_path = reveal_shortest_path(G, finish, shortest_distance)  # Здесь находим путь по вершинам
    print(shortest_path)


def reveal_shortest_path(G, finish, shortest_distance):
    path = ([finish], [])
    distance = shortest_distance[finish]
    while distance != 0:
        for name, weight in G[finish].items():
            if distance == shortest_distance[name] + weight:
                path[0].append(name)
                path[1].append(weight)
                distance = shortest_distance[name]
                finish = name
    path = (path[0][::-1], path[1][::-1])
    return path


def read_graph():
    M = int(input())  # M - количество рёбер в графе (связей между вершинами)
    G = {}
    for i in range(M):
        a, b, weight = input().split()  # Создаем связь между двумя вершинами a, b и расстоянием weight
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)

    return G


def dijcstra(G, start):
    Q = deque()  # Очередь
    s = {start: 0}  # Словарь кратчайших путей по индентефикаторам
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if u not in s or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                Q.append(u)
    return s


def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

if __name__ == '__main__':
    main()
