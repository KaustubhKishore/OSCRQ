import os

class Debian:
    nc = '\033[91m' + "[NC]" + '\033[0m' + " "
    c = '\33[32m' + "[C]" + '\033[0m' + " "
    info = '\33[94m' + "[INFO]" + '\033[0m' + " "
    
    def __init__(self):
        self.id = "unique id"
        self.score = 0
        self.infoScore = 0

        self.ncScore = 0
        self.ncInfoScore = 0

    def score_getter(self):
        return self.score

    def runner(self):
        self.freevxfs_1_1_1_1()
        self.jffs2_1_1_1_2()
        self.hfs_1_1_1_3()
        self.hfsplus_1_1_1_4()
        self.squashfs_1_1_1_5()
        self.udf_1_1_1_6()
        return 1

    def Compliant(self, audit):
        print(Debian.c + audit)
        self.score += 1
    
    def NotCompliant(self, audit):
        print(Debian.nc + audit)
        self.ncScore += 1

    def InfoCompliant(self, audit):
        print(Debian.info + Debian.c + audit)
        self.infoScore +=1
    
    def InfoNotCompliant(self, audit):
        print(Debian.info + Debian.nc + audit)
        self.ncInfoScore += 1


    def freevxfs_1_1_1_1(self):
        cmdOne = "modprobe -n -v freevxfs"
        cmdTwo = "lsmod | grep freevxfs"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()
        

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        
    def jffs2_1_1_1_2(self):
        cmdOne = "modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        cmdTwo = "lsmod | grep jffs2"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")

    def hfs_1_1_1_3(self):
        cmdOne = "modprobe -n -v hfs"
        cmdTwo = "lsmod | grep hfs"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of hfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfs filesystems is disabled (Scored)")

    def hfsplus_1_1_1_4(self):
        cmdOne = "modprobe -n -v hfsplus"
        cmdTwo = "lsmod | grep hfsplus"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()
        
        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")

    def squashfs_1_1_1_5(self):
        cmdOne = "modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        cmdTwo = "lsmod | grep squashfs"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()
        
        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of squashfs filesystems is disabled (Scored)")
            
        else:
            self.NotCompliant("Ensure mounting of squashfs filesystems is disabled (Scored)")


    def udf_1_1_1_6(self):
        cmdOne = "modprobe -n -v udf | grep -E '(udf|install)'"
        cmdTwo = "lsmod | grep udf"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of udf filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of udf filesystems is disabled (Scored)")
        

# if __name__ == "__main__":
#     obj = Debian()
#     obj.runner()
