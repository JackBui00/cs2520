import turtle as t
def print_start():
    t.up()
    t.setpos(-250,0)
    t.down()
    t.left(90)
    t.speed(5)
    t.forward(20)
    t.backward(20)
    t.right(90)

def print_end():
    t.up()
    t.forward(10)
    t.down()
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.exitonclick()
    t.clear()
    t.reset()

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


def print_barcode(barcode):
    barcode = barcode.replace('-','')
    key =[[1,1,0,0,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0],[0,1,0,0,1],[0,1,0,1,0],[0,1,1,0,0],[1,0,0,0,1],[1,0,0,1,0],[1,0,1,0,0]]
    barcode_breakdown = []
    for integer in barcode:
        barcode_breakdown.append(int(integer))
    print(barcode_breakdown)
    print(sum(barcode_breakdown))
    sum_of_barcode = sum(barcode_breakdown)
    barcode_breakdown.append(10 - sum_of_barcode % 10)
    print(barcode_breakdown)
    print_start()
    for value in barcode_breakdown:
        for value_two in key[value]:
            if value_two == 0:
                print_zero()
            else:
                print_one()
    print_end()
