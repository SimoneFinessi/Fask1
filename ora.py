import datetime
adesso = int(datetime.datetime.now().time().hour)


if adesso >=0:
    buon="buongiorno"
elif adesso>=12:
     buon="buon pranzo"
elif adesso>=16:
     buon="buon pomeriggio"
elif adesso>=19:
     buon="buona cena"
elif adesso>=22:
     buon="buona notte"
print(buon)
print(adesso)