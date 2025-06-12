import random
import os

# variabili
GIORNO_ATTUALE = 1
GAME = True
ENERGIA = 10
ENERGIA_MAX = 100
ENERGIA_GIORNALIERA = 1
CIBO = 10
CIBO_MAX = 100
CIBO_GIORNALIERO = 0
PRODUZIONE_CIBO_GIORNALIERA = 0
GUADAGNO_PERDITA_CIBO = [-1, 0, 1]
ACQUA = 10
ACQUA_MAX = 100
ACQUA_GIORNALIERA = 0
PRODUZIONE_ACQUA_GIORNALIERA = 0
GUADAGNO_PERDITA_ACQUA = [-1, 0, 1]
ANIMALI = 0
ANIMALI_MAX = 10
ANIMALI_CIBO = 0
ANIMALI_ACQUA = 0
ANIMALI_PREDATORI = 0
ENERGIA_1 = 3
ENERGIA_2 = 3
ENERGIA_3 = 3
ENERGIA_4 = 3
ENERGIA_5 = 3
ENERGIA_6 = 5
ENERGIA_7 = 4
ENERGIA_8 = 1
ENERGIA_9 = 1
VEGETAZIONE = 0
VEGETAZIONE_MAX = 10
STATO_VEGETAZIONE = False
PERSONE = 3
CASE = 3
DA_DISSETARE = 0
DA_SFAMARE = 0
GIORNI_RIMASTI_ACQUA = 3
GIORNI_RIMASTI_CIBO = 5
SCELTE = f" 1. Coltiva campi, {ENERGIA_1} energia\n 2. Crea pozzi, {ENERGIA_2} energia\n 3. Caccia, {ENERGIA_3} energia\n 4. Pianta piante, {ENERGIA_4} energia\n 5. Cura vegetazione, {ENERGIA_5} energia\n 6. Produzione veloce, {ENERGIA_6} energia\n 7. Crea case, {ENERGIA_7} energia, 5 cibo e acqua\n 8. Sfama animali, {ENERGIA_8} energia\n 9. Disseta animali, {ENERGIA_9} energia\n 10. statistiche\n 11. Termina il giorno\n 12. Esci"

# funzioni
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_giorno():
    if GIORNO_ATTUALE > 1:
        print(f"Giorno {GIORNO_ATTUALE - 1} terminato, risultati: {CIBO_GIORNALIERO} cibo prodotto, {ACQUA_GIORNALIERA} acqua prodotta")
    print(f"inizio del giorno: {GIORNO_ATTUALE}")
    if GIORNO_ATTUALE > 1:
        produzione_giornaliera()
    else:
        print("Benvenuto in Life Simulator, dovrai gestire un tuo mondo con le risorse, se le persone non mangiano per 4 giorni o non bevono per 2 giorni allora hai perso la partita.")
    print(f"risorse:\ncibo attuale: {CIBO}, guadagno: {CIBO_GIORNALIERO}\nacqua attuale: {ACQUA}, guadagno: {ACQUA_GIORNALIERA}\nenergia attuale: {ENERGIA}\nanimali: {ANIMALI}, predatori: {ANIMALI_PREDATORI}")
    input("Premi invio per giocare...")
    clear_screen()
    gioca_giorno()

def produzione_giornaliera():
    global CIBO_GIORNALIERO, ACQUA_GIORNALIERA, CIBO, ACQUA, PRODUZIONE_CIBO_GIORNALIERA, PRODUZIONE_ACQUA_GIORNALIERA, GUADAGNO_PERDITA_CIBO, GUADAGNO_PERDITA_ACQUA
    global GIORNO_ATTUALE, CIBO_MAX, ACQUA_MAX, DA_SFAMARE, DA_DISSETARE
    global ENERGIA, ENERGIA_GIORNALIERA, ENERGIA_MAX, GIORNI_RIMASTI_ACQUA, GIORNI_RIMASTI_CIBO
    global ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    global GAME, ANIMALI_MAX, VEGETAZIONE, VEGETAZIONE_MAX, STATO_VEGETAZIONE, PERSONE, CASE
    MODIFICA_CIBO = random.choice(GUADAGNO_PERDITA_CIBO)
    MODIFICA_ACQUA = random.choice(GUADAGNO_PERDITA_ACQUA)
    CIBO_GIORNALIERO = PRODUZIONE_CIBO_GIORNALIERA + MODIFICA_CIBO
    CIBO += CIBO_GIORNALIERO
    ACQUA_GIORNALIERA = PRODUZIONE_ACQUA_GIORNALIERA + MODIFICA_ACQUA
    ACQUA += ACQUA_GIORNALIERA
    ENERGIA += ENERGIA_GIORNALIERA
    CIBO -= PERSONE
    ACQUA -= PERSONE
    if CIBO >= DA_SFAMARE:
        CIBO -= DA_SFAMARE
        DA_SFAMARE = 0
        GIORNI_RIMASTI_CIBO = 4
    if ACQUA >= DA_DISSETARE:
        ACQUA -= DA_DISSETARE
        DA_DISSETARE = 0
        GIORNI_RIMASTI_ACQUA = 2
    if PERSONE > CIBO:
        DA_SFAMARE = PERSONE - CIBO
        GIORNI_RIMASTI_CIBO -= 1
    if PERSONE > CIBO:
        DA_DISSETARE = PERSONE - ACQUA
        GIORNI_RIMASTI_ACQUA -= 1
    if GIORNI_RIMASTI_CIBO == 0:
        sconfitta()
    if GIORNI_RIMASTI_ACQUA == 0:
        sconfitta()
    if ANIMALI > 0:
        ANIMALI_CIBO += (ANIMALI + random.randint(0, 2))
        ANIMALI_ACQUA += (ANIMALI + random.randint(0, 2))
    if ANIMALI_CIBO > CIBO:
        ANIMALI_CIBO = CIBO
    if ANIMALI_ACQUA > ACQUA:
        ANIMALI_ACQUA = ACQUA
    if ENERGIA > ENERGIA_MAX:
        ENERGIA = ENERGIA_MAX
    if ACQUA > ACQUA_MAX:
        ACQUA = ACQUA_MAX
    if CIBO > CIBO_MAX:
        CIBO = CIBO_MAX

def sconfitta():
    print("Purtroppo sei arrivato alla fine del tuo fantastico viaggio, hai scoperto, creato, curato e molto altro;\nma non sei riuscito a sfamare/dissetare tutta la popolazione e purtroppo hai perso.")
    input("Continua...")
    mostra_statistiche_finali()
    scelta = int(input("1. rigioca\n2. esci"))
    if scelta == 1:
        reset()
        run_giorno()
    elif scelta == 2:
        print("Arrivederci")
        exit()

def avvenimento():
    global CIBO, ACQUA, ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    scelta_evento = random.choice([True, False])
    if scelta_evento:
        evento = random.randint(1, 10)
    else:
        print("Nessun evento speciale oggi.")
        input("premi invio per continuare...")
        return
    if evento == 1:
        perditaCibo = random.randint(1, 5)
        CIBO -= perditaCibo
        print(f"Una siccità ha danneggiato i campi!, perdi {perditaCibo} cibo")
        input("premi invio per continuare...")
    elif evento == 2:
        perditaAcqua = random.randint(1, 4)
        ACQUA -= perditaAcqua
        print(f"Una siccità ha ridotto la produzione di acqua!, perdi {perditaAcqua} acqua")
        input("premi invio per continuare...")
    elif evento == 3:
        perditaAnimali = random.randint(1, 2)
        ANIMALI -= perditaAnimali
        if ANIMALI < 0:
            ANIMALI = 0
            print("Un predatore ha attaccato i tuoi animali, purtroppo li hai persi tutti!")
            return
        print(f"Un predatore ha attaccato il tuo bestiame!, perdi {perditaAnimali} animali")
        input("premi invio per continuare...")
    elif evento == 4:
        predatoriUccisi = random.randint(1, 3)
        ANIMALI_PREDATORI -= predatoriUccisi
        if ANIMALI_PREDATORI < 0:
            ANIMALI_PREDATORI = 0
        print(f"Un cacciatore di passaggio ha ucciso {predatoriUccisi} predatori!")
        input("premi invio per continuare...")
    elif evento == 5:
        ciboBonus = random.randint(1, 5)
        print(f"I campi hanno fruttato piu cibo del dovuto, guadagni {ciboBonus} cibo!")
        CIBO += ciboBonus
        input("premi invio per continuare...")
    elif evento == 6:
        acquaBonus = random.randint(1, 5)
        print(f"I pozzi hanno fruttato piu acqua del dovuto, guadagni {acquaBonus} acqua!")
        ACQUA += acquaBonus
        input("premi invio per continuare...")
    elif evento == 7:
        print("Gli animali sono sazi da ieri, non hai bisogno di sfamarli oggi.")
        ANIMALI_CIBO = 0
        ANIMALI_ACQUA = 0
        input("premi invio per continuare...")
    else:
        print("Nessun evento speciale oggi.")
        input("premi invio per continuare...")

def mostra_statistiche():
    clear_screen()
    global GIORNO_ATTUALE
    global CIBO, CIBO_MAX, ACQUA, ACQUA_MAX
    global CIBO, ACQUA, ENERGIA, VEGETAZIONE, STATO_VEGETAZIONE
    global ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    global PRODUZIONE_CIBO_GIORNALIERA, PRODUZIONE_ACQUA_GIORNALIERA
    global CASE, PERSONE
    print(f"Statistiche del giorno {GIORNO_ATTUALE}:")
    print(f"Cibo: {CIBO}/{CIBO_MAX}, Produzione giornaliera: {PRODUZIONE_CIBO_GIORNALIERA}")
    print(f"Acqua: {ACQUA}/{ACQUA_MAX}, Produzione giornaliera: {PRODUZIONE_ACQUA_GIORNALIERA}")
    print(f"Energia: {ENERGIA}/{ENERGIA_MAX}")
    print(f"Vegetazione: {VEGETAZIONE}/{VEGETAZIONE_MAX}, Stato: {'Buono' if STATO_VEGETAZIONE else 'Cattivo'}")
    print(f"Animali: {ANIMALI}, Predatori: {ANIMALI_PREDATORI}, Cibo per animali: {ANIMALI_CIBO}, Acqua per animali: {ANIMALI_ACQUA}")
    print(f"Case: {CASE}, Persone: {PERSONE}")

def mostra_statistiche_finali():
    clear_screen()
    global GIORNO_ATTUALE
    global CIBO, CIBO_MAX, ACQUA, ACQUA_MAX
    global CIBO, ACQUA, ENERGIA, VEGETAZIONE, STATO_VEGETAZIONE
    global ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    global PRODUZIONE_CIBO_GIORNALIERA, PRODUZIONE_ACQUA_GIORNALIERA
    global CASE, PERSONE
    print(f"Statistiche finali, giorni giocati: {GIORNO_ATTUALE}")
    print(f"Cibo: {CIBO}/{CIBO_MAX}, Produzione giornaliera: {PRODUZIONE_CIBO_GIORNALIERA}")
    print(f"Acqua: {ACQUA}/{ACQUA_MAX}, Produzione giornaliera: {PRODUZIONE_ACQUA_GIORNALIERA}")
    print(f"Energia: {ENERGIA}/{ENERGIA_MAX}")
    print(f"Vegetazione: {VEGETAZIONE}/{VEGETAZIONE_MAX}, Stato: {'Buono' if STATO_VEGETAZIONE else 'Cattivo'}")
    print(f"Animali: {ANIMALI}, Predatori: {ANIMALI_PREDATORI}, Cibo per animali: {ANIMALI_CIBO}, Acqua per animali: {ANIMALI_ACQUA}")
    print(f"Case: {CASE}, Persone: {PERSONE}")
    print("")


def gioca_giorno():
    global ACQUA, CIBO, GIORNO_ATTUALE, ENERGIA, VEGETAZIONE, STATO_VEGETAZIONE
    global ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    global PRODUZIONE_CIBO_GIORNALIERA, PRODUZIONE_ACQUA_GIORNALIERA
    global GAME, ANIMALI_MAX, VEGETAZIONE, VEGETAZIONE_MAX, STATO_VEGETAZIONE, PERSONE, CASE, SCELTE
    GAME = True
    avvenimento()
    clear_screen()
    while GAME:
        clear_screen()
        print(SCELTE)
        scelta = ""
        scelta = str(input("Cosa vuoi fare?"))
        if scelta == "1":
            if ENERGIA >= ENERGIA_1:
                PRODUZIONE_CIBO_GIORNALIERA += 2
                ENERGIA -= ENERGIA_1
                print("Hai coltivato i campi, produzione di cibo aumentata di 2!")
            else:
                print("Non hai abbastanza energia per coltivare i campi!")
        elif scelta == "2":
            if ENERGIA >= ENERGIA_2:
                PRODUZIONE_ACQUA_GIORNALIERA += 2
                ENERGIA -= ENERGIA_2
                print("Hai costruito un pozzo, produzione acqua aumentata di 2")
            else:
                print("Non hai abbastanza energia per costruire un pozzo!")
        elif scelta == "3":
            if ENERGIA >= ENERGIA_3:
                if ANIMALI_PREDATORI > 0:
                    ANIMALI_PREDATORI -= 1
                    ENERGIA -= ENERGIA_3
                    print("Hai ucciso un predatore!")
                else:
                    print("Non ci sono predatori da uccidere!")
            else:
                print("Non hai abbastanza energia per uccidere i predatori!")
        elif scelta == "4":
            if ENERGIA >= ENERGIA_4:
                VEGETAZIONE += 1
                if VEGETAZIONE > VEGETAZIONE_MAX:
                    VEGETAZIONE = VEGETAZIONE_MAX
                ENERGIA -= ENERGIA_4
                print("Hai piantato una pianta, vegetazione aumentata di 1!")
            else:
                print("Non hai abbastanza energia per piantare una pianta!")
        elif scelta == "5":
            if VEGETAZIONE > 0:
                if ENERGIA >= ENERGIA_5:
                    if not STATO_VEGETAZIONE:
                        STATO_VEGETAZIONE = True
                        ENERGIA -= ENERGIA_5
                        print("Hai curato la vegetazione, ora è in buono stato!")
                    else:
                        print("La vegetazione è già in buono stato!")
                else:
                    print("Non hai abbastanza energia per curare la vegetazione!")
            else:
                print("Non hai vegetazione da curare!")
        elif scelta == "6":
            if ENERGIA >= ENERGIA_6:
                CIBO += random.randint(5, 10)
                ACQUA += random.randint(5, 10)
                ENERGIA -= ENERGIA_6
                print("Produzione veloce attivata, hai guadagnato cibo e acqua!")
            else:
                print("Non hai abbastanza energia per la produzione veloce!")
        elif scelta == "7":
            if ENERGIA >= ENERGIA_7:
                if CIBO >= 5 and ACQUA >= 5:
                    CASE += 1
                    PERSONE += random.randint(1, 3)
                    CIBO -= 5
                    ACQUA -= 5
                    ENERGIA -= ENERGIA_7
                    print("Hai creato una casa")
                else:
                    print("Non hai abbastanza cibo o acqua per creare una casa!")
            else:
                print("Non hai abbastanza energia per creare una casa!")
        elif scelta == "8":
            if ANIMALI > 0:
                if ENERGIA >= ENERGIA_8:
                    if CIBO >= ANIMALI_CIBO:
                        CIBO -= ANIMALI_CIBO
                        print(f"Hai sfamato gli animali, {ANIMALI_CIBO} cibo spesi!")
                        ENERGIA -= ENERGIA_8
                    else:
                        print("Non hai abbastanza cibo per sfamare gli animali!")
                else:
                    print("Non hai abbastanza energia per sfamare gli animali!")
            else:
                print("Non hai animali da sfamare!")
        elif scelta == "9":
            if ANIMALI > 0:
                if ENERGIA >= ENERGIA_9:
                    if ACQUA >= ANIMALI_ACQUA:
                        ACQUA -= ANIMALI_ACQUA
                        print(f"Hai dissetato gli animali, {ANIMALI_ACQUA} acqua spesi!")
                        ENERGIA -= ENERGIA_9
                    else:
                        print("Non hai abbastanza acqua per dissetare gli animali!")
                else:
                    print("Non hai abbastanza energia per dissetare gli animali!")
            else:
                print("Non hai animali da dissetare!")
        elif scelta == "10":
            mostra_statistiche()
        elif scelta == "11":
            GIORNO_ATTUALE += 1
            GAME = False
            clear_screen()
            run_giorno()
        elif scelta == "12":
            print("Grazie per aver giocato!")
            GAME = False
            clear_screen()
            exit(0)
        else:
            print("Scelta non valida")
            clear_screen()
            continue
        input("Premi invio per continuare...")

def reset():
    global CIBO_GIORNALIERO, ACQUA_GIORNALIERA, CIBO, ACQUA, PRODUZIONE_CIBO_GIORNALIERA, PRODUZIONE_ACQUA_GIORNALIERA, GUADAGNO_PERDITA_CIBO, GUADAGNO_PERDITA_ACQUA
    global GIORNO_ATTUALE, CIBO_MAX, ACQUA_MAX, DA_SFAMARE, DA_DISSETARE
    global ENERGIA, ENERGIA_GIORNALIERA, ENERGIA_MAX, GIORNI_RIMASTI_ACQUA, GIORNI_RIMASTI_CIBO
    global ANIMALI, ANIMALI_PREDATORI, ANIMALI_CIBO, ANIMALI_ACQUA
    global GAME, ANIMALI_MAX, VEGETAZIONE, VEGETAZIONE_MAX, STATO_VEGETAZIONE, PERSONE, CASE
    global ENERGIA_1, ENERGIA_2, ENERGIA_3, ENERGIA_4, ENERGIA_5, ENERGIA_6, ENERGIA_7, ENERGIA_8, ENERGIA_9
    GIORNO_ATTUALE = 1
    GAME = True
    ENERGIA = 10
    ENERGIA_MAX = 100
    ENERGIA_GIORNALIERA = 1
    CIBO = 10
    CIBO_MAX = 100
    CIBO_GIORNALIERO = 0
    PRODUZIONE_CIBO_GIORNALIERA = 0
    GUADAGNO_PERDITA_CIBO = [-1, 0, 1]
    ACQUA = 10
    ACQUA_MAX = 100
    ACQUA_GIORNALIERA = 0
    PRODUZIONE_ACQUA_GIORNALIERA = 0
    GUADAGNO_PERDITA_ACQUA = [-1, 0, 1]
    ANIMALI = 0
    ANIMALI_MAX = 10
    ANIMALI_CIBO = 0
    ANIMALI_ACQUA = 0
    ANIMALI_PREDATORI = 0
    ENERGIA_1 = 3
    ENERGIA_2 = 3
    ENERGIA_3 = 3
    ENERGIA_4 = 3
    ENERGIA_5 = 3
    ENERGIA_6 = 5
    ENERGIA_7 = 4
    ENERGIA_8 = 1
    ENERGIA_9 = 1
    VEGETAZIONE = 0
    VEGETAZIONE_MAX = 10
    STATO_VEGETAZIONE = False
    PERSONE = 3
    CASE = 3
    DA_DISSETARE = 0
    DA_SFAMARE = 0
    GIORNI_RIMASTI_ACQUA = 3
    GIORNI_RIMASTI_CIBO = 5

# start
if __name__ == "__main__":
    run_giorno()
