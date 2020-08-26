from util import Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()
    # set up graph
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])

    # do BFS
    # create a queue
    q = Queue()
    # add start word to Queue (like a path)
    q.enqueue([starting_node])
    # create a visited set
    visited = set()

    # If the input individual has no parents, the function should return -1.
    ancestor = -1

    # while queue not empty
    while q.size() > 0:
        # pop current path off queue
        current_path = q.dequeue()
        current_node = current_path[-1]

        # if current node has not been visited:
        if current_node not in visited:
            # add current node
            visited.add(current_node)

            # See if the current node is less than the parent then
            # ances
            if (current_node < ancestor) or (len(current_path) > 1):
                # set the parent as the current node
                ancestor = current_node

            # Check for the neighbors of the current_node
            for neighbor in graph.get_neighbors(current_node):
                # copy the path
                new_path = current_path.copy()
                # add the neighbor to the path
                new_path.append(neighbor)
                # and add the path to the queue
                q.enqueue(new_path)

    return ancestor

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1), 10)