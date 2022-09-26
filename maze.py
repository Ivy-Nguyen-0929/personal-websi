import pygame
import time
import random

width = 500
height = 500
FPS = 30

white = (255, 255, 255)
black = (0, 0, 0)
purple = (75,0,130)
blue = (0, 0, 255)
green = (173,255,47)

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze generator trial 1")
clock = pygame.time.Clock()

# set up maze variables
x = 0
y = 0
w = 20  # width of the cell
grid = []
visited = []
stack = []
solution = {}


def build_grid(x, y, w):  # create a 20x20 grid
    for i in range(1, 21):
        x = 20
        y = y + 20
        for j in range(1, 21):
            pygame.draw.line(screen, white, [x, y], [x + w, y])
            pygame.draw.line(screen, white, [x + w, y], [x + w, y + w])
            pygame.draw.line(screen, white, [x + w, y + w], [x, y + w])
            pygame.draw.line(screen, white, [x, y], [x, y + w])
            grid.append((x, y))
            x = x + 20
            pygame.display.update()


def go_up(x, y):
    pygame.draw.rect(screen, purple, (x + 1, y - w + 1, 19, 39))
    pygame.display.update()


def go_down(x, y):
    pygame.draw.rect(screen, purple, (x+1, y+1, 19, 39))
    pygame.display.update()

def go_left(x, y):
    pygame.draw.rect(screen, purple, (x - w + 1, y + 1, 39, 19))
    pygame.display.update()

def go_right(x, y):
    pygame.draw.rect(screen, purple, (x + 1, y + 1, 39, 19))
    pygame.display.update()

def single_cell(x, y):  # draw a single width cell
    pygame.draw.rect(screen, white, (x + 1, y +1, 18, 18))
    pygame.display.update()


def backtrack_cell(x, y):  # use to recolor the path the single cell have visited
    pygame.draw.rect(screen, purple, (x +1, y+1, 18, 18))
    pygame.display.update()


def solution_cell(x, y):
    pygame.draw.rect(screen, green, (x + 8, y + 8, 5, 5))
    pygame.display.update()


def carve_maze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        time.sleep(0.03)
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("r")
        if (x - w, y) not in visited and (x - w, y) in grid:
            cell.append("l")
        if (x, y - w) not in visited and (x, y - w) in grid:
            cell.append("u")
        if (x, y + w) not in visited and (x, y + w) in grid:
            cell.append("d")

        if len(cell) > 0:
            cell_choose = (random.choice(cell))

            if cell_choose == "r":
                go_right(x, y)
                solution[(x + w, y)] = x, y
                x = x + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_choose == "l":
                go_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_choose == "u":
                go_up(x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_choose == "d":
                go_down(x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

        else:
            x, y = stack.pop()
            single_cell(x, y)
            time.sleep(0.05)
            backtrack_cell(x, y)


def plot_route_back(x,y):
    solution_cell(x,y)
    while (x,y) != (20,20):
        x,y = solution[x,y]
        solution_cell(x,y)
        time.sleep(0.1)


x, y = 20, 20
build_grid(40, 0, 20)
carve_maze(x, y)
plot_route_back(400,400)

running = True
while running:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

