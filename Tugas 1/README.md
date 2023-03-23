# Tugas 1 
# Fisika Komputasi

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
    H-->E;
    E--end-->I[/Plot x vs y/];
    I-->J([Selesai]);
    E--do-->F("x[i+1] = x[i]+vx[i]*dt<br/>vx[i+1] = vx_0<br/>y[i+1] = y[i]+vy[i]*dt<br/>vy[i+1] = vy[i]+ay*dt");
    F-->G{"y[i] < 0"};
    G--Y-->H("x[i+1] = x[i+1]<br/>y[i+1] = -y[i+1]<br/>vx[i+1] = vx[i+1]<br/>vy[i+1] = -c*vy[i+1]");
```
