d = """
3
7 4
2 4 6
8 5 9 3 
"""

tum_satirlar = [satir.split() for satir in d.split('\n')][1:-1]
toplam = 0
print(tum_satirlar)
for i,satir in enumerate(tum_satirlar):
    print(i,satir)

def sum_bizarre(tum_satirlar):
    flag = 0
    toplam = 0

    for i,satir in enumerate(tum_satirlar):
        if flag > 0 :
            satir =satir[flag - 1 : flag + 2]
            mod = 0
        else :
            satir =satir[flag: flag +2]
            mod = 1
        satir =[int(eleman)for eleman in satir]
        if mod :
            secilen_sayi = max(satir)
        else :
            secilen_sayi = min(satir)
        toplam+= secilen_sayi
        flag = satir.index(secilen_sayi)

    print(toplam)

sum_bizarre(tum_satirlar)