'''
==================
Tugas 1. Fisika Komputasi
Buatlah 3-buah Fungsi Syarat Batas dan 3-buah Gaya
untuk kasus gerak peluru 2D. Buat Flowchart keseluruhannya
1. Syarat Batas:
    a. Berhenti,
    b. Memantul, dan
    c. Periodik/Warp Around
2. Gaya:
    a. Gravitasi,
    b. Listrik, dan
    c. Magnet
==================
by. Julian Evan Chrisnanto
v.1 : Initial build - 22.3.2023
v.2 : Magnetic Force updated - 23.3.2023
==================
'''

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

def menu_2():
    print('----------')
    print('Kondisi 2')
    print('1. Gaya Gravitasi')
    print('2. Gaya Listrik')
    print('3. Gaya Magnet')
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

def gayagravitasi(m,gx,gy):
    Fx = m*gx
    Fy = m*gy
    return Fx, Fy

def gayalistrik(q,Ex,Ey):
    Fx = q*Ex
    Fy = q*Ey
    return Fx, Fy

def gayamagnet(i,q,Bz,vx,vy,Bx=0,By=0,vz=0):
    Fx = q*((vy[i]*Bz)-(vz*By))
    Fy = q*((vz*Bx)-(vx[i]*Bz))
    return Fx, Fy

def gerak2d_1(k):
    dt, ay = 0.0001, -9.8
    ta = float(input('Waktu awal (s): '))
    tb = float(input('Waktu akhir (s): '))
    v0 = float(input('Kecepatan awal (m/s): '))
    theta = float(input('Sudut (o): '))
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
    t = np.arange(ta,tb,dt)

    for i in range(0,Nstep-1):
        x[i+1] = x[i]+vx[i]*dt
        vx[i+1] = vx_0
        y[i+1] = y[i]+vy[i]*dt
        vy[i+1] = vy[i]+ay*dt
        if k == 1:
            if y[i] < 0:
                x,y,vx,vy = berhenti(i,x,y,vx,vy)
                bat_y = [0 for i in range(len(x))]
                plt.plot(x,bat_y,'k--')
                break
        elif k == 2:
            if y[i] < 0:
                x,y,vx,vy = memantul(i,c,x,y,vx,vy)
                bat_x = np.linspace(0,int(max(x)),len(y))
                bat_y = [0 for i in range(len(y))]
                plt.plot(bat_x,bat_y,'k--')
        elif k == 3:
            if y[i] < 0:
                x,y,vx,vy = memantul(i,1,x,y,vx,vy)
                bat_y = [0 for i in range(len(x))]
                plt.plot(x,bat_y,'k--')
            if x[i] > lb:
                x = periodik(i,lb,x)
                bat_x = [lb for i in range(len(x))]
                bat_x_0 = [0 for i in range(len(x))]
                bat_y = np.linspace(0,int(max(y)+1),len(x))
                plt.plot(bat_x_0,bat_y,'k--')
                plt.plot(bat_x,bat_y,'k--')

    plt.plot(x,y,label='$v_0$ : %.1f m/s\n\u03B8 : $%.1f^o$\nt : %d s' %(v0,theta,tb))
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Gerak Peluru 2D (%s)' %kondisi)
    plt.legend()
    plt.grid()
    plt.show()
    return ta, tb, v0, theta

def gerak2d_2(k,ta,tb,v0,theta):
    dt = 0.0001
    if k == 1:
        m = float(input('Massa (kg): '))
        gx = float(input('gx (m/s^2): '))
        gy = float(input('gy (m/s^2): '))
        kondisi = 'Gaya Gravitasi'
        param_x = '$g_x$'
        param_y = '$g_y$'
        val_x = gx
        val_y = gy
        unit_x = '$m/s^2$'
        unit_y = '$m/s^2$'
    if k == 2:
        m = float(input('Massa (kg): '))
        q = float(input('Muatan (C): '))
        Ex = float(input('Ex (V/m): '))
        Ey = float(input('Ey (V/m): '))
        kondisi = 'Gaya Listrik'
        param_x = '$E_x$'
        param_y = '$E_y$'
        val_x = Ex
        val_y = Ey
        unit_x = 'V/m'
        unit_y = 'V/m'
    if k == 3:
        m = float(input('Massa (kg): '))
        q = float(input('Muatan (C): '))
        Bz = float(input('Bz (A/m): '))
        kondisi = 'Gaya Magnet'
        param_x = '$B_z$'
        param_y = 'q'
        val_x = Bz
        val_y = q
        unit_x = 'A/m'
        unit_y = 'C'
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
        if k == 1:
            Fx,Fy = gayagravitasi(m,gx,gy)
            x[i+1] = x[i]+vx[i]*dt
            y[i+1] = y[i]+vy[i]*dt
            vx[i+1] = vx[i]+(Fx/m)*dt
            vy[i+1] = vy[i]+(Fy/m)*dt
        if k == 2:
            Fx,Fy = gayalistrik(q,Ex,Ey)
            x[i+1] = x[i]+vx[i]*dt
            y[i+1] = y[i]+vy[i]*dt
            vx[i+1] = vx[i]+(Fx/m)*dt
            vy[i+1] = vy[i]+(Fy/m)*dt
        if k == 3:
            Fx,Fy = gayamagnet(i,q,Bz,vx,vy,0,0,0)
            x[i+1] = x[i]+vx[i]*dt
            y[i+1] = y[i]+vy[i]*dt
            vx[i+1] = vx[i]+(Fx/m)*dt
            vy[i+1] = vy[i]+(Fy/m)*dt
    
    plt.plot(x,y,label=' %s : %.1f %s | %s : %.1f %s' %(param_x,val_x,unit_x,param_y,val_y,unit_y))
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.title('Gerak Peluru 2D (%s) | $v_0$ : %.1f m/s | \u03B8 : $%.1f^o$ | t : %d s' %(kondisi,v0,theta,tb))
    plt.legend()
    plt.grid()
    plt.show()
    return ta,tb,v0,theta

menu_1()
pilih = int(input('Pilih: '))
ta,tb,v0,theta = gerak2d_1(pilih)
menu_2()
pilih = int(input('Pilih: '))
gerak2d_2(pilih,ta,tb,v0,theta)