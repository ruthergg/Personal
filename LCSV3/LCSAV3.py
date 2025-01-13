def PlayerSS(x, y):
    TT = y
    if x == 1:
        K = True
        L = True
        P = True
        while(K):
            try:
                print("How many kills")
                TPSNI = input()
                PK = float(TPSNI)
                K = False
            except Exception as i: 
                print(i)
        while(L):
            try:
                print("How many deaths")
                TPSNI = input()
                PD = float(TPSNI)
                L = False
            except Exception as i: 
                print(i)
        while(P):
            try:
                print("How many Assists")
                TPSNI = input()
                PA = float(TPSNI)
                P = False
            except Exception as i: 
                print(i)
        if PK == 0: KFS = 0
        else:
            KS = (PK / (TT * 0.114))
            if KS > 1: KS = 1
            KFS = KS * 58
        if PA == 0: AFS = 0
        else:
            AS = (PA / (TT * 0.19))
            if AS > 1: AS = 1
            AFS = AS * 42
        PS = AFS + KFS + (-3 * (PD - (TT * .058)))
        return PS
    if x == 2:
        K = True
        L = True
        P = True
        while(K):
            try:
                print("How many kills")
                TPSNI = input()
                PK = float(TPSNI)
                K = False
            except Exception as i: 
                print(i)
        while(L):
            try:
                print("How many deaths")
                TPSNI = input()
                PD = float(TPSNI)
                L = False
            except Exception as i: 
                print(i)
        while(P):
            try:
                print("How many Assists")
                TPSNI = input()
                PA = float(TPSNI)
                P = False
            except Exception as i: 
                print(i)
        if PK == 0: KFS = 0
        else:
            KS = (PK / (TT * 0.07))
            if KS > 1: KS = 1
            KFS = KS * 34
        if PA == 0: AFS = 0
        else:
            AS = (PA / (TT * 0.305))
            if AS > 1: AS = 1
            AFS = AS * 66
        PS = AFS + KFS + (-3 * (PD - (TT * .05)))
        return PS
    if x == 3:
        K = True
        L = True
        P = True
        while(K):
            try:
                print("How many kills")
                TPSNI = input()
                PK = float(TPSNI)
                K = False
            except Exception as i: 
                print(i)
        while(L):
            try:
                print("How many deaths")
                TPSNI = input()
                PD = float(TPSNI)
                L = False
            except Exception as i: 
                print(i)
        while(P):
            try:
                print("How many Assists")
                TPSNI = input()
                PA = float(TPSNI)
                P = False
            except Exception as i: 
                print(i)
        if PK == 0: KFS = 0
        else:
            KS = (PK / (TT * 0.114))
            if KS > 1: KS = 1
            KFS = KS * 63
        if PA == 0: AFS = 0
        else:
            AS = (PA / (TT * 0.19))
            if AS > 1: AS = 1
            AFS = AS * 37
        PS = AFS + KFS + (-3 * (PD - (TT * .056)))
        return PS
    if x == 4:
        K = True
        L = True
        P = True
        while(K):
            try:
                print("How many kills")
                TPSNI = input()
                PK = float(TPSNI)
                K = False
            except Exception as i: 
                print(i)
        while(L):
            try:
                print("How many deaths")
                TPSNI = input()
                PD = float(TPSNI)
                L = False
            except Exception as i: 
                print(i)
        while(P):
            try:
                print("How many Assists")
                TPSNI = input()
                PA = float(TPSNI)
                P = False
            except Exception as i: 
                print(i)
        if PK == 0: KFS = 0
        else:
            KS = (PK / (TT * 0.114))
            if KS > 1: KS = 1
            KFS = KS * 68
        if PA == 0: AFS = 0
        else:
            AS = (PA / (TT * 0.19))
            if AS > 1: AS = 1
            AFS = AS * 32
        PS = AFS + KFS + (-3 * (PD - (TT * .028)))
        return PS
    if x == 5:
        K = True
        L = True
        P = True
        while(K):
            try:
                print("How many kills")
                TPSNI = input()
                PK = float(TPSNI)
                K = False
            except Exception as i: 
                print(i)
        while(L):
            try:
                print("How many deaths")
                TPSNI = input()
                PD = float(TPSNI)
                L = False
            except Exception as i: 
                print(i)
        while(P):
            try:
                print("How many Assists")
                TPSNI = input()
                PA = float(TPSNI)
                P = False
            except Exception as i: 
                print(i)
        if PK == 0: KFS = 0
        else:
            KS = (PK / (TT * 0.114))
            if KS > 1: KS = 1
            KFS = KS * 18
        if PA == 0: AFS = 0
        else:
            AS = (PA / (TT * 0.19))
            if AS > 1: AS = 1
            AFS = AS * 82
        PS = AFS + KFS + (-3 * (PD - (TT * .048)))
        return PS

def TeamPS(a, b, c, d, e):
    Tops = a * .1
    Jgs = b * .3
    Mids = c * .2
    Adcs = d * .1
    Sups = e * .3
    f = Tops + Jgs + Mids + Adcs + Sups
    return f

def PlayerScoreImport1():
    LL = []
    FN = open("PlayerScores.txt", "r")
    fs = FN.read()
    try:
        LL = fs.split(",")
        return LL
    except:
        print("Fuck You")

def PlayerScoreImport2():
    LL = []
    FN = open("PlayerGames.txt", "r")
    fs = FN.read()
    try:
        LL = fs.split(",")
        return LL
    except:
        print("Fuck You")
        
def SSExport(g, s):
    Sfile = open("PlayerScores.txt", 'w')
    Gfile = open("PlayerGames.txt", "w")
    b = 0
    for x in g:
        if b < 39:
            Gfile.write(str(x) + ",")
            b = b + 1
        else:
            Gfile.write(str(x))
    for x in s:
        if b < 78:
            Sfile.write(str(x) + ",")
            b = b + 1
        else:
            Sfile.write(str(x))
    Gfile.close
    Sfile.close
    
def ScoreCompile(NPS, CPS, NG):
    OP = NG / (NG + 1)
    NP = 1 / (NG + 1)
    NCPS = (CPS * OP) + (NPS * NP)
    return NCPS

def TeamScorePerWin(x, y):
    if x > y:
        tot = x + y
        l = x / tot
        j = y / tot
        result = str(l * 100) + "% / " + str(j * 100) + "%" 
        return result

    elif y > x:
        tot = y + x
        l = y / tot
        j = x / tot
        result = str(l * 100) + "% / " + str(j * 100) + "%" 
        return result
    else: return "50% / 50%"

def TeamScoreSS(x, y):
    if x > y:
        tot = x + y
        l = x / tot
        if (l * 100) >= 60: return "2 - 0"
        else: return "2 - 1"

    elif y > x:
        tot = y + x
        l = y / tot
        if (l * 100) >= 60: return "2 - 0"
        else: return "2 - 1"
    else: return "50% / 50%"

def TeamScoreSSB5(x, y):
    if x > y:
        tot = x + y
        l = x / tot
        if (l * 100) >= 70: return "3 - 0"
        if (l * 100) <= 69 and (l * 100) >= 61: return "3 - 1"
        if (l * 100) >= 50 and (l * 100) <= 60: return "3 - 2"

    elif y > x:
        tot = y + x
        l = y / tot
        if (l * 100) >= 70: return "3 - 0"
        if (l * 100) <= 69 and (l * 100) >= 61: return "3 - 1"
        if (l * 100) >= 50 and (l * 100) <= 60: return "3 - 2"
    else: return "50% / 50%"

print("Welcome to the LCS prediction Program")
iuq = open("Database.txt", "r")
d2 = iuq.read()
try:
    print(d2)
except:
    pass

K = True
OTS = ""

PlayerScores = []
Teams = "DIG, FLY, C9, 100T, SHOP, IMT, NRG, TL"
TeamScoresStrL = []
TeamScores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

TSFileO = open('TeamScores.txt', 'r')
TeamScoresStr = TSFileO.read()
TeamScoresStrL = TeamScoresStr.split(",")
u = True
y = 0
try:
    while(u == True):
        try:
            TeamScores[y] = float(TeamScoresStrL[y])
            y = 1 + y
        except Exception as kl:
            u = False
except Exception as y :
    print(TeamScoresStr)
    print(TeamScoresStrL)
    print(TeamScores)
    print(y)
TSFileO.close

# DIGS = 0  | 0 1 2 3 4 
# FLYS = 1  | 5 6 7 8 9 
# C9S = 2   | 10 11 12 13 14
# S100T = 3 | 15 16 17 18 19 
# SHOPS = 4 | 20 21 22 23 24
# IMTS = 5  | 25 26 27 28 29 
# NRGS = 6  | 30 31 32 33 34 
# TLS = 7   | 35 36 37 38 39

PS = []
PG = []
TPS = PlayerScoreImport1()
TPG = PlayerScoreImport2()
for x in TPS:
    PS.append(float(x))
for x in TPG:
    PG.append(float(x))

DIGScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    DIGScores[0] = PS[0]
    DIGScores[1] = PS[1]
    DIGScores[2] = PS[2]
    DIGScores[3] = PS[3]
    DIGScores[4] = PS[4]
except:
    pass

FLYScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    FLYScores[0] = PS[5]
    FLYScores[1] = PS[6]
    FLYScores[2] = PS[7]
    FLYScores[3] = PS[8]
    FLYScores[4] = PS[9]
except:
    pass

C9Scores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    C9Scores[0] = PS[10]
    C9Scores[1] = PS[11]
    C9Scores[2] = PS[12]
    C9Scores[3] = PS[13]
    C9Scores[4] = PS[14]
except:
    pass

S100TScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    S100TScores[0] = PS[15]
    S100TScores[1] = PS[16]
    S100TScores[2] = PS[17]
    S100TScores[3] = PS[18]
    S100TScores[4] = PS[19]
except:
    pass

SHOPScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    SHOPScores[0] = PS[20]
    SHOPScores[1] = PS[21]
    SHOPScores[2] = PS[22]
    SHOPScores[3] = PS[23]
    SHOPScores[4] = PS[24]
except:
    pass

IMTScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    IMTScores[0] = PS[25]
    IMTScores[1] = PS[26]
    IMTScores[2] = PS[27]
    IMTScores[3] = PS[28]
    IMTScores[4] = PS[29]
except:
    pass

NRGScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    NRGScores[0] = PS[30]
    NRGScores[1] = PS[31]
    NRGScores[2] = PS[32]
    NRGScores[3] = PS[33]
    NRGScores[4] = PS[34]
except:
    pass

TLScores = [0.0, 0.0, 0.0, 0.0, 0.0]
try:
    TLScores[0] = PS[35]
    TLScores[1] = PS[36]
    TLScores[2] = PS[37]
    TLScores[3] = PS[38]
    TLScores[4] = PS[39]
except:
    pass

TLDC = False
FLYDC = False
DIGDC = False
C9DC = False
S100TDC = False
SHOPDC = False
IMTDC = False
NRGDC = False


while(K):
    print("(I)nput Player match data")
    print("(P)red Winner of Game")
    print("(T)ier Lists")
    print("(B)uild Predition Data")
    print("(Q)uit")

    ans = input()
    
    TeamScores[0] = TeamPS(DIGScores[0], DIGScores[1], DIGScores[2], DIGScores[3], DIGScores[4])
    TeamScores[1] = TeamPS(FLYScores[0], FLYScores[1], FLYScores[2], FLYScores[3], FLYScores[4])
    TeamScores[2] = TeamPS(C9Scores[0], C9Scores[1], C9Scores[2], C9Scores[3], C9Scores[4])
    TeamScores[3] = TeamPS(S100TScores[0], S100TScores[1], S100TScores[2], S100TScores[3], S100TScores[4])
    TeamScores[4] = TeamPS(SHOPScores[0], SHOPScores[1], SHOPScores[2], SHOPScores[3], SHOPScores[4])
    TeamScores[5] = TeamPS(IMTScores[0], IMTScores[1], IMTScores[2], IMTScores[3], IMTScores[4])
    TeamScores[6] = TeamPS(NRGScores[0], NRGScores[1], NRGScores[2], NRGScores[3], NRGScores[4])
    TeamScores[7] = TeamPS(TLScores[0], TLScores[1], TLScores[2], TLScores[3], TLScores[4])
    Fuck = True
    uyi = True
    qw = True
    match ans:
        case "I":
            Z = True
            while(Z):
                print("What team are you imputing data for (TL, FLY, 100T, DIG, IMT, SHOP, NRG, C9)")
                ans2 = input()
                while qw == True:
                    print("What was game time in minutes?")
                    ans10 = input()
                    if int(ans10) < 15:
                        qw == True
                        print("Wrong")
                    else: qw = False
                rans = float(ans10)
                if ans2 == "TL":
                    while Fuck == True:
                        print("Impact")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        TLScores[0] = ScoreCompile(PKDA, TLScores[0], PG[35])
                        PG[35] = PG[35] + 1
                        print("Umti")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        TLScores[1] = ScoreCompile(PKDA, TLScores[1], PG[36])
                        PG[36] = PG[36] + 1
                        print("Apa")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        TLScores[2] = ScoreCompile(PKDA, TLScores[2], PG[37])
                        PG[37] = PG[37] + 1
                        print("Yeon")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        TLScores[3] = ScoreCompile(PKDA, TLScores[3], PG[38])
                        PG[38] = PG[38] + 1
                        print("Corejj")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        TLScores[4] = ScoreCompile(PKDA, TLScores[4], PG[39])
                        PG[39] = PG[39] + 1
                        TLDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "FLY":
                    while Fuck == True:
                        print("Bwipo")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        FLYScores[0] = ScoreCompile(PKDA, FLYScores[0], PG[5])
                        PG[5] = PG[5] + 1
                        print("Inspired")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        FLYScores[1] = ScoreCompile(PKDA, FLYScores[1], PG[6])
                        PG[6] = PG[6] + 1
                        print("Quad")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        FLYScores[2] = ScoreCompile(PKDA, FLYScores[2], PG[7])
                        PG[7] = PG[7] + 1
                        print("Massu")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        FLYScores[3] = ScoreCompile(PKDA, FLYScores[3], PG[8])
                        PG[8] = PG[8] + 1
                        print("Busio")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        FLYScores[4] = ScoreCompile(PKDA, FLYScores[4], PG[9])
                        PG[9] = PG[9] + 1
                        FLYDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "100T":
                    while Fuck == True:
                        print("Sniper")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        S100TScores[0] = ScoreCompile(PKDA, S100TScores[0], PG[15])
                        PG[15] = PG[15] + 1
                        print("River")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        S100TScores[1] = ScoreCompile(PKDA, S100TScores[1], PG[16])
                        PG[16] = PG[16] + 1
                        print("Quid")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        S100TScores[2] = ScoreCompile(PKDA, S100TScores[2], PG[17])
                        PG[17] = PG[17] + 1
                        print("Meech")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        S100TScores[3] = ScoreCompile(PKDA, S100TScores[3], PG[18])
                        PG[18] = PG[18] + 1
                        print("Eyla")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        S100TScores[4] = ScoreCompile(PKDA, S100TScores[4], PG[19])
                        PG[19] = PG[19] + 1
                        S100TDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "DIG":
                    while Fuck == True:
                        print("Licorice")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        DIGScores[0] = ScoreCompile(PKDA, DIGScores[0], PG[0])
                        PG[0] = PG[0] + 1
                        print("Spica")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        DIGScores[1] = ScoreCompile(PKDA, DIGScores[1], PG[1])
                        PG[1] = PG[1] + 1
                        print("Jensen")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        DIGScores[2] = ScoreCompile(PKDA, DIGScores[2], PG[2])
                        PG[2] = PG[2] + 1
                        print("Zven")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        DIGScores[3] = ScoreCompile(PKDA, DIGScores[3], PG[3])
                        PG[3] = PG[3] + 1
                        print("Isles")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        DIGScores[4] = ScoreCompile(PKDA, DIGScores[4], PG[4])
                        PG[4] = PG[4] + 1
                        DIGDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "IMT":
                    while Fuck == True:
                        print("Castle")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        IMTScores[0] = ScoreCompile(PKDA, IMTScores[0], PG[25])
                        PG[25] = PG[25] + 1
                        print("Armao")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        IMTScores[1] = ScoreCompile(PKDA, IMTScores[1], PG[26])
                        PG[26] = PG[26] + 1
                        print("Mask")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        IMTScores[2] = ScoreCompile(PKDA, IMTScores[2], PG[27])
                        PG[27] = PG[27] + 1
                        print("Tactical")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        IMTScores[3] = ScoreCompile(PKDA, IMTScores[3], PG[28])
                        PG[28] = PG[28] + 1
                        print("Olleh")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        IMTScores[4] = ScoreCompile(PKDA, IMTScores[4], PG[29])
                        PG[29] = PG[29] + 1
                        IMTDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "SHOP":
                    while Fuck == True:
                        print("Fakegod")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        SHOPScores[0] = ScoreCompile(PKDA, SHOPScores[0], PG[20])
                        PG[20] = PG[20] + 1
                        print("Bugi")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        SHOPScores[1] = ScoreCompile(PKDA, SHOPScores[1], PG[21])
                        PG[21] = PG[21] + 1
                        print("Insanity")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        SHOPScores[2] = ScoreCompile(PKDA, SHOPScores[2], PG[22])
                        PG[22] = PG[22] + 1
                        print("Bvoy")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        SHOPScores[3] = ScoreCompile(PKDA, SHOPScores[3], PG[23])
                        PG[23] = PG[23] + 1
                        print("Zeyzal")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        SHOPScores[4] = ScoreCompile(PKDA, SHOPScores[4], PG[24])
                        PG[24] = PG[24] + 1
                        SHOPDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "NRG":
                    while Fuck == True:
                        print("Dhokla")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        NRGScores[0] = ScoreCompile(PKDA, NRGScores[0], PG[30])
                        PG[30] = PG[30] + 1
                        print("Contracts")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        NRGScores[1] = ScoreCompile(PKDA, NRGScores[1], PG[31])
                        PG[31] = PG[31] + 1
                        print("Palafox")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        NRGScores[2] = ScoreCompile(PKDA, NRGScores[2], PG[32])
                        PG[32] = PG[32] + 1
                        print("Fbi")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        NRGScores[3] = ScoreCompile(PKDA, NRGScores[3], PG[33])
                        PG[33] = PG[33] + 1
                        print("Huhi")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        NRGScores[4] = ScoreCompile(PKDA, NRGScores[4], PG[34])
                        PG[34] = PG[34] + 1
                        NRGDC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                elif ans2 == "C9":
                    while Fuck == True:
                        print("Thanatos")
                        m = PlayerSS(1, rans)
                        PKDA = m
                        C9Scores[0] = ScoreCompile(PKDA, C9Scores[0], PG[10])
                        PG[10] = PG[10] + 1
                        print("Blaber")
                        m = PlayerSS(2, rans)
                        PKDA = m
                        C9Scores[1] = ScoreCompile(PKDA, C9Scores[1], PG[11])
                        PG[11] = PG[11] + 1
                        print("Jojopyun")
                        m = PlayerSS(3, rans)
                        PKDA = m
                        C9Scores[2] = ScoreCompile(PKDA, C9Scores[2], PG[12])
                        PG[12] = PG[12] + 1
                        print("Berserker")
                        m = PlayerSS(4, rans)
                        PKDA = m
                        C9Scores[3] = ScoreCompile(PKDA, C9Scores[3], PG[13])
                        PG[13] = PG[13] + 1
                        print("Vulcan")
                        m = PlayerSS(5, rans)
                        PKDA = m
                        C9Scores[4] = ScoreCompile(PKDA, C9Scores[4], PG[14])
                        PG[14] = PG[14] + 1
                        C9DC = True
                        print("did you do it right? (Y/N)")
                        ans3 = input()
                        if ans3 == "Y":
                            Z = False
                            Fuck = False
                        if ans3 == "N":
                            Z = True
                            Fuck = True
                else:
                    Z = True
        case "Q":
            print("Does the Data base need to be updated? (Y/N)")
            ans7 = input()
            if ans7 == 'Y': 
                print("How up to date is this database?")
                ans6 = open("Database.txt", "w")
                ocs = input()
                ans6.write(ocs)
                ans6.close
            print("Thanks for using the program bye bye") 
            K = False
        case "P":
            print("Bo3 or Bo5")
            ans11 = input()
            if ans11 == "Bo3":
                U = True
                while(U):
                    print("Who are the two teams playing?")
                    print("Team 1")
                    T1 = input()
                    print("Team 2")
                    T2 = input()
                    print("Does this look correct? (Y/N)")
                    print(T1 + " Vs " + T2)
                    ans5 = input()
                    if(ans5 == "Y"): 
                        if T1 in Teams: 
                            Teamcheck = True
                        else: Teamcheck = False
                        if T2 in Teams: Teamcheck = True
                        else: Teamcheck = False
                        if Teamcheck == True: 
                            print("Teams check out.")
                            U = False
                            if T1 == "TL": T1S = TeamScores[7]
                            elif T1 == "FLY": T1S = TeamScores[1]
                            elif T1 == "100T": T1S = TeamScores[3]
                            elif T1 == "DIG": T1S = TeamScores[0]
                            elif T1 == "IMT": T1S = TeamScores[5]
                            elif T1 == "NRG": T1S = TeamScores[6]
                            elif T1 == "C9": T1S = TeamScores[2]
                            elif T1 == "SHOP": T1S = TeamScores[4]

                            if T2 == "TL": T2S = TeamScores[7]
                            elif T2 == "FLY": T2S = TeamScores[1]
                            elif T2 == "100T": T2S = TeamScores[3]
                            elif T2 == "DIG": T2S = TeamScores[0]
                            elif T2 == "IMT": T2S = TeamScores[5]
                            elif T2 == "NRG": T2S = TeamScores[6]
                            elif T2 == "C9": T2S = TeamScores[2]
                            elif T2 == "SHOP": T2S = TeamScores[4]
                            MSTF = False
                            if T1S > T2S: 
                                print(T1 + " is favored to win over " + T2)
                                print(TeamScorePerWin(T1S,T2S))
                                print(TeamScoreSS(T1S,T2S))
                            elif T1S < T2S: 
                                print(T2 + " is favored to win over " + T1)
                                print(TeamScorePerWin(T1S,T2S))
                                print(TeamScoreSS(T1S,T2S))
                            else: 
                                print("The Teams are evenly matched")
                                print(TeamScorePerWin(T1S,T2S))
                        if Teamcheck == False: 
                            print("Team or Teams are not in the data base please try again")
                            U = True
                    if(ans5 == "N"): U = True
            if ans11 == "Bo5":
                U = True
                while(U):
                    print("Who are the two teams playing?")
                    print("Team 1")
                    T1 = input()
                    print("Team 2")
                    T2 = input()
                    print("Does this look correct? (Y/N)")
                    print(T1 + " Vs " + T2)
                    ans5 = input()
                    if(ans5 == "Y"): 
                        if T1 in Teams: 
                            Teamcheck = True
                        else: Teamcheck = False
                        if T2 in Teams: Teamcheck = True
                        else: Teamcheck = False
                        if Teamcheck == True: 
                            print("Teams check out.")
                            U = False
                            if T1 == "TL": T1S = TeamScores[7]
                            elif T1 == "FLY": T1S = TeamScores[1]
                            elif T1 == "100T": T1S = TeamScores[3]
                            elif T1 == "DIG": T1S = TeamScores[0]
                            elif T1 == "IMT": T1S = TeamScores[5]
                            elif T1 == "NRG": T1S = TeamScores[6]
                            elif T1 == "C9": T1S = TeamScores[2]
                            elif T1 == "SHOP": T1S = TeamScores[4]

                            if T2 == "TL": T2S = TeamScores[7]
                            elif T2 == "FLY": T2S = TeamScores[1]
                            elif T2 == "100T": T2S = TeamScores[3]
                            elif T2 == "DIG": T2S = TeamScores[0]
                            elif T2 == "IMT": T2S = TeamScores[5]
                            elif T2 == "NRG": T2S = TeamScores[6]
                            elif T2 == "C9": T2S = TeamScores[2]
                            elif T2 == "SHOP": T2S = TeamScores[4]
                            MSTF = False
                            if T1S > T2S: 
                                print(T1 + " is favored to win over " + T2)
                                print(TeamScorePerWin(T1S,T2S))
                                print(TeamScoreSSB5(T1S,T2S))
                            elif T1S < T2S: 
                                print(T2 + " is favored to win over " + T1)
                                print(TeamScorePerWin(T1S,T2S))
                                print(TeamScoreSSB5(T1S,T2S))
                            else: 
                                print("The Teams are evenly matched")
                                print(TeamScorePerWin(T1S,T2S))
                        if Teamcheck == False: 
                            print("Team or Teams are not in the data base please try again")
                            U = True
                    if(ans5 == "N"): U = True
        case "B": 
            if DIGDC == True:
                PS[0] = DIGScores[0]
                PS[1] = DIGScores[1]
                PS[2] = DIGScores[2]
                PS[3] = DIGScores[3]
                PS[4] = DIGScores[4]
                print("DIG is up to date")
            if FLYDC == True:
                PS[5] = FLYScores[0] 
                PS[6] = FLYScores[1] 
                PS[7] = FLYScores[2] 
                PS[8] = FLYScores[3] 
                PS[9] = FLYScores[4] 
                print("FLY is up to date")
            if C9DC == True:
                PS[10] = C9Scores[0] 
                PS[11] = C9Scores[1] 
                PS[12] = C9Scores[2] 
                PS[13] = C9Scores[3] 
                PS[14] = C9Scores[4] 
                print("C9 is up to date")
            if S100TDC == True:
                PS[15] = S100TScores[0] 
                PS[16] = S100TScores[1] 
                PS[17] = S100TScores[2] 
                PS[18] = S100TScores[3] 
                PS[19] = S100TScores[4] 
                print("100T is up to date")
            if SHOPDC == True:
                PS[20] = SHOPScores[0] 
                PS[21] = SHOPScores[1] 
                PS[22] = SHOPScores[2] 
                PS[23] = SHOPScores[3] 
                PS[24] = SHOPScores[4]
                print("SHOP is up to date")
            if IMTDC == True:
                PS[25] = IMTScores[0] 
                PS[26] = IMTScores[1] 
                PS[27] = IMTScores[2] 
                PS[28] = IMTScores[3]
                PS[29] = IMTScores[4] 
                print("IMT is up to date")
            if NRGDC == True:
                PS[30] = NRGScores[0] 
                PS[31] = NRGScores[1] 
                PS[32] = NRGScores[2] 
                PS[33] = NRGScores[3] 
                PS[34] = NRGScores[4] 
                print("NRG is up to date")
            if TLDC == True:
                PS[35] = TLScores[0] 
                PS[36] = TLScores[1] 
                PS[37] = TLScores[2] 
                PS[38] = TLScores[3] 
                PS[39] = TLScores[4] 
                print("TL is up to date")
            
            print("Everything is up to date")
            S100TDC = False
            FLYDC = False
            TLDC = False
            NRGDC = False
            IMTDC = False
            SHOPDC = False
            C9DC = False
            DIGDC = False

            SSExport(PG, PS)

            TSFileC = open('TeamScores.txt', 'w')
            for x in TeamScores:
                OTS = str(x) + ","
                TSFileC.write(OTS)
            TSFileC.close
        case "T":
            print("What list would you like to see?")
            print("(L)ane")
            print("(T)eams")
            ans8 = input()
            if ans8 == "L":
                print("What lane would you like to see?")
                print("(T)op")
                print("(J)ungle")
                print("(M)id")
                print("(A)dc")
                print("(S)upport")
                ans9 = input()
                match ans9:
                    case "T":
                        TList = [DIGScores[0], FLYScores[0], C9Scores[0], S100TScores[0], SHOPScores[0], IMTScores[0], NRGScores[0], TLScores[0]]
                        TTeirlist = sorted(TList, reverse=True)
                        for x in TTeirlist:
                            num = round(x,2)
                            if x == TList[0]:
                                print("Licorice " + str(num))
                            elif x == TList[1]:
                                print("Bwipo " + str(num))
                            elif x == TList[2]:
                                print("Thanatos " + str(num))
                            elif x == TList[3]:
                                print("Sniper " + str(num))
                            elif x == TList[4]:
                                print("Fakegod " + str(num))
                            elif x == TList[5]:
                                print("Castle " + str(num))
                            elif x == TList[6]:
                                print("Dhokla " + str(num))
                            elif x == TList[7]:
                                print("Impact " + str(num))
                            else: print("Something isnt right")
                    case "J":
                        JList = [DIGScores[1], FLYScores[1], C9Scores[1], S100TScores[1], SHOPScores[1], IMTScores[1], NRGScores[1], TLScores[1]]
                        JTeirlist = sorted(JList, reverse=True)
                        for x in JTeirlist:
                            num = round(x,2)
                            if x == JList[0]:
                                print("Spica " + str(num))
                            elif x == JList[1]:
                                print("Inspired " + str(num))
                            elif x == JList[2]:
                                print("Blaber " + str(num))
                            elif x == JList[3]:
                                print("River " + str(num))
                            elif x == JList[4]:
                                print("Bugi " + str(num))
                            elif x == JList[5]:
                                print("Armao " + str(num))
                            elif x == JList[6]:
                                print("Contracts " + str(num))
                            elif x == JList[7]:
                                print("Umti " + str(num))
                            else: print("Something isnt right")
                    case "M":
                        MList = [DIGScores[2], FLYScores[2], C9Scores[2], S100TScores[2], SHOPScores[2], IMTScores[2], NRGScores[2], TLScores[2]]
                        MTeirlist = sorted(MList, reverse=True)
                        for x in MTeirlist:
                            num = round(x,2)
                            if x == MList[0]:
                                print("Jensen " + str(num))
                            elif x == MList[1]:
                                print("Quad " + str(num))
                            elif x == MList[2]:
                                print("Jojopyun " + str(num))
                            elif x == MList[3]:
                                print("Quid " + str(num))
                            elif x == MList[4]:
                                print("Insanity " + str(num))
                            elif x == MList[5]:
                                print("Mask " + str(num))
                            elif x == MList[6]:
                                print("Palafox " + str(num))
                            elif x == MList[7]:
                                print("APA " + str(num))
                            else: print("Something isnt right")
                    case "A": 
                        AList = [DIGScores[3], FLYScores[3], C9Scores[3], S100TScores[3], SHOPScores[3], IMTScores[3], NRGScores[3], TLScores[3]]
                        ATeirlist = sorted(AList, reverse=True)
                        for x in ATeirlist:
                            num = round(x,2)
                            if x == AList[0]:
                                print("Zven " + str(num))
                            elif x == AList[1]:
                                print("Massu " + str(num))
                            elif x == AList[2]:
                                print("Berserker " + str(num))
                            elif x == AList[3]:
                                print("Meech " + str(num))
                            elif x == AList[4]:
                                print("Bvoy " + str(num))
                            elif x == AList[5]:
                                print("Tactical " + str(num))
                            elif x == AList[6]:
                                print("FBI " + str(num))
                            elif x == AList[7]:
                                print("Yeon " + str(num))
                            else: print("Something isnt right")
                    case "S":
                        SList = [DIGScores[4], FLYScores[4], C9Scores[4], S100TScores[4], SHOPScores[4], IMTScores[4], NRGScores[4], TLScores[4]]
                        STeirlist = sorted(SList, reverse=True)
                        for x in STeirlist:
                            num = round(x,2)
                            if x == SList[0]:
                                print("Isles " + str(num))
                            elif x == SList[1]:
                                print("Busio " + str(num))
                            elif x == SList[2]:
                                print("Vulcan " + str(num))
                            elif x == SList[3]:
                                print("Eyla " + str(num))
                            elif x == SList[4]:
                                print("Zeyzal " + str(num))
                            elif x == SList[5]:
                                print("Olleh " + str(num))
                            elif x == SList[6]:
                                print("Huhi " + str(num))
                            elif x == SList[7]:
                                print("Core JJ " + str(num))
                            else: print("Something isnt right")

            elif ans8 == "T":
                Teirlist = sorted(TeamScores, reverse=True) #Lowest to Highest
                for x in Teirlist:
                    num = round(x,2)
                    if x == TeamScores[0]:
                        print("DIG " + str(num))
                    elif x == TeamScores[1]:
                        print("FLY " + str(num))
                    elif x == TeamScores[2]:
                        print("C9 " + str(num))
                    elif x == TeamScores[3]:
                        print("100T " + str(num))
                    elif x == TeamScores[4]:
                        print("SHOP " + str(num))
                    elif x == TeamScores[5]:
                        print("IMT " + str(num))
                    elif x == TeamScores[6]:
                        print("NRG " + str(num))
                    elif x == TeamScores[7]:
                        print("TL " + str(num))
                    else: print("Something isnt right")
                