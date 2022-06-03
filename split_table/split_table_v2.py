def make_graph(pluses):
    graph = {}
    not_in_graph = True
    for el in pluses:
        for s_el in pluses:
            if el != s_el:
                if el not in graph:
                    graph[el] = []
                if s_el[0] == el[0] or s_el[1] == el[1]:
                    if graph[el]:
                        for node in graph[el]:
                            if s_el[0] == node[0] or s_el[1] == node[1]:
                                d_x_n = el[1] - node[1]
                                d_x_o = el[1] - s_el[1]
                                d_y_n = el[0] - node[0]
                                d_y_o = el[0] - s_el[0]
                                if ((d_x_n < 0 and d_x_o < 0) or (d_y_n < 0 and d_y_o < 0)) or (
                                        (d_x_n > 0 and d_x_o > 0) or (d_y_n > 0 and d_y_o > 0)):
                                    not_in_graph = False
                                    if abs(d_x_o) < abs(d_x_n) or abs(d_y_o) < abs(d_y_n):
                                        ind = graph[el].index(node)
                                        graph[el] = graph[el][:ind] + [s_el] + graph[el][ind + 1:]
                    if not_in_graph:
                        graph[el].append(s_el)
                        continue
                    not_in_graph = True
    return graph


def find_closest_neighbours(field, start_pos):
    start_pos = list(start_pos)
    current_pos = start_pos
    closest_neighbours = []
    directions = ['up', 'right', 'down', 'left']
    direction_ind = 0
    pos_change = {'up': [(lambda x: x - 1)(current_pos[0]), current_pos[1]],
                  'right': [current_pos[0], (lambda x: x + 1)(current_pos[1])],
                  'down': [(lambda x: x + 1)(current_pos[0]), current_pos[1]],
                  'left': [current_pos[0], (lambda x: x + 1)(current_pos[1])]}
    while direction_ind < 5:
        try:
            current_pos = pos_change[directions[direction_ind]]
            if field[current_pos[0]][current_pos[1]] == '+':
                closest_neighbours.append(current_pos)
                direction_ind += 1
                current_pos = start_pos
            elif field[current_pos[0]][current_pos[1]] not in '|-':
                raise IndexError
        except IndexError:
            direction_ind += 1
            current_pos = start_pos
    return closest_neighbours


def break_pieces(shape):
    shape_list = shape.split('\n')
    print(*shape_list, sep='\n')
    where_pluses = []
    for i in range(len(shape_list)):
        for j in range(len(shape_list[i])):
            if shape_list[i][j] == '+':
                where_pluses.append((i, j))
    print(where_pluses)
    graph = {}
    for el in where_pluses:
        graph[el] = find_closest_neighbours(shape_list, el)


test_data_1 = '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  ' \
              '|\n|  |                   |\n|  |                   |\n+--+-------------------+ '
test_data_2 = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|    ' \
              '  |     |\n+------+-----+ '
test_data_3 = '''

         +------------+--+      +--+
         |            |  |      |  |
         | +-------+  |  |      |  |
         | |       |  |  +------+  |
         | |       |  |            |
         | |       |  |    +-------+
         | +-------+  |    |        
 +-------+            |    |        
 |       |            |    +-------+
 |       |            |            |
 +-------+            |            |
         |            |            |
    +----+---+--+-----+------------+
    |    |   |  |     |            |
    |    |   |  +-----+------------+
    |    |   |                     |
    +----+---+---------------------+
    |    |                         |
    |    | +----+                  |
+---+    | |    |     +------------+
|        | |    |     |             
+--------+-+    +-----+             
'''
break_pieces(test_data_1)
