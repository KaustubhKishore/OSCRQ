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
        "tmp_1_1_2",  # Requires testing.
        "nodev_1_1_3",  # Might need testing
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
        "sudoinstalled_1_3_1",  # Left optional LDAP check for now
        "sudopty_1_3_2",
        "sudolog_1_3_3",
        "aide_1_4_1",
        "fsintegrity_1_4_2",
        "bootloaderconfig_1_5_1",
        "bootloaderpassword_1_5_2",
        "authroot_1_5_3",
        "xdnx_1_6_1",  # Leaving out one check which shouldn't be a problem
        "aslr_1_6_2",
        "prelink_1_6_3",
        "coredumps_1_6_4",
        "apparmor_1_7_1_1",  # Utils may not be useful. change or to and if imp. later on
        "aabootloader_1_7_1_2",
        "aaprofiles_1_7_1_3",
        "aaenforce_1_7_1_4",
        "motd_1_8_1_1",
        "locallogin_1_8_1_2",
        "remotelogin_1_8_1_3",
        "permmotd_1_8_1_4",
        "permissue_1_8_1_5",
        "permissuenet_1_8_1_6",  # gdm is optional
        "gdmconfig_1_8_2",
        "updates_1_9",
        "xinetd_2_1_1",
        "openbsdinetd_2_1_2",
        "timesync_2_2_1_1",
        "timesyncd_2_2_1_2",
        "chronyconfig_2_2_1_3",  # optional check.
        "ntpconfig_2_2_1_4",  # Left some additional checks
        "xwindow_2_2_2",
        "avahi_2_2_3",
        "cups_2_2_4",
        "dhcp_2_2_5",
        "ldap_2_2_6",
        "nfsrpc_2_2_7",
        "dns_2_2_8",
        "ftp_2_2_9",
        "http_2_2_10",
        "email_2_2_11",
        "samba_2_2_12",
        "httpproxy_2_2_13",
        "snmp_2_2_14",
        "mtalocal_2_2_15",
        "rsync_2_2_16",
        "nis_2_2_17",
        "nisclient_2_3_1",
        "rshclient_2_3_2",
        "talkclient_2_3_3",
        "telnetclient_2_3_4",
        "ldaputils_2_3_5",
        "ipvsix_3_1_1",
        "wireless_3_1_2",
        "packetredir_3_2_1",
        "ipforward_3_2_2",
        "srpackets_3_3_1",
        "icmp_3_3_2",
        "secureicmp_3_3_3",
        "suspackets_3_3_4",
        "broadicmp_3_3_5",
        "bogusicmp_3_3_6"
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

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of freevxfs filesystems is disabled (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure mounting of freevxfs filesystems is disabled (Scored)"
            )

    def jffs2_1_1_1_2(self):
        cmdOne = r"modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        cmdTwo = r"lsmod | grep jffs2"
        cmdThree = r"/sbin/modprobe -n -v jffs2 | grep -E '(jffs2|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of jffs2 filesystems is disabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure mounting of jffs2 filesystems is disabled (Scored)"
            )

    def hfs_1_1_1_3(self):
        cmdOne = r"modprobe -n -v hfs"
        cmdTwo = r"lsmod | grep hfs"
        cmdThree = r"/sbin/modprobe -n -v hfs"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of hfs filesystems is disabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure mounting of hfs filesystems is disabled (Scored)")

    def hfsplus_1_1_1_4(self):
        cmdOne = r"modprobe -n -v hfsplus"
        cmdTwo = r"lsmod | grep hfsplus"
        cmdThree = r"/sbin/modprobe -n -v hfsplus"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of hfsplus filesystems is disabled (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure mounting of hfsplus filesystems is disabled (Scored)"
            )

    def squashfs_1_1_1_5(self):
        cmdOne = r"modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        cmdTwo = r"lsmod | grep squashfs"
        cmdThree = r"/sbin/modprobe -n -v squashfs | grep -E '(squashfs|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of squashfs filesystems is disabled (Scored)"
            )

        else:
            self.NotCompliant(
                "Ensure mounting of squashfs filesystems is disabled (Scored)"
            )

    def udf_1_1_1_6(self):
        cmdOne = r"modprobe -n -v udf | grep -E '(udf|install)'"
        cmdTwo = r"lsmod | grep udf"
        cmdThree = r"/sbin/modprobe -n -v udf | grep -E '(udf|install)'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
            (outputOne == "install /bin/true \n" or outputThree == "install /bin/true \n") and
            (outputTwo == "")
        ):
            self.Compliant(
                "Ensure mounting of udf filesystems is disabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure mounting of udf filesystems is disabled (Scored)")

    def fat_1_1_1_7(self):
        cmdOne = r"grep -E -i '\svfat\s' /etc/fstab"
        cmdTwo = r"modprobe -n -v vfat | grep -E '(vfat|install)'"
        cmdThree = r"lsmod | grep vfat"
        cmdFour = r"/sbin/modprobe -n -v vfat | grep -E '(vfat|install)'"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if (
            (outputTwo == "install /bin/true \n" or outputFour == "install /bin/true \n") and
            (outputThree == "")
        ):
            self.InfoCompliant(
                "Ensure mounting of FAT filesystems is limited (Not Scored)"
            )
        else:
            self.InfoNotCompliant(
                "Ensure mounting of FAT filesystems is limited (Not Scored)"
            )

        if outputOne != "":
            print("Ensure FAT filesystem is used only where appropirate:\n" + outputOne)

    def tmp_1_1_2(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"grep -E '\s/tmp\s' /etc/fstab | grep -E -v '^\s*#'"
        cmdThree = r"systemctl is-enabled tmp.mount"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if(
            (outputOne != "") and
            (outputTwo != "" or outputThree == "enabled\n")
        ):
            self.Compliant("Ensure /tmp is configured (Scored)")
        else:
            self.NotCompliant("Ensure /tmp is configured (Scored)")

    def nodev_1_1_3(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v nodev"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nodev option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nodev option set on /tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nodev option set on /tmp partition (Scored)")

    def nosuid_1_1_4(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v nosuid"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nosuid option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nosuid option set on /tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nosuid option set on /tmp partition (Scored)")

    def noexec_1_1_5(self):
        cmdOne = r"mount | grep -E '\s/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/tmp\s' | grep -v noexec"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure noexec option set on /tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure noexec option set on /tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure noexec option set on /tmp partition (Scored)")

    def sepvar_1_1_6(self):
        cmdOne = r"mount | grep -E '\s/var\s'"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.NotCompliant(
                "Ensure separate partition exists for /var (Scored)")
        elif "/var" in outputOne:
            self.Compliant(
                "Ensure separate partition exists for /var (Scored)")
        else:
            self.NotCompliant(
                "Ensure separate partition exists for /var (Scored)")

    def sepvartmp_1_1_7(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.NotCompliant(
                "Ensure separate partition exists for /var/tmp (Scored)")
        elif "/var/tmp" in outputOne:
            self.Compliant(
                "Ensure separate partition exists for /var/tmp (Scored)")
        else:
            self.NotCompliant(
                "Ensure separate partition exists for /var/tmp (Scored)")

    def nodevvartemp_1_1_8(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v nodev"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nodev option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nodev option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nodev option set on /var/tmp partition (Scored)")

    def nosuidvartmp_1_1_9(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v nosuid"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nosuid option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nosuid option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nosuid option set on /var/tmp partition (Scored)")

    def noexecvartmp_1_1_10(self):
        cmdOne = r"mount | grep -E '\s/var/tmp\s'"
        cmdTwo = r"mount | grep -E '\s/var/tmp\s' | grep -v noexec"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure noexec option set on /var/tmp partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure noexec option set on /var/tmp partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure noexec option set on /var/tmp partition (Scored)")

    def varlog_1_1_11(self):
        cmdOne = r"mount | grep /var/log"
        outputOne = self.caller(cmdOne)

        if "/var/log" in outputOne:
            self.Compliant(
                "Ensure separate partition exists for /var/log (Scored)")
        else:
            self.NotCompliant(
                "Ensure separate partition exists for /var/log (Scored)")

    def varlogaudit_1_1_12(self):
        cmdOne = r"mount | grep /var/log/audit"
        outputOne = self.caller(cmdOne)

        if "/var/log/audit" in outputOne:
            self.Compliant(
                "Ensure separate partition exists for /var/log/audit (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure separate partition exists for /var/log/audit (Scored)"
            )

    def home_1_1_13(self):
        cmdOne = r"mount | grep /home"
        outputOne = self.caller(cmdOne)

        if "/home" in outputOne:
            self.Compliant(
                "Ensure separate partition exists for /home (Scored)")
        else:
            self.NotCompliant(
                "Ensure separate partition exists for /home (Scored)")

    def nodevhome_1_1_14(self):
        cmdOne = r"mount | grep -E '\s/home\s'"
        cmdTwo = r"mount | grep -E '\s/home\s' | grep -v nodev"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nodev option set on /home partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nodev option set on /home partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nodev option set on /home partition (Scored)")

    def nodevdevshm_1_1_15(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v nodev"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nodev option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nodev option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nodev option set on /dev/shm partition (Scored)")

    def nosuiddevshm_1_1_16(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v nosuid"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure nosuid option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure nosuid option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure nosuid option set on /dev/shm partition (Scored)")

    def noexecdevshm_1_1_17(self):
        cmdOne = r"mount | grep -E '\s/dev/shm\s'"
        cmdTwo = r"mount | grep -E '\s/dev/shm\s' | grep -v noexec"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if outputOne == "":
            self.NotCompliant(
                "Ensure noexec option set on /dev/shm partition (Scored)")
        elif outputTwo == "":
            self.Compliant(
                "Ensure noexec option set on /dev/shm partition (Scored)")
        else:
            self.NotCompliant(
                "Ensure noexec option set on /dev/shm partition (Scored)")

    def removable_1_1_18_and_19_and_20(self):
        cmdOne = r"mount"
        outputOne = self.caller(cmdOne)

        self.InfoNotSure(
            "Ensure nodev,nosuid and noexec option set on removable media partitions (Not Scored)"
        )

        if outputOne != "":
            print(
                "Verify manually that all removable media has nodev,nosuid and noexec option set:\n"
                + outputOne
            )

    def stickybitwwd_1_1_21(self):
        cmdOne = r"df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.Compliant(
                "Ensure sticky bit is set on all world-writable directories (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure sticky bit is set on all world-writable directories (Scored)"
            )

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

        if (
            (outputOne == "install /bin/true" or outputThree == "install /bin/true") and
            (outputTwo == "")
        ):
            self.Compliant("Disable USB Storage (Scored)")
        else:
            self.NotCompliant("Disable USB Storage (Scored)")

    def packagemanager_1_2_1(self):
        cmdOne = r"apt-cache policy"
        outputOne = self.caller(cmdOne)

        self.InfoNotSure(
            "Ensure package manager repositories are configured (Not Scored)"
        )
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
        # cmdTwo = r"dpkg -s sudo-ldap"

        outputOne = self.caller(cmdOne)
        # outputTwo = self.caller(cmdTwo)

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

        if (
            "enabled" in outputOne and
            "enabled" in outputTwo and
            "active (running)" in outputThree
        ):
            self.Compliant(
                "Ensure filesystem integrity is regularly checked (Scored)")
        else:
            self.NotCompliant(
                "Ensure filesystem integrity is regularly checked (Scored)"
            )

    def bootloaderconfig_1_5_1(self):
        cmdOne = r"stat /boot/grub/grub.cfg"
        outputOne = self.caller(cmdOne)

        if (
            ("Uid: (    0/    root)" in outputOne) and
            ("Gid: (    0/    root)" in outputOne) and
            ("-r--------" in outputOne)
        ):
            self.Compliant(
                "Ensure permissions on bootloader config are configured (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure permissions on bootloader config are configured (Scored)"
            )

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
            self.Compliant(
                "Ensure authentication required for single user mode (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure authentication required for single user mode (Scored)"
            )

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

        if (
            ("kernel.randomize_va_space = 2" in outputOne or "kernel.randomize_va_space = 2" in outputTwo) and
            ("kernel.randomize_va_space = 2" in outputThree)
        ):
            self.Compliant(
                "Ensure address space layout randomization (ASLR) is enabled (Scored)"
            )
        else:
            self.NotCompliant(
                "Ensure address space layout randomization (ASLR) is enabled (Scored)"
            )

    def prelink_1_6_3(self):
        cmdOne = r"dpkg -s prelink"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure prelink is disabled (Scored)")
        else:
            self.NotCompliant("Ensure prelink is disabled (Scored)")

    def coredumps_1_6_4(self):
        cmdOne = r'grep "hard core" /etc/security/limits.conf /etc/security/limits.d/*'
        cmdTwo = r"sysctl fs.suid_dumpable"
        cmdThree = r"/usr/sbin/sysctl fs.suid_dumpable"
        cmdFour = r'grep "fs.suid_dumpable" /etc/sysctl.conf /etc/sysctl.d/*'

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if(
            ("* hard core 0" in outputOne) and
            ("fs.suid_dumpable = 0" in outputTwo or "fs.suid_dumpable = 0" in outputThree) and
            ("fs.suid_dumpable = 0" in outputFour)
        ):
            self.Compliant("Ensure core dumps are restricted (Scored)")
        else:
            self.NotCompliant("Ensure core dumps are restricted (Scored)")

    def apparmor_1_7_1_1(self):
        cmdOne = r"dpkg -s apparmor"
        cmdTwo = r"dpkg -s apparmor-utils"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if(
            "install ok installed" in outputOne or
            "install ok installed" in outputTwo
        ):
            self.Compliant("Ensure AppArmor is installed (Scored)")
        else:
            self.NotCompliant("Ensure AppArmor is installed (Scored)")

    def aabootloader_1_7_1_2(self):
        cmdOne = r'grep "^\s*linux" /boot/grub/grub.cfg | grep -v "apparmor=1"'
        cmdTwo = r'grep "^\s*linux" /boot/grub/grub.cfg | grep -v "security=apparmor"'
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if(
            outputOne == "" and
            outputTwo == ""
        ):
            self.Compliant(
                "Ensure AppArmor is enabled in the bootloader configuration (Scored)")
        else:
            self.NotCompliant(
                "Ensure AppArmor is enabled in the bootloader configuration (Scored)")

    def aaprofiles_1_7_1_3(self):
        cmdOne = r"apparmor_status | grep profiles"
        cmdTwo = r"/usr/sbin/apparmor_status | grep profiles"
        cmdThree = r"apparmor_status | grep processes"
        cmdFour = r"/usr/sbin/apparmor_status | grep processes"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if(
            ("unconfined" not in outputOne + outputTwo) and
            ("0 processes are unconfined" in outputThree + outputFour)
        ):
            self.Compliant(
                "Ensure all AppArmor Profiles are in enforce or complain mode (Scored)")
        else:
            self.NotCompliant(
                "Ensure all AppArmor Profiles are in enforce or complain mode (Scored)")

    def aaenforce_1_7_1_4(self):
        cmdOne = r"apparmor_status"
        outputOne = self.caller(cmdOne)

        if(
            "0 profiles are in complain mode" in outputOne and
            "0 processes are unconfined" in outputOne
        ):
            self.Compliant(
                "Ensure all AppArmor Profiles are enforcing (Scored)")
        else:
            self.NotCompliant(
                "Ensure all AppArmor Profiles are enforcing (Scored)")

    def motd_1_8_1_1(self):
        cmdOne = r"""grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/motd"""
        outputOne = self.caller(cmdOne)

        if(outputOne == ""):
            self.Compliant(
                "Ensure message of the day is configured properly (Scored)")
        else:
            self.NotCompliant(
                "Ensure message of the day is configured properly (Scored)")

    def locallogin_1_8_1_2(self):
        cmdOne = r"""grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/issue"""
        outputOne = self.caller(cmdOne)

        if(outputOne == ""):
            self.Compliant(
                "Ensure local login warning banner is configured properly (Scored)")
        else:
            self.NotCompliant(
                "Ensure local login warning banner is configured properly (Scored)")

    def remotelogin_1_8_1_3(self):
        cmdOne = r"""grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/issue.net"""
        outputOne = self.caller(cmdOne)

        if(outputOne == ""):
            self.Compliant(
                "Ensure remote login warning banner is configured properly (Scored)")
        else:
            self.NotCompliant(
                "Ensure remote login warning banner is configured properly (Scored)")

    def permmotd_1_8_1_4(self):
        cmdOne = r"stat /etc/motd"
        outputOne = self.caller(cmdOne)

        if "Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne:
            self.Compliant(
                "Ensure permissions on /etc/motd are configured (Scored)")
        else:
            self.NotCompliant(
                "Ensure permissions on /etc/motd are configured (Scored)")

    def permissue_1_8_1_5(self):
        cmdOne = r"stat /etc/issue"
        outputOne = self.caller(cmdOne)

        if(
           "Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
           ):
            self.Compliant(
                "Ensure permissions on /etc/issue are configured (Scored)")
        else:
            self.NotCompliant(
                "Ensure permissions on /etc/issue are configured (Scored)")

    def permissuenet_1_8_1_6(self):
        cmdOne = r"stat /etc/issue.net"
        outputOne = self.caller(cmdOne)

        if(
           "Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
           ):
            self.Compliant(
                "Ensure permissions on /etc/issue.net are configured (Scored)")
        else:
            self.NotCompliant(
                "Ensure permissions on /etc/issue.net are configured (Scored)")

    def gdmconfig_1_8_2(self):
        cmdOne = r"dpkg -s gdm3 | grep 'install ok installed'"
        cmdTwo = r"cat /etc/gdm3/greeter.dconf-defaults | grep banner-message-enable=true"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if "install ok installed" in outputOne:
            if outputTwo[0] != "#":
                self.Compliant(
                    "Ensure GDM login banner is configured (Scored)")
            else:
                self.NotCompliant(
                    "Ensure GDM login banner is configured (Scored)")
        else:
            self.Compliant(
                "Ensure GDM login banner is configured (Scored) - GDM Not installed")

    def updates_1_9(self):
        cmdOne = r"apt -s upgrade"
        outputOne = self.caller(cmdOne)

        if "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded" in outputOne:
            self.InfoCompliant(
                "Ensure updates, patches, and additional security software are installed (Not Scored)")
        else:
            self.InfoNotCompliant(
                "Ensure updates, patches, and additional security software are installed (Not Scored)")

    def xinetd_2_1_1(self):
        cmdOne = r"dpkg -s xinetd"
        outputOne = self.caller(cmdOne)

        if "'xinetd' is not installed" in outputOne:
            self.Compliant("Ensure xinetd is not installed (Scored)")
        else:
            self.NotCompliant("Ensure xinetd is not installed (Scored)")

    def openbsdinetd_2_1_2(self):
        cmdOne = r"dpkg -s openbsd-inetd"
        outputOne = self.caller(cmdOne)

        if "'openbsd-inetd' is not installed" in outputOne:
            self.Compliant("Ensure openbsd-inetd is not installed (Scored)")
        else:
            self.NotCompliant("Ensure openbsd-inetd is not installed (Scored)")

    def timesync_2_2_1_1(self):
        cmdOne = r"systemctl is-enabled systemd-timesyncd"
        cmdTwo = r"dpkg -s chrony"
        cmdThree = r"dpkg -s ntp"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if(
            "enabled" in outputOne or
            "install ok installed" in outputTwo or
            "install ok installed" in outputThree
        ):
            self.Compliant(" Ensure time synchronization is in use (Scored)")
        else:
            self.NotCompliant(
                " Ensure time synchronization is in use (Scored)")

    def timesyncd_2_2_1_2(self):
        cmdOne = r"systemctl is-enabled systemd-timesyncd.service"
        outputOne = self.caller(cmdOne)

        if "enabled" in outputOne:
            self.InfoCompliant(
                "Ensure systemd-timesyncd is configured (Not Scored)")
        else:
            self.InfoNotCompliant(
                "Ensure systemd-timesyncd is configured (Not Scored)")

    def chronyconfig_2_2_1_3(self):
        cmdOne = r"dpkg -s chrony"
        cmdTwo = r'grep -E "^(server|pool)" /etc/chrony.conf'
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if "install ok installed" in outputOne:
            if "server" in outputTwo:
                self.Compliant("Ensure chrony is configured (Scored)")
            else:
                self.NotCompliant("Ensure chrony is configured (Scored)")
        else:
            self.Compliant(
                "Ensure chrony is configured (Scored) + Chrony is not used")

    def ntpconfig_2_2_1_4(self):
        cmdOne = r"dpkg -s ntp"
        cmdTwo = r'grep "^restrict" /etc/ntp.conf'
        cmdThree = r'grep -E "^(server|pool)" /etc/ntp.conf'
        cmdFour = r'grep "RUNASUSER=ntp" /etc/init.d/ntp'
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if "install ok installed" in outputOne:
            if (
                "restrict -6 default" in outputTwo and
                "server" in outputThree and
                "RUNASUSER=ntp" in outputFour
            ):
                self.Compliant("Ensure ntp is configured (Scored)")
            else:
                self.NotCompliant("Ensure ntp is configured (Scored)")
        else:
            self.Compliant(
                "Ensure ntp is configured (Scored) + NTP not installed")

    def xwindow_2_2_2(self):
        cmdOne = r"dpkg -l xserver-xorg*"
        outputOne = self.caller(cmdOne)

        if "no packages found" in outputOne:
            self.Compliant("Ensure X Window System is not installed (Scored)")
        else:
            self.NotCompliant(
                "Ensure X Window System is not installed (Scored)")

    def avahi_2_2_3(self):
        cmdOne = r"systemctl is-enabled avahi-daemon"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure Avahi Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure Avahi Server is not enabled (Scored)")

    def cups_2_2_4(self):
        cmdOne = r"systemctl is-enabled cups"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure CUPS is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure CUPS is not enabled (Scored)")

    def dhcp_2_2_5(self):
        cmdOne = r"systemctl is-enabled isc-dhcp-server"
        cmdTwo = r"systemctl is-enabled isc-dhcp-server6"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if(
            "enabled" not in outputOne and
            "enabled" not in outputTwo
        ):
            self.Compliant("Ensure DHCP Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure DHCP Server is not enabled (Scored)")

    def ldap_2_2_6(self):
        cmdOne = r"systemctl is-enabled slapd"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure LDAP server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure LDAP server is not enabled (Scored)")

    def nfsrpc_2_2_7(self):
        cmdOne = r"systemctl is-enabled nfs-server"
        cmdTwo = r"systemctl is-enabled rpcbind"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if(
            "enabled" not in outputOne and
            "enabled" not in outputTwo
        ):
            self.Compliant("Ensure NFS and RPC are not enabled (Scored)")
        else:
            self.NotCompliant("Ensure NFS and RPC are not enabled (Scored)")

    def dns_2_2_8(self):
        cmdOne = r"systemctl is-enabled bind9"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure DNS Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure DNS Server is not enabled (Scored)")

    def ftp_2_2_9(self):
        cmdOne = r"systemctl is-enabled vsftpd"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure FTP Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure FTP Server is not enabled (Scored)")

    def http_2_2_10(self):
        cmdOne = r"systemctl is-enabled apache2"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure HTTP server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure HTTP server is not enabled (Scored)")

    def email_2_2_11(self):
        cmdOne = r"systemctl is-enabled dovecot"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure email services are not enabled (Scored)")
        else:
            self.NotCompliant("Ensure email services are not enabled (Scored)")

    def samba_2_2_12(self):
        cmdOne = r"systemctl is-enabled smbd"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure Samba is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure Samba is not enabled (Scored)")

    def httpproxy_2_2_13(self):
        cmdOne = r"systemctl is-enabled squid"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure HTTP Proxy Server is not enabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure HTTP Proxy Server is not enabled (Scored)")

    def snmp_2_2_14(self):
        cmdOne = r"systemctl is-enabled snmpd"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure SNMP Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure SNMP Server is not enabled (Scored)")

    def mtalocal_2_2_15(self):
        cmdOne = r"ss -lntu | grep -E ':25\s' | grep -E -v '\s(127.0.0.1|::1):25\s'"
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.Compliant(
                "Ensure mail transfer agent is configured for local-only mode (Scored)")
        else:
            self.NotCompliant(
                "Ensure mail transfer agent is configured for local-only mode (Scored)")

    def rsync_2_2_16(self):
        cmdOne = r"systemctl is-enabled rsync"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure rsync service is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure rsync service is not enabled (Scored)")

    def nis_2_2_17(self):
        cmdOne = r"systemctl is-enabled nis"
        outputOne = self.caller(cmdOne)

        if "enabled" not in outputOne:
            self.Compliant("Ensure NIS Server is not enabled (Scored)")
        else:
            self.NotCompliant("Ensure NIS Server is not enabled (Scored)")

    def nisclient_2_3_1(self):
        cmdOne = r"dpkg -s nis"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure NIS Client is not installed (Scored)")
        else:
            self.NotCompliant("Ensure NIS Client is not installed (Scored)")

    def rshclient_2_3_2(self):
        cmdOne = r"dpkg -s rsh-client"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure rsh client is not installed (Scored)")
        else:
            self.NotCompliant("Ensure rsh client is not installed (Scored)")

    def talkclient_2_3_3(self):
        cmdOne = r"dpkg -s talk"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure talk client is not installed (Scored)")
        else:
            self.NotCompliant("Ensure talk client is not installed (Scored)")

    def telnetclient_2_3_4(self):
        cmdOne = r"dpkg -s telnet"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure telnet client is not installed (Scored)")
        else:
            self.NotCompliant("Ensure telnet client is not installed (Scored)")

    def ldaputils_2_3_5(self):
        cmdOne = r"dpkg -s ldap-utils"
        outputOne = self.caller(cmdOne)

        if "is not installed" in outputOne:
            self.Compliant("Ensure LDAP client is not installed (Scored)")
        else:
            self.NotCompliant("Ensure LDAP client is not installed (Scored)")

    def ipvsix_3_1_1(self):
        cmdOne = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "ipv6.disable=1" """
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.InfoCompliant("Disable IPv6 (Not Scored)")
        else:
            self.InfoNotCompliant("Disable IPv6 (Not Scored)")

    def wireless_3_1_2(self):
        cmdOne = r"nmcli radio all"
        outputOne = self.caller(cmdOne)

        temp = outputOne.find("\n")
        temp = outputOne[temp:].split()

        testOne = temp[1]
        testTwo = temp[3]

        if(
            "disabled" in testOne and
            "disabled" in testTwo
        ):
            self.Compliant("Ensure wireless interfaces are disabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure wireless interfaces are disabled (Scored)")

    def packetredir_3_2_1(self):
        cmdOne = r"sysctl net.ipv4.conf.all.send_redirects"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.send_redirects"

        cmdThree = r"sysctl net.ipv4.conf.default.send_redirects"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.send_redirects"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if(
            (
                "net.ipv4.conf.all.send_redirects = 0" in outputOne or
                "net.ipv4.conf.all.send_redirects = 0" in outputTwo
            ) and
            (
                "net.ipv4.conf.default.send_redirects = 0" in outputThree or
                "net.ipv4.conf.default.send_redirects = 0" in outputFour
            ) and
            (
                "net.ipv4.conf.all.send_redirects = 0" in outputFive
            ) and
            (
                "net.ipv4.conf.default.send_redirects= 0" in outputSix
            )
        ):
            self.Compliant(
                "Ensure packet redirect sending is disabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure packet redirect sending is disabled (Scored)")

    def ipforward_3_2_2(self):
        cmdOne = r"sysctl net.ipv4.ip_forward"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.ip_forward"

        cmdThree = r"""grep -E -s "^\s*net\.ipv4\.ip_forward\s*=\s*1" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf"""

        cmdFour = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "ipv6.disable=1" """

        cmdFive = r"sysctl net.ipv6.conf.all.forwarding"
        cmdSix = r"/usr/sbin/sysctl net.ipv6.conf.all.forwarding"
        cmdSeven = r"""grep -E -s "^\s*net\.ipv6\.conf\.all\.forwarding\s*=\s*1" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)
        outputSeven = self.caller(cmdSeven)

        if(
            (
                "net.ipv4.ip_forward = 0" in outputOne or
                "net.ipv4.ip_forward = 0" in outputTwo
            ) and
            (
                outputThree == ""
            )
        ):
            if outputFour != "":
                if(
                    (
                        "net.ipv6.conf.all.forwarding = 0" in outputFive or
                        "net.ipv6.conf.all.forwarding = 0" in outputSix
                    ) and
                    (
                        outputSeven == ""
                    )
                ):
                    self.Compliant("Ensure IP forwarding is disabled (Scored)")
                else:
                    self.NotCompliant(
                        "Ensure IP forwarding is disabled (Scored)")
            else:
                self.Compliant("Ensure IP forwarding is disabled (Scored)")
        else:
            self.NotCompliant("Ensure IP forwarding is disabled (Scored)")

    def srpackets_3_3_1(self):
        cmdOne = r"sysctl net.ipv4.conf.all.accept_source_route"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.accept_source_route"

        cmdThree = r"sysctl net.ipv4.conf.default.accept_source_route"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.accept_source_route"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.accept_source_route" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.accept_source_route" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if (
            (
                "net.ipv4.conf.all.accept_source_route = 0" in outputOne or
                "net.ipv4.conf.all.accept_source_route = 0" in outputTwo

            ) and
            (
                "net.ipv4.conf.default.accept_source_route = 0" in outputThree or
                "net.ipv4.conf.default.accept_source_route = 0" in outputFour
            ) and
            (
                "net.ipv4.conf.all.accept_source_route= 0" in outputFive and
                "#" not in outputFive
            ) and
            (
                "net.ipv4.conf.default.accept_source_route= 0" in outputSix and
                "#" not in outputSix
            )
        ):
            cmdSeven = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "ipv6.disable=1" """
            outputSeven = self.caller(cmdSeven)

            if outputSeven != "":
                cmdEight = r"sysctl net.ipv6.conf.all.accept_source_route"
                cmdNine = r"/usr/sbin/sysctl net.ipv6.conf.all.accept_source_route"

                cmdTen = r"sysctl net.ipv6.conf.default.accept_source_route"
                cmdEleven = r"/usr/sbin/sysctl net.ipv6.conf.default.accept_source_route"

                cmdTwelve = r"""grep "net\.ipv6\.conf\.all\.accept_source_route" /etc/sysctl.conf /etc/sysctl.d/*"""
                cmdThirteen = r"""grep "net\.ipv6\.conf\.default\.accept_source_route" /etc/sysctl.conf /etc/sysctl.d/*"""

                outputEight = self.caller(cmdEight)
                outputNine = self.caller(cmdNine)
                outputTen = self.caller(cmdTen)
                outputEleven = self.caller(cmdEleven)
                outputTwelve = self.caller(cmdTwelve)
                outputThirteen = self.caller(cmdThirteen)

                if (
                    (
                        "net.ipv6.conf.all.accept_source_route = 0" in outputEight or
                        "net.ipv6.conf.all.accept_source_route = 0" in outputNine
                    ) and
                    (
                        "net.ipv6.conf.default.accept_source_route = 0" in outputTen or
                        "net.ipv6.conf.default.accept_source_route = 0" in outputEleven
                    ) and
                    (
                        "net.ipv4.conf.all.accept_source_route = 0" in outputTwelve and
                        "#" not in outputTwelve
                    ) and
                    (
                        "net.ipv6.conf.default.accept_source_route = 0" in outputThirteen and
                        "#" not in outputTwelve
                    )
                ):
                    self.Compliant(
                        "Ensure source routed packets are not accepted (Scored)")
                else:
                    self.NotCompliant(
                        "Ensure source routed packets are not accepted (Scored)")
            else:
                self.Compliant(
                    "Ensure source routed packets are not accepted (Scored)")
        else:
            self.NotCompliant(
                "Ensure source routed packets are not accepted (Scored)")

    def icmp_3_3_2(self):
        cmdOne = r"sysctl net.ipv4.conf.all.accept_redirects"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.accept_redirects"

        cmdThree = r"sysctl net.ipv4.conf.default.accept_redirects"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.accept_redirects"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if (
            (
                "net.ipv4.conf.all.accept_redirects = 0" in outputOne or
                "net.ipv4.conf.all.accept_redirects = 0" in outputTwo
            ) and
            (
                "net.ipv4.conf.default.accept_redirects = 0" in outputThree or
                "net.ipv4.conf.default.accept_redirects = 0" in outputFour
            ) and
            (
                "net.ipv4.conf.all.accept_redirects = 0" in outputFive and
                "#" not in outputFive
            ) and
            (
                "net.ipv4.conf.default.accept_redirects = 0" in outputSix and
                "#" not in outputSix
            )
        ):
            cmdSeven = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "ipv6.disable=1" """
            outputSeven = self.caller(cmdSeven)

            if outputSeven != "":
                cmdEight = r"sysctl net.ipv6.conf.all.accept_redirects"
                cmdNine = r"/usr/sbin/sysctl net.ipv6.conf.all.accept_redirects"

                cmdTen = r"sysctl net.ipv6.conf.default.accept_redirects"
                cmdEleven = r"/usr/sbin/sysctl net.ipv6.conf.default.accept_redirects"

                cmdTwelve = r"""grep "net\.ipv6\.conf\.all\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""
                cmdThirteen = r"""grep "net\.ipv6\.conf\.default\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""

                outputEight = self.caller(cmdEight)
                outputNine = self.caller(cmdNine)
                outputTen = self.caller(cmdTen)
                outputEleven = self.caller(cmdEleven)
                outputTwelve = self.caller(cmdTwelve)
                outputThirteen = self.caller(cmdThirteen)

                if (
                    (
                        "net.ipv6.conf.all.accept_redirects = 0" in outputEight or
                        "net.ipv6.conf.all.accept_redirects = 0" in outputNine
                    ) and
                    (
                        "net.ipv6.conf.default.accept_redirects = 0" in outputTen or
                        "net.ipv6.conf.default.accept_redirects = 0" in outputEleven
                    ) and
                    (
                        "net.ipv6.conf.all.accept_redirects = 0" in outputTwelve and
                        "#" not in outputTwelve
                    ) and
                    (
                        "net.ipv6.conf.default.accept_redirects = 0" in outputThirteen and
                        "#" not in outputThirteen
                    )
                ):
                    self.Compliant(
                        "Ensure ICMP redirects are not accepted (Scored)")
                else:
                    self.NotCompliant(
                        "Ensure ICMP redirects are not accepted (Scored)")

            else:
                self.Compliant(
                    "Ensure ICMP redirects are not accepted (Scored)")
        else:
            self.NotCompliant(
                "Ensure ICMP redirects are not accepted (Scored)")

    def secureicmp_3_3_3(self):
        cmdOne = r"sysctl net.ipv4.conf.all.secure_redirects"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.secure_redirects"

        cmdThree = r"sysctl net.ipv4.conf.default.secure_redirects"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.secure_redirects"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.secure_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.secure_redirects" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if(
            (
                "net.ipv4.conf.all.secure_redirects = 0" in outputOne or
                "net.ipv4.conf.all.secure_redirects = 0" in outputTwo
            ) and
            (
                "net.ipv4.conf.default.secure_redirects = 0" in outputThree or
                "net.ipv4.conf.default.secure_redirects = 0" in outputFour
            ) and
            (
                "net.ipv4.conf.all.secure_redirects = 0" in outputFive
            ) and
            (
                "net.ipv4.conf.default.secure_redirects = 0" in outputSix
            )
        ):
            self.Compliant(
                "Ensure secure ICMP redirects are not accepted (Scored)")
        else:
            self.NotCompliant(
                "Ensure secure ICMP redirects are not accepted (Scored)")

    def suspackets_3_3_4(self):
        cmdOne = r"sysctl net.ipv4.conf.all.log_martians"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.log_martians"

        cmdThree = r"sysctl net.ipv4.conf.default.log_martians"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.log_martians"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.log_martians" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.log_martians" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if(
            (
                "net.ipv4.conf.all.log_martians = 1" in outputOne or
                "net.ipv4.conf.all.log_martians = 1" in outputTwo
            ) and
            (
                "net.ipv4.conf.default.log_martians = 1" in outputThree or
                "net.ipv4.conf.default.log_martians = 1" in outputFour
            ) and
            (
                "net.ipv4.conf.all.log_martians = 1" in outputFive and
                "#" not in outputFive
            ) and
            (
                "net.ipv4.conf.default.log_martians = 1" in outputSix and
                "#" not in outputSix
            )
        ):
            self.Compliant("Ensure suspicious packets are logged (Scored)")
        else:
            self.NotCompliant("Ensure suspicious packets are logged (Scored)")

    def broadicmp_3_3_5(self):
        cmdOne = r"sysctl net.ipv4.icmp_echo_ignore_broadcasts"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.icmp_echo_ignore_broadcasts"

        cmdThree = r"""grep "net\.ipv4\.icmp_echo_ignore_broadcasts" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if(
            (
                "net.ipv4.icmp_echo_ignore_broadcasts = 1" in outputOne or
                "net.ipv4.icmp_echo_ignore_broadcasts = 1" in outputTwo
            ) and
            (
                "net.ipv4.icmp_echo_ignore_broadcasts = 1" in outputThree and
                "#" not in outputThree
            )
        ):
            self.Compliant(
                "Ensure broadcast ICMP requests are ignored (Scored)")
        else:
            self.NotCompliant(
                "Ensure broadcast ICMP requests are ignored (Scored)")
    
    def bogusicmp_3_3_6(self):
        pass