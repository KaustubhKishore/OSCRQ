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
        "varlog_1_1_11",
        "varlogaudit_1_1_12",
        "home_1_1_13",
        "nodevhome_1_1_14",
        "nodevdevshm_1_1_15",
        "nosuiddevshm_1_1_16",
        "noexecdevshm_1_1_17",
        "removable_1_1_18_and_19_and_20",
        "stickybitwwd_1_1_21",
        "automounting_1_1_22",
        "usbstorage_1_1_23",
        "packagemanager_1_2_1",
        "gpgkeys_1_2_2",
        "sudoinstalled_1_3_1",
        "sudopty_1_3_2",
        "sudolog_1_3_3",
        "aide_1_4_1",
        "fsintegrity_1_4_2",
        "bootloaderconfig_1_5_1",
        "bootloaderpassword_1_5_2",
        "authroot_1_5_3",
        "xdnx_1_6_1", #Leaving out one check which shouldn't be a problem
        "aslr_1_6_2"
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
    
    def varlog_1_1_11(self):
        cmdOne = r"mount | grep /var/log"
        outputOne = self.caller(cmdOne)

        if "/var/log" in outputOne:
            self.Compliant("Ensure separate partition exists for /var/log (Scored)")
        else:
            self.NotCompliant("Ensure separate partition exists for /var/log (Scored)")
        
    def varlogaudit_1_1_12(self):
        cmdOne = r"mount | grep /var/log/audit"
        outputOne = self.caller(cmdOne)

        if "/var/log/audit" in outputOne:
            self.Compliant("Ensure separate partition exists for /var/log/audit (Scored)")
        else:
            self.NotCompliant("Ensure separate partition exists for /var/log/audit (Scored)")

    def home_1_1_13(self):
        cmdOne = r"mount | grep /home"
        outputOne = self.caller(cmdOne)

        if "/home" in outputOne:
            self.Compliant("Ensure separate partition exists for /home (Scored)")
        else:
            self.NotCompliant("Ensure separate partition exists for /home (Scored)")

    def nodevhome_1_1_14(self):
        cmdOne = r"mount | grep -E '\s/home\s'"
        cmdTwo = r"mount | grep -E '\s/home\s' | grep -v nodev"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure nodev option set on /home partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nodev option set on /home partition (Scored)")
        else:
            self.NotCompliant("Ensure nodev option set on /home partition (Scored)")
    
    def nodevdevshm_1_1_15(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v nodev"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure nodev option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nodev option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant("Ensure nodev option set on /dev/shm partition (Scored)")

    def nosuiddevshm_1_1_16(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v nosuid"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure nosuid option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure nosuid option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant("Ensure nosuid option set on /dev/shm partition (Scored)")
    
    def noexecdevshm_1_1_17(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v noexec"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant("Ensure noexec option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant("Ensure noexec option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant("Ensure noexec option set on /dev/shm partition (Scored)")
    
    def removable_1_1_18_and_19_and_20(self):
        cmdOne = r"mount"
        outputOne = self.caller(cmdOne)

        self.InfoNotSure("Ensure nodev,nosuid and noexec option set on removable media partitions (Not Scored)")

        if outputOne != "":
            print("Verify manually that all removable media has nodev,nosuid and noexec option set:\n" + outputOne)
    
    def stickybitwwd_1_1_21(self):
        cmdOne = r"df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.Compliant("Ensure sticky bit is set on all world-writable directories (Scored)")
        else:
            self.NotCompliant("Ensure sticky bit is set on all world-writable directories (Scored)")
    
    def automounting_1_1_22(self):
        cmdOne = r"systemctl is-enabled autofs"
        cmdTwo = r"dpkg -s autofs"

        outputOne = self.caller(cmdOne).strip()
        outputTwo = self.caller(cmdTwo)

        if outputOne == "disabled" or "package 'autofs' is not installed" in outputTwo:
            self.Compliant("Disable Automounting (Scored)")
        else:
            self.NotCompliant("Disable Automounting (Scored)")

    def usbstorage_1_1_23(self):
        cmdOne = r"modprobe -n -v usb-storage"
        cmdTwo = r"lsmod | grep usb-storage"
        cmdThree = r"/sbin/modprobe -n -v usb-storage"

        outputOne = self.caller(cmdOne).strip()
        outputTwo = self.caller(cmdTwo).strip()
        outputThree = self.caller(cmdThree).strip()

        if (outputOne == "install /bin/true" or outputThree == "install /bin/true") and outputTwo == "":
            self.Compliant("Disable USB Storage (Scored)")
        else:
            self.NotCompliant("Disable USB Storage (Scored)")

    def packagemanager_1_2_1(self):
        cmdOne = r"apt-cache policy"
        outputOne = self.caller(cmdOne)
        
        self.InfoNotSure("Ensure package manager repositories are configured (Not Scored)")
        if outputOne != "":
            print("verify the package repositories: \n" + outputOne)
    
    def gpgkeys_1_2_2(self):
        cmdOne = r"apt-key list"
        outputOne = self.caller(cmdOne)

        self.InfoNotSure("Ensure GPG keys are configured (Not Scored)")
        if outputOne != "":
            print("Verify GPG keys are configured correctly:\n" + outputOne)
    
    def sudoinstalled_1_3_1(self):
        cmdOne = r"dpkg -s sudo"
        cmdTwo = r"dpkg -s sudo-ldap"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if "install ok installed" in outputOne:
            self.Compliant("Ensure sudo is installed (Scored)")
        else:
            self.NotCompliant("Ensure sudo is installed (Scored)")
    
    def sudopty_1_3_2(self):
        cmdOne = r"grep -Ei '^\s*Defaults\s+([^#]+,\s*)?use_pty(,\s+\S+\s*)*(\s+#.*)?$' /etc/sudoers /etc/sudoers.d/*"
        outputOne = self.caller(cmdOne)

        if "use_pty" in outputOne:
            self.Compliant("Ensure sudo commands use pty (Scored)")
        else:
            self.NotCompliant("Ensure sudo commands use pty (Scored)")
    
    def sudolog_1_3_3(self):
        cmdOne = r"grep -Ei '^\s*Defaults\s+logfile=\S+' /etc/sudoers /etc/sudoers.d/*"
        outputOne = self.caller(cmdOne)

        if "logfile=" in outputOne:
            self.Compliant("Ensure sudo log file exists (Scored)")
        else:
            self.NotCompliant("Ensure sudo log file exists (Scored)")
    
    def aide_1_4_1(self):
        cmdOne = r"dpkg -s aide"
        outputOne = self.caller(cmdOne)

        if "install ok installed" in outputOne:
            self.Compliant("Ensure AIDE is installed (Scored)")
        else:
            self.NotCompliant("Ensure AIDE is installed (Scored)")
    
    def fsintegrity_1_4_2(self):
        cmdOne = r"systemctl is-enabled aidecheck.service"
        cmdTwo = r"systemctl is-enabled aidecheck.timer"
        cmdThree = r"systemctl status aidecheck.timer"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if "enabled" in outputOne and "enabled" in outputTwo and "active (running)" in outputThree:
            self.Compliant("Ensure filesystem integrity is regularly checked (Scored)")
        else:
            self.NotCompliant("Ensure filesystem integrity is regularly checked (Scored)")

    def bootloaderconfig_1_5_1(self):
        cmdOne = r"stat /boot/grub/grub.cfg"
        outputOne = self.caller(cmdOne)

        if "Uid: (    0/    root)" in outputOne and "Gid: (    0/    root)" in outputOne and "-r--------" in outputOne:
            self.Compliant("Ensure permissions on bootloader config are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on bootloader config are configured (Scored)")

    
    def bootloaderpassword_1_5_2(self):
        cmdOne = r'grep "^set superusers" /boot/grub/grub.cfg'
        cmdTwo = r'grep "^password" /boot/grub/grub.cfg'

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if "set superusers" in outputOne and "password" in outputTwo:
            self.Compliant("Ensure bootloader password is set (Scored)")
        else:
            self.NotCompliant("Ensure bootloader password is set (Scored)")
    
    def authroot_1_5_3(self):
        cmdOne = r"grep ^root:[*\!]: /etc/shadow"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.Compliant("Ensure authentication required for single user mode (Scored)")
        else:
            self.NotCompliant("Ensure authentication required for single user mode (Scored)")
    

    def xdnx_1_6_1(self):
        cmdOne = r"journalctl | grep 'protection: active'"
        outputOne = self.caller(cmdOne)

        if "NX (Execute Disable) protection: active" in outputOne:
            self.Compliant("Ensure XD/NX support is enabled (Scored)")
        else:
            self.NotCompliant("Ensure XD/NX support is enabled (Scored)")
    

    def aslr_1_6_2(self):
        cmdOne = r"sysctl kernel.randomize_va_space"
        cmdTwo = r"/usr/sbin/sysctl kernel.randomize_va_space"
        cmdThree = r'grep "kernel\.randomize_va_space" /etc/sysctl.conf /etc/sysctl.d/*'

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if ("kernel.randomize_va_space = 2" in outputOne or "kernel.randomize_va_space = 2" in outputTwo) and "kernel.randomize_va_space = 2" in outputThree:
            self.Compliant("Ensure address space layout randomization (ASLR) is enabled (Scored)")
        else:
            self.NotCompliant("Ensure address space layout randomization (ASLR) is enabled (Scored)")
        