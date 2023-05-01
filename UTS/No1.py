'''
==================
UTS. Fisika Komputasi
[1] Sebelumnya pada perkuliahan sudah dibahas
mengenai system chaos pada bandul.
Pelajari sistem chaos berikut yaitu
Persamaan Lorentz
dx/dt = sigma(y-x)
dy/dy = rho.x-y-xz
dz/dt = xy - beta.z
==================
by. Julian Evan Chrisnanto
v.1 : Initial build - 15.4.2023
==================
'''

import matplotlib.pyplot as plt
import numpy as np

# Membuat fungsi untuk simulasi chaos Lorentz's Butterfly
def lorentz_butterfly():
    dt, sigma, beta, rho = 0.01, 10, 12, 28 # Mendefinisikan parameter pada Lorentz Butterfly
    x0, y0, z0 = 1, 1, 1 # Titik koordinat awal
    ta = float(input('Waktu awal (s): '))
    tb = float(input('Waktu akhir (s): '))
    Nstep = int((tb-ta)/dt)

    x = np.zeros(Nstep)
    y = np.zeros(Nstep)
    z = np.zeros(Nstep)
    vx = np.zeros(Nstep)
    vy = np.zeros(Nstep)
    vz = np.zeros(Nstep)
    x[0], y[0], z[0] = x0, y0, z0
    vx[0], vy[0], vz[0] = 0, 0, 0 # Kecepatan awal

    # Membuat perhitungan perubahan posisi dengan metode Euler
    for i in range(0, Nstep-1):
        x[i+1] = x[i] + sigma*(y[i]-x[i])*dt
        y[i+1] = y[i] + (rho*x[i]-y[i]-x[i]*z[i])*dt
        z[i+1] = z[i] + (x[i]*y[i]-beta*z[i])*dt
        vx[i+1] = (x[i+1]-x[i])/dt
        vy[i+1] = (y[i+1]-y[i])/dt
        vz[i+1] = (z[i+1]-z[i])/dt

    # Menampilkan pada grafik
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') # Menjadikan grafik dalam proyeksi 3D
    ax.plot(x, z, y, linewidth=0.5)
    ax.set_xlabel('X(m)')
    ax.set_ylabel('Z(m)')
    ax.set_zlabel('Y(m)')
    plt.title("Lorentz's Butterfly (sigma=%.2f, rho=%.2f, beta=%.2f)" %(sigma, rho, beta))
    plt.show()


lorentz_butterfly()