import os
from helper import Helper

class Debian(Helper):

    profile = [
        "freevxfs_1_1_1_1", 
        "jffs2_1_1_1_2",
        "hfs_1_1_1_3", 
        "hfsplus_1_1_1_4", 
        "squashfs_1_1_1_5", 
        "udf_1_1_1_6"
    ]
    
    
    def __init__(self):
        super().__init__()
        self.id = "unique id"
        

    def runner(self):
        allfuncs = dir(Debian)
        for f in allfuncs:
            if f in self.profile:
                call = getattr(Debian, f)
                call(self)


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
        