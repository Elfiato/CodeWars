def shortest_knight_path(p1, p2):
    start_pos, end_pos = (ord(p1[0]) - 96, int(p1[1])), (ord(p2[0]) - 96, int(p2[1]))
    visited = [start_pos]
    queue = [start_pos]
    node_dict = {}
    counter = 0
    current_layer_node_count = 1
    next_layer_node_count = 0
    layer_counter = 0
    while True:
        current_pos = queue.pop(0)
        node_dict[current_pos] = knight_move(current_pos)
        counter += 1
        old_queue_len = len(queue)

        if current_pos == end_pos:
            break

        for neighbor in node_dict[current_pos]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

        next_layer_node_count += len(queue) - old_queue_len
        if counter == current_layer_node_count:
            layer_counter += 1
            current_layer_node_count = next_layer_node_count
            next_layer_node_count = 0
            counter = 0

    return layer_counter


def knight_move(start_pos):
    result = []
    pre_result = [(start_pos[0] - 2, start_pos[1] + 1), (start_pos[0] - 1, start_pos[1] + 2),
                  (start_pos[0] + 1, start_pos[1] + 2), (start_pos[0] + 2, start_pos[1] + 1),
                  (start_pos[0] + 2, start_pos[1] - 1), (start_pos[0] + 1, start_pos[1] - 2),
                  (start_pos[0] - 1, start_pos[1] - 2), (start_pos[0] - 2, start_pos[1] - 1)]
    for pos in pre_result:
        if 0 < pos[0] < 9 and 0 < pos[1] < 9:
            result.append(pos)
    return result

print(shortest_knight_path('g2', 'a7'))