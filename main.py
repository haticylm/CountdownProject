import time


zaman = input("Zamanı dakika ve saniye olarak arada boşluk koyarak girin:\n ")
dk, sn = zaman.split()

dk = int(dk)
sn = int(sn)
sn += dk * 60

for sayac in range(sn,-1,-1):
    print(sayac)
    if sayac == 0:
        print("~~~SÜRE DOLDU~~~")
    else:
        pass
    time.sleep(1)



