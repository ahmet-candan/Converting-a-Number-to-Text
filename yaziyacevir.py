def yaziya_donustur(deger):
    birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Atmış","Yetmiş","Seksen","Doksan"]
    
    
    a = deger%10
    b = deger//10
    

    return onlar[b] + " " + birler[a]


while True:
    girdi = input("Yazıya Çevirmek İstediğiniz İki Basamaklı Sayıyı Girin, Çıkmak İçin q'ya Basabilirsiniz:")
    if (girdi=="q"):
        print("Çıkış Yapılıyor")
        break
    else:
        girdi=int(girdi)
        print("Sayının Yazıya Dönüştürükmüş Hali: ",yaziya_donustur(girdi))