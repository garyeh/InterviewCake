# Making Change

# my_rect = {
# 'left_x' : 1,
# 'bottom_y' : 5,
# 'width' : 10,
# 'height' : 4
# }

def rect_intersection(rect1, rect2):
    highest_left_x = max(rect_1['left_x'], rect_2['left_x'])
    lowest_right_x = min(rect_1['left_x'] + rect_1['width'], rect_2['left_x'] + rect_2['width'])
    highest_bottom_y = max(rect_1['bottom_y'], rect_2['bottom_y'])
    lowest_top_y = min(rect_1['bottom_y'] + rect_1['height'], rect_2['bottom_y'] + rect_2['height'])

    if highest_left_x >= lowest_right_x or highest_bottom_y >= lowest_top_y:
        return None

    # We know at this point intersection starts at highest_left_x and highest_bottom_y

    return {
        'left_x': highest_left_x,
        'right_x': highest_bottom_y,
        'width': lowest_right_x - highest_left_x,
        'height': lowest_top_y - highest_bottom_y
    }
