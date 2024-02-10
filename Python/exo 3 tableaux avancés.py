t = [i for i in range(1, 65)]

def transf_tab1dim_tab2dim(t: list) -> list :
    m = [[0]*8 for _ in range(8)]
    for i in range(8):
      for j in range(8):
        m[i][j] = t[i*8+j]
    return m

print(transf_tab1dim_tab2dim(t))