class Ucus():
   
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
        self.ucak_tipi = 777

    def anons_kalkis(self):
        print(ucus1.kalkis + " 'dan " + ucus1.varis + " 'ya seyahat edecek olan " + ucus1.kod + " 'no'lu seyahat yolcuları uçağınız kalkışa hazırdır. "  )
    def ucak_tipi_degisim(self, update):
        self.ucak_tipi = update
    
ucus1 = Ucus("tk101","IST","ANK",60,175,125)
print(ucus1.anons_kalkis())
ucus1.ucak_tipi_degisim(737)
