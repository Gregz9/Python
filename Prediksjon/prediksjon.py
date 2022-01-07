# Her er din funksjon med din egen prediksjon
def min_prediksjon(alder, kjonn, sivilstatus, gjeld, betalingshistorikk, utdanningsnivo):
    # ...
    return

# Dette limer du inn under
def test_min_prediksjon():

    antall_predikert = 0
    antall_riktig_predikert = 0

    filnavn = "individer1000.txt"
    fil = open(filnavn)
    for linje in fil:
        data = linje.strip().split(",")
        alder = int(data[1])
        kjonn = data[2]
        sivilstatus = data[3]
        gjeld = int(data[4])
        betalingshistorikk = []
        for i in range(0, 3):
            betalingshistorikk.append(data[5+i])

        utdanningsnivo = data[8]
        fasit = data[9]

        prediksjon = min_prediksjon(alder, kjonn, sivilstatus, gjeld, betalingshistorikk, utdanningsnivo)

        if prediksjon == fasit:
            antall_riktig_predikert += 1

        antall_predikert += 1



    print(antall_riktig_predikert, "av", antall_predikert, "ble riktig predikert")


test_min_prediksjon()