from turtle import Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food
#screen setup
s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake")
s.tracer(0)

#creating snake object.This triggers the constructor i.e. def init which in turn
#triggers the create snake function.
snake=Snake()
food=Food()
score=ScoreBoard()

#moving the snake using keys
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")



#ensures game is running until game over
game_is_on=True
while game_is_on:

    s.update()
    time.sleep(0.1)
    #score.line_for_border()

    snake.move()

#detecting when the snake head collides with food
    if snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        snake.extend()

#detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() <-295 or snake.head.ycor() >270 or snake.head.ycor() <-290:
        score.reset_game()
        snake.reset_snake()
#detect collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            score.reset_game()
            snake.reset_snake()
s.exitonclick()