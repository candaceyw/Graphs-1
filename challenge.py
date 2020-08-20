# Summing Values from a Dictionary
# Given an object/dictionary with keys and values that consist of both strings and integers,
# design an algorithm to calculate and return the sum of all of the numeric values.
# Verbalize your thought process as much as possible before writing any code.
#
# Run through the UPER problem solving framework while going through your thought process.
#
my_dict = {
"cat" : "bob",
"dog" : 23,
19 : 18,
90 : "fish"
}

def sum_values(d):
    total = 0
    for value in d.values():
        if type(value) == int:
            total += value

    return total

print(sum_values(my_dict))


def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # Create an empty queue and enqueue the PATH TO STARTING_VERTEX

    # create an empty set to track visited vertices
    q = Queue()
    visited = []
    q.enqueue([starting_vertex])
    # while the queue is not empty:
    while q.size() > 0:
        # get current vertex PATH (dequeue from queue)
        curr_path = q.dequeue()
        # SET THE CURRENT VERTEX TO THE LAST ELEMENT OF THE PATH
        curr_node = curr_path[-1]
        print('bfs curr_node; ', curr_node)
        # CHECK IF THE CURRENT VERTEX IS DESTINATION
        # IF IT IS, STOP AND RETURN
        if curr_node is destination_vertex:
            return curr_path
        # Check if the current vertex has not been visited:
        if curr_node not in visited:
            # add the current vertex to a visited_set
            # Mark the current vertex as visited
            visited.append(curr_node)

            for neighbor in self.get_neighbors(curr_node):
                # TAKE CURRENT PATH
                new_path = curr_path.copy()
                # APPEND THE NEIGHBOR TO IT
                new_path.append(neighbor)
                # QUEUE UP NEW PATH
                q.enqueue(new_path)
                # queue up NEW PATHS WITH EACH NEIGHBOR:


        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex PATH (dequeue from queue)
            path = queue.dequeue()
            # set the current vertex to the LAST element of the PATH
            current = path[-1]
            # Check if the current vertex has not been visited:
            if current not in visited:
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                if current is destination_vertex:
                # IF IT IS, STOP AND RETURN
                    return current
                # Mark the current vertex as visited
                visited.add(current)
                    # Add the current vertex to a visited_set
                # Queue up NEW paths with each neighbor:
                path.extend(self.get_neighbors(current))
                queue.enqueue(path)
