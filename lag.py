from math import pi,sin,cos,exp
import desi
from PyQt5.Qt import QCoreApplication
height = [0, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000, 11250, 12500, 13750, 15000, 16250, 17500, 18750,
              20000, 21250, 22500, 23750, 25000, 26250, 27500, 28750, 30000, 31250, 32500, 33700, 35000, 36200,
              37500,
              38700, 40000, 41200, 42500, 43700, 45000, 46200, 47500, 48700, 50000, 51200, 52400, 53800, 55000,
              56400,
              57400, 58800, 60000, 61400, 62400, 63800, 65000, 66400, 67400, 68800, 70000, 71400, 72400, 73800,
              75000,
              76400, 77400, 78800, 80000]
Roh = [1.22500, 1.08463, 0.956954, 0.841153, 0.736429, 0.642019, 0.557192, 0.481246, 0.41351, 0.35948,
           0.288375, 0.236977, 0.194755, 0.160067, 0.131568, 0.108152, 0.0889097, 0.0727376, 0.0595626, 0.0488328,
           0.0400837, 0.032941, 0.0271026, 0.023247, 0.0184101, 0.015199, 0.0125298, 0.0100755, 0.00846334,
           0.00682111, 0.00578343, 0.00466989, 0.00435826, 0.00399566, 0.00278926, 0.00235552, 0.00196627,
           0.00166803, 0.00140116, 0.00120695, 0.00102687, 8.84644e-4, 7.69418e-4, 6.54117e-4, 5.68096e-4,
           4.80867e-4, 4.2625e-4, 3.59275e-4, 3.09676e-4, 2.59758e-4, 2.28728e-4, 1.90954e-4, 1.63209e-4,
           1.3552e-4, 1.18446e-4, 9.78309e-5, 8.28284e-5, 6.79965e-5, 5.88106e-5, 4.77908e-5, 3.9921e-5,
           3.22815e-5, 2.76906e-5, 2.22853e-5,  # 1.8458e-5,
           0]
Ph = [101325, 87718, 74691.7, 63693.3, 54048.3, 45624.6, 38299.7, 31959.8, 26499.9, 21823.5, 17934, 14737.6,
          12111.8, 9954.59, 8182.24, 6725.96, 5529.29, 4548.17, 3745.58, 3088.24, 2549.21, 2106.68, 1742.94,
          1433.62, 1197.03, 936.41, 825.76, 675.69, 574.592, 477.28, 404.137, 331.654,
          287.143, 244.535, 205.979, 176.189, 149.101, 128.071, 108.857, 93.7688, 79.7787, 68.7287,
          59.1759, 49.95842, 42.5249, 35.4636, 31.0991, 25.8157, 21.9586, 18.81322,
          15.7858, 12.9682, 10.9297, 8.92599, 7.7082, 6.25886, 5.22088, 4.21115, 3.60393, 2.89109, 2.38814,
          1.90579, 1.61924, 1.28568,  # 1.05247,
          0]
Ah = [340.294, 335.463, 330.563, 325.592, 320.545, 315.42, 310.212, 304.918, 299.532, 295.069, 295.069,
          295.069, 295.069, 295.069, 295.069, 295.069, 295.069, 295.871, 296.713, 297.553, 298.389, 299.489,
          300.054, 300.883, 301.709, 302.532, 303.752, 305.944, 308.299, 310.458, 312.778, 314.903, 317.189,
          319.284, 321.537, 323.602, 325.823, 327.86, 329.21, 329.799, 329.799, 329.799, 328.137,
          325.768, 323.724, 321.324, 319.599, 317.17, 315.073, 312.611, 310.841, 308.346, 306.193,
          303.662, 301.842, 299.277, 297.061, 294.456, 292.903, 291.02, 289.396, 287.491, 286.124, 284.198,
          282.538, 0]
a = [0.043, 0.043, 0.046, 0.048, 0.047, 0.045, 0.039, 0.036, 0.042, 0.047, 0.052, 0.055, 0.06, 0.064, 0.069,
     0.07,
     0.072], [0.3, 0.5, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 3, 3.5, 4.5, 5.5, 6]
b = [0.64, 0.64, 0.68, 0.8, 1, 1.12, 0.95, 0.75, 0.64, 0.6, 0.53, 0.46, 0.41, 0.35, 0.3, 0.3, 0.3], \
    [0.5, 0.7, 0.9, 1, 1.1, 1.125, 1.5, 1.75, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 5.6]
x = []
for i in range(14):
    x.append(5000 * i + 5000)
x.append(80000)
y = [0.6, 0.8, 1, 1.5, 2, 3, 4, 6, 8, 10, 12]
z = [0.002, 0.006, 0.014, 0.023, 0.038, 0.047, 0.055, 0.072, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.02, 0.038, 0.047, 0.055, 0.072, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.02, 0.038, 0.047, 0.055, 0.072, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.017, 0.034, 0.043, 0.055, 0.072, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.015, 0.031, 0.039, 0.055, 0.072, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.013, 0.026, 0.033, 0.043, 0.063, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.011, 0.022, 0.028, 0.04, 0.054, 0.064, 0.084, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.011, 0.022, 0.024, 0.033, 0.043, 0.054, 0.065, 0.077, 0.089, 0.102, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.011, 0.022, 0.024, 0.033, 0.036, 0.045, 0.054, 0.064, 0.076, 0.087, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.011, 0.022, 0.024, 0.033, 0.027, 0.035, 0.044, 0.054, 0.064, 0.075, 0.085, 0.112], \
    [0.001, 0.004, 0.011, 0.011, 0.022, 0.024, 0.033, 0.027, 0.035, 0.044, 0.054, 0.064, 0.075, 0.070, 0.090]
x2 = [40000, 50000, 60000, 70000, 80000, 90000]
y2 = [6, 8, 10, 14, 20]
z2 = [23e-3, 23e-3, 23e-3, 23e-3, 23e-3, 23e-3], [23e-3, 23e-3, 32e-3, 43e-3, 55e-3, 70e-3], \
     [23e-3, 20e-3, 28e-3, 38e-3, 48e-3, 60e-3], [23e-3, 20e-3, 23e-3, 30e-3, 37e-3, 45e-3], \
     [23e-3, 20e-3, 16e-3, 22e-3, 29e-3, 36e-3]
gc = 9.82
R = 6371000

def cx1(M, h):
    i, j, rez = 0, 0, 0
    while h > x[i]:
        i += 1
        if i == len(x):
            i -= 1
            break
    while M > y[j]:
        j += 1
        if j == len(y):
            j -= 1
            break
    if M <= y[0] and h <= x[0]:
        xx = z[0][0] * h / x[0]
        rez = (xx * M) / y[j]
    elif h <= x[0]:
        xx, xx1 = z[j][0] * h / x[0], \
                  z[j - 1][0] * h / x[0]
        rez = (xx * (M - y[j - 1]) + xx1 * (y[j] - M)) / (y[j] - y[j - 1])
    elif M <= y[0]:
        xx, xx1 = z[0][i] * M / y[0], z[0][i - 1] * M / y[0]
        rez = (xx * (h - x[i - 1]) + xx1 * (x[i] - h)) / (x[i] - x[i - 1])
    else:
        xx, xx1 = (z[j][i] * (h - x[i - 1]) + z[j][i - 1] * (x[i] - h)) / (x[i] - x[i - 1]), (
                z[j - 1][i] * (h - x[i - 1]) + z[j - 1][i - 1] * (x[i] - h)) / (x[i] - x[i - 1])
        rez = (xx * (M - y[j - 1]) + xx1 * (y[j] - M)) / (y[j] - y[j - 1])
    return inte(M, b[1], b[0]) + rez
def cy1(M):
    if M <= a[1][0]:
        return a[1][0]
    elif M >= a[1][len(a[1]) - 1]:
        return a[1][len(a[1]) - 1]
    return inte(M, a[1], a[0])
def cx2(M, h):
    i, j, rez = 0, 0, 0
    while h > x2[i]:
        i += 1
        if i == len(x2):
            i -= 1
            break
    while M > y2[j]:
        j += 1
        if j == len(y2):
            j -= 1
            break
    if M <= y2[0] and h <= x2[0]:
        xx = z2[0][0] * h / x2[0]
        rez = (xx * M) / y2[j]
    elif h <= x2[0]:
        xx, xx1 = z2[j][0] * h / x2[0], \
                  z2[j - 1][0] * h / x2[0]
        rez = (xx * (M - y2[j - 1]) + xx1 * (y2[j] - M)) / (y2[j] - y2[j - 1])
    elif M <= y2[0]:
        xx, xx1 = z2[0][i] * M / y2[0], z2[0][i - 1] * M / y2[0]
        rez = (xx * (h - x2[i - 1]) + xx1 * (x2[i] - h)) / (x2[i] - x2[i - 1])
    else:
        xx, xx1 = (z2[j][i] * (h - x2[i - 1]) + z2[j][i - 1] * (x2[i] - h)) / (x2[i] - x2[i - 1]), (
                z2[j - 1][i] * (h - x2[i - 1]) + z2[j - 1][i - 1] * (x2[i] - h)) / (x2[i] - x2[i - 1])
        rez = (xx * (M - y2[j - 1]) + xx1 * (y2[j] - M)) / (y2[j] - y2[j - 1])
    return rez
cy2 = 5e-2

def rass(self):
    self.consoletext.clear()
    mka = float(self.textEdit_8.toPlainText())  # kg
    m1 = float(self.textEdit_9.toPlainText())  # kg
    mc1 = float(self.textEdit_4.toPlainText())  # kg/s
    t1 = float(self.textEdit_45.toPlainText())  # s
    md1 = m1 - mc1 * t1  # kg
    p1 = float(self.textEdit.toPlainText())  # N
    s1 = float(self.textEdit_2.toPlainText())  # m^2
    sm1 = float(self.textEdit_3.toPlainText())  # m^2
    m2 = float(self.textEdit_10.toPlainText())  # kg
    mc2 = float(self.textEdit_31.toPlainText())  # kg/s
    mc22= mc2
    t2 = float(self.textEdit_46.toPlainText())  # s
    md2 = m2 - mc2 * t2  # kg
    s2 = float(self.textEdit_30.toPlainText())  # m^2
    s22 = s2
    p2 = float(self.textEdit_29.toPlainText())  # N
    p22 = p2
    sm2 = float(self.textEdit_32.toPlainText())  # m^2
    tv = float(self.textEdit_44.toPlainText())  # s
    t3 = float(self.textEdit_47.toPlainText())  # s
    hal = float(self.textEdit_7.toPlainText())
    deltav = float(self.textEdit_54.toPlainText())
    deltatt = float(self.textEdit_55.toPlainText())
    if (self.groupBox_8.isChecked() == True):
        tmt = float(self.textEdit_64.toPlainText())
        mc22 = float(self.textEdit_53.toPlainText())
        t2 += t1 - tmt
        t3 = mc2 / mc22 * tmt + t2
        p22 = float(self.textEdit_51.toPlainText())
        s22 = float(self.textEdit_52.toPlainText())

    self.textEdit_25.setText(str(m1 + m2 + mka))
    tt11, tt12 = float(self.textEdit_27.toPlainText()) / 180 * pi, float(self.textEdit_62.toPlainText()) / 180 * pi
    ae1, ae2 = float(self.textEdit_26.toPlainText()), float(self.textEdit_61.toPlainText())
    tt21, tt22 = float(self.textEdit_28.toPlainText()) / 180 * pi, float(self.textEdit_63.toPlainText()) / 180 * pi
    if proverca(t1,t3,p1,sm1,p2,mc1,mc2,m1,m2,mka,md1,s1,s2,sm2)==1:
        self.consoletext.setText(str("КА легок для данной РН"))
    else:
        regtask(self, tv, t1, t2, t3, s1, s2, p1, p2, sm1, sm2, mc1, mc2, m1, m2, mka, md1, deltav,
                deltatt, ae1, ae2, hal, tt11, tt12, tt21, tt22,mc22,s22,p22)

def proverca(t1,t3,p1,sm1,p2,mc1,mc2,m1,m2,mka,md1,s1,s2,sm2):
    def telo(V,H,m,ter):
        plot, davl, skzv = inte(H, height, Roh), inte(H, height, Ph), inte(H, height, Ah)
        Mah = V / skzv
        if ter <= t1:
            return V+(((p1 - davl * s1)  - cx1(Mah, H) * plot * sm1 * V ** 2 / 2) / m - gc / (1 + H / R) ** 2),H+V,m+mc1,ter+1
        else:
            return V+(((p2 - davl * s2)  - cx2(Mah, H) * plot * sm2 * V ** 2 / 2) / m - gc/ (1 + H / R) ** 2),H+V,m+mc2,ter+5
    V,H,m,ter=0,0,m1 + m2 + mka,0
    while ter<=t1:
        V, H, m, ter=telo(V,H,m,ter)
    m-=md1
    while ter<=t3:
        V, H, m, ter = telo(V, H, m, ter)
    if (V>(398600440/(R+H))**0.5):
        return 1
def inte(H, xx, yy):
        if H >= xx[len(xx) - 1]:
            return yy[len(xx) - 1]
        if H <= xx[0]:
            return yy[0]
        l = len(xx) - 1
        while H < xx[l]:
            l = l - 1
        return yy[l + 1] - (yy[l + 1] - yy[l]) * (xx[l + 1] - H) / (xx[l + 1] - xx[l])
def regtask(self,tv,t1,t2,t3,s1,s2,p1,p2,sm1,sm2,mc1,mc2,M1,M2,mka,md1,deltav,deltatt,ae1,ae2,hal,tt11,tt12,tt21,tt22,mc22,s22,p22):
    def polet1():
        time1, h1, v1, m1, TT1, fi1, tt = 0, 0, 0, M1 + M2 + mka, pi / 2, 0, pi / 2
        mTT1, mh1, mt1, mtt1, ml1 = [], [], [], [], []
        mTT1.append(TT1 * 180 / pi)
        mh1.append(h1)
        mtt1.append((alpha(time1) * pi / 180 + TT1 - fi1) / pi * 180)
        mt1.append(time1)
        ml1.append(fi1 * 0.18 / pi * R)
        while time1 < t1:
            v1, TT1, h1, fi1, m1 = runge(v1, TT1, h1, fi1, m1, time1,F1)
            time1 += sh
            mTT1.append(TT1 * 180 / pi)
            mh1.append(h1)
            mtt1.append((alpha(time1) * pi / 180 + TT1 - fi1) / pi * 180)
            mt1.append(time1)
            ml1.append(fi1*0.18/pi*R)
        return mTT1, mh1, mt1, mtt1, ml1, time1, h1, v1, m1, TT1, fi1, mtt1[len(mtt1) - 1] / 180 * pi
    def polet2(time1, h1, v1, m1, TT1, fi1, tt1, TET1):
        TET1= TET1
        time2, h2, v2, m2, TT2, fi2, tt = time1, h1, v1, m1, TT1, fi1, tt1
        mTT2, mh2, mt2, mtt2, ml2 = [], [], [], [], []
        while time2 < t2:
            v2, TT2, h2, fi2, m2 = runge(v2, TT2, h2, fi2, m2, time2, F2)
            time2 += sh
            mTT2.append(TT2 * 180 / pi)
            mh2.append(h2)
            mtt2.append((tt + TET1 * (time2 - t1)) * 180 / pi)
            mt2.append(time2)
            ml2.append(fi2 * 0.18 / pi * R)
        return mTT2, mh2, mt2, mtt2, ml2, time2, h2, v2, m2, TT2, fi2, mtt2[len(mtt2) - 1] / 180 * pi
    def polet3(time2, h2, v2, m2, TT2, fi2, tt2, TET2):
        TET2 = TET2
        time3, h3, v3, m3, TT3, fi3 = time2, h2, v2, m2, TT2, fi2
        mTT3, mh3, mt3, mtt3, ml3 = [], [], [], [], []
        while time3 <= t3:
            v3, TT3, h3, fi3, m3 = runge(v3, TT3, h3, fi3, m3, time3, F3)
            time3 += sh
            mTT3.append(TT3 * 180 / pi)
            mh3.append(h3)
            mtt3.append((tt2 + TET2 * (time3 - t2)) * 180 / pi)
            mt3.append(time3)
            ml3.append(fi3 * 0.18 / pi * R)
            if (h3<90000):
                return 0,0,0,0,0,0,0,0,0,False
        return mTT3, mh3, mt3, mtt3, ml3, h3, m3, TT3, fi3, v3
    def alpha(t):
            a = 0.14
            if t <= tv:
                return 0
            else:
                return 4 * ae * exp(a * (tv - t)) * (1 - exp(a * (tv - t)))
    def F1(V, tetta, H, fi, m, t):
            plot, davl, skzv = inte(H, height, Roh), inte(H, height, Ph), inte(H, height, Ah)
            Mah = V / skzv
            if V == 0 or t <= tv:
                return (((p1 - davl * s1) * cos(alpha(t) * pi / 180) - cx1(Mah,
                                                                               H) * plot * sm1 * V ** 2 / 2) / m - gc \
                            * sin(tetta) / (1 + H / R) ** 2) * sh, \
                           0, \
                           V * sin(tetta) * sh, \
                           0, \
                           -mc1 * sh
            else:
                return (((p1 - davl * s1) * cos(alpha(t) * pi / 180) - cx1(Mah,H) * plot * sm1 * V ** 2 / 2) / m - gc \
                            * sin(tetta) / (1 + H / R) ** 2) * sh, \
                           1 / V * (((p1 - davl * s1) * sin(alpha(t) * pi / 180) + cy1(
                               Mah) * plot * sm1 * V ** 2 / 2 * alpha(t) * pi / 180) / m - (gc * cos(tetta) / (1 + H / R) ** 2
                                                                   * (1 - V ** 2 / 7900 ** 2 * (1 + H / R)))) * sh, \
                           V * sin(tetta) * sh, \
                           V * cos(tetta) / (R + H) * sh, \
                           -mc1 * sh
    def F2(V, tetta, H, fi, m, t):

        plot, davl, skzv = inte(H, height, Roh), inte(H, height, Ph), inte(H, height, Ah)
        Mah = V / skzv
        return (((p2 - davl * s2) * cos(tt1 + TET1 * (t - t1) - tetta + fi) - cx2(Mah,
                                                                                 H) * plot * sm2 * V ** 2 / 2) / m - gc * sin(
            tetta) / (1 + H / R) ** 2) * sh, \
               1 / V * (((p2 - davl * s2) * (
                       tt1 + TET1 * (
                       t - t1) - tetta + fi) + cy2 * plot * sm2 * V ** 2 / 2 * alpha(
                   t) * pi / 180) / m -
                        (gc * cos(tetta) / (1 + H / R) ** 2 * (
                                1 - V ** 2 / 7900 ** 2 * (1 + H / R)))) * sh, \
               V * sin(tetta) * sh, \
               V * cos(tetta) / (R + H) * sh, \
               -mc2 * sh
    def F3(V, tetta, H, fi, m, t):

        plot, davl, skzv = inte(H, height, Roh), inte(H, height, Ph), inte(H, height, Ah)
        Mah = V / skzv
        return (((p22 - davl * s22) * cos(tt2 + TET2 * (t - t1) - tetta + fi) - cx2(Mah,
                                                                                   H) * plot * sm2 * V ** 2 / 2) / m - gc * sin(
            tetta) / (1 + H / R) ** 2) * sh, \
               1 / V * (((p22 - davl * s22) * (
                       tt2 + TET2 * (
                       t - t1) - tetta + fi) + cy2 * plot * sm2 * V ** 2 / 2 * alpha(
                   t) * pi / 180) / m -
                        (gc * cos(tetta) / (1 + H / R) ** 2 * (
                                1 - V ** 2 / 7900 ** 2 * (1 + H / R)))) * sh, \
               V * sin(tetta) * sh, \
               V * cos(tetta) / (R + H) * sh, \
               -mc22 * sh
    def runge(v, TT, h, fi, m, t,F):
        cf1 = F(v, TT, h, fi, m, t)
        cf2 = F(v + cf1[0] / 2, TT + cf1[1] / 2, h + cf1[2] / 2, fi + cf1[3] / 2, m + cf1[4] / 2,
                t + sh / 2)
        cf3 = F(v + cf2[0] / 2, TT + cf2[1] / 2, h + cf2[2] / 2, fi + cf2[3] / 2, m + cf2[4] / 2,
                t + sh / 2)
        cf4 = F(v + cf3[0], TT + cf3[1], h + cf3[2], fi + cf3[3], m + cf3[4], t + sh)
        A = [v, TT, h, fi, m]
        for el in range(len(A)):
            A[el] += (cf1[el] + 2 * cf2[el] + 2 * cf3[el] + cf4[el]) / 6
        return A[0], A[1], A[2], A[3], A[4]

    for k in range(-int(ae1 * 1000000), -int(ae2 * 1000000), -int(hal * 1000000)):

        sh = 1
        ae = -k / 10 ** 6
        mTT1, mh1, mt1, mtt1, ml1, time1, h1, v1, m1, TT1, fi1, tt1 = polet1()
        m1 -= md1
        sh = 5
        v3,h3=0,0
        TET11, TET21 = tt11,tt12
        v= 0
        self.textEdit_48.setText(str(-k / 10 ** 6))
        while (abs(v3 - (398600.44 * 10 ** 9 / (R + h3)) ** 0.5) > deltav):
                TET1 = (TET11 + TET21) / 2
                self.textEdit_49.setText(str(TET1 / pi * 180))
                TT3 = deltatt + 1
                mTT2, mh2, mt2, mtt2, ml2, time2, h2, v2, m2, TT2, fi2, tt2 = polet2(time1, h1, v1, m1, TT1, fi1, tt1, TET1)
                TET12, TET22 = tt21, tt22
                w=0
                while (abs(TT3) / pi * 180 > deltatt):
                    TET2 = (TET12 + TET22) / 2
                    self.textEdit_50.setText(str(TET2 / pi * 180))
                    mTT3, mh3, mt3, mtt3, ml3, h3, m3, TT3, fi3, v3 = polet3(time2, h2, v2, m2, TT2, fi2, tt2, TET2)
                    if v3 == False:
                        break
                    if (TT3 > 0):
                        TET12 = TET2
                    else:
                        TET22 = TET2
                    w+=1
                    if (w>20):
                        break
                    QCoreApplication.processEvents()
                if (v3 - (398600.44 * 10 ** 9 / (R + h3)) ** 0.5 > 0):
                    TET21 = TET1
                else:
                    TET11 = TET1
                if (v == 15):
                    break
                v += 1
        if (abs(v3 - (398600.44 * 10 ** 9 / (R + h3)) ** 0.5) < deltav and abs(TT3) / pi * 180 < deltatt):
                desi.Ui_MainWindow.plot(self, [mTT1 + mTT2 + mTT3, mh1 + mh2 + mh3, mtt1 + mtt2 + mtt3, mt1 + mt2 + mt3,
                                           ml1 + ml2 + ml3])
                self.consoletext.setText(self.consoletext.toPlainText() + "αэкс=" + str(-k / 10 ** 6) + "°   ϑ1`=" + str(
                TET1) + "°/сек  ϑ2`=" + str(TET2) + "°/сек\nH=" + str(h3) + "м  θ=" + str(TT3) + "°  V=" + str(
                v3) + "м/с  dV=" + str(abs(v3 - (398600.44 * 10 ** 9 / (R + h3)) ** 0.5)) + "м/с\n" + "\n")
        QCoreApplication.processEvents()
