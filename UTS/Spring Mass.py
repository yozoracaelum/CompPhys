'''
==================
UTS. Fisika Komputasi
[2] Sistem pegas dengan 3-buah massa
dengan k1 = k4 = Ak, k2 = k3 = (Y+1)k
m1 = m2 =m3 = 1/2(Z+1)m
# 140310200025
# AB = 20
# YZ = 25

A = 2, Y = 2, Z = 5
k1 = k4 = 2k
k2 = k3 = 3k
m1 = m2 = m3 = 1/2(5+1) = 3m
Fd = A = 2N

==================
by. Julian Evan Chrisnanto
v.1 : Initial build - 17.4.2023
v.2 : 1 Spring Mass added - 18.4.2023
==================
'''

import matplotlib.pyplot as plt
import numpy as np

# Membuat fungsi untuk simulasi sistem pegas
def pegas():
    dt = 0.001
    ta = float(input('Waktu awal (s): '))
    tb = float(input('Waktu akhir (s): '))
    m1, m2, m3 = 3, 3, 3 # Massa setiap beban
    k1, k4 = 2, 2 # Konstanta pegas 1 dan 4
    k2, k3 = 3, 3 # konstanta pegas 2 dan 3
    x1_0 = float(input('Posisi awal m1: '))
    x2_0 = float(input('Posisi awal m2: '))
    x3_0 = float(input('Posisi awal m3: '))
    Fd = 2 # Gaya luar
    Nstep = int((tb-ta)/dt)
    x1 = np.zeros(Nstep)
    x2 = np.zeros(Nstep)
    x3 = np.zeros(Nstep)
    v1 = np.zeros(Nstep)
    v2 = np.zeros(Nstep)
    v3 = np.zeros(Nstep)
    t = np.arange(ta, tb, dt)
    x1[0], x2[0], x3[0] = x1_0, x2_0, x3_0

    # Membuat update posisi dengan metode Euler
    for i in range(0, Nstep-1):
        v1[i+1] = v1[i] + (1/m1)*(-(k1+k2)*x1[i]+k2*x2[i] + Fd)*dt
        v2[i+1] = v2[i] + (1/m2)*(k2*x1[i]-(k2+k3)*x2[i]+k3*x3[i])*dt
        v3[i+1] = v3[i] + (1/m3)*(k3*x2[i]-(k3+k4)*x3[i])*dt
        x1[i+1] = x1[i] + v1[i]*dt
        x2[i+1] = x2[i] + v2[i]*dt
        x3[i+1] = x3[i] + v3[i]*dt

    plt.plot(t, x1, label='m1 = 3m')
    plt.plot(t, x2, label='m2 = 3m')
    plt.plot(t, x3, label='m3 = 3m')
    plt.xlabel('t (s)')
    plt.ylabel('Posisi (m)')
    plt.legend()
    plt.grid()
    plt.title('Sistem Pegas | k1 = %dk, k2 = %dk, k3 = %dk, k4 = %dk | Fd = %.2fN' %
              (k1, k2, k3, k4, Fd))
    plt.show()

#pegas()

# def spring_mass_external():
#     dt = 0.001
#     t_start = float(input('Enter start time (s): '))
#     t_end = float(input('Enter end time (s): '))
#     m1, m2, m3 = 3, 3, 3
#     k1, k4 = 2, 2
#     k2, k3 = 3, 3
#     x1_0 = float(input('Enter initial position of m1: '))
#     x2_0 = float(input('Enter initial position of m2: '))
#     x3_0 = float(input('Enter initial position of m3: '))
#     Fd = float(input('Enter external force amplitude: '))
#     omega = float(input('Enter external force frequency: '))
#     phi = float(input('Enter external force phase: '))
#     Nstep = int((t_end - t_start) / dt)
#     x1 = np.zeros(Nstep)
#     x2 = np.zeros(Nstep)
#     x3 = np.zeros(Nstep)
#     v1 = np.zeros(Nstep)
#     v2 = np.zeros(Nstep)
#     v3 = np.zeros(Nstep)
#     t = np.arange(t_start, t_end, dt)
#     x1[0], x2[0], x3[0] = x1_0, x2_0, x3_0

#     for i in range(0, Nstep-1):
#         v1[i+1] = v1[i] + (1/m1)*(-(k1+k2)*x1[i]+k2*x2[i] +
#                                   Fd*np.sin(omega*t[i] + phi))*dt
#         v2[i+1] = v2[i] + (1/m2)*(k2*x1[i]-(k2+k3)*x2[i]+k3*x3[i])*dt
#         v3[i+1] = v3[i] + (1/m3)*(k3*x2[i]-(k3+k4)*x3[i])*dt
#         x1[i+1] = x1[i] + v1[i]*dt
#         x2[i+1] = x2[i] + v2[i]*dt
#         x3[i+1] = x3[i] + v3[i]*dt

#     plt.plot(t, x1, label='m1 = 3m')
#     plt.plot(t, x2, label='m2 = 3m')
#     plt.plot(t, x3, label='m3 = 3m')
#     plt.xlabel('t (s)')
#     plt.ylabel('Position (m)')
#     plt.legend()
#     plt.grid()
#     plt.title('3 Spring-Mass System with External Force | k1 = %dk, k2 = %dk, k3 = %dk, k4 = %dk' %
#               (k1, k2, k3, k4))
#     plt.show()


def springmass():
    dt = 0.01
    ta = 0
    tb = 10
    n = int(input('Jumlah Pegas: '))
    Nstep = int((tb-ta)/dt)
    M = np.zeros((n-1, n-1))
    K = np.zeros((n-1, n-1))
    X = np.zeros((n-1, Nstep))
    V = np.zeros((n-1, 1))
    A = np.zeros((n-1, 1))
    k, m, x = [], [], []
    ind = 1
    for i in range(n):
        k1 = int(input('k%d: ' % ind))
        ind += 1
        k.append(k1)
    ind = 1
    for j in range(n-1):
        m1 = int(input('m%d: ' % ind))
        ind += 1
        m.append(m1)
    for i in range(n-1):
        for j in range(n-1):
            if i == j:
                K[i, j] = k[i]+k[i+1]
        if i == 0:
            K[i, i+1] = -k[i+1]
        if 0 < i < n-2:
            K[i, i-1] = -k[i]
            K[i, i+1] = -k[i+1]
        if i == n-2:
            K[i, i-1] = -k[i]
    for i in range(n-1):
        for j in range(n-1):
            if i == j:
                M[i, j] = m[i]
    ind = 1
    for i in range(n-1):
        x1 = int(input('x%d: ' % ind))
        ind += 1
        x.append(x1)
    for i in range(n-1):
        X[i, 0] = x[i]
    x = np.array(x).reshape((n-1, 1))
    # print(K)
    M1 = np.linalg.inv(M)
    A1 = np.dot(M1, K)
    A = np.dot(A1, x)
    print('M')
    print(M)
    print('A')
    print(A)
    print('K')
    print(K)
    print('X')
    print(x)
    # print(A1)
    # print(A)
    # print('---')
    # print(x)
    # print('---')
    # for j in range(n-1):
    #     V[j,0] += A[j,0]*dt
    #     x[j,0] += V[j,0]*dt
    # print(V)
    # print(x)
    # for i in range(0,Nstep-1):
    #     for j in range(n-1):
    #         # print(A[j,0])
    #         A = np.dot(A1,x)
    #         V[j,0] += A[j,0]*dt
    #         x[j,0] += V[j,0]*dt
    #         X[j,i] = x[j,0]
    # print(X)

# springmass()
import matplotlib.pyplot as plt
import numpy as np

#define the parameters of springs system
ta = float(input('Waktu awal: '))
tb = float(input('Waktu akhir: '))
#k = 10 #konstanta pegas
k1, k4 = 2, 2
k2, k3 = 7, 7
m1 = 3 #massa beban
m2 = 3 #massa beban
m3 = 3 #massa beban
a = 5 #gaya luar
dt = 0.05
x1_0 = 5
x2_0 = 7
x3_0 = 9


Nstep = int((tb-ta)/dt)
x1 = np.zeros(Nstep)
x2 = np.zeros(Nstep)
x3 = np.zeros(Nstep)
v1 = np.zeros(Nstep)
v1 = np.zeros(Nstep)
v2 = np.zeros(Nstep)
v3 = np.zeros(Nstep)
x1[0] = x1_0
x2[0] = x2_0
x3[0] = x3_0

t = np.arange(ta,tb,dt)

#Hukum Hooke
for i in range(0,Nstep-1):
    v1[i+1] = v1[i] + ((-(k1+k2) * x1[i] + (k2 * x2[i])) * dt)/m1
    v2[i+1] = v2[i] + ((k2 * x1[i] - (k2 + k3)* x2[i] + (k3 * x3[i])) * dt)/m2
    v3[i+1] = v3[i] + ((k3 * x2[i] - (k3 + k4)* x3[i]) * dt)/m3
    x1[i+1] = x1[i] + v1[i] * dt
    x2[i+1] = x2[i] + v2[i] * dt
    x3[i+1] = x3[i] + v3[i] * dt

plt.plot(t,x1, label='x1')
plt.plot(t,x2, label='x2')
plt.plot(t,x3, label='x3')
plt.xlabel('Waktu (s)')
plt.ylabel('Pergeseran (m)')
plt.legend()

plt.show()
