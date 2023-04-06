import matplotlib.pyplot as plt
import numpy as np

def menu():
    print('1. Gerak 1D : v const')
    print('2. Gerak 2D : v const')
    print('3. Gerak 1D : a const')
    print('4. Gerak 2D : a const')
    print('5. Gerak Bandul GHS')
    print('6. Gerak Bandul Teredam')
    print('7. Gerak Bandul Gaya Konstan')
    print('8. Gerak Bandul Gaya Tidak Konstan')
'''
Gerak 1D : Kecepatan konstan
'''
def gerak1d():
    dt = 0.1
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    vx = float(input('Kecepatan awal: '))
    Nstep = int((tb-ta)/dt)
    x = np.zeros(Nstep)
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        x[i+1] = x[i]+vx*dt

    plt.plot(t,x)
    plt.xlabel('t(s)')
    plt.ylabel('x(m)')
    plt.title('Gerak 1D | $v_0$ : %.1f m/s' %vx)
    plt.show()
'''
Gerak 2D : Kecepatan konstan
'''
def gerak2d():
    dt = 0.1
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    vx = float(input('Kecepatan-x awal: '))
    vy = float(input('Kecepatan-y awal: '))
    Nstep = int((tb-ta)/dt)
    x = np.zeros(Nstep)
    y = np.zeros(Nstep)
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        x[i+1] = x[i]+vx*dt
        y[i+1] = y[i]+vy*dt

    plt.plot(x,y)
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Gerak 2D | $v_x^0$ : %.1f m/s | $v_y^0$ : %.1f m/s' %(vx,vy))
    plt.show()
'''
Gerak 1D : Percepatan konstan
'''
def gerak1d_1():
    dt = 0.1
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    vx_0 = float(input('Kecepatan awal: '))
    ax = float(input('Percepatan: '))
    Nstep = int((tb-ta)/dt)
    x = np.zeros(Nstep)
    vx = np.zeros(Nstep)
    vx[0] = vx_0
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        x[i+1] = x[i]+vx[i]*dt
        vx[i+1] = vx[i]+ax*dt

    plt.plot(t,x,'-o')
    plt.xlabel('t(s)')
    plt.ylabel('x(m)')
    plt.title('Gerak 1D | $v_x^0$ : %.1f m/s | a : %.1f m/$s^2$' %(vx_0, ax))
    plt.show()
'''
Gerak 2D : Percepatan konstan
'''
def gerak2d_1():
    dt, ay = 0.0001, -9.8
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    v0 = float(input('Kecepatan awal: '))
    theta = float(input('Sudut: '))
    c = float(input('Koefisien: '))
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
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        x[i+1] = x[i]+vx[i]*dt
        vx[i+1] = vx_0
        y[i+1] = y[i]+vy[i]*dt
        vy[i+1] = vy[i]+ay*dt
        if y[i] < 0:
            y[i+1] = -y[i+1]
            vy[i+1] = -c*vy[i+1]

    plt.plot(x,y)
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Gerak 2D | $v_0$ : %.1f | $theta$ : $%.1f^o$' %(v0, theta))
    #plt.ylim([0,10])
    plt.grid()
    plt.show()

def bandulGHS():
    dt, g = 0.0001, 9.8
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    w0 = float(input('Kecepatan sudut awal: '))
    theta0 = float(input('Sudut: '))
    L = float(input('Panjang tali: '))
    Nstep = int((tb-ta)/dt)
    w = np.zeros(Nstep)
    theta = np.zeros(Nstep)
    w[0] = w0
    theta[0] = theta0
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        w[i+1] = w[i] - (g/L)*theta[i]*dt
        theta[i+1] = theta[i] + w[i+1]*dt

    plt.subplot(1,2,1)
    plt.plot(t,theta)
    plt.grid()
    plt.xlabel('t(s)')
    plt.ylabel('theta')
    plt.subplot(1,2,2)
    plt.plot(theta,w)
    plt.grid()
    plt.xlabel('theta')
    plt.ylabel('omega')
    plt.suptitle('Gerak Bandul GHS | $w_0$ : %.1f | $theta_0$ : $%.1f^o$' %(w0, theta0))
    plt.show()

def bandulTeredam():
    dt, g = 0.0001, 9.8
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    w0 = float(input('Kecepatan sudut awal: '))
    theta0 = float(input('Sudut: '))
    L = float(input('Panjang tali: '))
    q = float(input('Konstanta redaman: '))
    Nstep = int((tb-ta)/dt)
    w = np.zeros(Nstep)
    theta = np.zeros(Nstep)
    w[0] = w0
    theta[0] = theta0
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        w[i+1] = w[i] - ((g/L)*theta[i] + q*w[i])*dt
        theta[i+1] = theta[i] + w[i+1]*dt

    plt.subplot(1,2,1)
    plt.plot(t,theta)
    plt.grid()
    plt.xlabel('t(s)')
    plt.ylabel('theta')
    plt.subplot(1,2,2)
    plt.plot(theta,w)
    plt.grid()
    plt.xlabel('theta')
    plt.ylabel('omega')
    plt.suptitle('Gerak Bandul Teredam | $w_0$ : %.1f | $theta_0$ : $%.1f^o$ | q : %.2f' %(w0, theta0, q))
    plt.show()

def bandulForceKonstan():
    dt, g = 0.0001, 9.8
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    w0 = float(input('Kecepatan sudut awal: '))
    theta0 = float(input('Sudut: '))
    L = float(input('Panjang tali: '))
    q = float(input('Konstanta redaman: '))
    Fd = float(input('Gaya Luar: '))
    Ohmd = float(input('Frekuensi Fd: '))
    Nstep = int((tb-ta)/dt)
    w = np.zeros(Nstep)
    theta = np.zeros(Nstep)
    w[0] = w0
    theta[0] = theta0
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        w[i+1] = w[i] - ((g/L)*theta[i] + q*w[i] - Fd*Ohmd*t[i])*dt
        theta[i+1] = theta[i] + w[i+1]*dt

    plt.subplot(1,2,1)
    plt.plot(t,theta)
    plt.grid()
    plt.xlabel('t(s)')
    plt.ylabel('theta')
    plt.subplot(1,2,2)
    plt.plot(theta,w)
    plt.grid()
    plt.xlabel('theta')
    plt.ylabel('omega')
    plt.suptitle('Gerak Bandul Fd Konstan| $w_0$ : %.1f | $theta_0$ : $%.1f^o$ | q : %.2f | $F_d$ : %.1f | $Ohm_d$ : %.1f' %(w0, theta0, q, Fd, Ohmd))
    plt.show()

def bandulForceTKonstan():
    dt, g = 0.0001, 9.8
    ta = float(input('Waktu awal: '))
    tb = float(input('Waktu akhir: '))
    w0 = float(input('Kecepatan sudut awal: '))
    theta0 = float(input('Sudut: '))
    L = float(input('Panjang tali: '))
    q = float(input('Konstanta redaman: '))
    Fd = float(input('Gaya Luar: '))
    Ohmd = float(input('Frekuensi Fd: '))
    Nstep = int((tb-ta)/dt)
    w = np.zeros(Nstep)
    theta = np.zeros(Nstep)
    w[0] = w0
    theta[0] = theta0
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        w[i+1] = w[i] - ((g/L)*theta[i] + q*w[i] - Fd*np.sin(Ohmd*t[i]))*dt
        theta[i+1] = theta[i] + w[i+1]*dt

    plt.subplot(1,2,1)
    plt.plot(t,theta)
    plt.grid()
    plt.xlabel('t(s)')
    plt.ylabel('theta')
    plt.subplot(1,2,2)
    plt.plot(theta,w)
    plt.grid()
    plt.xlabel('theta')
    plt.ylabel('omega')
    plt.suptitle('Gerak Bandul Fd Tak Konstan| $w_0$ : %.1f | $theta_0$ : $%.1f^o$ | q : %.2f | $F_d$ : %.1f | $Ohm_d$ : %.1f' %(w0, theta0, q, Fd, Ohmd))
    plt.show()

def main():
    menu()
    inp = int(input('Select: '))
    if inp == 1:
        gerak1d()
    elif inp == 2:
        gerak2d()
    elif inp == 3:
        gerak1d_1()
    elif inp == 4:
        gerak2d_1()
    elif inp == 5:
        bandulGHS()
    elif inp == 6:
        bandulTeredam()
    elif inp == 7:
        bandulForceKonstan()
    elif inp == 8:
        bandulForceTKonstan()
main()