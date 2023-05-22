import turtle
import datetime

# アナログ時計の描画
def draw_clock(hour, minute, second):
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=500, height=500)
    window.tracer(0)

    # 時計の外側の円を描画
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(3)
    pen.up()
    pen.goto(0, -200)
    pen.down()
    pen.circle(200)

    # 時針を描画
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.right(hour * 30 + minute * 0.5)
    pen.down()
    pen.pensize(4)
    pen.forward(100)

    # 分針を描画
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.right(minute * 6)
    pen.down()
    pen.pensize(3)
    pen.forward(180)

    # 秒針を描画
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.right(second * 6)
    pen.down()
    pen.pensize(2)

    # 前の秒針を消去
    pen.color("white")
    pen.backward(190)
    pen.color("black")

    pen.forward(190)

    window.update()

# 現在時刻の取得とアナログ時計の更新
def update_clock():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    draw_clock(hour, minute, second)
    turtle.ontimer(update_clock, 1000)

# メイン関数
def main():
    turtle.mode("logo")
    turtle.tracer(0)
    update_clock()
    turtle.done()

if __name__ == "__main__":
    main()
