import math

def beregn_score(valg_spiller1, valg_spiller2): 

    if((valg_spiller1 == "svik") and (valg_spiller2 == "svik")):
        return [1, 1]
    if((valg_spiller1 == "samarbeid") and (valg_spiller2 == "svik")):
        return [0, 5]
    if((valg_spiller1 == "svik") and (valg_spiller2 == "samarbeid")):
        return [5, 0]
    if((valg_spiller1 == "samarbeid") and (valg_spiller2 == "samarbeid")):
        return [3, 3]

def spill_snilt(motstanderens_valg): 
    counter = 0

    if(len(motstanderens_valg) == 0): 
        return "samarbeid"

    for valg in motstanderens_valg: 
        if (valg == "svik"): 
            counter += 1 
    
    if (counter >= math.ceil(len(motstanderens_valg) / 2)): 
        return "svik"
    else: 
        return "samarbeid"

def spill_slemt(motstanderens_valg): 
    counter = 0

    if(len(motstanderens_valg) == 0): 
        return "samarbeid"

    if(len(motstanderens_valg) >= 5):
        return "samarbeid"

    for valg in motstanderens_valg: 
        if (valg == "svik"): 
            counter += 1 
    
    if (counter >= math.ceil(len(motstanderens_valg) / 2)): 
        return "svik"
    else: 
        return "svik"

def utfoer_spill():
    mostander1_valg = []
    mostander2_valg = []
    score_spiller1 = 0 
    score_spiller2 = 0 

    count = 0 
    choice = str(input("Press any button to continue, or enter q to quit the game: "))
    while(choice != "q"): 
        while (count < 11): 
            valg1 = spill_snilt(mostander2_valg)
            valg2 = spill_slemt(mostander1_valg)

            mostander1_valg.append(valg2)
            mostander2_valg.append(valg1)

            score1, score2 = beregn_score(valg1, valg2)
            
            score_spiller1 += score1
            score_spiller2 += score2
            print(score_spiller1)
            count += 1
        count = 0 
        choice = str(input("Press any button to continue, or enter q to quit the game: "))
    
    if (score_spiller1 > score_spiller2): 
        print(f'Spiller nr.1 vant, med poeng-differanse lik {score_spiller1-score_spiller2}')
    elif (score_spiller1 < score_spiller2): 
        print(f'Spiller nr.2 vant, med poeng-differanse lik {score_spiller2-score_spiller1}')
    else: 
        print(f'Uavgjort, poengsum {score_spiller1}')



if __name__ == '__main__': 

    utfoer_spill()