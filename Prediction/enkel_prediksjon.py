import random 

def enkel_prediskjon():
    gender = str(input("Enter your gender:" )).lower()
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    martial_stat = str(input("Enten your current martial: ")).lower()
    debt = int(input("Enter the debt you have amassed: "))
    print(f' Du er en {martial_stat} {gender} på omtrent {age} år med {debt} kr i gjeld')

    if((gender == "mann") and (age < 30) and (debt > 100000) and (martial_stat == "singel")): 
        print(f'{name}, basert på vår predikasjon kommer ikke du til å betale gjelden din \n', 
        f'tilsvarende en sum lik {debt} kr')
    elif((gender == "mann") and (age < 25) and (debt > 200000)): 
        print(f'{name}, basert på vår prediksjon kommer ikke du til å betale gjelden din \n', 
        f'tilsvarende en sum lik {debt} kr')
    elif((gender == "kvinne") and (martial_stat == "singel") and (age < 28) and (debt > 300000)):
        print(f'{name}, basert på vår prediksjon kommer ikke du til å betale gjelden din\n', 
        f'tilsvarende en sum lik {debt} kr')
    else: 
        print(f'{name}, ifølge vårt estimat kommer du til å betale gjedlen din')

def prediksjon_med_historikk(): 
    gender = str(input("Enter your gender: ")).lower()
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    martial_stat = str(input("Enten your current martial: ")).lower()
    debt = int(input("Enter the debt you have amassed: "))
    utdanning = str(input("Enter level of education: "))
    customer_iD = random.randrange(100, 100000)

    inntekt = 0

    """Utdanningsnivå skal oppgis som: ukjent, grunnskole, hoeyskole, universitet"""

    betallingshistorikk = []
    utdannings_niva = dict()
    utdannings_niva["ukjent"] = 300000
    utdannings_niva["grunnskole"] = 260000
    utdannings_niva["hoeyskole"] = 500000
    utdannings_niva["universitet"] = 700000

    """Forventet input fra brukeren for spørsmålet om betallingshistorikk er: 
       betalt eller ikke_betalt """

    forste_maned = str(input("Enter b for 'betalt' or i for 'ikke_betalt': "))
    if(forste_maned == "b"): 
        forste_maned = "betalt"
    else: 
        forste_maned = "ikke_betalt"
    betallingshistorikk.append(forste_maned)
    andre_maned = str(input("Enter b for 'betalt' or i for 'ikke_betalt': "))
    if(andre_maned == "b"): 
        andre_maned = "betalt"
    else: 
        andre_maned = "ikke_betalt"
    betallingshistorikk.append(andre_maned)
    fjerde_maned = str(input("Enter b for 'betalt' or i for 'ikke_betalt': "))
    if(fjerde_maned == "b"): 
        fjerde_maned = "betalt"
    else: 
        fjerde_maned = "ikke_betalt"
    betallingshistorikk.append(fjerde_maned)

    counter = 0
    for maned in betallingshistorikk: 
        if(maned == "ikke_betalt"): 
            counter += 1  
    
    
    if((gender == "mann") and (utdannings_niva.get(utdanning) > 3*debt)): 
        print(f'{name}, basert på opplysningene du har gitt oss, antar vi at du kommer '
              f'til på betale ned gjelden din')
    elif(counter >= 2): 
        print(f'{name}, basert på din tidligere betallingshistorikk antar vi at du',
        f'ikke kommer til å betale ned gjelden din')
    elif((gender == "mann") and (age < 30) and (debt > 100000) and (martial_stat == "singel")): 
        print(f'{name}, basert på vår predikasjon kommer ikke du til å betale gjelden din \n', 
        f'tilsvarende en sum lik {debt} kr')
    elif((gender == "mann") and (age < 25) and (debt > 200000)): 
        print(f'{name}, basert på vår prediksjon kommer ikke du til å betale gjelden din \n', 
        f'tilsvarende en sum lik {debt} kr')
    elif((gender == "kvinne") and (martial_stat == "singel") and (age < 28) and (debt > 300000)):
        print(f'{name}, basert på vår prediksjon kommer ikke du til å betale gjelden din\n', 
        f'tilsvarende en sum lik {debt} kr')
    else: 
        print(f'{name}, ifølge vårt estimat kommer du til å betale gjedlen din')

    bestem_laan(customer_iD)

def bestem_laan(customer_iD): 
    iD_numbers = dict()
    file1 = open("iD.txt", "r") 
    lines = file1.readlines()
    for iD in lines: 
        iD_numbers[int(iD)] = int(iD)
    
    if(iD_numbers.__contains__(customer_iD)):
        print(f'{customer_iD} kan ikke få tildelt lån.')
    else: 
        print(f'Kunde med iD {customer_iD} er ikke på svartlisten, og kan dermed få tildelt lån',
                'dersom innsyn i tidligere historikk, økonomi og nåværende arbeidssituasjon virker lovende.')






if __name__ == '__main__': 
    #enkel_prediskjon()
    prediksjon_med_historikk()

    
