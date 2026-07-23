from PriorityQueue import PriorityQueue

def dijkstra(graph, sNode, eNode):

    # Initialise dictionaries
    prev = {n: None for n in graph.adjList.keys()}
    visited = {n: False for n in graph.adjList.keys()}
    distances = {n: float('inf') for n in graph.adjList.keys()}

    distances[sNode] = 0

    queue = PriorityQueue()
    queue.add_task(0, sNode)

    while queue:

        removedDist, removedNode = queue.pop_task()

        # Ignore already processed nodes
        if visited[removedNode]:
            continue

        visited[removedNode] = True

        # Stop once destination is reached
        if removedNode == eNode:
            break

        # Check neighbours
        for edge in graph.adjList[removedNode]:

            if visited[edge.node]:
                continue

            new_dist = removedDist + edge.weight

            if new_dist < distances[edge.node]:

                distances[edge.node] = new_dist
                prev[edge.node] = removedNode

                queue.add_task(new_dist, edge.node)


    # Build shortest path
    path = []

    current = eNode

    if distances[eNode] == float('inf'):
        return None, []

    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()

    return distances[eNode], path