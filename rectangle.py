class point:
    def __init__(self,x,y) -> None:
        pass
        self.x = x
        self.y = y
    def __str__(self) -> str:
        pass
        return f'{self.x},{self.y}'
class rectangle:
    def __init__(self,pos,w,h):
        self.corner = pos
        self.width = w
        self.height = h        
    def __str__(self):
            return f'{self.corner},{self.width},{self.height}'

def createrectangle(x,y,width,height):
    return rectangle(point(x,y),width,height)

def strrectangle(rec):
    return str(rec)

def shiftrectangle(rec,dx,dy):
    ix,iy = rec.corner.x,rec.corner.y
    rec.corner.x = ix+dx
    rec.corner.y = iy+dy

def offsetrectangle(rec,dx,dy):
    ix,iy = rec.corner.x,rec.corner.y
    return createrectangle(ix+dx,iy+dy,rec.width,rec.height)

r1 = createrectangle(10,20,30,40)
print(strrectangle(r1))
shiftrectangle(r1,-10,-20)
print(strrectangle(r1))
r2 = offsetrectangle(r1,100,100)
print(strrectangle(r1))
print(strrectangle(r2))
