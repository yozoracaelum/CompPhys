import matplotlib.pyplot as plt
import numpy as np


def menu_1():
    print('Gerak Peluru 2D')
    print('----------')
    print('Kondisi 1')
    print('1. Berhenti')
    print('2. Memantul')
    print('3. Periodik/Warp Around')
    print('----------')


def berhenti(i, x, y, vx, vy):
    x[i+1] = x[i]
    y[i+1] = 0
    vx[i+1] = 0
    vy[i+1] = 0
    return x, y, vx, vy


def memantul(i, c, x, y, vx, vy):
    x[i+1] = x[i+1]
    y[i+1] = -y[i+1]
    vx[i+1] = vx[i+1]
    vy[i+1] = -c*vy[i+1]
    return x, y, vx, vy


def periodik(i, lb, x):
    x[i+1] = x[i+1] - lb
    return x


def gerak2d_1(k):
    dt, ay = 0.0001, -9.8
    ta = float(input('Waktu awal (s): '))
    tb = float(input('Waktu akhir (s): '))
    v0 = 22
    theta = 25
    if k == 1:
        kondisi = 'Berhenti'
    elif k == 2:
        c = float(input('Koefisien redam (c): '))
        kondisi = 'Memantul'
    elif k == 3:
        lb = float(input('Batas kanan (m): '))
        kondisi = 'Periodik/Warp Around'
    rad = (np.pi/180)*theta
    Nstep = int((tb-ta)/dt)
    vx_0 = v0*np.cos(rad)
    vy_0 = v0*np.sin(rad)
    x = np.zeros(Nstep)
    vx = np.zeros(Nstep)
    vy = np.zeros(Nstep)
    vx[0] = vx_0
    vy[0] = vy_0
    y = np.zeros(Nstep)
    t = np.arange(ta, tb, dt)

    for i in range(0, Nstep-1):
        x[i+1] = x[i]+vx[i]*dt
        vx[i+1] = vx_0
        y[i+1] = y[i]+vy[i]*dt
        vy[i+1] = vy[i]+ay*dt
        if k == 1:
            if y[i] < 0:
                x, y, vx, vy = berhenti(i, x, y, vx, vy)
                bat_y = [0 for i in range(len(x))]
                plt.plot(x, bat_y, 'k--')
                break
        elif k == 2:
            if y[i] < 0:
                x, y, vx, vy = memantul(i, c, x, y, vx, vy)
                bat_x = np.linspace(0, int(max(x)), len(y))
                bat_y = [0 for i in range(len(y))]
                plt.plot(bat_x, bat_y, 'k--')
        elif k == 3:
            if y[i] < 0:
                x, y, vx, vy = memantul(i, 1, x, y, vx, vy)
                bat_y = [0 for i in range(len(x))]
                plt.plot(x, bat_y, 'k--')
            if x[i] > lb:
                x = periodik(i, lb, x)
                bat_x = [lb for i in range(len(x))]
                bat_x_0 = [0 for i in range(len(x))]
                bat_y = np.linspace(0, int(max(y)+1), len(x))
                plt.plot(bat_x_0, bat_y, 'k--')
                plt.plot(bat_x, bat_y, 'k--')
    plt.plot(x, y)
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Gerak Peluru 2D (%s) | $v_0$ : %.1f m/s | \u03B8 : $%.1f^o$ | t : %d s' %
              (kondisi, v0, theta, tb))
    plt.grid()
    plt.show()


menu_1()
pilih = int(input('Pilih: '))
gerak2d_1(pilih)
