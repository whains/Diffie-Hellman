# Lab 4

p = 3270109567857046576197891860617191428821193465503094783988113943420401667148530068844326167420301738751072921517518613328414770184363055804417224694443
print("p: \n" + str(p) + "\n")

a = 2728161051867526546738253503055490376799804281267477573620035266923568764268138521523138281542337226756141006697492437805059205777679802493935211904526
print("a: \n" + str(a) + "\n")

g = 5
print("g: \n" + str(g) + "\n")


def modularExponentiation(g, a, p):
    result = 1
    while a != 0:
        if a & 0x01:
            result = result * g % p
        a = a >> 1
        g = g * g % p
    return result


print("Our A result: \n" + str(modularExponentiation(g, a, p)) + "\n")

# Paste computer result here
computerResult = 88085122626591916891799750503271326419311359872927691074564823053555046819386816213832008494730985079682334694063546153353265408913522948110663590780
print("Computer's B result: \n" + str(computerResult) + "\n")

print("The secret key: \n" + str(modularExponentiation(computerResult, a, p)) + "\n")

