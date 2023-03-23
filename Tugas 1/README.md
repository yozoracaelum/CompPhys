# Tugas 1 
# Fisika Komputasi
### Julian Evan Chrisnanto | 140310200025

Buatlah 3-buah Fungsi Syarat Batas dan 3-buah Gaya<br>
untuk kasus gerak peluru 2D. Buat Flowchart keseluruhannya<br>
1. Syarat Batas:<br>
    a. Berhenti,<br>
    b. Memantul, dan<br>
    c. Periodik/Warp Around<br>
2. Gaya:<br>
    a. Gravitasi,<br>
    b. Listrik, dan<br>
    c. Magnet<br>

# Kondisi 1 (Syarat Batas)
## a. Berhenti
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta/];
    B-->C(dt = 0.0001, ay = -9.8);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F("x[i+1] = x[i]+vx[i]*dt<br/>vx[i+1] = vx_0<br/>y[i+1] = y[i]+vy[i]*dt<br/>vy[i+1] = vy[i]+ay*dt");
    F-->G{"y[i] < 0"};
    G--Y-->H("x[i+1] = x[i]<br/>y[i+1] = 0<br/>vx[i+1] = 0<br/>vy[i+1] = 0");
```
## b. Memantul
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta,c/];
    B-->C(dt = 0.0001, ay = -9.8);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F("x[i+1] = x[i]+vx[i]*dt<br/>vx[i+1] = vx_0<br/>y[i+1] = y[i]+vy[i]*dt<br/>vy[i+1] = vy[i]+ay*dt");
    F-->G{"y[i] < 0"};
    G--Y-->H("x[i+1] = x[i+1]<br/>y[i+1] = -y[i+1]<br/>vx[i+1] = vx[i+1]<br/>vy[i+1] = -c*vy[i+1]");
```
## c. Periodik/Warp Around
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta,lb/];
    B-->C(dt = 0.0001, ay = -9.8);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    J-->E;
    E--end-->K[/Plot x vs y/];
    K-->L([Selesai]);
    E--do-->F("x[i+1] = x[i]+vx[i]*dt<br/>vx[i+1] = vx_0<br/>y[i+1] = y[i]+vy[i]*dt<br/>vy[i+1] = vy[i]+ay*dt");
    F-->G{"y[i] < 0"};
    G--Y-->H("x[i+1] = x[i+1]<br/>y[i+1] = -y[i+1]<br/>vx[i+1] = vx[i+1]<br/>vy[i+1] = -c*vy[i+1]");
    H-->I{"x[i] > lb"};
    I--Y-->J("x[i+1] = x[i+1] - lb");
```
# Kondisi 2 (Gaya Luar)
## a. Gravitasi
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta,m,gx,gy/];
    B-->C(dt = 0.0001);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F[["Fgravitasi(m,gx,gy)"]];
    F-->G(Fx = m*gx<br/>Fy = m*gy);
    G-->H("x[i+1] = x[i]+vx[i]*dt<br/>y[i+1] = y[i]+vy[i]*dt<br/>vx[i+1] = vx[i]+(Fx/m)*dt<br/>vy[i+1] = vy[i]+(Fy/m)*dt");
```
## b. Listrik
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta,m,q,Ex,Ey/];
    B-->C(dt = 0.0001);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F[["Flistrik(q,Ex,Ey)"]];
    F-->G(Fx = q*Ex<br/>Fy = q*Ey);
    G-->H("x[i+1] = x[i]+vx[i]*dt<br/>y[i+1] = y[i]+vy[i]*dt<br/>vx[i+1] = vx[i]+(Fx/m)*dt<br/>vy[i+1] = vy[i]+(Fy/m)*dt");
```
## c. Magnet
```mermaid
graph TD;
    A([Mulai])-->B[/Input ta,tb,v0,theta,m,q,Bz/];
    B-->C(dt = 0.0001);
    C-->D("rad = (pi/180)*theta<br/>Nstep = (tb-ta)/dt<br/>vx_0 = v0*cos(rad)<br/>vy_0 = v0*sin(rad)");
    D-->E{{n->1 to Nstep}};
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F[["Fmagnet(q,Bz,vx,vy)"]];
    F-->G("Fx = q*((vy[i]*Bz)-(vz*By))<br/>Fy = q*((vz*Bx)-(vx[i]*Bz))");
    G-->H("x[i+1] = x[i]+vx[i]*dt<br/>y[i+1] = y[i]+vy[i]*dt<br/>vx[i+1] = vx[i]+(Fx/m)*dt<br/>vy[i+1] = vy[i]+(Fy/m)*dt");
```
