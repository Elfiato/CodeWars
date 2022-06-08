from collections import deque


def position_change(direction, current_pos):
    if direction == 'up':
        current_pos[0] -= 1
    elif direction == 'right':
        current_pos[1] += 1
    elif direction == 'down':
        current_pos[0] += 1
    else:
        current_pos[1] -= 1
    return current_pos


def find_closest_neighbours(field, start_pos):
    start_pos = list(start_pos)
    current_pos = start_pos.copy()
    closest_neighbours = []
    directions = ['up', 'down', 'right', 'left']
    direction_ind = 0
    while direction_ind < 5:
        try:
            current_pos = position_change(directions[direction_ind], current_pos)
            if (current_pos[0] > len(field) or current_pos[0] < 0) or (
                    current_pos[1] > len(field[3]) or current_pos[1] < 0):
                raise IndexError
            if field[current_pos[0]][current_pos[1]] == '+':
                closest_neighbours.append(tuple(current_pos))
                direction_ind += 1
                current_pos = start_pos.copy()
            elif field[current_pos[0]][current_pos[1]] not in '|-':
                raise IndexError
        except IndexError:
            direction_ind += 1
            current_pos = start_pos.copy()
    return closest_neighbours


def find_figure(graph, start_node):
    que = deque([(start_node, None)])
    parents = {}
    is_start_node = False
    visited = []
    end_node = start_node
    while not is_start_node:
        if not que:
            return set()
        current_node, parent = que.popleft()
        parents[current_node] = [parent]
        try:
            if parents[parent] != [None]:
                parents[current_node].extend(parents[parent])
        except KeyError:
            pass
        visited.append(current_node)
        for el in graph[current_node]:
            if el != parent and el != start_node:
                if el in visited:
                    counter = 0
                    for i in parents[current_node] + [current_node]:
                        for j in parents[el] + [el]:
                            if i == j:
                                counter += 1
                    if counter == 1:
                        is_start_node = True
                        end_node = el, current_node
                        break
                que.append((el, current_node))
    return set([end_node[0]] + parents[end_node[0]] + parents[end_node[1]] + [end_node[1]])


def filter_figure_point(figure, field):
    res = []
    hor_up, hor_low = None, None
    vert_up, vert_low = None, None
    save_flag = True
    for el1 in figure:
        for el2 in figure:
            if el1[0] == el2[0]:
                if el2[1] > el1[1]:
                    hor_up = el2[1]
                elif el2[1] < el1[1]:
                    hor_low = el2[1]
            if el1[1] == el2[1]:
                if el2[0] > el1[0]:
                    vert_up = el2[0]
                elif el2[0] < el1[0]:
                    vert_low = el2[0]
        if vert_up is not None and vert_low is not None:
            save_flag = False
            for i in range(vert_low, vert_up + 1):
                if not field[i][el1[1]] in '|+':
                    save_flag = True
        elif hor_up is not None and hor_low is not None:
            save_flag = False
            for j in range(hor_low, hor_up + 1):
                if not field[el1[0]][j] in '-+':
                    save_flag = True
        if save_flag:
            res.append(el1)
        hor_low, hor_up, vert_low, vert_up = None, None, None, None
        save_flag = True
    return res


def find_max_min_cord(cords):
    mx_Y, mn_Y = cords[0][0], cords[0][0]
    mx_X, mn_X = cords[0][1], cords[0][1]
    for c in cords:
        if c[0] > mx_Y:
            mx_Y = c[0]
        elif c[0] < mn_Y:
            mn_Y = c[0]
        if c[1] > mx_X:
            mx_X = c[1]
        elif c[1] < mn_X:
            mn_X = c[1]
    return mx_Y, mn_Y, mx_X, mn_X


def draw_figure(figure, field):
    if not figure:
        return
    is_angle_flag = False
    result_figure = []
    figure = filter_figure_point(list(figure), field)
    mx_y, mn_y, mx_x, mn_x = find_max_min_cord(figure)
    y_b, x_b = mx_y - mn_y + 1, mx_x - mn_x + 1
    is_put_el = False
    for i in range(y_b):
        result_figure.append('')
        for j in range(x_b):
            for point in figure:
                if i == point[0] - mn_y and j == point[1] - mn_x:
                    is_angle_flag = True
                    break
            if is_angle_flag:
                result_figure[-1] += '+'
                is_angle_flag = False
                continue
            try:
                if result_figure[-1][-1] in '+-':
                    result_figure[-1] += '-'
                    is_put_el = True
            except IndexError:
                pass
            try:
                if result_figure[-2][j] in '+|':
                    result_figure[-1] += '|'
                    is_put_el = True
            except IndexError:
                pass
            try:
                if result_figure[-2][j] == '+':
                    if result_figure[-3][j] in '+|' and result_figure[-1][-1] == '|':
                        result_figure[-1] = result_figure[-1][:-1] + ' '
            except IndexError:
                pass
            try:
                if result_figure[-1][-2] == '+':
                    if result_figure[-1][-3] in '+-' and result_figure[-1][-1] == '-':
                        result_figure[-1] = result_figure[-1][:-1] + ' '
            except IndexError:
                pass
            if not is_put_el:
                result_figure[-1] += ' '
            is_put_el = False
        result_figure[-1] = result_figure[-1].rstrip()
    for st_ind in range(len(result_figure)):
        f_st = False
        tmp_st = result_figure[st_ind]
        for row_ind in range(len(result_figure[st_ind])):
            if not f_st and result_figure[st_ind][row_ind] in '|+':
                f_st = True
            if f_st and result_figure[st_ind][row_ind] == ' ' and field[st_ind + mn_y][row_ind + mn_x] != ' ' and \
                    tmp_st[row_ind - 1] not in '+|':
                result_figure[st_ind] = result_figure[st_ind][:row_ind] + field[st_ind + mn_y][row_ind + mn_x] + \
                                        result_figure[st_ind][row_ind + 1:]
    return '\n'.join(result_figure)


def break_pieces(shape):
    shape_list = shape.split('\n')
    where_pluses = []
    for i in range(len(shape_list)):
        for j in range(len(shape_list[i])):
            if shape_list[i][j] == '+':
                where_pluses.append((i, j))

    graph = {}
    for el in where_pluses:
        graph[el] = find_closest_neighbours(shape_list, el)

    figures_angle_coordinates = []
    figures_in_lines = []
    for node in graph:
        figure = find_figure(graph, node)
        if figure not in figures_angle_coordinates:
            figures_angle_coordinates.append(figure)
            figure_in_line = draw_figure(figure, shape_list)
            if figure_in_line:
                figures_in_lines.append(figure_in_line)
    print(*figures_in_lines, sep='\n')
    return figures_in_lines


def break_pieces2(shape):
    shape_list = shape.split('\n')
    print(*shape_list, sep='\n')
    where_pluses = []
    for i in range(len(shape_list)):
        for j in range(len(shape_list[i])):
            if shape_list[i][j] == '+':
                where_pluses.append((i, j))

    graph = {}
    for el in where_pluses:
        graph[el] = find_closest_neighbours(shape_list, el)

    figures_angle_coordinates = []
    figures_in_lines = []
    for node in graph:
        figure = find_figure(graph, node)
        if figure not in figures_angle_coordinates:
            print(figure)
            figures_angle_coordinates.append(figure)
            figures_in_lines.append(draw_figure(figure, shape_list))
    print(*figures_in_lines, sep='\n#############\n')
    return figures_in_lines


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
test_data_4 = '''
+-------+ +----------+
|       | |          |
| +-+ +-+ +-+    +-+ |
+-+ | |     |  +-+ +-+
    | +-----+--+
+-+ |          +-+ +-+
| +-+  +----+    | | |
| |    |    |    +-+ |
| +----++ +-+        |
|       | |          |
+-------+ +----------+'''
test_data_5 = '''
+--------+
|        |
|  +--+  |
|  |  |  |
|  +--+  |
|        |
+--------+'''
test_data_6 = '''+------------+
|            |
|            |
|            |
+------+-----+
|      |     |
|      |     |
+------+-----+'''

test_data_ex = [
    ('Description example',
     [(
         '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+',
         ['+-----+\n|     |\n|     |\n+-----+', '+------+\n|      |\n|      |\n+------+',
          '+------------+\n|            |\n|            |\n|            |\n+------------+'])]),
    ('Simple shapes',
     [(
         '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  |\n|  |                   |\n|  |                   |\n+--+-------------------+',
         [
             '                 +--+\n                 |  |\n                 |  |\n+----------------+  |\n|                   |\n|                   |\n+-------------------+',
             '+-------------------+\n|                   |\n|                   |\n|  +----------------+\n|  |\n|  |\n+--+']),
         (
             '\n           +-+             \n           | |             \n         +-+-+-+           \n         |     |           \n      +--+-----+--+        \n      |           |        \n   +--+-----------+--+     \n   |                 |     \n   +-----------------+     ',
             ['+-+\n| |\n+-+', '+-----+\n|     |\n+-----+', '+-----------+\n|           |\n+-----------+',
              '+-----------------+\n|                 |\n+-----------------+']),
         ('\n+---+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+',
          ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+',
           '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+']),
         (
             '\n+---+------------+---+\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n|   |            |   |\n|   |            |   |\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n+---+------------+---+',
             ['+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+', '+---+\n|   |\n+---+',
              '+---+\n|   |\n|   |\n|   |\n|   |\n+---+', '+---+\n|   |\n|   |\n|   |\n|   |\n+---+',
              '+------------+\n|            |\n+------------+', '+------------+\n|            |\n+------------+',
              '+------------+\n|            |\n|            |\n|            |\n|            |\n+------------+']),
         (
             '\n                 \n   +-----+       \n   |     |       \n   |     |       \n   +-----+-----+ \n         |     | \n         |     | \n         +-----+ ',
             ['+-----+\n|     |\n|     |\n+-----+', '+-----+\n|     |\n|     |\n+-----+']),
     ]),
    ('Nested pieces',
     [('\n+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+',
       ['+--+\n|  |\n+--+', '+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+'])]),
    ('Convoluted borders',
     [(
         '\n+-------+ +----------+\n|       | |          |\n| +-+ +-+ +-+    +-+ |\n+-+ | |     |  +-+ +-+\n    | +-----+--+\n+-+ |          +-+ +-+\n| +-+  +----+    | | |\n| |    |    |    +-+ |\n| +----++ +-+        |\n|       | |          |\n+-------+ +----------+',
         ['+-+\n| |\n| |\n| +-----+\n|       |\n+-------+',
          '+-------+\n|       |\n| +-+ +-+\n+-+ | |\n    | +--------+\n    |          +-+ +-+\n  +-+  +----+    | | |\n  |    |    |    +-+ |\n  +----+  +-+        |\n          |          |\n          +----------+',
          '+----------+\n|          |\n+-+    +-+ |\n  |  +-+ +-+\n  +--+'])]),
    ('edo_red97\'s big shape',
     [(
         '\n         +------------+--+      +--+\n         |            |  |      |  |\n         | +-------+  |  |      |  |\n         | |       |  |  +------+  |\n         | |       |  |            |\n         | |       |  |    +-------+\n         | +-------+  |    |        \n +-------+            |    |        \n |       |            |    +-------+\n |       |            |            |\n +-------+            |            |\n         |            |            |\n    +----+---+--+-----+------------+\n    |    |   |  |     |            |\n    |    |   |  +-----+------------+\n    |    |   |                     |\n    +----+---+---------------------+\n    |    |                         |\n    |    | +----+                  |\n+---+    | |    |     +------------+\n|        | |    |     |             \n+--------+-+    +-----+             ',
         ['    +----+\n    |    |\n    |    |\n+---+    |\n|        |\n+--------+',
          '+--+\n|  |\n|  +------------------+\n|                     |\n+---------------------+',
          '+--+      +--+\n|  |      |  |\n|  |      |  |\n|  +------+  |\n|            |\n|    +-------+\n|    |\n|    |\n|    +-------+\n|            |\n|            |\n|            |\n+------------+',
          '+---+\n|   |\n|   |\n|   |\n+---+', '+----+\n|    |\n|    |\n|    |\n+----+', '+-----+\n|     |\n+-----+',
          '+-------+\n|       |\n|       |\n+-------+', '+-------+\n|       |\n|       |\n|       |\n+-------+',
          '+------------+\n|            |\n+------------+',
          '+------------+\n|            |\n| +-------+  |\n| |       |  |\n| |       |  |\n| |       |  |\n| +-------+  |\n|            |\n|            |\n|            |\n|            |\n|            |\n+------------+',
          '+-------------------------+\n|                         |\n| +----+                  |\n| |    |     +------------+\n| |    |     |\n+-+    +-----+'])]),
    ('My tests',
     [(
         '+----------+',
         [])]
     ),
]
break_pieces(test_data_6)

# for task in test_data_ex:
#     print(task[0])
#     for task2 in task[1]:
#         res = sorted(break_pieces2(task2[0]))
#         expected = task2[1]
#         print(res, expected, sep='\n')
#         if res == task2[1]:
#             print('\n Nice!!\n')

# for task in test_data_ex:
#     print(task[0])
#     for task2 in task[1]:
#         res = sorted(break_pieces(task2[0]))
#         expected = task2[1]
#         print(res, expected, sep='\n')
#         if res == task2[1]:
#             print('Nice!!')
#         else:
#             print('Wrong!')
