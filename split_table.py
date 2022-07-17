'''
https://www.codewars.com/kata/527fde8d24b9309d9b000c4e
'''

from collections import deque
from math import inf


def find_all_one_figure_points(first_point, all_point):
    result = []
    visited = []
    horizontal_flag = True
    que = deque((first_point,))
    while que:
        current_point = que.popleft()
        if current_point not in visited:
            closest_point = find_closest_points(current_point, all_point)
            if horizontal_flag:
                nxt_point = closest_point[1]
            else:
                nxt_point = closest_point[0]
            result.append(nxt_point)
            que.append(nxt_point)
            visited.append(current_point)
            horizontal_flag = not horizontal_flag
    return result


def find_closest_points(first_point, all_point):
    mn_delta_x, mn_delta_y = inf, inf
    mn_x, mn_y = first_point, first_point
    for el in all_point:
        if el != first_point:
            if el[1] == first_point[1]:
                cur_mn_delta_y = abs(el[0] - first_point[0])
                if cur_mn_delta_y < mn_delta_y:
                    mn_delta_y = cur_mn_delta_y
                    mn_y = el
            if el[0] == first_point[0]:
                cur_mn_delta_x = abs(el[1] - first_point[1])
                if cur_mn_delta_x < mn_delta_x:
                    mn_delta_x = cur_mn_delta_x
                    mn_x = el
    return mn_y, mn_x


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


def draw_figure(all_figure):
    is_angle_flag = False
    result_figures = []

    for figure in all_figure:
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


def break_pieces(shape):
    shape_list = shape.split('\n')
    print(*shape_list, sep='\n')
    where_pluses = []
    for i in range(len(shape_list)):
        for j in range(len(shape_list[i])):
            if shape_list[i][j] == '+':
                where_pluses.append((i, j))
    all_figure = []
    for el in where_pluses:
        figure_points = set(find_all_one_figure_points(el, where_pluses))
        if figure_points not in all_figure:
            all_figure.append(figure_points)
    draw_figure(all_figure)


def print_test_data(test_data):
    if isinstance(test_data, str):
        print(test_data)
        return None
    for i in test_data:
        print_test_data(i)


test_data_1 = '\n+-------------------+--+\n|                   |  |\n|                   |  |\n|  +----------------+  ' \
              '|\n|  |                   |\n|  |                   |\n+--+-------------------+ '
test_data_2 = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|    ' \
              '  |     |\n+------+-----+ '
break_pieces(test_data_1)

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
             ['+-----+\n|     |\n|     |\n+-----+', '+-----+\n|     |\n|     |\n+-----+'])]),
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
          '+-------------------------+\n|                         |\n| +----+                  |\n| |    |     +------------+\n| |    |     |\n+-+    +-----+'])])]

print_test_data(test_data_ex)
