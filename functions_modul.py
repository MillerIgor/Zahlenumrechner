def dec_to(num_to_change, to_system_base):
    """
        Umwandelt die Zahl vom Dezimalzahlensystem nach ein anderes Zahlensystem (die höhste Systembasis is 16)

        :param (str) num_to_change: Zahl zum Umwandeln
        :param (int) to_system_base: basis der Zielzahlensystem

        :return: (str): umgewandelte Zahl
    """
    x = int(num_to_change)
    # zuweisen die Zeichenkette, die das Ergebnis der Konvertierung erhalten soll
    result = ''
    # ein Wörterbuch zuweisen, um die Ziffern in der umzuwandelnden Zahl durch Buchstaben als Ergebnis zu ersetzen
    numbers_to_letters = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    while x != 0:
        # prüfen ob die Zielzahlsystem hat Basis größe als 10, damit die Umgewandelte Zahl richtig dargestel wurde
        if to_system_base > 10:
            # prüfen, ob die Ziffer in einen Buchstaben ersetzt werden soll
            if x % to_system_base > 9:
                # fügen die umgewandelte Ziffer an das Ende der umgewandelten Zahl an.
                result = numbers_to_letters[x % to_system_base].upper() + result
                # dividieren die Zahl durch basis des Zahlensystems, laut des Algorithmus
                x = x // to_system_base
            else:
                # fügen die umgewandelte Ziffer an das Ende der umgewandelten Zahl an.
                result = str(x % to_system_base) + result
                # dividieren die Zahl durch basis des Zahlensystems, laut des Algorithmus
                x = x // to_system_base
        else:
            # fügen die umgewandelte Ziffer an das Ende der umgewandelten Zahl an.
            result = str(x % to_system_base) + result
            # dividieren die Zahl durch basis des Zahlensystems, laut des Algorithmus
            x = x // to_system_base
    return result


def to_dec(num_to_change, system_base):
    """ Umwandelt die Zahl von einem Zahlensystem (die höhste Systembasis is 16) nach Dezimalzahlensystem

        :param (str) num_to_change: Zahl zum Umwandeln
        :param (int) system_base: Zahlensystem der Zahl

        :return (str): umgewandelte Zahl
    """
    # Berechnen die höchste Stellenwert
    y = len(num_to_change) - 1
    result = 0
    # ein Wörterbuch zuweisen, um die Buchstaben in der umzuwandelnden Zahl durch Zahlen als Ergebnis zu ersetzen
    letters_to_numbers = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    # ein List zuweisen, um die alle ersetzte Zahlen behalten
    digits_list = []
    # die Liste mit Zahlen ausfüllen.
    for n in range(y):
        if num_to_change[n].lower() in letters_to_numbers.keys():
            digits_list.append(letters_to_numbers[num_to_change[n].lower()])
        else:
            digits_list.append(int(num_to_change[n]))
    # der Zahl laut des Algorithmus umwandeln
    for d in digits_list:
        result += d * pow(system_base, y)
        y -= 1
    return result


def check_hex(zahl):
    """Überprüft ob die Zahl hexadezimal ist.

    :arg
        zahl(str): Die eingegeben Zahl zu überprüfen

    :returns
        bool: True, wenn die Zahl hexadezimal ist
    """
    for z in zahl:
        if z in '0123456789abcdefABCDEF':
            result = True
        else:
            return False
    return result


def check_oktal(zahl):
    """Überprüft ob die Zahl oktal ist.

        :arg
            zahl(str): Die eingegeben Zahl zu überprüfen

        :returns
            bool: True, wenn die Zahl oktal ist
        """
    for z in zahl:
        if z in '01234567':
            result = True
        else:
            return False
    return result


def check_dual(zahl):
    """Überprüft ob die Zahl dual ist.

        :arg
            zahl(str): Die eingegeben Zahl zu überprüfen

        :returns
            bool: True, wenn die Zahl dual ist
        """
    for z in zahl:
        if z in '10':
            result = True
        else:
            return False
    return result


def check_decimal(zahl):
    """Überprüft ob die Zahl dezimal ist.

        :arg
            zahl(str): Die eingegeben Zahl zu überprüfen

        :returns
            bool: True, wenn die Zahl dezimal ist
        """
    for z in zahl:
        if z in '0123456789':
            result = True
        else:
            return False
    return result
