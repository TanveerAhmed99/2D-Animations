from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

class Raindrop:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.sliding = False
        self.slide_direction = 0  # -1 for left, 1 for right
        self.original_speed = speed

    def reset_position(self):
        self.x = random.uniform(0, 500)
        self.y = random.uniform(0, 800)
        self.sliding = False
        self.speed = self.original_speed

class RainSimulation:
    def __init__(self, width=500, height=500, num_raindrops=300):
        self.width = width
        self.height = height
        self.rain_direction = 0
        self.day = False
        self.raindrops = []
        
        # Initialize raindrops
        for _ in range(num_raindrops):
            x = random.uniform(0, width)
            y = random.uniform(0, height + 300)
            speed = random.uniform(2, 6)
            self.raindrops.append(Raindrop(x, y, speed))

    def check_roof_collision(self, x, y):
        # Left roof line: from (100,250) to (250,400)
        # Right roof line: from (250,400) to (400,250)
        if x >= 100 and x <= 400:
            if x <= 250:  # Left side of roof
                roof_y = 250 + (x - 100) * (150/150)
                return y <= roof_y, "left"
            else:  # Right side of roof
                roof_y = 400 - (x - 250) * (150/150)
                return y <= roof_y, "right"
        return False, None

    def update_raindrops(self):
        for drop in self.raindrops:
            if not drop.sliding:
                # Normal falling
                drop.x += self.rain_direction
                drop.y -= drop.speed
                
                # Check for collision with roof
                collision, side = self.check_roof_collision(drop.x, drop.y)
                if collision:
                    drop.sliding = True
                    drop.slide_direction = -1 if side == "left" else 1
                    drop.speed = drop.original_speed * 0.7
            else:
                # Sliding behavior
                if drop.slide_direction == -1:  # Sliding left
                    drop.x -= drop.speed
                    drop.y = 250 + (drop.x - 100) * (150/150)
                    if drop.x <= 100:  # Reached left edge
                        drop.sliding = False
                        drop.speed = drop.original_speed
                else:  # Sliding right
                    drop.x += drop.speed
                    drop.y = 400 - (drop.x - 250) * (150/150)
                    if drop.x >= 400:  # Reached right edge
                        drop.sliding = False
                        drop.speed = drop.original_speed
            
            # Reset if drop goes off screen
            if drop.y < 0 or drop.x < 0 or drop.x > self.width:
                drop.reset_position()

    def draw_line(self, x1, y1, x2, y2):
        glPointSize(5) 
        glLineWidth(3)
        glBegin(GL_LINES)
        glVertex2f(x1, y1) 
        glVertex2f(x2, y2)
        glEnd()

    def draw_square(self, x1, y1, x2, y2, x3, y3, x4, y4):
        glPointSize(5) 
        glLineWidth(3)
        glBegin(GL_QUADS)
        glVertex2f(x1, y1) 
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)
        glVertex2f(x4, y4)
        glEnd()

    def draw_house(self):
        # House outline
        self.draw_line(100, 250, 250, 400)  # Left roof
        self.draw_line(250, 400, 400, 250)  # Right roof
        self.draw_line(100, 250, 400, 250)  # Top of walls
        self.draw_line(110, 250, 390, 250)
        self.draw_line(110, 50, 390, 50)    # Bottom
        self.draw_line(110, 250, 110, 50)   # Left wall
        self.draw_line(390, 250, 390, 50)   # Right wall
        
        # Door
        self.draw_line(225, 150, 225, 50)
        self.draw_line(223, 150, 276, 150)
        self.draw_line(275, 150, 275, 50)
        
        # Windows
        self.draw_square(130, 200, 130, 150, 180, 150, 180, 200)
        self.draw_square(320, 200, 320, 150, 370, 150, 370, 200)
        
        # Doorknob
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(265, 100)
        glEnd()

    def draw_raindrops(self):
        for drop in self.raindrops:
            if self.day:
                glColor3f(0, 0, 1)
            else:
                glColor3f(1, 1, 1)
            
            if drop.sliding:
                # Draw angled raindrop when sliding
                angle = math.pi/4 if drop.slide_direction == 1 else 3*math.pi/4
                end_x = drop.x + 10 * math.cos(angle)
                end_y = drop.y + 10 * math.sin(angle)
                self.draw_line(drop.x, drop.y, end_x, end_y)
            else:
                # Draw vertical raindrop when falling
                self.draw_line(drop.x, drop.y, drop.x, drop.y+10)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Set up viewport and projection
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, self.width, 0.0, self.height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Set background color based on time of day
        if self.day:
            glClearColor(1, 1, 1, 1)
            glColor3f(0, 0, 0)
        else:
            glClearColor(0, 0, 0, 0)
            glColor3f(1, 1, 1)

        # Draw scene elements
        self.draw_house()
        self.update_raindrops()
        self.draw_raindrops()
        
        glutSwapBuffers()

    def render_timer(self, value):
        glutPostRedisplay()
        glutTimerFunc(16, self.render_timer, 0)

    def handle_special_keys(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.rain_direction += 1
        elif key == GLUT_KEY_LEFT:
            self.rain_direction -= 1

    def handle_keyboard(self, key, x, y):
        if key == b"d":
            self.day = True
        elif key == b"n":
            self.day = False

    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(b"Rain Simulation")
        
        # Register callbacks
        glutDisplayFunc(self.display)
        glutTimerFunc(0, self.render_timer, 0)
        glutSpecialFunc(self.handle_special_keys)
        glutKeyboardFunc(self.handle_keyboard)
        
        glutMainLoop()

# Create and run the simulation
simulation = RainSimulation(500, 500, 300)
simulation.run()
