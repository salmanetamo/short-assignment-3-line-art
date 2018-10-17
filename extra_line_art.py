from aluLib import *

# Don't forget you must create an additional function. Go check out the instructions!

# Parameters that contain an x represent x coordinates, and y represent y coordinates
# Parameters with a 1 define the first line, parameters with a 2 define the second
# x1a and y1a define 1 point together, same for x2a and y2a etc.


def draw_line_art(x1a, y1a, x1b, y1b, x2a, y2a, x2b, y2b, line_count):
    set_stroke_color(1, 0, 0)

    draw_line(x1a, y1a, x1b, y1b)
    draw_line(x2a, y2a, x2b, y2b)

    # Get the lists of the coordinates needed to draw the intermediate lines
    line_1_x_coord_list = get_intermediate_values(x1a, x1b, line_count)
    line_2_x_coord_list = get_intermediate_values(x2a, x2b, line_count)
    line_1_y_coord_list = get_intermediate_values(y1a, y1b, line_count)
    line_2_y_coord_list = get_intermediate_values(y2a, y2b, line_count)

    # Get list of colors
    colors_list = get_intermediate_colors(line_count)
    reverse_index = line_count
    #Drawing the intermediate lines
    for i in range(line_count):
        set_stroke_color(colors_list[i][0], colors_list[i][1], colors_list[i][2])
        draw_line(line_1_x_coord_list[i], line_1_y_coord_list[i], line_2_x_coord_list[reverse_index],
                  line_2_y_coord_list[reverse_index])

        reverse_index -= 1


def get_intermediate_values(start_value, end_value, line_count):
    coordinates_list = []
    current_coord = start_value
    for i in range(line_count):
        coordinates_list.append(current_coord)
        current_coord += (end_value - start_value)/(line_count - 1)
    coordinates_list.append(end_value)

    return coordinates_list

# Get the colors for the intermediate lines
def get_intermediate_colors(line_count):
    colors_list = []
    red = 0
    green = 0
    blue = 1

    for i in range(line_count):
        colors_list.append([red, green, blue])
        red += 1 / line_count
        blue -= 1 / line_count

    return colors_list



def main():
    # Start some line art, the first 4 parameters represent the coordinates of 2 points, which define a line
    # The next 4 coordinates also represent 2 points, which define a second line
    # The final parameter represents how many partial lines are desired
    set_clear_color(0, 0, 0)
    clear()
    draw_line_art(350, 50, 20, 80, 350, 300, 40, 220, 50)

start_graphics(main)