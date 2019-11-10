import pygame


def get_distance_between_circles(circle1_centre, circle2_centre):
    return (circle1_centre[0] - circle2_centre[0])**2 + (circle1_centre[0] - circle2_centre[1])**2


def is_collision(circle1_centre, circle2_centre, circle1_radius, circle2_radius):
    distance_between_circles = get_distance_between_circles(circle1_centre, circle2_centre)
    if distance_between_circles <= (circle1_radius + circle2_radius)**2:
        return True
    else:
        return False


if __name__ == '__main__':
    pygame.init()
    circle1_centre = (250, 250)
    circle2_centre = (0, 0)
    while True:
        # Test with two circles
        pass

