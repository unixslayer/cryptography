
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str = raw_input("Message: ")

n = len(str)

for shift in range(26):
    out = ""
    for i in range(n):
        c = str[i]
        loc = alpha.find(c)
        newloc = (loc + shift)%26
        out += alpha[newloc]

    print "{shift}: {out}".format(shift=shift, out=out)
