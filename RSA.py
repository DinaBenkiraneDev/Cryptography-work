#  Auteur: Dina Benkirane
#          Zheng Long Yang

import random
import math


class RSA:
    def __init__(self, message_clair):
        self.message_clair = message_clair
        print("Test Function")

    # pour efectuer l'algorithme d'exponentiation rapide.
    # Peut etre remplacer par une fenetre glissante TODO?
    def squareAndMultiply(self, base, exposant, number):
        # Initialisation variable et cas de base
        resultat = 1
        if (exposant == 0):
            return resultat

        # change exposant --> binaire
        binaryexp = []
        while (exposant != 0):
            # print("exposant ", exposant)
            binaryexp.append(exposant % 2)
            exposant = exposant // 2
        # print("Current Binary length: ",binaryexp.__len__())

        # Algo
        if (binaryexp[0] == 1):
            resultat = base
        if (binaryexp.__len__() == 1):
            return resultat
        for x in range(1, binaryexp.__len__()):
            base = pow(base, 2) % number
            # print("base",base)
            if (binaryexp[x] == 1):
                resultat = base * resultat % number
                # print("resultat if",resultat)
        return resultat

    # calcule le pgcd() entre deux nombre a l'aide de l'algorithme d'euclide etendu.
    def EEA(self, a, b):
        # il faut que a soit plus grand que b
        if (a < b):
            tmp = b
            b = a
            a = tmp
        # cas de base
        if (b == 0):
            d = a
            x = 1
            y = 0
            return (d, x, y)
        # initialisation de variable
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        # trouve un x et y ou ax+by=d
        while (b > 0):
            q = a // b
            r = a - q * b
            x = x2 - q * x1
            y = y2 - q * y1

            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y

        d = a
        x = x2
        y = y2
        return (d, x, y)

    # vous permettant de verifer si un nombre est premier.
    def millerRabin(self, number, iteration):
        #    Cas d'exception
        if (number <= 1):
            return False
        if (number <= 3):
            return True
        if (number % 2 == 0):
            return False

        s = number - 1
        # print("s:",s)
        while (s % 2 == 0):
            s = s // 2
        # print("s after while:",s)
        for i in range(iteration):
            randInt = random.randint(2, number - 2)
            # print("random int:",randInt)
            temp = s

            modExpen = self.squareAndMultiply(randInt, temp, number)
            j = 1
            while (j <= s - 1 and modExpen != number - 1 and modExpen != 1):
                modExpen = pow(modExpen, 2) % number
                if (modExpen == 1):
                    return False
                j += 1

            if (modExpen != number - 1 and temp % 2 == 0):
                return False
        return True

    # etablie tous les parametres initiaux requis.
    def genKeys(self, message_clair):
        n = 0
        p = -1
        # Factor Crt exponent, and coefficient
        dP = -1
        dQ = -1
        qInv = -1
        # the i-th factor
        r_i = 0
        # the i-th factor of CRT exponent
        d_i = 0
        t_i = 0
        m_byte = message_clair.bit_length()
        L = 0
        # 1023 ici juste parce que je veux rentrer dans la boucle et generer un p au moin
        q = self.getPrimeNumber(random.randrange(512, 1023))
        n = 0
        # genere un p qui va donner
        while (n.bit_length() < 1024):
            p = self.getPrimeNumber(random.randrange(512, 1024))
            n = p * q

        k = n.bit_length()

        # Calcul de Phi de n
        phi_n = (p - 1) * (q - 1)

        # Choisir l'exposant e (doit être de 9 bit tel que dis en démonstration)
        e = random.getrandbits(9)
        while (self.EEA(phi_n, e) != 1):
            e = random.getrandbits(9)

        # calculer Clé privé d IDKKKK

    def decrypt(self):
        message_decrypter = ""
        return message_decrypter
        # g, x, y = egcd(a, m)

    # if g != 1:
    #    raise Exception('modular inverse does not exist')
    # else:
    #    return x % m

    # Create a prime number
    def getPrimeNumber(self, length):
        prime = random.getrandbits(length)
        # A partir du nombre genere diminuer de 1 jusqua temps quon trouve un nombre
        # premier
        while (prime != self.millerRabin(prime, 39)):
            prime -= 1
        return prime

    def main(self):
        print("Boop")


# TODO
# L'utilisation d'un exposant public petit, tel que discute en demonstration.
# Une decryption rapide en utilisant le domaine CRT.
# L'utilisation du OEAP.

test = RSA("Suce ma bite G")
# print(test.millerRabin(1387,80))
# print (test.squareAndMultiply(5,596,1234))
# print(test.EEA(31,2))