class Kisi: # Kisi bilgileri sınıfı
    def __init__(self): # Nesnedeki, değişkenleri set eden bir metottur.
        self.name = 'Serdar Unlu'
        self.cinsiyet = 'Erkek'
        self.yas=26

is_kisi = Kisi()

class Adres: # Adres bilgilerini sınıfı
    def __init__(self):
        #adres nitelikleri (attributes)
        self.isim = " "
        self.adres = " "
        self.ulke = " "
        self.sehir = " "
        self.ilce = " "
        self.postaKodu = " "

# Bir is adresi yarat
is_adresi = Adres()

# bu adresicin alanlari doldur
is_adresi.isim= "İs adresi"
is_adresi.adres = ""
is_adresi.ulke= "Turkiye"
is_adresi.sehir= "Ankara"
is_adresi.ilce = ""
is_adresi.postaKodu= "06100"

ev_adresi = Adres()

# bu adresicin alanlari doldur
ev_adresi.isim= "Ev adresi"
ev_adresi.adres = ""
ev_adresi.ulke= "Turkiye"
ev_adresi.sehir= "Ankara"
ev_adresi.ilce = ""
ev_adresi.postaKodu= "06100"

print(is_kisi.name, "beyin ev adresi: " + ev_adresi.ulke, "İs adresi ise: "+ is_adresi.sehir)
