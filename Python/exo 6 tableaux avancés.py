def elt_max(tab) -> int:
    elt_max = tab[0]
    for elt_tab in tab:
        if elt_tab > elt_max:
            elt_max = elt_tab
    return elt_max

print(elt_max([-6, -9, -997, -12]))