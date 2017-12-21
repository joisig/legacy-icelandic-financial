#!/usr/bin/env python3

import csv
import sys

# Leiðbeiningar:
#
# Passa að dálkar í Excel skjalinu heiti nákvæmlega:
# BANKANUMER, HOFUDBNR, SKULDABNR, KENNITALA, GJALDDAGI,
# GREIDSLUDAG, AFBORGUN, VEXTIR, VERDBAETUR, DRVEXTIR,
# KOSTNADUR, EFTIRSTODVAR, ATHUGASEMDIR
#
# Röð dálka skiptir ekki máli. Það mega vera aðrir dálkar líka í skjalinu.
#
# GJALDDAGI og GREIDSLUDAG þurfa nú þegar að vera á forminu YYYYMMDD.
#
# Aðra dálka þarf ekki að núllfylla, forritið sér um það.
#
# Til að keyra:
# 1. Í Excel, gera File / Save As... og velja Comma Separated Values, vista
#    sem t.d. inntak.csv í sömu möppu og þetta forrit.
# 2. Opna 'cmd' forritið í Windows.
# 3. Gera 'cd' inn í möppuna þar sem þetta forrit er
# 4. Gera: python3 skattskil.py inntak.csv > uttak.txt
#
# Nú ætti útakið að vera í skránni uttak.txt í sömu möppu.


def padFront(num, char, msg):
    numSpaces = num - len(msg)
    return (char * numSpaces) + msg


def toChar(num, msg):
    return padFront(num, ' ', msg)


def toNumber(num, number):
    if isinstance(number, str):
        return padFront(num, '0', number)
    else:
        return toNumber(num, str(number))


def makeLine(bankanumer, hofudbnr, skuldabnr, kennitala, gjalddagi,
               greidsludag, afborgun, vextir, verdbaetur, drvextir,
               kostnadur, eftirstodvar, athugasemdir):
    lineParts = [
        toChar(4, bankanumer),
        toChar(2, hofudbnr),
        toChar(6, skuldabnr),
        toNumber(10, kennitala),
        #dateToChar(gjalddagi),
        #dateToChar(greidsludag),
        toNumber(8, gjalddagi),
        toNumber(8, greidsludag),
        toNumber(9, afborgun.replace('.', '')),
        toNumber(9, vextir.replace('.', '')),
        toNumber(9, verdbaetur.replace('.', '')),
        toNumber(9, drvextir),
        toNumber(9, kostnadur),
        toNumber(9, eftirstodvar.replace('.', '')),
        toChar(10, athugasemdir)
    ]
    return "".join(lineParts)


def makeLineFromDict(dict):
    return makeLine(
        dict["BANKANUMER"], dict["HOFUDBNR"], dict["SKULDABNR"], dict["KENNITALA"],
        dict["GJALDDAGI"], dict["GREIDSLUDAG"], dict["AFBORGUN"], dict["VEXTIR"],
        dict["VERDBAETUR"], dict["DRVEXTIR"], dict["KOSTNADUR"],
        dict["EFTIRSTODVAR"], dict["ATHUGASEMDIR"]
    )


def run(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, dialect='excel', delimiter=';')
        dictList = []
        for line in reader:
            print(makeLineFromDict(line))

if __name__ == '__main__':
    run(sys.argv[1])
