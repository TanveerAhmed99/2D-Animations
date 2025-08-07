from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import random

# Constants
WIDTH, HEIGHT = 600, 500
POINT_SIZE = 5.0

# Global control variables
FREEZE = False
pointSpeed = 1.5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.random(), random.random(), random.random())
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        self.blink = False
        self.blink_time = 0
        self.blink_state = True

    def draw(self):
        if self.blink and not FREEZE:
            if time.time() - self.blink_time > 0.3:
                self.blink_state = not self.blink_state
                self.blink_time = time.time()
            glColor3fv(self.color if self.blink_state else (0, 0, 0))
        else:
            glColor3fv(self.color)

        glPointSize(POINT_SIZE)
        glBegin(GL_POINTS)
        glVertex2f(self.x, self.y)
        glEnd()

    def animate(self):
        if FREEZE:
            return

        self.x += self.direction_x * pointSpeed
        self.y += self.direction_y * pointSpeed

        if self.x < -WIDTH // 2 or self.x > WIDTH // 2:
            self.direction_x *= -1
        if self.y < -HEIGHT // 2 or self.y > HEIGHT // 2:
            self.direction_y *= -1

    def start_blinking(self):
        self.blink = True
        self.blink_time = time.time()

class App:
    def __init__(self):
        self.points = []

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-WIDTH // 2, WIDTH // 2, -HEIGHT // 2, HEIGHT // 2)

        for point in self.points:
            point.animate()
            point.draw()

        glutSwapBuffers()

    def mouse_click(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            for point in self.points:
                point.start_blinking()
            print("Blinking started")
        elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            gl_x = x - WIDTH // 2
            gl_y = HEIGHT // 2 - y
            self.points.append(Point(gl_x, gl_y))
            print(f"Point created at ({gl_x}, {gl_y})")

    def key_press(self, key, x, y):
        global FREEZE
        if key == b' ':
            FREEZE = not FREEZE
            print("Freeze!!" if FREEZE else "Unfreeze!!")

    def special_key(self, key, x, y):
        global pointSpeed
        if key == GLUT_KEY_UP:
            pointSpeed += 0.1
            print("Speed increased")
        elif key == GLUT_KEY_DOWN:
            pointSpeed = max(0.1, pointSpeed - 0.1)
            print("Speed decreased")



app = App()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Circle_Blinker")

glutDisplayFunc(app.display)
glutIdleFunc(glutPostRedisplay)
glutMouseFunc(app.mouse_click)
glutKeyboardFunc(app.key_press)
glutSpecialFunc(app.special_key)

glutMainLoop()



