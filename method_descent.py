
from pylab import *

from matplotlib import cm
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#create 3d axes
fig = plt.figure()
ax = plt.axes(projection='3d')
#set title
ax.set_title('Градиентный спуск с постоянным шагом')

X = np.arange(-350, 350)
Y = np.arange(-350, 350)
X, Y = np.meshgrid(X, Y)
Z = 2 * X * X + X * Y + Y * Y
surf = ax.plot_surface(X, Y, Z, cmap=cm.summer,
                       linewidth=0, antialiased=False)


def fun(x):
    return 2 * x[0] * x[0] + x[0] * x[1] + x[1] * x[1]

#`x
def dx1(x):
    return 4 * x[0] + x[1]
#`y
def dx2(x):
    return x[0] + 2 * x[1]


def fun_text():
    return "f(x1,x2) = 2*(x1)^2 + x1*x2\n+ (x2)^2"

def delta_f(x):
    return [dx1(x),dx2(x)]

def norm( vector):
    res = 0
    for i in vector:
        res += i ** 2
    return np.sqrt(res)



e = 0.01
e1 = 0.1
e2 = 0.15
m = 100
k = 0
x2 = [0.5, 1]
x1 = x2
res = []

while True:
    if norm(delta_f(x2)) >= e1:
        if k < m:
            tk = 0.1
            x1 = list(x2)
            while True:
                x2 = np.array(x1) - np.array([i * tk for i in delta_f(x1)])
                if fun(x2) - fun(x1) < 0:
                    break
                else:
                    tk /= 2
            if norm(x2 - x1) < e2 and norm([fun(x2) - fun(x1)]) < e2:
                res = list(x2)
                break
            else:
                k += 1
        else:
            res = x2
            break
    else:
        res = x2
        break
res.append(fun(res))
print( "Координаты найденной точки\nминимума:\nx = "+str(round(res[0],3))+"\ny = "+str(round(res[1],3))+"\nz = "+str(round(res[2],3))+"\nКоличество итераций = "+str(k))
ax.scatter(res[0] , res[1] , res[2], color='black',s=80)

plt.show()
