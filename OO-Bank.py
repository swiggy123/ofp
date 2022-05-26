# %% Create Class
from datetime import datetime
import itertools
#%%
class kontos():
    minimum_kontostand = 0
    def __init__(self,kennung:int):
        self.kennung = kennung
        self.saldo = 0
        self.buchungshistorie = {}
    def bareinzahlung(self,betrag):
        self.saldo += betrag
        self.buchungshistorie[datetime.today()] = ("Bareinzahlung",betrag)
    def letzte_buchung_prüfen(self,anzahl_buchungen):
        return dict(itertools.islice(sorted(self.buchungshistorie.items(),reverse=True), anzahl_buchungen))
        
    def abbuchen_konto(self,betrag,konto_gutschrift,minimum_kontostand= minimum_kontostand):
        if self.saldo - minimum_kontostand > betrag:
            self.saldo -= betrag
            self.buchungshistorie[datetime.today()] = ("Belastung",-betrag,konto_gutschrift)
        else:
            print(betrag)
            raise ValueError
    def gutschrift(self,betrag,belastungskonto):
        self.saldo += betrag
        self.buchungshistorie[datetime.today()] = ("Gutschrift",betrag,belastungskonto)
class jugendkonto(kontos):
    pass
class privatkonto(kontos):
    abbuchgebühr = 0.01
    def abbuchen_konto(self, betrag,konto_gutschrift,abbuchgebühr, minimum_kontostand=-1000):
        super().abbuchen_konto((1 + abbuchgebühr)*betrag,konto_gutschrift, minimum_kontostand)
        
class sparkonto(kontos):
    pass
class bankkonto(kontos):
    pass


# %%
class OO_Bank(jugendkonto,privatkonto,sparkonto,bankkonto):
    def __init__(self,saldo_konto) -> None:
        self.bankkonto = bankkonto(1)
        self.bankkonto.saldo = saldo_konto
        self.konto = {}
        self.kennummer_kontos = 10

    def create_konto(self,kontotyp):
        if kontotyp == "Jugendkonto":
            self.konto[self.kennummer_kontos] = jugendkonto(self.kennummer_kontos)
        elif kontotyp == "Privatkonto":
            self.konto[self.kennummer_kontos] = privatkonto(self.kennummer_kontos)
        elif kontotyp == "Sparkonto":
            self.konto[self.kennummer_kontos] = sparkonto(self.kennummer_kontos)
        else:
            return "Der Kontotyp ist nicht vorhanden"
        self.kennummer_kontos +=1

    def bareinzahlung(self, kennung, Barbetrag):
        if kennung in self.konto and Barbetrag > 0:
            self.konto[kennung].bareinzahlung(Barbetrag)
        else:
            print("Kennung unbekannt oder Barbetrag negativ")
    
    def check_saldo(self,kennung):
        return self.konto[kennung].saldo
    
    def konto_löschen(self,kennung):
        if self.check_saldo(kennung) == 0:
            del self.konto[kennung]
        else:
            return "Es hat noch Geld auf dem Konto"
    def letzte_buchung_prüfen(self, kennung,anzahl_buchungen=1):
        return self.konto[kennung].letzte_buchung_prüfen(anzahl_buchungen)
    def buchung_von_konto(self,kennung_belastungskonto:int,kennung_gutschrift_konto:int,betrag:float):
        try:
            self.konto[kennung_belastungskonto].abbuchen_konto(betrag,kennung_gutschrift_konto)
            self.konto[kennung_gutschrift_konto].gutschrift(betrag,kennung_belastungskonto)
        except:
            print("kontostand ist zu klein")
        if isinstance(self.konto[kennung_belastungskonto],privatkonto):
            self.bankkonto.gutschrift(privatkonto.abbuchgebühr * betrag,kennung_belastungskonto)
        
            


# %%
bank_object=OO_Bank(1000)
# %%
bank_object.create_konto("Jugendkonto")
bank_object.create_konto("Privatkonto")
bank_object.create_konto("Sparkonto")
# %%
bank_object.bareinzahlung(10,1000)
bank_object.bareinzahlung(11,400)
bank_object.bareinzahlung(12,700)
#%%
bank_object.check_saldo(11)

# %%
bank_object.buchung_von_konto(11,10,100)
# %%
bank_object.check_saldo(11)
# %%
bank_object.letzte_buchung_prüfen(11,2)

# %%
bank_object.bareinzahlung(11,400)
# %%
bank_object.bareinzahlung(11,700)
bank_object.letzte_buchung_prüfen(11)
# %%

youth=jugendkonto(10)
# %%
youth.bareinzahlung(10000)
# %%
youth.abbuchen_konto(1000,11,0)
# %%
