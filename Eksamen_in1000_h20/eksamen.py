



def karantene(vaksinert, farge): 

    if(vaksinert): 
        return 0
    elif((not vaksinert) and ((farge == "reod") or (farge == "oransje"))): 
        return 10 
        
    elif((not vaksinert) and (farge == "groenn")) :
        return 3

def tell_grader(fag, bsc, msc):
    
    if((fag.lower() == bsc.lower()) and (fag.lower () == msc.lower())): 
        return 2 
    elif((fag.lower() == bsc.lower()) or (fag.lower () == msc.lower())):
        return 1
    else: 
        return 0

def fjern_vokaler(setning, vokal_liste): 

    for vokal in vokal_liste: 
        setning = setning.replace(vokal, "")
    
    return setning

fjern_vokaler("ha det fint", ["a", "e", "i", "o", "u"])


def summer_rabatt(vareliste, forpris, nypris): 
    sum_spart = 0 
    for vare in vareliste: 
        sum_spart += forpris[vare]-nypris[vare]
        print(forpris[vare])

    return sum_spart

def sjekk_reise(reise): 

    for i in range(1,len(reise)):
        if reise[i-1][1] != reise[i][0]: 
            return False 
        elif reise[i-1][1] == reise[i][0]: 
            continue
    return True
        

class Terter: 

    def __init__(self): 
        self._tekst = {}
        for i in range(0, 7): 
            self._tekst[i] = None 

    def hent_dagens_gave(self, dag): 
        if 24 < dag <= 31: 
            dag = f'{dag}.desember'
        else: 
            dag = f'{dag}.januar'
        print(dag)

# 4a)
class Onske: 
    
    def __init__(self, beskrivelse, antall, minimumpris): 
        self._beskrivelse = beskrivelse
        self._antall = antall 
        self._minimumpris = minimumpris 
    
    def passer(self, maksimumpris): 
        """ Metoden returnerer 'False' om kravene ikke er oppfylt eller self._antall er 0, ellers True"""
        if(maksimumpris > minimumpris or self._antall > 0): 
            return True
        else: 
            return False
    
    def valgt(self): 
        self._antall -= 1
        return self._beskrivelse 
        
    def hent_pris(self): 
        return self._minimumpris
    
    def hent_beskrivelse(self): 
        return self._beskrivelse
        
    def hent_antall(self): 
        return self._antall
    
    def __str__(self): 
        """Merk at dette er en måte Python tillater å formatere en tekststreng på"""
        return f'Denne oensken er: {self._beskrivelse} og koster {self._minimumpris}'
        
# 4b)
class Onskeliste: 
    
    def __init__(self): 
        self._onskeliste = []
        
    def nytt_onske(self, beskrivelse, antall, minmumpris=1000):
        """Legger inn minimumpris som forhaandsbestemt parameter, som kan endres dersom et argumentblir sendt inn når metoden kalles på"""
        onske = Onske(beskrivelse, antall, minimumpris)
        self._onskeliste.append(onske)
    
    def hent_onsker(self, maksimumpris): 
        mulige_gaver = []
        for onske in self._onskeliste: 
            if onske.passer(): 
                str = onske.__str__() 
                mulige_gaver.append[onske.hent_beskrivelse]
            else: 
                mulige_gaver.append['Ikke valgbart oenske']
        
        return mulige_gaver 
            
            
        def onske_oppfylles(self, index): 
            
            index -= 1
            self._onskeliste[index].valgt()
            
            """Index 0 blir for brukeren av metoden argument 1"""

# 4c)
class Gave: 
    
    def __init__(self, beskrivelse, giver): 
        self._beskrivelse = beskrivelse 
        self._giver = giver
        
    def gave_beskrivelse(self): 
        return f'Denne gaven er {self._beskrivelse}, og er fra {self._giver}'

# 4d)
class JuleferieKalender: 
    
    def __init__(self, ant_dager): 
        self._kalender = {}
        for i in range(0,7):
            dag = 25 
            self._kalender[dag] = None
            dag += 1
        if ant_dager > 6: 
            for j in range(7, ant_dager): 
                dag = 1 
                self._kalender[dag] = None
                dag += 1 
                
        
    def ny_gave(self, beskrivelse, giver, dag): 
        gave = Gave(beskrivelse, giver)
        
        self._kalender[dag] = gave 
        
    def hent_dagens_gave(self, dag): 
        
        if self._kalender[dag] != None: 
            if 24 < dag <= 31: 
                dag = f'{dag}.desember: {self._kalender[dag].gave_beskrivelse}'
            else: 
                dag = f'{dag}.januar:  {self._kalender[dag].gave_beskrivelse}'
        else: 
            return f'Ingen gave idag'
        
    def hent_ant_dager(self): 
        return len(self._kalender)
    
    def hent_kalender(self): 
        return self._kalender

# 4e) 

class Julegavefikser: 
    
    def __init__ (self, ant_dager): 
        self._kalender = JuleferieKalender(ant_dager)
        self._onskeliste = Onskeliste()
        self._dag = 25
    
    def les_onsker_fra_fil(self, filnavn): 
        
        fil = open(filnavn, "r")
        linjer = fil.readlines()
        
        for linje in linjer: 
            linje.split(";")
            ny_onske = Onske(linje[0], int(linje[1]), int(linje[2]))
            self._onskeliste.append(onske)

# 4f)    
    def velg_gave(self, maksimumpris):
        mulige_gaver = {}
        i = 1
        for onske in self._onskeliste: 
            if onske.passer(): 
                str =  (f'Dette er onske nr.{i}: {onske.hent_beskrivelse()}, og har pris {onske.hent_pris()')
                mulige_gaver.append[onske.hent_beskrivelse]
            else: 
                mulige_gaver.append[(f'Dette er onske nr.{i}: Ikke valgbart oenske')]
        
        for setning in mulige_gaver: 
            print(setning)
        
        giver_valg = int(input("Oppgi nummeret på onsken du har lyst å oppfylle for Dolly: "))
        
        self._onskelise[giver_valg-1].valgt()
        
        hvilken_dag = int(input("Hvilken dag onsker du at Dolly skal få gaven: "))
        navn = str(input("Hva er navnet ditt? "))
        
        self._kalender.ny_gave(self._onskeliste[giver_valg-1].hent_beskrivelse, navn, hvilken_dag)
        
    def ny_dag(self):
    """Begynte med å legge til en ny variabel i Julegavefikser klassen som jeg kaller dag og gir startverdi lik 25"""
    
        self._kalender.hent_dagens_gave(self._dag)
        
        oppdater_dag()
    
    
    def oppdater_dag(self): 
        """Bruker denne metoden til å oppdater instansvariabelen self._dag"""
        if(self._dag > 31):
            self._dag = 1
        
        self._dag += 1
