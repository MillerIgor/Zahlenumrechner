from functions_modul import *

print("Zahlenumrechner")
while True:
    print("Bitte wählen Sie ....\n"
          "(1) Hexadezimalzahl umwandeln.\n"
          "(2) Dezimalzahl umwandeln.\n"
          "(3) Oktalzahl umwandeln.\n"
          "(4) Dualzahl umwandeln.\n"
          "(q) Beenden")
    user_wahl = input("Ihre Wahl: ")
    if user_wahl == '1':
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            if check_hex(zahl):  # Überprüfen ob die Zahl im richtigen Format eingegeben wurde
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(d) Dezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(b) Dualzahl")
                user_wahl1 = input("Ihre Wahl: ")
                if user_wahl1.lower() == 'd':
                    try:
                        print(f"Ergebnis: {to_dec(zahl, 16)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                elif user_wahl1.lower() == 'o':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 16), 8)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                elif user_wahl1.lower() == 'b':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 16), 2)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!\n")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe!\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe!\n")
    elif user_wahl == '2':
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            if check_decimal(zahl):  # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(b) Dualzahl")
                user_wahl1 = input("Ihre Wahl: ")
                if user_wahl1 == 'h':
                    try:
                        print(f"Ergebnis: {dec_to(zahl, 16)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                elif user_wahl1.lower() == 'o':
                    try:
                        print(f"Ergebnis: {dec_to(zahl, 8)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
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
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            if check_oktal(zahl):  # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(d) Dezimalzahl\n"
                      "(b) Dualzahl")
                user_wahl1 = input("Ihre Wahl: ")
                if user_wahl1 == 'h':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 8), 16)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("Überprüfen Sie Ihre Eingabe!")
                elif user_wahl1.lower() == 'd':
                    try:
                        print(f"Ergebnis: {to_dec(zahl, 8)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                elif user_wahl1.lower() == 'b':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 8), 2)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                else:
                    print("\nPassen Sie Ihre Eingabe auf!")
                    continue
            else:
                print("\nÜberprüfen Sie Ihre Eingabe.\n")
        except:
            print("\nÜberprüfen Sie Ihre Eingabe!\n")
            continue
    elif user_wahl == '4':
        zahl = input("Bitte Zahl für Umrechnung eingeben: ")
        try:
            if check_dual(zahl):  # Überprüfen ob die Zahl in richtigen Format eingegeben wurde
                print("Eingegebene Zahl umrechnen in ...\n"
                      "(h) Hexadezimalzahl\n"
                      "(o) Oktalzahl\n"
                      "(d) Dezimalzahl")
                user_wahl1 = input("Ihre Wahl: ")
                if user_wahl1 == 'h':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 2), 16)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
                elif user_wahl1.lower() == 'o':
                    try:
                        print(f"Ergebnis: {dec_to(to_dec(zahl, 2), 8)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!")
                elif user_wahl1.lower() == 'd':
                    try:
                        print(f"Ergebnis: {to_dec(zahl, 2)}")
                        input("Weiter mit der Eingabe-Taste")
                    except:
                        print("\nÜberprüfen Sie Ihre Eingabe!\n")
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
        break
    else:
        print("\nÜberprüfen Sie Ihre Eingabe.\n")
