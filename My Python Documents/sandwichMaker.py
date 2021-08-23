## This programs ask for user about their sandwich preferences

import pyinputplus as pyip
print('Subway Erim\'e Hoşgeldiniz.\nSipariş vermek için herhangi bir tuşa basınız.')
promt = input()

totalPrice = 0.0
fiyat_listesi = {'buğday': 3.0,'beyaz': 2.0,'ekşi maya':3.5,
'Tavuk': 5.0,'Hindi': 6.0,'Jambon': 6.5,'Tofu': 5.5,
'Çedar': 2.5,'Beyaz': 2.0,'Kaşar': 3.0,
'Mayonez':0.25,'Hardal':0.25,'Marul':0.30,'domates':0.50}

# To allow for different sandwiches in the order

while True:
    #Make an empty dict to store the order details - reset order in the event of a second order
    order = {}
    print('Lütfen ekmek türünü seçiniz?\n')
    order['bread'] = pyip.inputMenu(['beyaz','buğday','ekşi maya'],numbered=True)
    print('Lütfen hangi eti tercih ettiğinizi seçiniz?\n')
    order['protein'] = pyip.inputMenu(['Tavuk','hindi','Jambon','Tofu'],numbered=True)
    wantCheese = pyip.inputYesNo('Peynir eklemek ister misiniz? \n',yesVal='evet',noVal='hayır')
    if wantCheese == 'evet':
        order['side'] = pyip.inputMenu(['Çedar','Beyaz','Kaşar'],numbered=True)
    wantDressing = pyip.inputYesNo('Extra olarak birşey eklemek ister misiniz?\n',yesVal='evet',noVal='hayır')
    if wantDressing == 'evet':
        order['side'] = pyip.inputMenu(['mayonez','Hardal','Marul','Domates'],numbered=True)
    orderNumber = pyip.inputInt('Kaç adet sandviç istersiniz?\n',min=1)
    #Calculate the cost order
    for choice in order:
        if order[choice] in fiyat_listesi.keys():
            totalPrice += fiyat_listesi[order[choice]]
    #Adjust if more than one
    totalPrice *= orderNumber
    anotherOrder = pyip.inputYesNo('Hepsi bu kadar mı?\n',yesVal='evet',noVal='hayır')
    if anotherOrder =='evet':
        break

# The string.format forces 2 decimal places (eg: 13.10 rather than 13.1)
print('Tamam, toplam ücret : ' + '{:.2f}'.format(totalPrice) + ' \nTeşekkürler')
