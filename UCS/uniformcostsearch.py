from PriorityQueue import PriorityQueue


def uniform_cost_search(graph, start, goal):

    previous = {
        node: None 
        for node in graph.adjList.keys()
    }


    visited = {
        node: False
        for node in graph.adjList.keys()
    }


    distances = {
        node: float('inf')
        for node in graph.adjList.keys()
    }



    distances[start] = 0


    queue = PriorityQueue()

    queue.add_task(0, start)



    while queue:


        current_distance, current_node = queue.pop_task()



        if visited[current_node]:

            continue



        visited[current_node] = True



        if current_node == goal:

            break



        for edge in graph.adjList[current_node]:


            new_distance = current_distance + edge.weight



            if new_distance < distances[edge.node]:


                distances[edge.node] = new_distance

                previous[edge.node] = current_node

                queue.add_task(
                    new_distance,
                    edge.node
                )



    if distances[goal] == float('inf'):

        return None, []



    path = []

    current = goal



    while current is not None:

        path.append(current)

        current = previous[current]



    path.reverse()



    return distances[goal], path