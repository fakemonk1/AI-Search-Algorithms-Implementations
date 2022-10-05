graph_neighbours = {}


def generate_graph():
    add_neighbours('0', ['8', '1'])
    add_neighbours('1', ['0', '2'])
    add_neighbours('2', ['10', '1'])
    add_neighbours('3', ['11', '4'])
    add_neighbours('4', ['3', '5'])
    add_neighbours('5', ['4', '6'])
    add_neighbours('6', ['5'])
    add_neighbours('7', ['15'])
    add_neighbours('8', ['0', '16', '9'])
    add_neighbours('9', ['8'])
    add_neighbours('10', ['2', '18'])
    add_neighbours('11', ['3', '19'])
    add_neighbours('12', ['13'])
    add_neighbours('13', ['12', '14', '21'])

    add_neighbours(14, [13, 15])
    add_neighbours(15, [7, 14, 23])
    add_neighbours(16, [8, 17, 24])
    add_neighbours(17, [16])
    add_neighbours(18, [10, 19])
    add_neighbours(19, [11, 20, 18])
    add_neighbours(20, [19, 28])
    add_neighbours(21, [13, 22])
    add_neighbours(22, [21])
    add_neighbours(23, [15, 31])
    add_neighbours(24, [16, 25])
    add_neighbours(25, [24, 26])
    add_neighbours(26, [25, 27])
    add_neighbours(27, [26, 35])
    add_neighbours(28, [20, 29])
    add_neighbours(29, [28, 30])
    add_neighbours(30, [29, 31])
    add_neighbours(31, [30, 23])
    add_neighbours(32, [40, 33])
    add_neighbours(33, [32, 34])
    add_neighbours(34, [33, 35])
    add_neighbours(35, [27, 34, 36])
    add_neighbours(36, [35, 37])
    add_neighbours(37, [36])

    add_neighbours(38, [46, 39])
    add_neighbours(39, [38, 47])
    add_neighbours(40, [32, 48])
    add_neighbours(41, [49, 42])
    add_neighbours(42, [41, 50, 43])
    add_neighbours(43, [42, 51, 44])
    add_neighbours(44, [43, 45])
    add_neighbours(45, [44, 46, 53])
    add_neighbours(46, [45, 38])
    add_neighbours(47, [39, 55])
    add_neighbours(48, [40, 56])
    add_neighbours(49, [41, 50])
    add_neighbours(50, [49, 42])
    add_neighbours(51, [43, 59])
    add_neighbours(52, [53])
    add_neighbours(53, [61, 52, 45])
    add_neighbours(54, [62])
    add_neighbours(55, [47, 63])
    add_neighbours(56, [48, 57])
    add_neighbours(57, [56, 58])
    add_neighbours(58, [57, 59])
    add_neighbours(59, [58, 51, 60])
    add_neighbours(60, [59])
    add_neighbours(61, [53])
    add_neighbours(62, [54, 63])
    add_neighbours(63, [55, 62])

    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

