
from ursina import *
app = Ursina()

window.color = color.white

dino = Animation('assets\dino',
                 Collider='box',
                 x=-5)

ground1 = Entity(
    model='quad',
    texture= 'assets\ground',
    scale=(50,0.5,1),
    z=1
)

ground2 = duplicate(ground1,x=50)
pair = [ground1,ground2]

cactus = Entity(
    model= 'quad',
    texture= 'assets\cacti'
)

def update():
    for ground in pair:
        ground.x -= 6*time.dt
        if ground.x <-35:
            ground.x += 100
            
    
        
        
        
        
camera.orthographic = True
camera.fov = 10
app.run()