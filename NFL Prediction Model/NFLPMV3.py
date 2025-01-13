import json
import pandas as pd

Teams = {"AZ"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "ATL" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "BAL" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "BUF" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "CAR" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "CHI" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "CIN" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "CLE" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "DAL" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "DEN" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "DET" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "GB"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "HOU" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "IND" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "JAC" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "KC"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "LV"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "LAC" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "LAR" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "MIA" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "MIN" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "NE"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "NO"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "NYG" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "NYJ" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "PHI" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "PIT" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "SF"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "SEA" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "TB"  : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "TEN" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "WAS" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0},
         "AVE" : {"ODPG" : 0.0, "OSPPD" : 0.0, "FGP" : 0.0, "TDP" : 0.0, "DDPG" : 0.0, "DSPPD" : 0.0, "TGP" : 0.0, "OTDH" : 0.0, "DTDH" : 0.0, "OTPG" : 0.0, "DTPG" : 0.0}}

def FODPG(OTGP, OTDH, DTDH, DTGP, Team):
    print(f"How many drives did the offense for {Team} have?")
    TGD = input()
    TGD = float(TGD)
    ONTGP = OTGP + 1
    NODPG = ((float(OTDH) + TGD) / ONTGP)
    FTGD = OTDH + TGD
    DNTGP = DTGP + 1
    NDDPG = ((float(DTDH) + TGD) / DNTGP)
    DFTGD = DTDH + TGD
    return NODPG, FTGD, ONTGP, NDDPG, DFTGD, DNTGP

def FODPG2(OTGP, OTDH, DTDH, DTGP, Team):
    print(f"How many drives did the offense for {Team} have?")
    TGD = input()
    TGD = float(TGD)
    NODPG = ((float(OTDH) + TGD) / OTGP)
    FTGD = OTDH + TGD
    NDDPG = ((float(DTDH) + TGD) / DTGP)
    DFTGD = DTDH + TGD
    return NODPG, FTGD, NDDPG, DFTGD

def FOSPPD(OSPPD, OFGP, OTDP, DSPPD, Team):
    print(f"How many drives did the {Team} offence score?")
    SD = input()
    SD = float(SD)
    FSD = SD + OSPPD
    print("How many were made field goals?")
    FGM = input()
    FGM = float(FGM)
    FFGM = OFGP + FGM
    TSD = SD - FGM
    FTDM = TSD + OTDP
    FSDP = SD + DSPPD
    return FFGM, FTDM, FSD, FSDP

def OTOF(Team, Team2):
    print(f"How Many Turnovers did the {Team} offence have?")
    ans1 = input()
    ctpg = Teams[Team]["OTPG"]
    tgp = Teams[Team]["TGP"]
    Ontpg = ((ctpg * (tgp - 1)) + float(ans1)) / (tgp)
    ctpg2 = Teams[Team2]["DTPG"]
    tgp2 = Teams[Team2]["TGP"]
    Dntpg = ((ctpg2 * (tgp2 - 1)) + float(ans1)) / (tgp2)
    return Ontpg, Dntpg

def DTOF(Team, Team2):
    print(f"How Many Turnovers did the {Team} defence have?")
    ans1 = input()
    ctpg = Teams[Team]["DTPG"]
    tgp = Teams[Team]["TGP"]
    Dntpg = ((ctpg * (tgp - 1)) + float(ans1)) / (tgp)
    ctpg2 = Teams[Team2]["OTPG"]
    tgp2 = Teams[Team2]["TGP"]
    Ontpg = ((ctpg2 * (tgp2 - 1)) + float(ans1)) / (tgp2)
    return Dntpg, Ontpg

def ImportData():
    kv = open("DataBase.txt", "r")
    f = kv.read()
    Teams2 = json.loads(f)
    return Teams2

def DataExport(Teams):
    kv = open("DataBase.txt", "w")
    ODS = json.dumps(Teams)
    kv.write(ODS)
    kv.close
   
def GameScoreCal(Teams, Team1, Team2):
    TOD = Teams[Team1]["ODPG"] - ((Teams[Team1]["ODPG"] - Teams[Team2]["DDPG"]) / 2)
    T1OSP = Teams[Team1]["OSPPD"] / Teams[Team1]["OTDH"]
    T2DSP = Teams[Team2]["DSPPD"] / Teams[Team2]["DTDH"]
    FOSP = T1OSP - ((T1OSP - T2DSP) / 2)
    TSD = TOD * FOSP
    T1FSP = Teams[Team1]["FGP"] / Teams[Team1]["OSPPD"]
    T1TSP = Teams[Team1]["TDP"] / Teams[Team1]["OSPPD"]
    TD = TSD * T1TSP
    FG = TSD * T1FSP
    t1tpg = Teams[Team2]["OTPG"]
    t2tpg = Teams[Team1]["DTPG"]
    numto = t1tpg + ((t2tpg - t1tpg) * .25)
    TP = (TD * 6) + (FG * 3) + (numto * 3)
    return TP

def sumfunc(df, thing):
    x = 0
    for index, row in df.iterrows():
        x = row[thing] + x
    y = x /32
    return y

print("Welcome to the NFL prediction Program.")
try:
    Teams = ImportData()
except:
    print("No data")
a = True

while a == True:
    print("Please Select an option.")
    print("(I)nput Data")
    print("(G)ame Predictions")
    print("(T)est")
    print("(P)ower Ranking")
    print("(Q)uit")
    ans1 = input()

    match ans1:
        case "I":
            mkl = Teams.keys()
            print(mkl)
            print("what two teams played this game?")
            Team1 = input("Team 1 ")
            Team2 = input("Team 2 ")
            Teams[Team1]["ODPG"], Teams[Team1]["OTDH"], Teams[Team1]["TGP"], Teams[Team2]["DDPG"], Teams[Team2]["DTDH"], Teams[Team2]["TGP"] = FODPG(Teams[Team1]["TGP"],Teams[Team1]["OTDH"], Teams[Team2]["DTDH"], Teams[Team2]["TGP"], Team1)
            Teams[Team2]["ODPG"], Teams[Team2]["OTDH"], Teams[Team1]["DDPG"], Teams[Team1]["DTDH"] = FODPG2(Teams[Team2]["TGP"],Teams[Team2]["OTDH"], Teams[Team1]["DTDH"], Teams[Team1]["TGP"], Team2)
            Teams[Team1]["FGP"], Teams[Team1]["TDP"], Teams[Team1]["OSPPD"], Teams[Team2]["DSPPD"] = FOSPPD(Teams[Team1]["OSPPD"], Teams[Team1]["FGP"], Teams[Team1]["TDP"], Teams[Team2]["DSPPD"], Team1)
            Teams[Team2]["FGP"], Teams[Team2]["TDP"], Teams[Team2]["OSPPD"], Teams[Team1]["DSPPD"] = FOSPPD(Teams[Team2]["OSPPD"], Teams[Team2]["FGP"], Teams[Team2]["TDP"], Teams[Team1]["DSPPD"], Team2)
            Teams[Team1]["OTPG"], Teams[Team2]["DTPG"] = OTOF(Team1, Team2)
            Teams[Team1]["DTPG"], Teams[Team2]["OTPG"] = DTOF(Team1, Team2)
            DataExport(Teams)

        case "G":
            print(Teams.keys())
            print("What Game is being played?")
            Team3 = input("Team 1 ")
            Team4 = input("Team 2 ")
            Team1S = round(GameScoreCal(Teams, Team3, Team4), 3)
            Team2S = round(GameScoreCal(Teams, Team4, Team3), 3)
            print(Team3 + " " + str(Team1S))
            print(Team4 + " " + str(Team2S))
            ODU = Team1S + Team2S
            nodu = round(ODU, 3)
            print("The Over/Under is " + str(nodu))
            SPD = Team1S - Team2S
            nspd = round(SPD, 3)
            print("The Spread is " + str(nspd))

        case "P":
            df = pd.DataFrame(Teams)
            Teamsdf = df.transpose()
            Teams["AVE"]["ODPG"] = sumfunc(Teamsdf, "ODPG")
            Teams["AVE"]["OSPPD"] = sumfunc(Teamsdf, "OSPPD")
            Teams["AVE"]["FGP"] = sumfunc(Teamsdf, "FGP")
            Teams["AVE"]["TDP"] = sumfunc(Teamsdf, "TDP")
            Teams["AVE"]["DDPG"] = sumfunc(Teamsdf, "DDPG")
            Teams["AVE"]["DSPPD"] = sumfunc(Teamsdf, "DSPPD")
            Teams["AVE"]["TGP"] = sumfunc(Teamsdf, "TGP")
            Teams["AVE"]["OTDH"] = sumfunc(Teamsdf, "OTDH")
            Teams["AVE"]["DTDH"] = sumfunc(Teamsdf, "DTDH")
            Teams["AVE"]["OTPG"] = sumfunc(Teamsdf, "OTPG")
            Teams["AVE"]["DTPG"] = sumfunc(Teamsdf, "DTPG")
            flk = Teams.keys()
            ranklist = []
            for x in flk:
                if x == "AVE":
                    pass
                else:
                    Team1S = round(GameScoreCal(Teams, "AVE", x), 3)
                    Team2S = round(GameScoreCal(Teams, x, "AVE"), 3)
                    SPD = Team2S - Team1S
                    ranklist.append([round(SPD, 2), x])
            teirlist = sorted(ranklist, reverse=True)
            oprt = 1
            for x in teirlist:
                print(f"{oprt}. {x[1]} {x[0]}")
                oprt = oprt + 1
            a = False
        case "Q":
            a = False
            print("Thanks for using the program.")

