chiffre = {chr(i + 65): chr((i + 13) % 26 + 65) for i in range(26)}
print('Chiffre = ', chiffre)

message = "BONJOUR, COMMENT ALLEZ-VOUS ?"
ch = ""
for c in message:
    # print('chiffre.get(c, c) = ', chiffre.get(c, c))
    ch = ch + chiffre.get(c, c)
print("ch = ", ch)

message = "OBAWBHE, PBZZRAG NYYRM-IBHF ?"
m = ""
for c in message:
    # print('chiffre.get(c, c) = ', chiffre.get(c, c))
    m = m + chiffre.get(c, c)
print("m = ", m)
