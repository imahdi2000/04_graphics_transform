from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

draw_line( 5, 5, 7, 8, screen, color )
pyt_test()
parse_file('script', edges, transform, screen, color )
