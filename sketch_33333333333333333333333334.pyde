sizeEl =250

def setup():
       size(600,400)
       background(255)
       
def draw():
    clear()
    global sizeEl

    ellipse(50,300,100,100)
    sizeEl=sizeEl+1
