inf = 9999


# printing the solution
def print_solution(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == inf:
                print("INF", end=" ")
            print(distance[i][j], end=" ")
        print(" ")


def floyd_warshall(nv, graph):
    distance = graph
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(nv, distance)


gr = [
    [0, 8, inf, 1],
    [inf, 0, 1, inf],
    [4, inf, 0, inf],
    [inf, 2, 9, 1]
]
floyd_warshall(4, gr)
