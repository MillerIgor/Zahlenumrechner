from functions_modul import *

print("Zahlenumrechner")
while True:
    # Benutzermenü ausgeben
    print("Bitte wählen Sie ....\n"
          "(1) Hexadezimalzahl umwandeln.\n"
          "(2) Dezimalzahl umwandeln.\n"
          "(3) Oktalzahl umwandeln.\n"
          "(4) Dualzahl umwandeln.\n"
          "(q) Beenden")
    # Benutzer nach seiner Wahl fragen
    user_wahl = input("Ihre Wahl: ")
    if user_wahl == '1':
        # Zahl zum Umwandeln nachfragen
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            # Überprüfen ob die Zahl im richtigen Format eingegeben wurde
            if check_hex(zahl):
                # Benutzer menü ausgeben
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(d) Dezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(b) Dualzahl")
                # Benutzer nach seiner Wahl fragen
                user_wahl1 = input("Ihre Wahl: ")
                # Durchführung der Konvertierung nach Wahl des Benutzers
                if user_wahl1.lower() == 'd':
                    print(f"Ergebnis: {to_dec(zahl, 16)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'o':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 16), 8)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'b':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 16), 2)}")
                    input("Weiter mit der Eingabe-Taste")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!\n")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe!\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe!\n")
    elif user_wahl == '2':
        # Zahl zum Umwandeln nachfragen
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
            if check_decimal(zahl):
                # Benutzer menü ausgeben
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(b) Dualzahl")
                # Benutzer nach seiner Wahl fragen
                user_wahl1 = input("Ihre Wahl: ")
                # Durchführung der Konvertierung nach Wahl des Benutzers
                if user_wahl1 == 'h':
                    print(f"Ergebnis: {dec_to(zahl, 16)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'o':
                    print(f"Ergebnis: {dec_to(zahl, 8)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'b':
                    print(f"Ergebnis: {dec_to(zahl, 2)}")
                    input("Weiter mit der Eingabe-Taste")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!\n")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe.\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe.\n")
    elif user_wahl == '3':
        # Zahl zum Umwandeln nachfragen
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
            if check_oktal(zahl):
                # Benutzer menü ausgeben
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(d) Dezimalzahl\n"
                      "(b) Dualzahl")
                # Benutzer nach seiner Wahl fragen
                user_wahl1 = input("Ihre Wahl: ")
                # Durchführung der Konvertierung nach Wahl des Benutzers
                if user_wahl1 == 'h':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 8), 16)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'd':
                    print(f"Ergebnis: {to_dec(zahl, 8)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'b':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 8), 2)}")
                    input("Weiter mit der Eingabe-Taste")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe.\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe!\n")
            continue
    elif user_wahl == '4':
        # Zahl zum Umwandeln nachfragen
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
            if check_dual(zahl):
                # Benutzer menü ausgeben
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(d) Dezimalzahl")
                # Benutzer nach seiner Wahl fragen
                user_wahl1 = input("Ihre Wahl: ")
                # Durchführung der Konvertierung nach Wahl des Benutzers
                if user_wahl1 == 'h':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 2), 16)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'o':
                    print(f"Ergebnis: {dec_to(to_dec(zahl, 2), 8)}")
                    input("Weiter mit der Eingabe-Taste")
                elif user_wahl1.lower() == 'd':
                    print(f"Ergebnis: {to_dec(zahl, 2)}")
                    input("Weiter mit der Eingabe-Taste")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!\n")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe.\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe.\n")
            continue
    elif user_wahl.lower() == 'q':
        print("\nAuf wiedersehen!")
        # das Program laut der Benutzerwahl beenden
        break
    else:
        print("\nÜberprüfen Sie Ihre Eingabe.\n")
