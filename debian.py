import subprocess as sp
from helper import Helper

class Debian(Helper):

    profile = [
        "freevxfs_1_1_1_1", 
        "jffs2_1_1_1_2",
        "hfs_1_1_1_3", 
        "hfsplus_1_1_1_4", 
        "squashfs_1_1_1_5", 
        "udf_1_1_1_6",
        "fat_1_1_1_7",
        "tmp_1_1_2" # Requires testing.
    ]
    
    
    def __init__(self):
        super().__init__()
        self.id = "unique id"
        

    def runner(self):
        for p in self.profile:
            call = getattr(Debian, p)
            call(self)

    def freevxfs_1_1_1_1(self):
        cmdOne = r"modprobe -n -v freevxfs"
        cmdTwo = r"lsmod | grep freevxfs"
        cmdThree = r"/sbin/modprobe -n -v freevxfs"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputThree = sp.Popen(cmdThree, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        
    def jffs2_1_1_1_2(self):
        cmdOne = r"modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        cmdTwo = r"lsmod | grep jffs2"

        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")

    def hfs_1_1_1_3(self):
        cmdOne = r"modprobe -n -v hfs"
        cmdTwo = r"lsmod | grep hfs"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of hfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfs filesystems is disabled (Scored)")

    def hfsplus_1_1_1_4(self):
        cmdOne = r"modprobe -n -v hfsplus"
        cmdTwo = r"lsmod | grep hfsplus"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        
        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")

    def squashfs_1_1_1_5(self):
        cmdOne = r"modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        cmdTwo = r"lsmod | grep squashfs"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        
        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of squashfs filesystems is disabled (Scored)")
            
        else:
            self.NotCompliant("Ensure mounting of squashfs filesystems is disabled (Scored)")

    def udf_1_1_1_6(self):
        cmdOne = r"modprobe -n -v udf | grep -E '(udf|install)'"
        cmdTwo = r"lsmod | grep udf"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()

        if(outputOne == 'install /bin/true \n' and outputTwo == ""):
            self.Compliant("Ensure mounting of udf filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of udf filesystems is disabled (Scored)")
        
    def fat_1_1_1_7(self):
        cmdOne = r"grep -E -i '\svfat\s' /etc/fstab"
        cmdTwo = r"modprobe -n -v vfat | grep -E '(vfat|install)'"
        cmdThree = r"lsmod | grep vfat"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputThree = sp.Popen(cmdThree, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()

        if(outputTwo == 'install /bin/true \n' and outputThree == ""):
            self.InfoCompliant("Ensure mounting of FAT filesystems is limited (Not Scored)")
            print("Ensure FAT filesystem is used only where appropirate:\n" + outputOne)
        else:
            self.InfoNotCompliant("Ensure mounting of FAT filesystems is limited (Not Scored)")
            print("Ensure FAT filesystem is used only where appropirate:\n" + outputOne)

    def tmp_1_1_2(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"grep -E '\s/tmp\s' /etc/fstab | grep -E -v '^\s*#'"
        cmdThree = r"systemctl is-enabled tmp.mount"
        outputOne = sp.Popen(cmdOne, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputTwo = sp.Popen(cmdTwo, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()
        outputThree = sp.Popen(cmdThree, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT).stdout.read().decode()


        if outputOne == "tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)" and (outputTwo == "tmpfs  /tmp    tmpfs   defaults,noexec,nosuid,nodev 0   0" or outputThree == "enabled"):
            self.Compliant("Ensure /tmp is configured (Scored)")
        else:
            self.NotCompliant("Ensure /tmp is configured (Scored)")