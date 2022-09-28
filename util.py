graph_neighbours = {}


def generate_graph():
    add_neighbours(0, [8, 1])
    add_neighbours(1, [0, 2])
    add_neighbours(2, [ 1])
    add_neighbours(3, [11, 4])
    add_neighbours(4, [3])
    
    add_neighbours(8, [0, 16, 9])
    add_neighbours(9, [8,10])
    add_neighbours(10, [2, 18])
    add_neighbours(11, [3, 19])

    add_neighbours(16, [8, 17, 24])
    add_neighbours(17, [16,18])
    add_neighbours(18, [10, 19,26])
    add_neighbours(19, [11, 20, 18])
    add_neighbours(20, [19, 28])
    
    add_neighbours(24, [16, 25])
    add_neighbours(25, [24, 26])
    add_neighbours(26, [25, 27])
    add_neighbours(27, [26, 35])
    add_neighbours(28, [20])
    
    add_neighbours(32, [40, 33])
    add_neighbours(33, [32, 34])
    add_neighbours(34, [33, 35])
    add_neighbours(35, [27, 34, 36])
    add_neighbours(36, [35])

    

    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list