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
        "tmp_1_1_2", # Requires testing.
        "nodev_1_1_3", # Might need testing
        "nosuid_1_1_4",
        "noexec_1_1_5",
        "sepvar_1_1_6",
        "sepvartmp_1_1_7",
        "nodevvartemp_1_1_8",
        "nosuidvartmp_1_1_9",
        "noexecvartmp_1_1_10",

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
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of freevxfs filesystems is disabled (Scored)")
        
    def jffs2_1_1_1_2(self):
        cmdOne = r"modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        cmdTwo = r"lsmod | grep jffs2"
        cmdThree = r"/sbin/modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of jffs2 filesystems is disabled (Scored)")

    def hfs_1_1_1_3(self):
        cmdOne = r"modprobe -n -v hfs"
        cmdTwo = r"lsmod | grep hfs"
        cmdThree = r"/sbin/modprobe -n -v hfs"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of hfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfs filesystems is disabled (Scored)")

    def hfsplus_1_1_1_4(self):
        cmdOne = r"modprobe -n -v hfsplus"
        cmdTwo = r"lsmod | grep hfsplus"
        cmdThree = r"/sbin/modprobe -n -v hfsplus"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of hfsplus filesystems is disabled (Scored)")

    def squashfs_1_1_1_5(self):
        cmdOne = r"modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        cmdTwo = r"lsmod | grep squashfs"
        cmdThree = r"/sbin/modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree) 

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of squashfs filesystems is disabled (Scored)")
            
        else:
            self.NotCompliant("Ensure mounting of squashfs filesystems is disabled (Scored)")

    def udf_1_1_1_6(self):
        cmdOne = r"modprobe -n -v udf | grep -E '(udf|install)'"
        cmdTwo = r"lsmod | grep udf"
        cmdThree = r"/sbin/modprobe -n -v udf | grep -E '(udf|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if( (outputOne == 'install /bin/true \n' or outputThree == 'install /bin/true \n') and outputTwo == ""):
            self.Compliant("Ensure mounting of udf filesystems is disabled (Scored)")
        else:
            self.NotCompliant("Ensure mounting of udf filesystems is disabled (Scored)")
        
    def fat_1_1_1_7(self):
        cmdOne = r"grep -E -i '\svfat\s' /etc/fstab"
        cmdTwo = r"modprobe -n -v vfat | grep -E '(vfat|install)'"
        cmdThree = r"lsmod | grep vfat"
        cmdFour = r"/sbin/modprobe -n -v vfat | grep -E '(vfat|install)'"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if( (outputTwo == 'install /bin/true \n' or outputFour == 'install /bin/true \n' ) and outputThree == ""):
            self.InfoCompliant("Ensure mounting of FAT filesystems is limited (Not Scored)")
        else:
            self.InfoNotCompliant("Ensure mounting of FAT filesystems is limited (Not Scored)")

        if outputOne != '':
            print("Ensure FAT filesystem is used only where appropirate:\n" + outputOne)


    def tmp_1_1_2(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"grep -E '\s/tmp\s' /etc/fstab | grep -E -v '^\s*#'"
        cmdThree = r"systemctl is-enabled tmp.mount"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if outputOne != "" and (outputTwo != "" or outputThree == "enabled\n"):
            self.Compliant("Ensure /tmp is configured (Scored)")
        else:
            self.NotCompliant("Ensure /tmp is configured (Scored)")
    

    def nodev_1_1_3(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v nodev"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        
        if outputOne == "":
            self.NotCompliant("Ensure nodev option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nodev option set on /tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure nodev option set on /tmp partition (Scored)")
            

    def nosuid_1_1_4(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v nosuid"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        
        if outputOne == "":
            self.NotCompliant("Ensure nosuid option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nosuid option set on /tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure nosuid option set on /tmp partition (Scored)")

    def noexec_1_1_5(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v noexec"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure noexec option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure noexec option set on /tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure noexec option set on /tmp partition (Scored)")

    def sepvar_1_1_6(self):
        cmdOne = r"mount | grep -E '\s/var\s'"
        outputOne = self.caller(cmdOne)
        
        if(outputOne == ""):
            self.NotCompliant("Ensure separate partition exists for /var (Scored)")
        elif "/var" in outputOne:
            self.Compliant("Ensure separate partition exists for /var (Scored)")
        else:
            self.NotCompliant("Ensure separate partition exists for /var (Scored)")

    def sepvartmp_1_1_7(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        outputOne = self.caller(cmdOne)
        
        if(outputOne == ""):
            self.NotCompliant("Ensure separate partition exists for /var/tmp (Scored)")
        elif "/var/tmp" in outputOne:
            self.Compliant("Ensure separate partition exists for /var/tmp (Scored)")
        else:
            self.NotCompliant("Ensure separate partition exists for /var/tmp (Scored)")

    def nodevvartemp_1_1_8(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v nodev"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure nodev option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nodev option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure nodev option set on /var/tmp partition (Scored)")
    
    def nosuidvartmp_1_1_9(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v nosuid"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure nosuid option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nosuid option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure nosuid option set on /var/tmp partition (Scored)")
    
    def noexecvartmp_1_1_10(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v noexec"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure noexec option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure noexec option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant("Ensure noexec option set on /var/tmp partition (Scored)")
    
