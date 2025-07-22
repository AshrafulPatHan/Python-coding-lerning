import turtle
import time

# টার্টল অবজেক্ট তৈরি
flower = turtle.Turtle()
flower.speed(10)
flower.color("red")

# ফুলের পাপড়ি আঁকা
for _ in range(36):
    for _ in range(2):
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(135)
    flower.right(10)

# ফুলের কেন্দ্র আঁকা
flower.color("yellow")
flower.begin_fill()
flower.circle(20)
flower.end_fill()

# অ্যানিমেশন যোগ করা
for _ in range(36):
    flower.right(10)
    time.sleep(0.1)

# প্রোগ্রাম শেষ করা
turtle.done()





