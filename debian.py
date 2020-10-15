import os

class Debian:
    nc = '\033[91m' + "[NC]" + '\033[0m' + " "
    c = '\33[32m' + "[C]" + '\033[0m' + " "
    info = '\33[94m' + "[INFO]" + '\033[0m' + " "
    
    def __init__(self):
        self.id = "unique id"
        self.score = 0
        
    def score_getter(self):
        return self.score

    def runner(self):
        self.freevxfs_1_1_1_1()
        self.jffs2_1_1_1_2()
        self.hfs_1_1_1_3()
        return 1

    def freevxfs_1_1_1_1(self):
        cmdOne = "modprobe -n -v freevxfs"
        cmdTwo = "lsmod | grep freevxfs"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()
        

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            print(Debian.c + "Ensure mounting of freevxfs filesystems is disabled (Scored)")
            self.score += 1
        else:
            print(Debian.nc + "Ensure mounting of freevxfs filesystems is disabled (Scored)")
        
    def jffs2_1_1_1_2(self):
        cmdOne = "modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        cmdTwo = "lsmod | grep jffs2"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            print(Debian.c + "Ensure mounting of jffs2 filesystems is disabled (Scored)")
            self.score += 1
        else:
            print(Debian.nc + "Ensure mounting of jffs2 filesystems is disabled (Scored)")

    def hfs_1_1_1_3(self):
        cmdOne = "modprobe -n -v hfs"
        cmdTwo = "lsmod | grep hfs"
        outputOne = os.popen(cmdOne).read()
        outputTwo = os.popen(cmdTwo).read()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            print(Debian.c + "Ensure mounting of hfs filesystems is disabled (Scored)")
            self.score += 1
        else:
            print(Debian.nc + "Ensure mounting of hfs filesystems is disabled (Scored)")


# if __name__ == "__main__":
#     obj = Debian()
#     obj.runner()
