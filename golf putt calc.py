import math

# starting parameters
mu = 0.1    # coefficient of friction
g = 9.8     # accel due to gravity (m/s^2)
t_f = 10    # stop time (s)
t = 0       # start time
dt = 0.001  # time interval for calculations
p_t = 1     # interval to print results
s0 = [-5,0] # starting position (m)
v0 = [1,1]  # starting velocity (m/s)
s = s0      # current position
v = v0      # current velocity


# example of a function with a 3D surface; f(x,y) returns height at (x,y)
def function(x,y):
    return 0.5*(math.sin(0.5*x))*(math.sin(0.5*y))
# ∂f/∂x at (x,y)
def partial_x(x,y):
    return 0.25*(math.cos(0.5*x))*(math.sin(0.5*y))
# ∂f/∂y at (x,y)
def partial_y(x,y):
    return 0.25*(math.sin(0.5*x))*(math.cos(0.5*y))
# gradient of function at (x,y)
def gradient(x,y):
    return [partial_x(x,y), partial_y(x,y)]
# angle of the gradient
def theta(x,y):
    return [math.atan(gradient(x,y)[0]), math.atan(gradient(x,y)[1])]
# magnitude of 2D vector
def magnitude(a,b):
    return math.sqrt(a**2+b**2)
# calculate acceleration due to gravity
def accel(s,v,g,mu):
    if v[0] != 0 or v[1] != 0:
        a_x = (-g*math.sin(theta(s[0],s[1])[0])*math.cos(theta(s[0],s[1])[0])
        -mu*g*math.cos(theta(s[0],s[1])[0])*(v[0]/magnitude(v[0],v[1])))
        a_y = (-g*math.sin(theta(s[0],s[1])[1])*math.cos(theta(s[0],s[1])[1])
        -mu*g*math.cos(theta(s[0],s[1])[1])*(v[1]/magnitude(v[0],v[1])))
    else:
        if (abs(-g*math.sin(theta(s[0],s[1])[0])*math.cos(theta(s[0],s[1])[0])) >
            abs(mu*g*math.cos(theta(s[0],s[1])[0]))):
                a_x = (-g*math.sin(theta(s[0],s[1])[0])*math.cos(theta(s[0],s[1])[0])
                       -mu*g*math.cos(theta(s[0],s[1])[0]))            
        else:
            a_x = 0
        if (abs(-g*math.sin(theta(s[0],s[1])[1])*math.cos(theta(s[0],s[1])[1])) >
            abs(mu*g*math.cos(theta(s[0],s[1])[1]))):
                a_y = (-g*math.sin(theta(s[0],s[1])[1])*math.cos(theta(s[0],s[1])[1])
                       -mu*g*math.cos(theta(s[0],s[1])[1]))            
        else:
            a_y = 0
    return [a_x, a_y]
a = accel # abbreviation

# calculation of ball's position, speed, velocity using Euler's method
# prints: time, position, velocity, and acceleration at time t
print(t, list(map(lambda x: round(x, 4),s)),
          list(map(lambda x: round(x, 4),v)),
          list(map(lambda x: round(x, 4),a(s,v,g,mu))))
while t < t_f:
    t += dt
    a_t = a(s,v,g,mu)
    s[0] += v[0]*dt
    s[1] += v[1]*dt
    v[0] += a_t[0]*dt
    v[1] += a_t[1]*dt
    if round(t,3) % p_t == 0:
        print(round(t,3), list(map(lambda x: round(x, 4),s)),
                list(map(lambda x: round(x, 4),v)),
                list(map(lambda x: round(x, 4),a(s,v,g,mu))))
    

