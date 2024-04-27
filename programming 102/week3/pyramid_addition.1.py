d = """
3
7 4
2 4 6
8 5 9 3
"""
tum_satirlar = [satir.split() for satir in d.split('\n')][1:-1]
toplam=0
print(tum_satirlar)
for i,satir in enumerate(tum_satirlar):
    print(i,satir)


def sum_min_per_line(tum_satirlar):
    flag = 0
    toplam = 0
    
    for satir in tum_satirlar :
        if flag > 0 :
            satir =satir[flag-1 : flag+2]
        else :
            satir= satir[flag:flag+2]
        satir= [int(eleman) for eleman in satir]
        en_kucuk=min(satir)
        toplam+=en_kucuk
        flag = satir.index(en_kucuk)
        
    print(toplam)


sum_min_per_line(tum_satirlar)


