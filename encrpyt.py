def encrpyt(txt):
    f=""
    for i in txt: 
        if ord(i) >= ord("A") and ord(i)<= ord('Z'):
            if ord(i)==ord("Z"):
                form=ord(i)-3
            else:
                form=ord(i)+3
            form=chr(form)
            f=f+form 
        if ord(i) >= (ord("a")) and ord(i)<= ord('z'):
            if ord(i)==ord("z"):
                form=ord(i)-3
            else:
                form=ord(i)+3
            form=chr(form)
            f=f+form 
    return f 
def decrpyt(txt):
    f=""
    for i in txt: 
        if ord(i) >= ord("A") and ord(i)<= ord('Z'):
            if ord(i)==(ord("Z")-3):
                form=ord(i)+3
            else:
                form=ord(i)-3
            form=chr(form)
            f=f+form  
        if ord(i) >= (ord("a")) and ord(i)<= ord('z'):
            if ord(i)==(ord("z")-3):
                form=ord(i)+3
            else:
                form=ord(i)-3
            form=chr(form)
            f=f+form
    return f 
print("Encrypted code: ",encrpyt("ABCZ"))
print("Decrypted code: ",decrpyt(encrpyt("ABCZ")))