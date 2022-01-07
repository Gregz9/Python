class Sang: 
    def __init__(self, artist, tittel):
        self._artist = artist 
        self._tittel = tittel
    
    def spill(self):
        sang = print('Spiller ' + self._tittel + ' av ' + self._artist)
        sang

    def sjekkArtist(self, navn):
        name1 = navn.split(' ')
        sjekk = self._artist.split(' ')
        for i in range(0, len(name1)):
            if name1[i] in sjekk:
                return True
            
       
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower(): 
            return True
        
        
    def sjekkArtistOgTittel(self, artist, tittel):
        tittelSjekk = self.sjekkTittel(tittel)
        artistSjekk = self.sjekkArtist(artist)
        if tittelSjekk and artistSjekk:
            return True
        
