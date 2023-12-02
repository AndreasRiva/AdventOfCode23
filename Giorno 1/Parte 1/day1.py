f = open("input.txt", "r").read()   # Apre il file ed esegue un cast da TextIoWrapper a String
somma = 0   # Soluzione finale

for linea in f.split("\n"): # Split per tutte le linee del file
    numeri = [] # Lista per i numeri presenti per ogni linea
    for carattere in linea: # Foreach sui singoli caratteri
        if carattere.isdigit(): # Se il singolo carattere è numerico
            numeri.append(carattere)    # Viene aggiunto alla lista numeri
    somma += int(numeri[0] + numeri[-1])    # Concatenazione della stringa con primo e ultimo elemento della lista numeri
                                            # Questa stringa verrà poi castata ad Int ed aggiunta a Somma
print(somma)    # Stampa della somma
