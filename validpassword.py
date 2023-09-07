def validpassword(password):
    result = []
    lenth = lower = upper = number = False
    for i in password:
        if len(password) >= 8:
            lenth = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if i.isdigit():
            number = True
    result.append(lenth)
    result.append(lower)
    result.append(upper)
    result.append(number)

    return all(result)


# Main program :
UserPassword = "limu#2022"
print(validpassword(UserPassword))

# -----------***-----------
# -----------***-----------
'''
# Another Solution :
def iflenth(password):
    if len(password) >= 8:
        return True
# --------
def iflower(password):
    for i in password:
        if i.islower():
            return True
# --------
def ifupper(password):
    for i in password:
        if i.isupper():
            return True
# --------
def ifdigit(password):
    for i in password:
        if i.isdigit():
            return True
# --------
def ifvalid(password):
    upper = ifupper(password)
    lenth = iflenth(password)
    lower = iflower(password)
    digit = ifdigit(password)
    result = [upper, lenth, lower, digit]
    return all(result)
# Main Program :
UserPassword = "Limu#2022"
print(ifvalid(UserPassword))
#
'''
