import turtle as t
#print begin barcode 
def print_start():
    t.up()
    t.setpos(-250,0)
    t.down()
    t.left(90)
    t.speed(5)
    t.forward(20)
    t.backward(20)
    t.right(90)
#print end of barcode
def print_end():
    t.up()
    t.forward(10)
    t.down()
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.exitonclick()


def print_zero():
    #t.speed(5)
    t.up()
    t.forward(10)
    t.down()
    t.left(90)
    t.forward(10)
    t.backward(10)
    t.right(90)


def print_one():
    #t.speed(5)
    t.up()
    t.forward(10)
    t.down()
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.right(90)



