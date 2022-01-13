import colorgram as cg

colors = cg.extract("image.jpg", 30)
rgb_colors = []

for color in colors:
    rgb_colors.append(color.rgb)

print (rgb_colors)

def draw_random_dots_in_rectangle(origin, number_of_dots, size=RECTANGLE_SIZE):
    # loops number_of_dots times
    for _ in range(number_of_dots):
        # generate a random position inside of given rectangle
        # using min/max, because of possible negative coordinates
        # weakness - does also place dots on the edges of the rectangle
        rand_x = randint(min(origin[0], origin[0] + size[0]), max(origin[0], origin[0] + size[0]))
        rand_y = randint(min(origin[1], origin[1] + size[1]), max(origin[1], origin[1] + size[1]))
        # moves to the random position
        move_turtle_to((rand_x, rand_y))
        # creates a dot
        t.dot(DOT_DIAMETER)