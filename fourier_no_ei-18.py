print(a * np.cos(beta) * (N / 2.), a * np.sin(beta) * (N / 2.))
# 21.7726138284 42.7779532829
vec_v = a * np.cos(vec_r_1 + beta)
np.fft.fft(vec_v)
# array([ -0.0000 +0.j   ,  21.7726+42.778j,   0.0000 +0.j   ,
# 0.0000 +0.j   ,   0.0000 +0.j   ,   0.0000 +0.j   ,
# -0.0000 +0.j   ,   0.0000 -0.j   ,  -0.0000 -0.j   ,
# -0.0000 +0.j   ,  -0.0000 -0.j   ,   0.0000 +0.j   ,
# -0.0000 +0.j   ,   0.0000 -0.j   ,   0.0000 +0.j   ,
# 0.0000 +0.j   ,  -0.0000 +0.j   ,   0.0000 +0.j   ,
# 0.0000 -0.j   ,   0.0000 +0.j   ,  -0.0000 -0.j   ,
# 0.0000 +0.j   ,  -0.0000 +0.j   ,   0.0000 +0.j   ,
# -0.0000 +0.j   ,  -0.0000 +0.j   ,  -0.0000 -0.j   ,
# -0.0000 +0.j   ,   0.0000 -0.j   ,  -0.0000 +0.j   ,
# 0.0000 -0.j   ,  21.7726-42.778j])