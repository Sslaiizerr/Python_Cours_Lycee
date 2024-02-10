def bissextile(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    else:
        return False


print(bissextile(2020))
print("-------------")
print(bissextile(2021))
print("-------------")
print(bissextile(2022))
print("-------------")
print(bissextile(2023))
print("-------------")
print(bissextile(2024))
