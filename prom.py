
def cdsnb():
    a = int(input("donnez le nombre des employés: "))
    while (a <= 4 or a >= 101):
        a = int(input("donnez le nombre des employés*: "))
    return a


def cdsnb(a):
    for i in range(len(a)):
        if (a[i].isalpha() == True):
            return False


def cdsMatric():
    a = input("donnez la matricule d'employé: ")
    while (cdsnb(a) == False or len(a) != 8):
        a = input("donnez la matricule d'employé*: ")
    return a


def cdsScores():
    a = int(input("donnez le score d'employé: "))
    while (a < 20 or a > 120):
        a = int(input("donnez le score d'employé*: "))
    return a


def checkEg(Matricules, longueur, a):
    for i in range(longueur):
        if (Matricules[i] == a):
            return False


def Remp(Matricules, Scores, Emps):
    s = 0
    for i in range(Emps):
        mat = cdsMatric()
        print("-----------------------")
        while(checkEg(Matricules, s, mat) == False):
            print("la matricule", mat, "deja existe!")
            mat = saisirMatric()
        Matricules.append(mat)
        s += 1
        sc = cdsScores()
        Scores.append(sc)


def Tri(Matricules, Scores, Emps):
    ech = True
    while ech == True:
        ech = False
        for i in range(Emps-1):
            if (Scores[i] <= Scores[i+1]):
                tmp = Matricules[i]
                Matricules[i] = Matricules[i+1]
                Matricules[i+1] = tmp
                tmp = Scores[i]
                Scores[i] = Scores[i+1]
                Scores[i+1] = tmp
                ech = True


def winners(Matricules, Emps):
    for i in range(round(0.25*Emps)):
        print("Liste des admis:")
        print(Matricules[i], end="")


# PP
Scores = []
Matricules = []
Emps = cdsnb()
Remp(Matricules, Scores, Emps)
Tri(Matricules, Scores, Emps)
winners(Matricules, Emps)
