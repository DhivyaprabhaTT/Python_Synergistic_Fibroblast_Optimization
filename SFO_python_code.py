import random
import time
import numpy as np

#time1 = datetime.datetime.now().time()

time1 = int(round(time.time() * 1000))   # milliseconds convertion

print(time1)


# Step 1 - Initialization

# Declare the discrete number of cells

cell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(cell)

# Random generation of position

print('**********Position**************')
position = []
for x in range(11):

    x = random.random()

    t = round(x,4)

    position.append(t)

    print(position)

# Random generation of velocity

print('**********Velocity**************')
velocity = []
for y in range(11):

    y = random.random()

    t1 = round(y,4)

    velocity.append(t1);

    print(velocity)

# Random generation of extracellular matrix

ecm = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10];

print(ecm)

# Parameter initialization

speed = 0.15;
L = 10;
rho = 0.5;
kro = 1000;
r = 0;

# Step 2 - Fitness evaluation

# Iteration count

for outer in range(1,10000):

    optima = random.choice(ecm)

    print('**********optima************')
    print(optima)

    for inner in range(0,10):

        print('**********n************')
        n = random.choice(ecm)
        print(n)
        
        print('**********index************')
        a = ecm.index(n)
        print(a)
        
        print('**********position************')
        p1 = position[a]
        print(p1)
        
        print('**********velocity************')
        v1 = velocity[a]
        print(v1)

# Objective function - Sphere benchmark function

        fx = np.multiply(n,n)

        print(fx)
        
#Step 3 - Reorientation of cell

if(optima <= n):

    cbest = n        # Minimization problem

# Step 4 - Velocity and Position updating equation

    torque = int(round(time.time() * 1000))   # milliseconds convertion

    print(torque)

    lag = (torque - time1)

    s = (speed / kro * L)

    vel = v1 + ((1 - rho) * n )+ (rho * (n * (inner - lag)/lag));

    print('****************velocity precision***************')

    vtemp = round(vel,4)

    print(vtemp)

    print('****************position precision***************')

    pos = p1 + (speed * vtemp)

    print(pos)

# Remodeling of collagen deposition

    velocity[a] = vtemp

    position[a] = pos

else:
    cbest = optima

print('Global Optimal Solution')

print(optima)








