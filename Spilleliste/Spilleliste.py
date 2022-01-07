from Sang import Sang
class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
    
    def lesFraFil(self, filnavn):
        infile = open(filnavn, 'r')
        for infile1 in infile:
            alleData = infile1.strip().split(';')
            (self._sanger).append(Sang(alleData[1], alleData[0]))
        infile.close()     
        
    def spillSang(self, sang):
        sang.spill()
    
    def spillAlle(self):
        låter = self._sanger
        for i in range(0, len(låter)):
           låter[i].spill()
           
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)
     
    def fjernSang(self, sang):
        self._sanger.remove(sang)
        
    def finnSang(self, tittel): 
        låta = self._sanger
        for i in range(0, len(låta)):
            if låta[i].sjekkTittel(tittel): 
                return låta[i]
            
    def hentArtistUtvalg(self, artistnavn):
        låt = self._sanger
        queenListe = []
        for i in range(0, len(låt)):
            if låt[i].sjekkArtist(artistnavn):
                queenListe.append(låt[i])
        return queenListe 
    
