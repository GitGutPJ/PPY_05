import math

def calc(dlugoscPodlogi, szerokoscPodlogi, dlugoscPanel, szerokoscPanel, pakietPaneli):
    wielkoscPodlogi = (dlugoscPodlogi*szerokoscPodlogi)
    wielkoscPodlogi += wielkoscPodlogi*0.1
    wielkoscPanelu = (dlugoscPanel*szerokoscPanel)
    iloscPaneli = wielkoscPodlogi/wielkoscPanelu
    iloscPaneli=math.ceil(iloscPaneli)
    iloscPaneli/=pakietPaneli
    iloscPaneli = math.ceil(iloscPaneli)
    return iloscPaneli

print("Ilosc paneli w: "+ str(calc(4, 4, 0.2, 1,10)))