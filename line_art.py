from aluLib import *

# Don't forget you must create an additional function. Go check out the instructions!

# Parameters that contain an x represent x coordinates, and y represent y coordinates
# Parameters with a 1 define the first line, parameters with a 2 define the second
# x1a and y1a define 1 point together, same for x2a and y2a etc.

def draw_line_art(x1a, y1a, x1b, y1b, x2a, y2a, x2b, y2b, line_count):
    set_stroke_color(0, 0, 0)
    draw_line(x1a, y1a, x1b, y1b)
    draw_line(x2a, y2a, x2b, y2b)


def main():
    # Start some line art, the first 4 parameters represent the coordinates of 2 points, which define a line
    # The next 4 coordinates also represent 2 points, which define a second line
    # The final parameter represents how many partial lines are desired
    draw_line_art(350, 50, 20, 80, 350, 300, 40, 220, 50)

start_graphics(main)