def create_graph():
    global COUNT_OF_GRAPHS
    COUNT_OF_GRAPHS += 1
    nods = list()
    work_array0 = list()
    work_array1 = list()
    for i in range(n := dpg.get_value("dimension")):
        for j in range(n):
            if (value := dpg.get_value(f"{i} {j}")) < 0:
                raise ValueError("Value < 0")
            work_array1.append(value)
        work_array0.append(work_array1)
        work_array1 = list()
    del work_array1
    max_distance = -1
    for i in range(n):
        for j in range(n):
            max_distance = max(max_distance, work_array0[i][j])
    print(max_distance)
    with (dpg.window(label=f"Graph {COUNT_OF_GRAPHS}", tag=f"graph{COUNT_OF_GRAPHS}", autosize=True, no_collapse=True)):
        with dpg.drawlist(width=max_distance * 20, height=max_distance * 20, tag=f"draw{COUNT_OF_GRAPHS}"):
            color = (127, 127, 127)

            for i in range(n):
                if i == 0:
                    x0 = rd.randint(150, 300)
                    y0 = rd.randint(150, 300)
                    dpg.draw_circle((x0, y0), 6, fill=color, tag=f"nod{i}{COUNT_OF_GRAPHS}")
                    nods.append((x0, y0, f"nod{i}{COUNT_OF_GRAPHS}"))
                    for j in range(n):
                        if j != i:
                            distance = work_array0[i][j] * 10
                            print(nods)
                            if distance != 0:
                                xn, yn = -1, -1
                                while not (xn >= 0 and yn >= 0):
                                    xn = rd.randint(-distance + nods[-1][0], distance + nods[-1][0])
                                    yn = rd.choice((-1, 1)) * int((distance ** 2 - (xn - nods[-1][0]) ** 2) ** 0.5
                                                                  ) + nods[-1][1]

                                dpg.draw_circle((xn, yn), 6, fill=color)
                                dpg.draw_line((nods[-1][0], nods[-1][1]), (xn, yn))
                                nods.append((xn, yn, f"nod{j}{COUNT_OF_GRAPHS}"))
                else:
                    pass



def ford_fulkerson(graph, source, sink):
    parent = [-1 for _ in range(len(graph))]
    max_flow = 0

    def bfs(graph, source, sink, parent):
        visited = [False for _ in range(len(graph))]
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[sink]

    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow