
def mapLayout(layout):
    map = {}
    row, col = 0,0
    print(layout)
    for l in layout:
        for v in l:
            map[(row, col)] = int(v)
            col +=1
        col = 0
        row += 1
    return map, row

# find all valid paths
# from 0,0...only 2 paths 0,1 and 1,0...after that both can go to 1,1
# calculate cost



# Python implementation to find the 
# shortest path in the graph using 
# dictionaries 
 
# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the 
    # graph in the BFS
    queue = [start]
     
    # If the desired node is 
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes 
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return

# find a path with all 1s and is it valid
# traverse every path

game_data = [
    '2413432311323',
    '3215453535623',
    '3255245654254',
    '3446585845452',
    '4546657867536',
    '1438598798454',
    '4457876987766',
    '3637877979653',
    '4654967986887',
    '4564679986453',
    '1224686865563',
    '2546548887735',
    '4322674655533'
]

map, max = mapLayout(game_data)

print(map)
