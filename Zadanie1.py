import math

def fun(dlugoscPodlogi, szerokoscPodlogi, dlugoscPanel, szerokoscPanel, pakietPaneli):
    wielkoscPodlogi = (dlugoscPodlogi*szerokoscPodlogi)
    wielkoscPodlogi += wielkoscPodlogi*0.1
    wielkoscPanelu = (dlugoscPanel*szerokoscPanel)
    iloscPaneli = wielkoscPodlogi/wielkoscPanelu
    iloscPaneli=math.ceil(iloscPaneli)
    iloscPaneli/=pakietPaneli
    iloscPaneli = math.ceil(iloscPaneli)
    return iloscPaneli


dlPodlogi = input("Podaj dlugosc podlogi")
dlPodlogi = float(dlPodlogi)
szPodlogi = input("Podaj szerokosc podlogi")
szPodlogi = float(szPodlogi)
dlPaneli = input("Podaj dlugosc paneli")
dlPaneli = float(dlPaneli)
szPaneli = input("Podaj szerokosc paneli")
szPaneli = float(szPaneli)
iloscPakietow = input("Ilosc pakietow")
iloscPakietow = float(iloscPakietow)

print("Ilosc paneli w: ", fun(dlPodlogi, szPodlogi, dlPaneli, szPaneli,iloscPakietow))