t = [i for i in range(1, 65)]

def transf_tab1dim_tab2dim(t: list) -> list :
  m = [[0]*8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      m[i][j] = t[i*8+j]
  return m

def transf_tab2dim_tab1dim(m) -> list:
  t = []
  for i in range(8):
    for j in range(8):
      t.append(m[i][j])
  return t

print(transf_tab2dim_tab1dim(transf_tab1dim_tab2dim(t)))