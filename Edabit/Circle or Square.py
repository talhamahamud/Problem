def circle_or_square(var1, var2):
    cir=2*var1*3.14
    sq=((var2)**(0.5))*4

    if cir>sq:
        print(True)
    else:
        print(False)

circle_or_square(5, 100)