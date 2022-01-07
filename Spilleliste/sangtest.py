from Sang import Sang
def hovedprogram():
    sang1 = Sang('Lady Gaga and Bradley Cooper', 'Shallow')
    
    # Sjekker metoden spill
    print('Spiller av test-objekt: ')
    sang1.spill()
    
    #Sjekker metoden sjekkArtist
    print('Tester sjekkArtist med ''Lady Gaga and Bradley Cooper'' ')
    assert(sang1.sjekkArtist('Lady Gaga and Bradley Cooper'))
    print('Tester sjekkArtist med ''Lord Gaga'' ')
    assert(sang1.sjekkArtist('Lord Gaga'))
    print('Tester sjekkArtist med ''Sadley '' ')
    assert(not sang1.sjekkArtist('Sadley'))
    print('Tester sjekkAritst med ''a'' ')
    assert(not sang1.sjekkArtist('a'))
    
    # Tester metoden sjekkTittel 
    print('Tester sjekkTittel med ''Shallow'' ')
    assert(sang1.sjekkTittel('Shallow'))
    print('Tester sjekkTittel med ''shaLlow'' ')
    assert(sang1.sjekkTittel('shaLlow'))
    print('Tester sjekkTittel med ''Hallow'' ')
    assert(not sang1.sjekkTittel('Hallow'))
    
    # Test av metoden sjekkArtistOgTittel
    print('Tester sjekkTittelOgArtist med ''Bradley Cooper'' og ''Shallow'' ')
    assert(sang1.sjekkArtistOgTittel('Bradley Cooper', 'Shallow'))
    print('Tester sjekkArtistOgTittel med ''Booper'' og ''Shallow'' ')
    assert(not sang1.sjekkArtistOgTittel('Booper', 'Shallow'))

hovedprogram()
