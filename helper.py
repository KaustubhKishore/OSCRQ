import subprocess as sp
import os
import platform
from datetime import datetime
from tabulate import tabulate

class Helper:

    nc = "\033[91m" + "[NC]" + "\033[0m" + " "
    c = "\033[92m" + "[C]" + "\033[0m" + " "
    info = "\033[94m" + "[INFO]" + "\033[0m" + " "


    def __init__(self):
        self.id = ""
        self.platform = ""
        self.dateAndTime = ""
        self.recordID = ""
        self.actualDateTimeObject = datetime.now()

        self.score = 0
        self.infoScore = 0

        self.ncScore = 0
        self.ncInfoScore = 0

        self.COMPLIANT = list()
        self.NOTCOMPLIANT = list()
        self.INFOCOMPLIANT = list()
        self.INFONOTCOMPLIANT = list()
        self.INFONOTSURE = list()

        self.getIdentifiers()

    def getIdentifiers(self):
        cmdOne = r"cat /sys/class/dmi/id/product_uuid"
        self.id = self.caller(cmdOne)
        self.platform = platform.version()

        self.dateAndTime = self.actualDateTimeObject.strftime("%d/%m/%Y %H:%M:%S")

    def Compliant(self, audit):
        self.COMPLIANT.append(audit)
        print("\n" + self.c + audit)
        print("-----------------")
        self.score += 1

    def NotCompliant(self, audit):
        self.NOTCOMPLIANT.append(audit)
        print("\n" + self.nc + audit)
        print("-----------------")
        self.ncScore += 1

    def InfoCompliant(self, audit):
        self.INFOCOMPLIANT.append(audit)
        print("\n" + self.info + self.c + audit)
        print("-----------------")
        self.infoScore += 1

    def InfoNotCompliant(self, audit):
        self.INFONOTCOMPLIANT.append(audit)
        print("\n" + self.info + self.nc + audit)
        print("-----------------")
        self.ncInfoScore += 1

    def InfoNotSure(self, audit):
        self.INFONOTSURE.append(audit)
        print("\n" + self.info + audit)
        print("-----------------")

    def score_getter(self):
        return self.score

    def infoScore_getter(self):
        return self.infoScore

    def ncScore_getter(self):
        return self.ncScore

    def ncInfoScore_getter(self):
        return self.ncInfoScore

    def caller(self, cmd):
        p = sp.Popen("timeout 7 "+cmd, shell=True, stdin=sp.PIPE,
                     stdout=sp.PIPE, stderr=sp.STDOUT, preexec_fn=os.setsid)
        outp = p.stdout.read().decode()
        p.kill()
        return (
            outp
        )
    def printer(self):
        finalList = list()
        headers = ["Audit", "Scored", "Compliant"]
        for i in self.COMPLIANT:
            temp = [i, "✅", "✅"]
            finalList.append(temp)

        for i in self.NOTCOMPLIANT:
            temp = [i, "✅", "❌"]
            finalList.append(temp)

        for i in self.INFOCOMPLIANT:
            temp = [i, "❌", "✅"]
            finalList.append(temp)

        for i in self.INFONOTCOMPLIANT:
            temp = [i, "❌", "❌"]
            finalList.append(temp)

        for i in self.INFONOTSURE:
            temp = [i, "❌", "➖"]
            finalList.append(temp)

        print(tabulate(finalList, headers=headers, tablefmt="fancy_grid", colalign=("left","center", "center")))
        try:
            filename = self.actualDateTimeObject.strftime("%d_%m_%Y_%H_%M_%S") + ".html"
            f = open(filename, "w+")
            html = tabulate(finalList, headers=headers, tablefmt="html", colalign=("left","center", "center"))
            f.write("""
            <h1>OSCARQ - Open Source Cyber Advanced Risk Quantification </h1>
            <b>Device Unique ID:</b> {} <br>
            <b>Platform:</b> {} <br>
            <b>Time of Benchmarking:</b> {} <br>
            <b>MongoDB Record Reference</b>: {} <br>
            <br>
            {}
            """.format(self.id, self.platform, self.dateAndTime, self.recordID, html))

            f.close()

        except Exception as e:
            print("File Error! ", e)

