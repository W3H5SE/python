import math
import dudraw
import random
#The class that I use for the particle's math
class Vector:
    def __init__(self, some_x=0, some_y=0):
        self.x = some_x
        self.y = some_y
    def limit(self, l):
        if(self.length() >= l):
            self.resize(l)
    def resize(self, l):
        length = math.sqrt(self.x ** 2 + self.y**2)
        self.x *= (l/length)
        self.y *= (l/length)
    def __add__(self, other_vector)->None:
        return Vector(self.x+other_vector.x, self.y + other_vector.y)
    def __sub__(self, other_vector)->None:
        return Vector(self.x-other_vector.x, self.y - other_vector.y)
    def __isub__(self, other_vector)->None:
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self
    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self
    def divide(self, s):
        self.x /= s
        self.y /= s
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def angle_in_radians(self):
        return math.tan((self.y/self.x))
#Didnt even use this
class Time:
    frame = 0
    def tick():
        Time.frame += 1
    def time():
        return Time.frame
#The parent class of all the other paricle classes.   
class Particle(Vector):
    def __init__(self,pos_x,pos_y,x_vel,y_vel, size, lifetime,red=0,blue=153):
        Vector.__init__(self,some_x=0, some_y=0)
        #red and blue are used to make my fire look nicer
        self.red=red
        self.blue=blue
        self.pos=Vector(pos_x,pos_y)
        self.vel=Vector(x_vel,y_vel)
        self.size=size
        self.color=dudraw.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.lifetime=lifetime
    #Checks to see if the particle should    
    def has_expired(self):
        if self.lifetime<=0:
            return True
        else:
            return False
    def move(self):
        if not self.has_expired():
            self.pos+=self.vel
            self.lifetime-=1
#will be used for fireworks and marbles
class accelerating_particle(Particle):
    def __init__(self,pos_x,pos_y,x_vel,y_vel,x_acc,y_acc,size, lifetime):
        self.acc=Vector(x_acc,y_acc)
        Particle.__init__(self,pos_x,pos_y,x_vel,y_vel,size, lifetime)
    def move(self):
        if not self.has_expired():
            self.pos+=self.vel+Vector(self.acc.x,self.acc.y)
class firework_particle(accelerating_particle):
    def __init__(self,pos_x,pos_y,x_vel,y_vel,x_acc,y_acc,size, lifetime):
        accelerating_particle.__init__(self,pos_x,pos_y,x_vel,y_vel,x_acc, y_acc,size, lifetime)
    def draw(self):
        #I just draw the square and choose a random color 
        dudraw.set_pen_color(self.color)
        dudraw.filled_square(self.pos.x,self.pos.y,self.size)
        self.lifetime-=1
class marble_particle(accelerating_particle):
    #I just draw a circle
    def __init__(self,pos_x,pos_y,x_vel,y_vel,x_acc,y_acc,size, lifetime):
        accelerating_particle.__init__(self,pos_x,pos_y,x_vel,y_vel,x_acc, y_acc,size, lifetime)
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.pos.x,self.pos.y,self.size)
        self.lifetime-=1
class spark_particle(Particle):
    def __init__(self,pos_x,pos_y,x_vel,y_vel, size, lifetime):
        Particle.__init__(self,pos_x,pos_y,x_vel,y_vel, size, lifetime)
        self.color = dudraw.Color(204,0,102)
    def draw(self):
        self.color
        dudraw.line(self.pos.x,self.pos.y,self.pos.x+self.vel.x,self.pos.y+self.vel.y)
class fire_particle(Particle):
    def __init__(self,pos_x,pos_y,x_vel,y_vel, size, lifetime,red=230,blue=153):
        Particle.__init__(self,pos_x,pos_y,x_vel,y_vel, size, lifetime)
        self.red=red
        self.blue=blue
    def draw(self):
        if not self.has_expired():
            dudraw.set_pen_color_rgb(self.red,0,self.blue)
            dudraw.filled_circle(self.pos.x,self.pos.y,self.size)
            #I make it go from pink to dark red using the math below
            if self.red-3>=77:
               self.red-=3
            if self.blue-3>=25:
                self.blue-=3
    def move(self):
        Particle.move(self)
        #I make the fire smaller each time
        self.size-=0.001
        self.lifetime-=1
#This is used to animate the lists           
class ParticleContainer(Particle):
    def __init__(self, x_pos, y_pos,particles=None):
        if particles==None:
            particles=[]
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.pos=Vector(x_pos, y_pos)
        self.particles=particles
    #How I animate everything
    def animate(self):
        if len(self.particles)>0:
            for particle in self.particles:
                if particle.has_expired():
                    self.particles.remove(particle)
                else:
                    particle.draw()
                    particle.move()
#This classed is used for fire and sparkler                  
class Emitter(ParticleContainer):
    def __init__(self,x_pos,y_pos,fire_rate):
        ParticleContainer.__init__(self,x_pos,y_pos)
        self.fire_rate=fire_rate
#Sparkler class       
class Sparkler(Emitter):
    def __init__(self, x_pos, y_pos, fire_rate):
        Emitter.__init__(self,x_pos, y_pos, fire_rate)
    def animate(self):
        ParticleContainer.animate(self)
        for i in range(self.fire_rate):
            #Each frame I append a sparkle particle to the particle container
            self.particles.append(spark_particle(self.x_pos,self.y_pos, x_vel=random.uniform(-0.07,0.07),y_vel=random.uniform(-0.07,0.07),size=0.04,lifetime=5))
#Fire's class
class Fire(Emitter):
    def __init__(self, x_pos, y_pos, fire_rate):
        Emitter.__init__(self,x_pos, y_pos, fire_rate)
    def animate(self):
        ParticleContainer.animate(self)
        for i in range(self.fire_rate):
            x_pos=self.x_pos
            y_pos=self.y_pos
            x_vel=random.uniform(-0.002,0.002)
            y_vel=random.uniform(0.002,0.005)
            size=random.uniform(0.01,0.03)
            lifetime=50
            #Each frame I append a sparkle particle to the particle container
            self.particles.append(fire_particle(x_pos,y_pos,x_vel,y_vel,size,lifetime))
#Firework class
class Firework(ParticleContainer):
    def __init__(self, x_pos, y_pos):
        ParticleContainer.__init__(self, x_pos, y_pos)
        ParticleContainer.animate(self)
        #Everytime Firework is called a 1000 firework particles are appended
        for particle in range(1000):
            x_pos=self.x_pos
            y_pos=self.y_pos
            x_vel=random.uniform(-0.04,0.04)
            y_vel=random.uniform(-0.04,0.04)
            x_acc=0
            #This makes it fall realistically
            y_acc=random.uniform(-0.008,-0.012)
            size=0.002
            lifetime=50
            self.particles.append(firework_particle(x_pos,y_pos,x_vel,y_vel,x_acc,y_acc,size,lifetime))
#Marble class
class Marbles(ParticleContainer):
    def __init__(self, x_pos, y_pos):
        ParticleContainer.__init__(self, x_pos, y_pos)
        #I add 10 marbles everytime it's called
        for particle in range(10):
            x_pos=random.uniform(0.05,0.95)
            y_pos=random.uniform(0.05,0.95)
            x_vel=random.uniform(-0.04,0.04)
            y_vel=random.uniform(-0.04,0.04)
            x_acc=0
            #This simulates gravity
            y_acc=random.uniform(-0.001,-0.002)
            size=0.05
            lifetime=500
            self.particles.append(marble_particle(x_pos,y_pos,x_vel,y_vel,x_acc,y_acc,size,lifetime))
    #Math is right but I didn't use it
    def intersect(self,circle_a,circle_b):
        if (circle_a.vel-circle_b.vel).length()<=circle_a.size+circle_b.size:
            pass
            # accel=circle_a.vel+circle_b.vel
            # circle_a.vel+=accel
            # circle_b.vel-=accel
    def animate(self):
        ParticleContainer.animate(self)
        #This is how collision is detected and handled
        for a in range(len(self.particles)):
            b=self.particles[a]
            for c in range(a+1,len(self.particles)):
                e=self.particles[c]
                f=b.pos-e.pos
                if f.length()<=b.size+e.size:
                   b_direction=f+b.vel
                   e_direction=e.vel+f
                   #This limits the speed of the marbles
                   b_direction.limit(0.02)
                   e_direction.limit(0.02)
                   b.vel=b_direction
                   e.direction=e_direction
        #This is how I get them to bounce off the walls
        for e in self.particles:
            if e.pos.x>1-e.size:
                e.vel.x*=-1
            if e.pos.x<e.size:
                e.vel.x*=-1
            if e.pos.y>1-e.size:
                e.vel.y*=-1
            if e.pos.y<e.size:
                e.vel.y*=-1
test=[]
test.append(Fire(0.5,0.5,50))
test.append(Marbles(0.5,0.5))
test.append(Sparkler(0.75,0.75,50))
key=''
#How i get the code to run
while key!='q':
    dudraw.clear_rgb(55,55,55)
    if dudraw.has_next_key_typed():
        key=dudraw.next_key_typed()
    for particle in test:
        particle.animate()
    dudraw.show(40)
    if key=='f':
        test.append(Firework(0.5,0.5))
        key=''