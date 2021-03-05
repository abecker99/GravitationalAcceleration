import math

class particle:
    def _int_(self,x,y,z,m):
        self.x = x
        self.y = y
        self.z = z
        self.m = m
particles= []
file = open("particleSmall.txt", "r")
for line in file:
    x, y, z, m = line.split(" ")
    p = particle()
    p.x = float(x)
    p.y = float(y)
    p.z = float(z)
    p.m = float(m)
    particles.append(p)

pos_x = float((input("What is the x position?: ")))
pos_y = float((input("What is the y position?: ")))
pos_z = float((input("What is the z position?: ")))
pos = [pos_x, pos_y, pos_z]
h = 1e-6

def gravPotential(pos, particles):
    phi = 0.0
    G = 6.674e-11
    for p in particles:
        r = math.sqrt((p.x - pos_x)**2 + (p.y - pos_y)**2 + (p.z - pos_z)**2)
        phi += -G*p.m/r
    return phi

def centralDifferenceGrav3DX(f, position, h, i, particles):
    x_1 = [0, 0, 0]
    x_2 = [0, 0, 0]
    for j in range (0, 3):
        x_1[j] = position[j]
        if (j == i):
            x_1[j] -= h/2
    for j in range (0, 3):
        x_2[j] = position[j]
        if (j == i):
            x_2[j] += h/2
    return (f(x_2, particles) - f(x_1, particles))/h

def centralDifferenceGrav3DY(f, position, h, i, particles):
    y_1 = [0, 0, 0]
    y_2 = [0, 0, 0]
    for j in range (0, 3):
        y_1[j] = position[j]
        if (j == i):
            y_1[j] -= h/2
    for j in range (0, 3):
        y_2[j] = position[j]
        if (j == i):
            y_2[j] += h/2
    return (f(y_2, particles) - f(y_1, particles))/h

def centralDifferenceGrav3DZ(f, position, h, i, particles):
    z_1 = [0, 0, 0]
    z_2 = [0, 0, 0]
    for j in range (0, 3):
        z_1[j] = position[j]
        if (j == i):
            z_1[j] -= h/2
    for j in range (0, 3):
        z_2[j] = position[j]
        if (j == i):
            z_2[j] += h/2
    return (f(z_2, particles) - f(z_1, particles))/h

dx = centralDifferenceGrav3DX(gravPotential, pos, h, 0, particles)
dy = centralDifferenceGrav3DY(gravPotential, pos, h, 1, particles)
dz = centralDifferenceGrav3DZ(gravPotential, pos, h, 2, particles)

Gradient = [dx, dy, dz]

def TotalMass(m, particles):
    Masstotal = 0
    for p in particles:
        Masstotal += int(float(m))
    return Masstotal

#F = ma
#for i in range (0,2):
#    Gradient = [dx, dy, dz]
#    if (i == 0):
#        ax = dx/TotalMass
#    if (i == 1):
#        ay = dy/TotalMass
#    if (i == 2):
#        az = dz/TotalMass
#Acceleration = [ax, ay, az]


print(Gradient)
#print(Acceleration)