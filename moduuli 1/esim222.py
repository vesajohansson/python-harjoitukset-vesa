ostoslista = ["maito","rahka","juusto","leipä","kahvi"]

while ostoslista:
    tuote = input("minkä tuotteen ostit?")

    if tuote in ostoslista:
        ostoslista.remove(tuote)
        print("jäljellä olevat tuotteet", ostoslista)
    else:
        print("tuotetta ei ole listalla! ")
