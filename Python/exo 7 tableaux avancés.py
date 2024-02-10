def elt_max(tab) -> int:
    elt_max = tab[0]
    for elt_tab in tab:
        if elt_tab > elt_max:
            elt_max = elt_tab
    return elt_max

def minima(tab) -> int:
    elt_min = tab[0]
    for elt_tab in tab:
        if elt_tab < elt_min:
            elt_min = elt_tab
    return elt_min

def max_minima(tab: list) -> int:
    elt_min = []
    for elt_tab in tab:
        elt_min.append(minima(elt_tab))
    
    value_max = elt_max(elt_min)
    return value_max
            

print(max_minima([[5, 4, 8, 3], [1, 9, 6, 4], [7, 3, 5, 2], [4, 6, 2, 8]]))