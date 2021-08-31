def dec_to(num_to_change, to_system_base):
    """
        Umwandelt die Zahl vom Dezimalzahlensystem nach ein anderes Zahlensystem (die höhste Systembasis is 16)

        :param (str) num_to_change: Zahl zum Umwandeln
        :param (int) to_system_base: basis der Zielzahlensystem

        :return: (str): umgewandelte Zahl
    """
    x = num_to_change
    y = int(to_system_base)
    result = ''
    numbers_to_letters = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    while x != 0:
        if y > 10:
            if x % y > 9:
                result = numbers_to_letters[x % y].upper() + result
                x = x // y
            else:
                result = str(x % y) + result
                x = x // y
        else:
            result = str(x % y) + result
            x = x // y
    return result


def to_dec(num_to_change, system_base):
    """ Umwandelt die Zahl von einem Zahlensystem (die höhste Systembasis is 16) nach Dezimalzahlensystem

        :param (str) num_to_change: Zahl zum Umwandeln
        :param (int) system_base: Zahlensystem der Zahl

        :return (str): umgewandelte Zahl
    """
    x = system_base
    y = len(num_to_change)
    result = 0
    digits_list = []
    letters_to_numbers = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for n in range(y):
        if num_to_change[n].lower() in letters_to_numbers.keys():
            digits_list.append(letters_to_numbers[num_to_change[n].lower()])
        else:
            digits_list.append(int(num_to_change[n]))
    for d in digits_list:
        y -= 1
        result += d * pow(x, y)
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
