#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Leiðbeiningar:
#
# Passa að dálkar í Excel skjalinu heiti nákvæmlega:
# BANKANUMER, HOFUDBNR, SKULDABNR, KENNITALA, GJALDDAGI,
# GREIDSLUDAG, AFBORGUN, VEXTIR, VERDBAETUR, DRVEXTIR,
# KOSTNADUR, EFTIRSTODVAR, ATHUGASEMDIR
#
# Röð dálka skiptir ekki máli. Það mega vera aðrir dálkar líka í skjalinu. En
# allir þessir dálkar þurfa að vera, og þurfa að heita nákvæmlega eins og að
# ofan, öll nöfn í hástöfum. Ath. að stafsetning á sumum dálkanöfnunum er
# óvenjuleg.
#
# GJALDDAGI og GREIDSLUDAG þurfa nú þegar að vera á forminu YYYYMMDD í Excel
# skjalinu - forritið sér ekki um að breyta úr hefðbundnu dagsetningarsniði.
#
# Aðra dálka þarf ekki að núllfylla, forritið sér um það.
#
# Til að keyra í vafra:
# 1. Fara hingað í vafra: http://www.compileonline.com/execute_python_online.php
# 2. Opna þessa skrá (sem þú ert að lesa) í Notepad og kópera allan texta
# 3. Paste-a allan texta inn í flipann sem heitir main.py á vefsíðunni, í
#    staðinn fyrir það sem er þar fyrir
# 4. Í Excel, gera File / Save As... og velja Comma Separated Values, vista
#    þá skrá og opna hana síðan með Notepad, kópera allan texta í henni
# 5. Paste-a allan texta inn í flipann sem heitir STDIN á vefsíðunni
# 6. Ýta á Execute takkann á vefsíðunni (lengst til vinstri, við hlið flipa)
# 7. Niðurstaðan birtist í "Result" flipanum hægra megin.
#
# Til að keyra á eigin tölvu:
# 0. Setja upp Python3 héðan: https://www.python.org/downloads/
# 1. Í Excel, gera File / Save As... og velja Comma Separated Values, vista
#    sem t.d. inntak.csv í sömu möppu og þetta forrit.
# 2. Opna 'cmd' forritið í Windows.
# 3. Gera 'cd' inn í möppuna þar sem þetta forrit er
# 4. Gera: python3 skattskil.py < inntak.csv > uttak.txt
# 5. Nú ætti útakið að vera í skránni uttak.txt í sömu möppu.


import csv
import sys


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


if __name__ == '__main__':
    reader = csv.DictReader(sys.stdin, dialect='excel', delimiter=';')
    dictList = []
    for line in reader:
        print(makeLineFromDict(line))
