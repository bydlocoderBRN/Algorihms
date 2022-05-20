import turtle


class MyTurtle:

    def __init__(self, moving_rules, speed, start_pos):
        self.moving_rules = moving_rules
        self.my_turtle = turtle
        self.my_turtle.clear()
        self.my_turtle.speed(speed)
        self.my_turtle.penup()
        self.my_turtle.setpos(start_pos)
        self.my_turtle.pendown()
        self.turtle_stack = []

    def __turtle_do(self, command, value):

        if command == "forward":
            self.my_turtle.forward(value)
        elif command == "backward":
            self.my_turtle.back(value)
        elif command == "right":
            self.my_turtle.right(value)
        elif command == "left":
            self.my_turtle.left(value)
        elif command == "save_pos":
            self.turtle_stack.append((self.my_turtle.xcor(), self.my_turtle.ycor(), self.my_turtle.heading()))
        elif command == "relocate":
            xcor, ycor, head = self.turtle_stack.pop()
            self.relocate_turtle((xcor, ycor, head))

    def start_turtle(self, commands_str):
        for move in commands_str:
            if move in self.moving_rules.keys():
                command = self.moving_rules.get(move).get("command")
                value = self.moving_rules.get(move).get("value")
                self.__turtle_do(command, value)
        # self.my_turtle.done()

    def relocate_turtle(self, my_tuple):
        self.my_turtle.up()
        self.my_turtle.goto(my_tuple[0], my_tuple[1])
        self.my_turtle.seth(my_tuple[2])
        self.my_turtle.down()


def l_system(axiom, rules, iterations):

    new_axiom = ""
    for i in range(iterations):

        for symb in axiom:
            if symb in rules.keys():
                new_axiom += rules.get(symb)

            else:
                new_axiom += symb

        axiom = new_axiom
        new_axiom=""

    return axiom


class FractalExplorer:
    def __init__(self, iterations=3):
        self.iterations = iterations
        self.axiom = ""
        self.rules = {}
        self.moving_rules = {}
        self.my_turtle = None

    def draw(self):
        moving_str = l_system(self.axiom, self.rules, self.iterations)

        self.my_turtle.start_turtle(moving_str)

    def select_koch(self):
        self.axiom = "F++F++F"
        self.rules = {"F": "F-F++F-F"}
        self.moving_rules = {
            "F": {"command": "forward", "value": 10},
            "B": {"command": "backward", "value": 10},
            "-": {"command": "right", "value": 60},
            "+": {"command": "left", "value": 60}
        }
        self.my_turtle = MyTurtle(moving_rules=self.moving_rules, speed=100, start_pos=(-300, -170))


    def select_serpinsky_triangle(self):
        self.axiom = "FXF--FF--FF"
        self.rules = {
            "F": "FF",
            "X": "--FXF++FXF++FXF--"
        }
        self.moving_rules = {
            "F": {"command": "forward", "value": 10},
            "-": {"command": "right", "value": 60},
            "+": {"command": "left", "value": 60}
        }
        self.my_turtle = MyTurtle(moving_rules=self.moving_rules, speed=100, start_pos=(-150, 100))

    def select_serpinsky_curve(self):
        self.axiom = "F+XF+F+XF"
        self.rules = {
            "X": "XF-F+F-XF+F+XF-F+F-X"
        }
        self.moving_rules = {
            "F": {"command": "forward", "value": 10},
            "-": {"command": "right", "value": 90},
            "+": {"command": "left", "value": 90}
        }
        self.my_turtle = MyTurtle(moving_rules=self.moving_rules, speed=100, start_pos=(-100, -250))

    def select_gilbert(self):
        self.axiom = "X"
        self.rules = {
            "X": "-YF+XFX+FY-",
            "Y": "+XF-YFY-FX+"
        }
        self.moving_rules = {
            "F": {"command": "forward", "value": 10},
            "-": {"command": "right", "value": 90},
            "+": {"command": "left", "value": 90}
        }
        self.my_turtle = MyTurtle(moving_rules=self.moving_rules, speed=100, start_pos=(0, 0))

    def select_pifagor_tree(self):
        self.axiom = "F[+X][-X]"
        self.rules = {
            "F": "FF",
            "X": "F[+F[+X][-X]][-F[+X][-X]]"
        }
        self.moving_rules = {
            "F": {"command": "forward", "value": 10},
            "-": {"command": "right", "value": 45},
            "+": {"command": "left", "value": 45},
            "[": {"command": "save_pos", "value": 90},
            "]": {"command": "relocate", "value": 90}
        }
        self.my_turtle = MyTurtle(moving_rules=self.moving_rules, speed=100, start_pos=(-150, 0))


def serpinsky_carpet(n, m):

    if n == 0:
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(m)
            turtle.left(90)
        turtle.end_fill()
    else:
        for _ in range(4):
            serpinsky_carpet(n - 1, m / 3)
            turtle.forward(m / 3)

            serpinsky_carpet(n - 1, m / 3)
            turtle.forward(m / 3)

            turtle.forward(m / 3)
            turtle.left(90)


fractal = FractalExplorer(4)
fractal.select_koch()
fractal.draw()
fractal.select_gilbert()
fractal.draw()
fractal.select_serpinsky_curve()
fractal.draw()
fractal.select_serpinsky_triangle()
fractal.draw()
fractal.select_pifagor_tree()
fractal.draw()

turtle.color = ("black")
turtle.speed(13)
turtle.pensize = 2
turtle.clear()
turtle.setpos((0, 0))
turtle.seth(0)
serpinsky_carpet(3, 200)


