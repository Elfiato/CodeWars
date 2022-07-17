'''
https://www.codewars.com/kata/527fde8d24b9309d9b000c4e
'''

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
            if current_pos[0] < len(field) and current_pos[1] < len(field[0]):
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
    while not is_start_node:
        current_node, parent = que.popleft()
        parents[current_node] = parent
        visited.append(current_node)
        for el in graph[current_node]:
            if el != parent:
                if el in visited:
                    is_start_node = True
                    end_node = el, current_node
                    break
                que.append((el, current_node))

    figure = [end_node[0]]
    f_parent = parents[end_node[0]]
    s_parent = end_node[1]
    for _ in range(2):
        while f_parent is not None:
            figure.append(f_parent)
            f_parent = parents[figure[-1]]
        if s_parent not in figure:
            figure.append(s_parent)
            f_parent = parents[figure[-1]]
    del figure[-1]
    return set(figure)


def find_figure2(graph, start_node):
    que = deque([(start_node, None)])
    parents = {}
    is_start_node = False
    while not is_start_node:
        current_node, parent = que.popleft()
        parents[current_node] = [parent]
        try:
            if parents[parent] != [None]:
                parents[current_node].extend(parents[parent])
        except KeyError:
            pass
        for el in graph[current_node]:
            if el != parent:
                que.append((el, current_node))
                if el == start_node:
                    is_start_node = True
                    end_node = current_node

    res = parents[end_node].copy() + [end_node]
    print(res)
    return set(res)


def filter_figure_point(figure):
    res = []
    hor_up, hor_low = False, False
    vert_up, vert_low = False, False
    for el1 in figure:
        for el2 in figure:
            if el1[0] == el2[0]:
                if el2[1] > el1[1]:
                    hor_up = el2
                else:
                    hor_low = el2
            if el1[1] == el2[1]:
                if el2[0] > el1[0]:
                    vert_up = el2
                else:
                    vert_low = el2
        if not (hor_up and hor_low or vert_up and vert_low):
            res.append(el1)
    return res


def find_max_min_cord(cords):
    mx_Y = cords[0][0]
    mn_Y = cords[0][0]
    mx_X = cords[0][1]
    mn_X = cords[0][1]
    for c in cords:
        if c[0] > mx_Y:
            mx_Y = c[0]
        if c[0] < mn_Y:
            mn_Y = c[0]
        if c[1] > mx_X:
            mx_X = c[1]
        if c[1] < mn_X:
            mn_X = c[1]
    return mx_Y, mn_Y, mx_X, mn_X


def draw_figure(all_figures):
    is_angle_flag = False
    result_figures = []

    for figure in all_figures:
        current_figure = sorted(figure)
        field_borders = find_max_min_cord(current_figure)
        print(current_figure)
        result_figures.append([])
        is_put_el = False
        for i in range(field_borders[0] - field_borders[1] + 1):
            result_figures[-1].append('')
            for j in range(field_borders[2] - field_borders[3] + 1):
                for point in current_figure:
                    if i == point[0] - field_borders[1] and j == point[1] - field_borders[3]:
                        is_angle_flag = True
                        break
                if is_angle_flag:
                    result_figures[-1][-1] += '+'
                    is_angle_flag = False
                    continue
                try:
                    if result_figures[-1][-1][-1] in '+-':
                        result_figures[-1][-1] += '-'
                        is_put_el = True
                except IndexError:
                    pass
                try:
                    if result_figures[-1][-2][j] in '+|':
                        result_figures[-1][-1] += '|'
                        is_put_el = True
                except IndexError:
                    pass
                try:
                    if result_figures[-1][-1][-2] == '+' or result_figures[-1][-2][j] == '+':
                        if (result_figures[-1][-1][-3] == '-' and result_figures[-1][-1][-1] == '-') or (
                                result_figures[-1][-3][j] == '|' and result_figures[-1][-1][-1] == '|'):
                            result_figures[-1][-1] = result_figures[-1][-1][:-1] + ' '
                except IndexError:
                    pass
                if not is_put_el:
                    result_figures[-1][-1] += ' '
                    continue
                is_put_el = False
    for i in result_figures:
        print('\n'.join(i))


def draw_figure2(all_figures, field):
    result_figures = []

    for figure in all_figures:
        current_figure = sorted(figure)
        field_borders = find_max_min_cord(current_figure)  # (max_Y, min_Y, max_X, min_X)
        y_b, x_b = (field_borders[0] - field_borders[1] + 1), (field_borders[2] - field_borders[3] + 1)
        mn_y, mn_x = field_borders[1], field_borders[3]
        is_angle_flag, is_put_el = False, False
        result_figures.append([])
        for i in range(y_b):
            result_figures[-1].append('')
            for j in range(x_b):
                for point in current_figure:
                    if i == point[0] - mn_y and j == point[1] - mn_x:
                        is_angle_flag = True
                        break
                if is_angle_flag:
                    result_figures[-1][-1] += '+'
                    is_angle_flag = False
                    continue
                try:
                    if result_figures[-1][-1][-1] in '-':
                        result_figures[-1][-1] += '-'
                        is_put_el = True
                except IndexError:
                    pass
                try:
                    if result_figures[-1][-2][j] in '|':
                        result_figures[-1][-1] += '|'
                        is_put_el = True
                except IndexError:
                    pass
                if not is_put_el:
                    result_figures[-1][-1] += ' '
                    continue
                is_put_el = False
    for i in result_figures:
        print('\n'.join(i))


def break_pieces(shape):
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

    figures = []
    for node in graph:
        figure = find_figure2(graph, node)
        if figure not in figures:
            figures.append(figure)
    draw_figure(figures)


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
break_pieces(test_data_2)
