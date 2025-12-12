import random
import time
import turtle


# Functions
def go_left():
    x_coord = hero.xcor()
    x_coord = x_coord - 20
    if x_coord < -380:
        x_coord = -380
    hero.setx(x_coord)


def go_right():
    x_coord = hero.xcor()
    x_coord = x_coord + 20
    if x_coord > 380:
        x_coord = 380
    hero.setx(x_coord)


# Screen Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightgray")
screen.title("Space Defenders")
screen.tracer(0)

# HERO Setup
hero = turtle.Turtle()
hero.shapesize(stretch_wid=3, stretch_len=3, outline=1)
hero.shape("triangle")
hero.color("cyan")
hero.up()
hero.goto(0, -250)
hero.seth(90)

# BULLET Setup
bullet = turtle.Turtle()
bullet.shape("classic")
bullet.color("black")
bullet.speed(0)
bullet.seth(90)
bullet.penup()
bullet.hideturtle()
bullet_speed = 25
bullet_state = "ready"


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(hero.xcor(), hero.ycor() + 10)
        bullet.showturtle()


pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.color("black")
pen.goto(0, 260)

score = 0
high_score = 0
pen.write(
    f"Score: 0 High Score: {high_score}", align="center", font=("Courier", 24, "normal")
)

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# VILLAIN Setup
enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.up()
enemy.goto(-200, 250)
enemy_speed = 2

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(fire_bullet, "space")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
    x_cord = enemy.xcor()
    x_cord += enemy_speed
    enemy.setx(x_cord)

    if x_cord > 280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
    if x_cord < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    if enemy.ycor() < -240:
        if score > high_score:
            high_score = score
            with open("highscore.txt", "w") as file:
                file.write(str(high_score))
        pen.goto(0, 0)
        pen.color("red")
        pen.write("GAME OVER", align="center", font=("Courier", 40, "bold"))
        game_is_on = False

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullet_state = "ready"
        if bullet.distance(enemy) < 25:
            score += 10
            pen.clear()
            pen.color("black")
            pen.goto(0, 260)
            pen.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Courier", 24, "normal"),
            )

            bullet.hideturtle()
            bullet_state = "ready"

            x_en = random.randint(-280, 280)
            y_en = 250
            enemy.goto(x_en, y_en)

            # Increase difficulty
            if enemy_speed > 0:
                enemy_speed += 0.2
            else:
                enemy_speed -= 0.2

screen.mainloop()
