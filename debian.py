from helper import Helper
from pymongo import MongoClient


class Debian(Helper):
    profile = [
        "freevxfs_1_1_1_1",
        "jffs2_1_1_1_2",
        "hfs_1_1_1_3",
        "hfsplus_1_1_1_4",
        "squashfs_1_1_1_5",
        "udf_1_1_1_6",
        "fat_1_1_1_7",
        "tmp_1_1_2",
        "nodev_1_1_3",
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
        "xdnx_1_6_1",
        "aslr_1_6_2",
        "prelink_1_6_3",
        "coredumps_1_6_4",
        "apparmor_1_7_1_1",
        "aabootloader_1_7_1_2",
        "aaprofiles_1_7_1_3",
        "aaenforce_1_7_1_4",
        "motd_1_8_1_1",
        "locallogin_1_8_1_2",
        "remotelogin_1_8_1_3",
        "permmotd_1_8_1_4",
        "permissue_1_8_1_5",
        "permissuenet_1_8_1_6",
        "gdmconfig_1_8_2",
        "updates_1_9",
        "xinetd_2_1_1",
        "openbsdinetd_2_1_2",
        "timesync_2_2_1_1",
        "timesyncd_2_2_1_2",
        "chronyconfig_2_2_1_3",
        "ntpconfig_2_2_1_4",
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
        "bogusicmp_3_3_6",
        "rpfilter_3_3_7",
        "tcpsyn_3_3_8",
        "ipv6router_3_3_9",
        "dccp_3_4_1",
        "sctp_3_4_2",
        "rds_3_4_3",
        "tipc_3_4_4",
        "firewall_3_5_1_1",
        "ufwservice_3_5_2_1",
        "ufwdeny_3_5_2_2",
        "ufwloopback_3_5_2_3",
        "ufwoutbound_3_5_2_4",  # Skip 3.5.2.5, Manual pref.
        "confnf_3_5_3",  # Skip nftables. Manual pref.
        "nfloop_3_5_3_4",
        "nfdeny_3_5_3_6",
        "nfservice_3_5_3_7",
        "nfrules_3_5_3_8",
        "ipdeny_3_5_4_1_1",
        "iploop_3_5_4_1_2",
        "ipoutb_3_5_4_1_3",  # Skip 3_5_4_1_4
        "ip6deny_3_5_4_2_1",
        "ip6loop_3_5_4_2_2",
        "ip6outb_3_5_4_2_3",  # Skip 3_5_4_2_4
        "auditd_4_1_1_1",
        "auditdenabled_4_1_1_2",
        "auditproc_4_1_1_3",
        "auditdbacklog_4_1_1_4",
        "auditdlogstorage_4_1_2_1",
        "auditddeleted_4_1_2_2",
        "auditdsystem_4_1_2_3",
        "auditdtime_4_1_3",
        "auditdusermodify_4_1_4",
        "auditdsysnet_4_1_5",
        "auditdmac_4_1_6",
        "auditdlogin_4_1_7",
        "auditdsession_4_1_8",
        "auditddac_4_1_9",
        "auditdufa_4_1_10", # Skip 4_1_11 - Manual
        "auditdfsmount_4_1_12",
        "auditdfiledel_4_1_13",
        "auditdsudoers_4_1_14",
        "auditdsudolog_4_1_15",
        "auditdkernel_4_1_16",
        "auditdconfig_4_1_17",
        "rsyslog_4_2_1_1",
        "rsyslogenabled_4_2_1_2",  # Skip 4_2_1_3 - Manual (Not Scored)
        "rsyslogperm_4_2_1_4",
        "rsyslogremote_4_2_1_5",
        "rsyslogremotedesignated_4_2_1_6",
        "journaldconfig_4_2_2_1",
        "journaldcompress_4_2_2_2",
        "journaldpers_4_2_2_3",  # Skip 4_2_3 (Scored) & 4_3
        "logrotate_4_4",
        "crond_5_1_1",
        "cronperm_5_1_2",
        "cronhourlyperm_5_1_3",
        "crondailyperm_5_1_4",
        "cronweeklyperm_5_1_5",
        "cronmonthlyperm_5_1_6",
        "crondperm_5_1_7",
        "atcron_5_1_8",
        "sshdconfig_5_2_1",  # Skip 5_2_2 & 5_2_3 Manual - (Scored)
        "sshone_5_2_4",
        "sshloglevel_5_2_5",
        "sshx11_5_2_6",
        "sshmaxauth_5_2_7",
        "sshignorerhost_5_2_8",
        "sshhostbased_5_2_9",
        "sshrootlogin_5_2_10",
        "sshempty_5_2_11",
        "sshuserenv_5_2_12",
        "sshstrongcipher_5_2_13",
        "strongmac_5_2_14",
        "strongkex_5_2_15",
        "sshidle_5_2_16",
        "sshlogingrace_5_2_17",  # Skip 5_2_18(Scored) - Manual
        "sshbanner_5_2_19",
        "sshpam_5_2_20",
        "sshtcp_5_2_21",
        "sshmax_5_2_22",
        "sshmaxsessions_5_2_23",
        "pwdreqs_5_3_1",
        "lockout_5_3_2",
        "passreuse_5_3_3",
        "passhashing_5_3_4",
        "passexp_5_4_1_1",
        "passmindays_5_4_1_2",
        "passexpwarn_5_4_1_3",
        "inactivepass_5_4_1_4",
        "lastpasschange_5_4_1_5",
        "sysaccs_5_4_2",
        "defgroupid_5_4_3",
        "umask_5_4_4",
        "shelltimeout_5_4_5",
        "sucmd_5_6",  # Skip 5_6(Scored) & 6_1_1(Not Scored)(Manual)
        "passwdperm_6_1_2",
        "gshadowperm_6_1_3",
        "shadowperm_6_1_4",
        "groupperm_6_1_5",
        "etcpasswdperm_6_1_6",
        "etcshadow_6_1_7",
        "etcgroup_6_1_8",
        "etcgshadow_6_1_9",
        "wwfiles_6_1_10",
        "unowned_6_1_11",
        "ungrouped_6_1_12",  # Skip 6_1_13 & 6_1_14(Not Scored) Manual
        "passwdnotempty_6_2_1",
        "nolegacy_6_2_2",
        "userhome_6_2_3",
        "nolegacy_6_2_4",
        "nolegacygroup_6_2_5",
        "rootuid_6_2_6",
        "rootpathintegrity_6_2_7",
        "userhomeperm_6_2_8",
        "usershome_6_2_9",
        "userdotfile_6_2_10",
        "nouserforward_6_2_11",
        "nousernetrc_6_2_12",
        "usernetrc_6_2_13",
        "nouserrhosts_6_2_14",
        "groupsetcpasswd_6_2_15",
        "noduplicateuid_6_2_16",
        "noduplicategid_6_2_17",
        "noduplicateusernames_6_2_18",
        "noduplicategroupname_6_2_19",
        "emptyshadow_6_2_20"
    ]

    def __init__(self):
        super().__init__()

    def runner(self):
        for p in self.profile:
            call = getattr(Debian, p)
            call(self)
        try:
            conn = MongoClient("mongodb+srv://Sanya:4wUubuaMachwQ9rn@cluster0.9w3mr.mongodb.net/OSCARQ?retryWrites=true&w=majority")
            print("Connection Successful")
            db = conn.OSCARQ
            collection = db.Debian

            benchmark = {
                "DeviceID": self.id.strip(),
                "Platform": self.platform.strip(),
                "BenchmarkingTime": self.dateandtime,
                "Compliant": self.COMPLIANT,
                "Not Compliant": self.NOTCOMPLIANT,
                "Info Compliant": self.INFOCOMPLIANT,
                "Info NotCompliant": self.INFONOTCOMPLIANT,
                "Info Manual": self.INFONOTSURE
            }

            recordID = collection.insert_one(benchmark)
            print("Pushed Successful")
        except Exception as e:
            print("Failure: ",e)
        self.printer()

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

        if (
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

        if (
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

        if (
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

        if (
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

        if (
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

        if (
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

        if (outputOne == ""):
            self.Compliant(
                "Ensure message of the day is configured properly (Scored)")
        else:
            self.NotCompliant(
                "Ensure message of the day is configured properly (Scored)")

    def locallogin_1_8_1_2(self):
        cmdOne = r"""grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/issue"""
        outputOne = self.caller(cmdOne)

        if (outputOne == ""):
            self.Compliant(
                "Ensure local login warning banner is configured properly (Scored)")
        else:
            self.NotCompliant(
                "Ensure local login warning banner is configured properly (Scored)")

    def remotelogin_1_8_1_3(self):
        cmdOne = r"""grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/issue.net"""
        outputOne = self.caller(cmdOne)

        if (outputOne == ""):
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

        if (
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

        if (
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

        if (
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

        if (
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

        if (
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

        try:
            testOne = temp[1]
            testTwo = temp[3]

            if (
                    "disabled" in testOne and
                    "disabled" in testTwo
            ):
                self.Compliant(
                    "Ensure wireless interfaces are disabled (Scored)")
            else:
                self.NotCompliant(
                    "Ensure wireless interfaces are disabled (Scored)")
        except:
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

        if (
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

        if (
                (
                        "net.ipv4.ip_forward = 0" in outputOne or
                        "net.ipv4.ip_forward = 0" in outputTwo
                ) and
                (
                        outputThree == ""
                )
        ):
            if outputFour != "":
                if (
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

        if (
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

        if (
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

        if (
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
        cmdOne = r"sysctl net.ipv4.icmp_ignore_bogus_error_responses"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.icmp_ignore_bogus_error_responses"

        cmdThree = r"""grep "net.ipv4.icmp_ignore_bogus_error_responses" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                (
                        "net.ipv4.icmp_ignore_bogus_error_responses = 1" in outputOne or
                        "net.ipv4.icmp_ignore_bogus_error_responses = 1" in outputTwo
                ) and
                (
                        "net.ipv4.icmp_ignore_bogus_error_responses = 1" in outputThree and
                        "#" not in outputThree
                )
        ):
            self.Compliant("Ensure bogus ICMP responses are ignored (Scored)")
        else:
            self.NotCompliant(
                "Ensure bogus ICMP responses are ignored (Scored)")

    def rpfilter_3_3_7(self):
        cmdOne = r"sysctl net.ipv4.conf.all.rp_filter"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.conf.all.rp_filter"

        cmdThree = r"sysctl net.ipv4.conf.default.rp_filter"
        cmdFour = r"/usr/sbin/sysctl net.ipv4.conf.default.rp_filter"

        cmdFive = r"""grep "net\.ipv4\.conf\.all\.rp_filter" /etc/sysctl.conf /etc/sysctl.d/*"""
        cmdSix = r"""grep "net\.ipv4\.conf\.default\.rp_filter" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if (
                (
                        "net.ipv4.conf.all.rp_filter = 1" in outputOne and
                        "net.ipv4.conf.all.rp_filter = 1" in outputTwo
                ) and
                (
                        "net.ipv4.conf.default.rp_filter = 1" in outputThree and
                        "net.ipv4.conf.default.rp_filter = 1" in outputFour
                ) and
                (
                        "net.ipv4.conf.all.rp_filter = 1" in outputFive and
                        "#" not in outputFive
                ) and
                (
                        "net.ipv4.conf.default.rp_filter = 1" in outputSix and
                        "#" not in outputSix
                )
        ):
            self.Compliant("Ensure Reverse Path Filtering is enabled (Scored)")
        else:
            self.NotCompliant(
                "Ensure Reverse Path Filtering is enabled (Scored)")

    def tcpsyn_3_3_8(self):
        cmdOne = r"sysctl net.ipv4.tcp_syncookies"
        cmdTwo = r"/usr/sbin/sysctl net.ipv4.tcp_syncookies"
        cmdThree = r"""grep "net\.ipv4\.tcp_syncookies" /etc/sysctl.conf /etc/sysctl.d/*"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                (
                        "net.ipv4.tcp_syncookies = 1" in outputOne or
                        "net.ipv4.tcp_syncookies = 1" in outputTwo
                ) and
                (
                        "net.ipv4.tcp_syncookies = 1" in outputThree and
                        "#" not in outputThree
                )
        ):
            self.Compliant("Ensure TCP SYN Cookies is enabled (Scored)")
        else:
            self.NotCompliant("Ensure TCP SYN Cookies is enabled (Scored)")

    def ipv6router_3_3_9(self):
        cmdOne = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "ipv6.disable=1" """
        outputOne = self.caller(cmdOne)

        if outputOne == "":
            self.Compliant(
                "Ensure IPv6 router advertisements are not accepted (Scored) + IPv6 Disabled")
        else:
            cmdTwo = r"sysctl net.ipv6.conf.all.accept_ra"
            cmdThree = r"/usr/sbin/sysctl net.ipv6.conf.all.accept_ra"

            cmdFour = r"sysctl net.ipv6.conf.default.accept_ra"
            cmdFive = r"/usr/sbin/sysctl net.ipv6.conf.default.accept_ra"

            cmdSix = r"""grep "net\.ipv6\.conf\.all\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*"""
            cmdSeven = r"""grep "net\.ipv6\.conf\.default\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*"""

            outputTwo = self.caller(cmdTwo)
            outputThree = self.caller(cmdThree)
            outputFour = self.caller(cmdFour)
            outputFive = self.caller(cmdFive)
            outputSix = self.caller(cmdSix)
            outputSeven = self.caller(cmdSeven)

            if (
                    (
                            "net.ipv6.conf.all.accept_ra = 0" in outputTwo or
                            "net.ipv6.conf.all.accept_ra = 0" in outputThree
                    ) and
                    (
                            "net.ipv6.conf.default.accept_ra = 0" in outputFour or
                            "net.ipv6.conf.default.accept_ra = 0" in outputFive
                    ) and
                    (
                            "net.ipv6.conf.all.accept_ra = 0" in outputSix and
                            "#" not in outputSix
                    ) and
                    (
                            "net.ipv6.conf.default.accept_ra = 0" in outputSeven and
                            "#" not in outputSeven
                    )
            ):
                self.Compliant(
                    "Ensure IPv6 router advertisements are not accepted (Scored)")
            else:
                self.NotCompliant(
                    " Ensure IPv6 router advertisements are not accepted (Scored)")

    def dccp_3_4_1(self):
        cmdOne = r"modprobe -n -v dccp"
        cmdTwo = r"/usr/sbin/modprobe -n -v dccp"

        cmdThree = r"lsmod | grep dccp"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                (
                        "install /bin/true" in outputOne or
                        "install /bin/true" in outputTwo
                ) and
                (
                        outputThree == ""
                )
        ):
            self.Compliant("Ensure DCCP is disabled (Scored)")
        else:
            self.NotCompliant("Ensure DCCP is disabled (Scored)")

    def sctp_3_4_2(self):
        cmdOne = r"modprobe -n -v sctp | grep -E '(sctp|install)'"
        cmdTwo = r"/usr/sbin/modprobe -n -v sctp | grep -E '(sctp|install)'"
        cmdThree = r"lsmod | grep sctp"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                (
                        "install /bin/true" in outputOne or
                        "install /bin/true" in outputTwo
                ) and
                (
                        outputThree == ""
                )
        ):
            self.Compliant("Ensure SCTP is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SCTP is disabled (Scored)")

    def rds_3_4_3(self):
        cmdOne = r"modprobe -n -v rds"
        cmdTwo = r"/usr/sbin/modprobe -n -v rds"
        cmdThree = r"lsmod | grep rds"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        if (
                (
                        "install /bin/true" in outputOne or
                        "install /bin/true" in outputTwo
                ) and
                (
                        outputThree == ""
                )
        ):
            self.Compliant("Ensure RDS is disabled (Scored)")
        else:
            self.NotCompliant("Ensure RDS is disabled (Scored)")

    def tipc_3_4_4(self):
        cmdOne = r"modprobe -n -v tipc | grep -E '(tipc|install)'"
        cmdTwo = r"/usr/sbin/modprobe -n -v tipc | grep -E '(tipc|install)'"
        cmdThree = r" lsmod | grep tipc"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                (
                        "install /bin/true" in outputOne or
                        "install /bin/true" in outputTwo
                ) and
                (
                        outputThree == ""
                )
        ):
            self.Compliant("Ensure TIPC is disabled (Scored)")
        else:
            self.NotCompliant("Ensure TIPC is disabled (Scored)")

    def firewall_3_5_1_1(self):
        cmdOne = r"dpkg -s ufw | grep -i status"
        cmdTwo = r"dpkg -s nftables | grep -i status"
        cmdThree = r"dpkg -s iptables | grep -i status"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                "install ok installed" in outputOne or
                "install ok installed" in outputTwo or
                "install ok installed" in outputThree
        ):
            self.Compliant("Ensure a Firewall package is installed (Scored)")
        else:
            self.NotCompliant(
                "Ensure a Firewall package is installed (Scored)")

    def ufwservice_3_5_2_1(self):
        cmdOne = r"systemctl is-enabled ufw"
        cmdTwo = r"ufw status | grep Status"
        cmdThree = r"/usr/sbin/ufw status | grep Status"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                "enabled" in outputOne and
                (
                        "active" in outputTwo or
                        "active" in outputThree
                )
        ):
            self.Compliant("Ensure ufw service is enabled (Scored)")
        else:
            self.NotCompliant("Ensure ufw service is enabled (Scored)")

    def ufwdeny_3_5_2_2(self):
        cmdOne = r"sudo ufw status verbose"
        cmdTwo = r"sudo /usr/sbin/ufw status verbose"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "deny (incoming)" in outputOne or
                        "deny (incoming)" in outputTwo
                ) and
                (
                        "deny (outgoing)" in outputOne or
                        "deny (outgoing)" in outputTwo
                ) and
                (
                        (
                                "disabled (routed)" in outputOne or
                                "disabled (routed)" in outputTwo
                        ) or
                        (
                                "deny (routed)" in outputOne or
                                "deny (routed)" in outputTwo
                        )
                )
        ):
            self.Compliant("Ensure default deny firewall policy (Scored)")
        else:
            self.NotCompliant("Ensure default deny firewall policy (Scored)")

    def ufwloopback_3_5_2_3(self):
        cmdOne = r"sudo /usr/sbin/ufw status verbose"
        cmdTwo = r"sudo ufw status verbose"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputFinal = outputOne + "\n" + outputTwo

        if (
                (
                        "Anywhere on lo             ALLOW IN    Anywhere" in outputFinal
                ) and
                (
                        "Anywhere                   DENY IN     127.0.0.0/8" in outputFinal
                ) and
                (
                        "Anywhere (v6) on lo        ALLOW IN    Anywhere (v6)" in outputFinal
                ) and
                (
                        "Anywhere (v6)              DENY IN     ::1" in outputFinal
                ) and
                (
                        "Anywhere                   ALLOW OUT   Anywhere on lo" in outputFinal
                ) and
                (
                        "Anywhere (v6)              ALLOW OUT   Anywhere (v6) on lo" in outputFinal
                )
        ):
            self.Compliant("Ensure loopback traffic is configured (Scored)")
        else:
            self.NotCompliant("Ensure loopback traffic is configured (Scored)")

    def ufwoutbound_3_5_2_4(self):
        cmdOne = r"ufw status numbered"
        cmdTwo = r"/usr/sbin/ufw status numbered"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        self.InfoNotSure(
            "Ensure outbound connections are configured (Not Scored)")
        if (
                "command not found" in outputOne or
                "failed" in outputOne
        ):
            print(
                "Verify all rules for new outbound connections match site policy:\n" + outputTwo)
        else:
            print(
                "Verify all rules for new outbound connections match site policy:\n" + outputOne)

    def confnf_3_5_3(self):
        print("(Skipped) - Configure nftables")
        print("(Skipped) - Ensure iptables are flushed (Not Scored)")
        print("(Skipped) - Ensure a table exists (Scored)")
        print("(Skipped) - Ensure base chains exist (Scored)")
        print("(Skipped) - Ensure loopback traffic is configured (Scored)")
        print("(Skipped) - Ensure outbound and established connections are configured (Not Scored)")

    def nfloop_3_5_3_4(self):
        cmdOne = r"""nft list ruleset | awk '/hook input/,/}/' | grep 'iif "lo" accept'"""
        cmdTwo = r"nft list ruleset | awk '/hook input/,/}/' | grep 'ip sddr'"

        cmdThree = r"""/usr/sbin/nft list ruleset | awk '/hook input/,/}/' | grep 'iif "lo" accept'"""
        cmdFour = r"/usr/sbin/nft list ruleset | awk '/hook input/,/}/' | grep 'ip sddr'"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)

        if (
                (
                        'iif "lo" accept' in outputOne or
                        'iif "lo" accept' in outputThree
                ) and
                (
                        "ip saddr 127.0.0.0/8 counter packets 0 bytes 0 drop" in outputTwo or
                        "ip saddr 127.0.0.0/8 counter packets 0 bytes 0 drop" in outputFour
                )
        ):
            self.Compliant("Ensure loopback traffic is configured (Scored)")
        else:
            self.NotCompliant("Ensure loopback traffic is configured (Scored)")

    def nfdeny_3_5_3_6(self):
        cmdOne = r"nft list ruleset | grep 'hook input'"
        cmdTwo = r"/usr/sbin/nft list ruleset | grep 'hook input'"

        cmdThree = r"nft list ruleset | grep 'hook forward'"
        cmdFour = r"/usr/sbin/nft list ruleset | grep 'hook forward'"

        cmdFive = r"nft list ruleset | grep 'hook output'"
        cmdSix = r"/usr/sbin/nft list ruleset | grep 'hook output'"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFour = self.caller(cmdFour)
        outputFive = self.caller(cmdFive)
        outputSix = self.caller(cmdSix)

        if (
                (
                        "type filter hook input priority 0; policy drop;" in outputOne or
                        "type filter hook input priority 0; policy drop;" in outputTwo
                ) and
                (
                        "type filter hook forward priority 0; policy drop;" in outputThree or
                        "type filter hook forward priority 0; policy drop;" in outputFour
                ) and
                (
                        "type filter hook output priority 0; policy drop;" in outputFive or
                        "type filter hook output priority 0; policy drop;" in outputSix
                )
        ):
            self.Compliant("Ensure default deny firewall policy (Scored)")
        else:
            self.NotCompliant("Ensure default deny firewall policy (Scored)")

    def nfservice_3_5_3_7(self):
        cmdOne = r"systemctl is-enabled nftables"
        outputOne = self.caller(cmdOne)

        if (
                "enabled" in outputOne
        ):
            self.Compliant("Ensure nftables service is enabled (Scored)")
        else:
            self.NotCompliant("Ensure nftables service is enabled (Scored)")

    def nfrules_3_5_3_8(self):
        cmdOne = r"""awk '/hook input/,/}/' $(awk '$1 ~ /^\s*include/ { gsub("\"","",$2);print $2 }' /etc/nftables.conf) """
        cmdTwo = r"""awk '/hook output/,/}/' $(awk '$1 ~ /^\s*include/ { gsub("\"","",$2);print $2 }' /etc/nftables.conf)"""
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "Ensure loopback traffic is configured" in outputOne or
                        "Ensure established connections are configured" in outputOne or
                        "Accept port 22(SSH) traffic from anywhere" in outputOne or
                        "Accept ICMP and IGMP from anywhere" in outputOne
                ) and
                (
                        "Base chain for hook output named output (Filters outbound network packets)" in outputTwo or
                        "type filter hook output priority 0; policy drop;" in outputTwo
                )
        ):
            self.Compliant("Ensure nftables rules are permanent (Scored)")
        else:
            self.NotCompliant("Ensure nftables rules are permanent (Scored)")

    def ipdeny_3_5_4_1_1(self):
        cmdOne = r"iptables -L"
        cmdTwo = r"/usr/sbin/iptables -L"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "Chain INPUT (policy DROP)" in outputOne and
                        "Chain FORWARD (policy DROP)" in outputOne and
                        "Chain OUTPUT (policy DROP)" in outputOne
                ) or
                (
                        "Chain INPUT (policy DROP)" in outputTwo and
                        "Chain FORWARD (policy DROP)" in outputTwo and
                        "Chain OUTPUT (policy DROP)" in outputTwo
                )
        ):
            self.Compliant("Ensure default deny firewall policy (Scored)")
        else:
            self.NotCompliant("Ensure default deny firewall policy (Scored)")

    def iploop_3_5_4_1_2(self):
        cmdOne = r"iptables -L INPUT -v -n"
        cmdTwo = r"/usr/sbin/iptables -L INPUT -v -n"

        cmdThree = r"iptables -L OUTPUT -v -n"
        cmdFour = r"/usr/sbin/iptables -L OUTPUT -v -n"

        outputOne = self.caller(cmdOne) + " " + self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree) + " " + self.caller(cmdFour)

        if (
                (
                        "ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0" in outputOne and
                        "DROP       all  --  *      *       127.0.0.0/8          0.0.0.0/0" in outputOne
                ) and
                (
                        "ACCEPT     all  --  *      lo      0.0.0.0/0            0.0.0.0/0" in outputTwo
                )
        ):
            self.Compliant("Ensure loopback traffic is configured (Scored)")
        else:
            self.NotCompliant("Ensure loopback traffic is configured (Scored)")

    def ipoutb_3_5_4_1_3(self):
        cmdOne = r"iptables -L -v -n"
        cmdTwo = r"/usr/sbin/iptables -L -v -n"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        self.InfoNotSure(
            "Ensure outbound and established connections are configured (Not Scored)")
        print("Verify all rules for new outbound, and established connections match site policy:")
        print(outputTwo)
        if (
                "command not found" in outputOne or
                "failed" in outputOne
        ):
            print(outputTwo)
        else:
            print(outputOne)

    def ip6deny_3_5_4_2_1(self):
        cmdOne = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v ipv6.disable=1"""
        cmdTwo = r"ip6tables -L"
        cmdThree = r"/usr/sbin/ip6tables -L"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)
        outputFinal = outputTwo + " " + outputThree

        if (outputOne == ""):
            self.Compliant("Ensure IPv6 default deny firewall policy (Scored)")
        else:
            if (
                    (
                            (
                                    "Chain INPUT (policy DROP)" in outputFinal or
                                    "Chain INPUT (policy REJECT)" in outputFinal
                            ) and
                            (
                                    "Chain FORWARD (policy DROP)" in outputFinal or
                                    "Chain FORWARD (policy REJECT)" in outputFinal
                            ) and
                            (
                                    "Chain OUTPUT (policy DROP)" in outputFinal or
                                    "Chain OUTPUT (policy REJECT)" in outputFinal
                            )
                    )
            ):
                self.Compliant("Ensure IPv6 default deny firewall policy (Scored)")
            else:
                self.NotCompliant("Ensure IPv6 default deny firewall policy (Scored)")

    def ip6loop_3_5_4_2_2(self):
        cmdOne = r"ip6tables -L INPUT -v -n"
        cmdTwo = r"/usr/sbin/ip6tables -L INPUT -v -n"

        cmdThree = r"ip6tables -L OUTPUT -v -n"
        cmdFour = r"/usr/sbin/ip6tables -L OUTPUT -v -n"

        outputOne = self.caller(cmdOne) + " " + self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree) + " " + self.caller(cmdFour)

        if (
                (
                        "ACCEPT     all      lo     *       ::/0                 ::/0" in outputOne and
                        "DROP       all      *      *       ::1                  ::/0" in outputOne
                ) and
                (
                        "ACCEPT     all      *      lo      ::/0                 ::/0" in outputTwo
                )
        ):
            self.Compliant("Ensure IPv6 loopback traffic is configured (Scored)")
        else:
            self.NotCompliant("Ensure IPv6 loopback traffic is configured (Scored)")

    def ip6outb_3_5_4_2_3(self):
        cmdOne = r"ip6tables -L -v -n"
        cmdTwo = r"/usr/sbin/ip6tables -L -v -n"
        cmdThree = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v ipv6.disable=1"""

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                outputThree == ""
        ):
            self.InfoCompliant("Ensure IPv6 outbound and established connections are configured (Not Scored)")
        else:
            self.InfoNotSure("Ensure IPv6 outbound and established connections are configured (Not Scored)")
            if (
                    "command not found" in outputOne or
                    "failed" in outputOne
            ):
                print("Verify all rules for new outbound, and established connections match site policy:")
                print(outputThree)
            else:
                print("Verify all rules for new outbound, and established connections match site policy:")
                print(outputTwo)

    def auditd_4_1_1_1(self):
        cmdOne = r"dpkg -s auditd audispd-plugins"
        outputOne = self.caller(cmdOne)
        if (
                'is not installed and no information' in outputOne
        ):
            self.NotCompliant("Ensure auditd is installed (Scored)")
        elif (
                'install ok installed' in outputOne
        ):
            self.Compliant("Ensure auditd is installed (Scored)")

    def auditdenabled_4_1_1_2(self):
        cmdOne = r"systemctl is-enabled auditd"
        outputOne = self.caller(cmdOne)

        if (
                "enabled" in outputOne
        ):
            self.Compliant("Ensure auditd service is enabled (Scored)")
        else:
            self.NotCompliant("Ensure auditd service is enabled (Scored)")

    def auditproc_4_1_1_3(self):
        cmdOne = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "audit=1" """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == ''
        ):
            self.Compliant("Ensure auditing for processes that start prior to auditd is enabled (Scored)")
        else:
            self.NotCompliant("Ensure auditing for processes that start prior to auditd is enabled (Scored)")

    def auditdbacklog_4_1_1_4(self):
        cmdOne = r"""grep "^\s*linux" /boot/grub/grub.cfg | grep -v "audit_backlog_limit=" """
        cmdTwo = r"""grep "audit_backlog_limit=" /boot/grub/grub.cfg"""
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        lisp = outputTwo.split()
        ranges = list()
        finalLisp = list()

        for i in range(len(lisp)):
            if "audit_backlog_limit" in lisp[i]:
                finalLisp.append(lisp[i])
        for i in finalLisp:
            temp = i.split('=')
            ranges.append(temp[1])
        if (
                outputOne == '' and
                i >= 8129 for i in ranges
        ):
            self.Compliant("Ensure audit_backlog_limit is sufficient (Scored)")
        else:
            self.NotCompliant("Ensure audit_backlog_limit is sufficient (Scored)")

    def auditdlogstorage_4_1_2_1(self):
        cmdOne = r"grep max_log_file /etc/audit/auditd.conf"
        outputOne = self.caller(cmdOne)

        if (
                "max_log_file" in outputOne
        ):
            self.Compliant("Ensure audit log storage size is configured (Scored)")
        else:
            self.NotCompliant("Ensure audit log storage size is configured (Scored)")

    def auditddeleted_4_1_2_2(self):
        cmdOne = r"grep max_log_file_action /etc/audit/auditd.conf"
        outputOne = self.caller(cmdOne)

        if (
                "max_log_file_action = keep_logs" in outputOne
        ):
            self.Compliant("Ensure audit logs are not automatically deleted (Scored)")
        else:
            self.NotCompliant("Ensure audit logs are not automatically deleted (Scored)")

    def auditdsystem_4_1_2_3(self):
        cmdOne = r"grep space_left_action /etc/audit/auditd.conf"
        cmdTwo = r"grep action_mail_acct /etc/audit/auditd.conf"
        cmdThree = r"grep admin_space_left_action /etc/audit/auditd.conf"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                "space_left_action = email" in outputOne and
                "action_mail_acct = root" in outputTwo and
                "admin_space_left_action = halt" in outputThree
        ):
            self.Compliant("Ensure system is disabled when audit logs are full (Scored)")
        else:
            self.NotCompliant("Ensure system is disabled when audit logs are full (Scored)")

    def auditdtime_4_1_3(self):
        cmdOne = r"grep time-change /etc/audit/rules.d/*.rules"
        cmdTwo = r"auditctl -l | grep time-change"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "-a always,exit -F arch=b32 -S adjtimex -S settimeofday -S stime -k time-change" in outputOne and
                        "-a always,exit -F arch=b32 -S clock_settime -k time-change" in outputOne and
                        "-w /etc/localtime -p wa -k time-change" in outputOne and
                        "-a always,exit -F arch=b32 -S stime,settimeofday,adjtimex -F key=time-change" in outputTwo and
                        "-a always,exit -F arch=b32 -S clock_settime -F key=time-change" in outputTwo and
                        "-w /etc/localtime -p wa -k time-change" in outputTwo
                ) or
                (
                        "-a always,exit -F arch=b64 -S adjtimex -S settimeofday -k time-change" in outputOne and
                        "-a always,exit -F arch=b64 -S clock_settime -k time-change" in outputOne and
                        "-w /etc/localtime -p wa -k time-change" in outputOne and
                        "-a always,exit -F arch=b64 -S adjtimex,settimeofday -F key=time-change" in outputTwo and
                        "-a always,exit -F arch=b64 -S clock_settime -F key=time-change" in outputTwo and
                        "-w /etc/localtime -p wa -k time-change" in outputTwo
                )
        ):
            self.Compliant("Ensure events that modify date and time information are collected (Scored)")
        else:
            self.NotCompliant("Ensure events that modify date and time information are collected (Scored)")

    def auditdusermodify_4_1_4(self):
        cmdOne = r"grep identity /etc/audit/rules.d/*.rules"
        cmdTwo = r"auditctl -l | grep identity"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                "-w /etc/group -p wa -k identity" in outputOne and
                "-w /etc/group -p wa -k identity" in outputTwo and
                "-w /etc/passwd -p wa -k identity" in outputOne and
                "-w /etc/passwd -p wa -k identity" in outputTwo and
                "-w /etc/gshadow -p wa -k identity" in outputOne and
                "-w /etc/gshadow -p wa -k identity" in outputTwo and
                "-w /etc/shadow -p wa -k identity" in outputOne and
                "-w /etc/shadow -p wa -k identity" in outputTwo and
                "-w /etc/security/opasswd -p wa -k identity" in outputOne and
                "-w /etc/security/opasswd -p wa -k identity" in outputTwo
        ):
            self.Compliant("Ensure events that modify user/group information are collected (Scored)")
        else:
            self.NotCompliant("Ensure events that modify user/group information are collected (Scored)")

    def auditdsysnet_4_1_5(self):
        cmdOne = r"grep system-locale /etc/audit/rules.d/*.rules"
        outputOne = self.caller(cmdOne)

        if (
                (
                        "-a always,exit -F arch=b32 -S sethostname,setdomainname -F key=system-locale" in outputOne and
                        "-w etc/issue -p wa -k system-locale" in outputOne and
                        "-w /etc/issue.net -p wa -k system-locale" in outputOne and
                        "-w /etc/hosts -p wa -k system-locale" in outputOne and
                        "-w /etc/network -p wa -k system-locale" in outputOne
                ) or
                (
                        "-a always,exit -F arch=b64 -S sethostname,setdomainname -F key=system-locale" in outputOne and
                        "-a always,exit -F arch=b32 -S sethostname,setdomainname -F key=system-locale" in outputOne and
                        "-w etc/issue -p wa -k system-locale" in outputOne and
                        "-w /etc/issue.net -p wa -k system-locale" in outputOne and
                        "-w /etc/hosts -p wa -k system-locale" in outputOne and
                        "-w /etc/network -p wa -k system-locale" in outputOne
                )
        ):
            self.Compliant("Ensure events that modify the system's network environment are collected (Scored)")
        else:
            self.NotCompliant("Ensure events that modify the system's network environment are collected (Scored)")

    def auditdmac_4_1_6(self):
        cmdOne = r"grep MAC-policy /etc/audit/rules.d/*.rules"
        outputOne = self.caller(cmdOne)

        if (
                "-w /etc/apparmor/ -p wa -k MAC-policy" in outputOne and
                "-w /etc/apparmor.d/ -p wa -k MAC-policy" in outputOne
        ):
            self.Compliant("Ensure events that modify the system's Mandatory Access Controls are collected (Scored)")
        else:
            self.NotCompliant("Ensure events that modify the system's Mandatory Access Controls are collected (Scored)")

    def auditdlogin_4_1_7(self):
        cmdOne = r"grep logins /etc/audit/rules.d/*.rules"
        outputOne = self.caller(cmdOne)

        if (
                "-w /var/log/faillog -p wa -k logins" in outputOne and
                "-w /var/log/lastlog -p wa -k logins" in outputOne and
                "-w /var/log/tallylog -p wa -k logins" in outputOne
        ):
            self.Compliant("Ensure login and logout events are collected (Scored)")
        else:
            self.NotCompliant("Ensure login and logout events are collected (Scored)")

    def auditdsession_4_1_8(self):
        cmdOne = r"grep -E '(session|logins)' /etc/audit/rules.d/*.rules"
        outputOne = self.caller(cmdOne)

        if (
                "-w /var/run/utmp -p wa -k session" in outputOne and
                "-w /var/log/wtmp -p wa -k logins" in outputOne and
                "-w /var/log/btmp -p wa -k logins" in outputOne
        ):
            self.Compliant("Ensure session initiation information is collected (Scored)")
        else:
            self.NotCompliant("Ensure session initiation information is collected (Scored)")

    def auditddac_4_1_9(self):
        cmdOne = r"awk '/^\s*UID_MIN/{print $2}' /etc/login.defs"
        cmdTwo = r"grep perm_mod /etc/audit/rules.d/*.rules"
        cmdThree = r"auditctl -l | grep perm_mod"

        minUID = str(int(self.caller(cmdOne)))
        outputOne = self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree)

        if (
                (
                        "-a always,exit -F arch=b32 -S chmod -S fchmod -S fchmodat -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S chown -S fchown -S fchownat -S lchown -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b32 -S lchown,fchown,chown,fchownat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b32 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo
                ) or
                (
                        "-a always,exit -F arch=b64 -S chmod -S fchmod -S fchmodat -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S chmod -S fchmod -S fchmodat -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b64 -S chown -S fchown -S fchownat -S lchown -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S chown -S fchown -S fchownat -S lchown -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b64 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b32 -S setxattr -S lsetxattr -S fsetxattr -S removexattr -S lremovexattr -S fremovexattr -F auid>=" + minUID + " -F auid!=4294967295 -k perm_mod" in outputOne and
                        "-a always,exit -F arch=b64 -S chmod,fchmod,fchmodat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b32 -S chmod,fchmod,fchmodat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b64 -S chown,fchown,lchown,fchownat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" and
                        "-a always,exit -F arch=b32 -S lchown,fchown,chown,fchownat -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b64 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo and
                        "-a always,exit -F arch=b32 -S setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr -F auid>=" + minUID + " -F auid!=-1 -F key=perm_mod" in outputTwo

                )
        ):
            self.Compliant("Ensure discretionary access control permission modification events are collected (Scored)")
        else:
            self.NotCompliant(
                "Ensure discretionary access control permission modification events are collected (Scored)")

    def auditdufa_4_1_10(self):
        cmdOne = r"awk '/^\s*UID_MIN/{print $2}' /etc/login.defs"
        cmdTwo = r"grep access /etc/audit/rules.d/*.rules"
        cmdThree = r"auditctl -l | grep access"

        minUID = str(int(self.caller(cmdOne)))
        outputOne = self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree)

        if (
                (
                        "-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat -F exit=-EACCES -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo and
                        "-a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat -F exit=-EPERM -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo

                ) or
                (
                        "-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b64 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b32 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b64 -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=" + minUID + " -F auid!=4294967295 -k access" in outputOne and
                        "-a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat -F exit=-EACCES -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo and
                        "-a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat -F exit=-EACCES -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo and
                        "-a always,exit -F arch=b64 -S open,truncate,ftruncate,creat,openat -F exit=-EPERM -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo and
                        "-a always,exit -F arch=b32 -S open,creat,truncate,ftruncate,openat -F exit=-EPERM -F auid>=" + minUID + " -F auid!=-1 -F key=access" in outputTwo
                )
        ):
            self.Compliant("nsure unsuccessful unauthorized file access attempts are collected (Scored)")
        else:
            self.NotCompliant("nsure unsuccessful unauthorized file access attempts are collected (Scored)")

    def auditdfsmount_4_1_12(self):
        cmdOne = r"awk '/^\s*UID_MIN/{print $2}' /etc/login.defs"
        cmdTwo = r"grep mounts /etc/audit/rules.d/*.rules"
        cmdThree = r"auditctl -l | grep mounts"

        minUID = str(int(self.caller(cmdOne)))
        outputOne = self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree)

        if (
                (
                        "-a always,exit -F arch=b32 -S mount -F auid>=" + minUID + " -F auid!=4294967295 -k mounts" in outputOne and
                        "-a always,exit -F arch=b32 -S mount -F auid>=" + minUID + " -F auid!=-1 -F key=mounts" in outputTwo
                ) or
                (
                        "-a always,exit -F arch=b32 -S mount -F auid>=" + minUID + " -F auid!=4294967295 -k mounts" in outputOne and
                        "-a always,exit -F arch=b64 -S mount -F auid>=" + minUID + " -F auid!=4294967295 -k mounts" in outputOne and
                        "-a always,exit -F arch=b32 -S mount -F auid>=" + minUID + " -F auid!=-1 -F key=mounts" in outputTwo and
                        "-a always,exit -F arch=b64 -S mount -F auid>=" + minUID + " -F auid!=-1 -F key=mounts" in outputTwo

                )
        ):
            self.Compliant("Ensure successful file system mounts are collected (Scored)")
        else:
            self.NotCompliant("Ensure successful file system mounts are collected (Scored)")

    def auditdfiledel_4_1_13(self):
        cmdOne = r"awk '/^\s*UID_MIN/{print $2}' /etc/login.defs"
        cmdTwo = r"grep delete /etc/audit/rules.d/*.rules"
        cmdThree = r"auditctl -l | grep delete"

        minUID = str(int(self.caller(cmdOne)))
        outputOne = self.caller(cmdTwo)
        outputTwo = self.caller(cmdThree)

        if (
                (
                        "-a always,exit -F arch=b32 -S unlink -S unlinkat -S rename -S renameat -F auid>=" + minUID + " -F auid!=4294967295 -k delete" in outputOne and
                        "-a always,exit -F arch=b32 -S unlink,rename,unlinkat,renameat -F auid>=" + minUID + " -F auid!=-1 -F key=delete" in outputTwo
                ) or
                (
                        "-a always,exit -F arch=b32 -S unlink -S unlinkat -S rename -S renameat -F auid>=" + minUID + " -F auid!=4294967295 -k delete" in outputOne and
                        "-a always,exit -F arch=b64 -S unlink -S unlinkat -S rename -S renameat -F auid>=" + minUID + " -F auid!=4294967295 -k delete" in outputOne and
                        "-a always,exit -F arch=b64 -S rename,unlink,unlinkat,renameat -F auid>=5100 -F auid!=-1 -F key=delete" in outputTwo and
                        "-a always,exit -F arch=b32 -S unlink,rename,unlinkat,renameat -F auid>=" + minUID + " -F auid!=-1 -F key=delete" in outputTwo

                )
        ):
            self.Compliant("Ensure file deletion events by users are collected (Scored)")
        else:
            self.NotCompliant("Ensure file deletion events by users are collected (Scored)")

    def auditdsudoers_4_1_14(self):
        cmdOne = r"grep scope /etc/audit/rules.d/*.rules"
        cmdTwo = r"auditctl -l | grep scope"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "-w /etc/sudoers -p wa -k scope" in outputOne and
                        "-w /etc/sudoers.d/ -p wa -k scope" in outputOne
                ) and
                (
                        "-w /etc/sudoers -p wa -k scope" in outputTwo and
                        "-w /etc/sudoers.d/ -p wa -k scope" in outputTwo
                )
        ):
            self.Compliant("Ensure changes to system administration scope (sudoers) is collected (Scored)")
        else:
            self.NotCompliant("Ensure changes to system administration scope (sudoers) is collected (Scored)")

    def auditdsudolog_4_1_15(self):
        cmdOne = r"""grep -E "^\s*-w\s+$(grep -r logfile /etc/sudoers* | sed -e 's/.*logfile=//;s/,? .*//')\s+-p\s+wa\s+-k\s+actions"/etc/audit/rules.d/*.rules  """
        cmdTwo = r"auditctl -l | grep actions"
        cmdThree = r"""echo "-w $(grep -r logfile /etc/sudoers* | sed -e 's/.*logfile=//;s/,? .*//') -p wa -k actions" """
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                "-w" in outputThree and
                "-p wa -k actions" in outputThree and
                ".log" in outputThree and
                outputOne.strip() == outputThree.strip() and
                outputTwo.strip() == outputThree.strip()
        ):
            self.Compliant("Ensure system administrator actions (sudolog) are collected (Scored)")

        else:
            self.NotCompliant("Ensure system administrator actions (sudolog) are collected (Scored)")

    def auditdkernel_4_1_16(self):
        cmdOne = r"grep modules /etc/audit/rules.d/*.rules"
        cmdTwo = r"auditctl -l | grep modules"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        if (
                (
                        "-w /sbin/insmod -p x -k modules" in outputOne and
                        "-w /sbin/insmod -p x -k modules" in outputTwo and
                        "-w /sbin/rmmod -p x -k modules" in outputOne and
                        "-w /sbin/rmmod -p x -k modules" in outputTwo and
                        "-w /sbin/modprobe -p x -k modules" in outputOne and
                        "-w /sbin/modprobe -p x -k modules" in outputTwo and
                        "-a always,exit -F arch=b32 -S init_module -S delete_module -k modules" in outputOne and
                        (
                                "-a always,exit -F arch=b32 -S init_module,delete_module -F key=modules" in outputTwo or
                                "-a always,exit -F arch=b64 -S init_module,delete_module -F key=modules" in outputTwo
                        )

                )
        ):
            self.Compliant("Ensure kernel module loading and unloading is collected (Scored)")
        else:
            self.NotCompliant("Ensure kernel module loading and unloading is collected (Scored)")

    def auditdconfig_4_1_17(self):
        cmdOne = r"""grep "^\s*[^#]" /etc/audit/rules.d/*.rules | tail -1"""
        outputOne = self.caller(cmdOne)

        if (
                "-e 2" in outputOne
        ):
            self.Compliant("Ensure the audit configuration is immutable (Scored)")
        else:
            self.NotCompliant("Ensure the audit configuration is immutable (Scored)")

    def rsyslog_4_2_1_1(self):
        cmdOne = r"dpkg -s rsyslog"
        outputOne = self.caller(cmdOne)

        if (
                "install ok installed" in outputOne
        ):
            self.Compliant("Ensure rsyslog is installed (Scored)")
        else:
            self.NotCompliant("Ensure rsyslog is installed (Scored)")

    def rsyslogenabled_4_2_1_2(self):
        cmdOne = r"systemctl is-enabled rsyslog"
        outputOne = self.caller(cmdOne)

        if (
                "enabled" in outputOne
        ):
            self.Compliant("Ensure rsyslog Service is enabled (Scored)")
        else:
            self.NotCompliant("Ensure rsyslog Service is enabled (Scored)")

    def rsyslogperm_4_2_1_4(self):
        cmdOne = r"grep ^\$FileCreateMode /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
        outputOne = self.caller(cmdOne)

        if (
                "$FileCreateMode 0640" in outputOne
        ):
            self.Compliant("Ensure rsyslog default file permissions configured (Scored)")
        else:
            self.NotCompliant("Ensure rsyslog default file permissions configured (Scored)")

    def rsyslogremote_4_2_1_5(self):
        cmdOne = r"""grep -E "^[^#](\s*\S+\s*)\s*action\(" /etc/rsyslog.conf /etc/rsyslog.d/*.conf | grep "target=" """
        outputOne = self.caller(cmdOne)

        if (
                outputOne != ""
        ):
            self.Compliant("Ensure rsyslog is configured to send logs to a remote log host (Scored)")
        else:
            self.NotCompliant("Ensure rsyslog is configured to send logs to a remote log host (Scored)")

    def rsyslogremotedesignated_4_2_1_6(self):
        cmdOne = r"grep '$ModLoad imtcp' /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
        cmdTwo = r"grep '$InputTCPServerRun' /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        "$ModLoad imtcp" in outputOne and
                        "#$ModLoad imtcp" not in outputOne and
                        "# $ModLoad imtcp" not in outputOne
                ) and
                (
                        "$InputTCPServerRun 514" in outputTwo and
                        "#$InputTCPServerRun 514" not in outputTwo and
                        "# $InputTCPServerRun 514" not in outputTwo
                )
        ):
            self.InfoCompliant("Ensure remote rsyslog messages are only accepted on designated log hosts. (Not Scored)")
        else:
            self.InfoNotCompliant(
                "Ensure remote rsyslog messages are only accepted on designated log hosts. (Not Scored)")

    def journaldconfig_4_2_2_1(self):
        cmdOne = r"grep -e ForwardToSyslog /etc/systemd/journald.conf"
        outputOne = self.caller(cmdOne)

        if (
                "ForwardToSyslog=yes" in outputOne
        ):
            self.Compliant("Ensure journald is configured to send logs to rsyslog (Scored)")
        else:
            self.NotCompliant("Ensure journald is configured to send logs to rsyslog (Scored)")

    def journaldcompress_4_2_2_2(self):
        cmdOne = r"grep -e Compress /etc/systemd/journald.conf"
        outputOne = self.caller(cmdOne)

        if (
                "Compress=yes" in outputOne
        ):
            self.Compliant("Ensure journald is configured to compress large log files (Scored)")
        else:
            self.NotCompliant("Ensure journald is configured to compress large log files (Scored)")

    def journaldpers_4_2_2_3(self):
        cmdOne = r"grep -e Storage /etc/systemd/journald.conf"
        outputOne = self.caller(cmdOne)

        if (
                "Storage=persistent" in outputOne
        ):
            self.Compliant("Ensure journald is configured to write logfiles to persistent disk (Scored)")
        else:
            self.NotCompliant("Ensure journald is configured to write logfiles to persistent disk (Scored)")

    def logrotate_4_4(self):
        cmdOne = r"""grep -E "^\s*create\s+\S+" /etc/logrotate.conf | grep -E -v "\s(0)?[0-6][04]0\s" """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == ""
        ):
            self.Compliant("Ensure logrotate assigns appropriate permissions (Scored)")
        else:
            self.NotCompliant("Ensure logrotate assigns appropriate permissions (Scored)")

    def crond_5_1_1(self):
        cmdOne = r"systemctl is-enabled cron"
        outputOne = self.caller(cmdOne)

        if (
                "enabled" in outputOne
        ):
            self.Compliant("Ensure cron daemon is enabled (Scored)")
        else:
            self.NotCompliant("Ensure cron daemon is enabled (Scored)")

    def cronperm_5_1_2(self):
        cmdOne = r"stat /etc/crontab"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/crontab are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/crontab are configured (Scored)")

    def cronhourlyperm_5_1_3(self):
        cmdOne = r"stat /etc/cron.hourly"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0700/drwx------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/cron.hourly are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/cron.hourly are configured (Scored)")

    def crondailyperm_5_1_4(self):
        cmdOne = r"stat /etc/cron.daily"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0700/drwx------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/cron.daily are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/cron.daily are configured (Scored)")

    def cronweeklyperm_5_1_5(self):
        cmdOne = r"stat /etc/cron.weekly"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0700/drwx------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/cron.weekly are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/cron.weekly are configured (Scored)")

    def cronmonthlyperm_5_1_6(self):
        cmdOne = r"stat /etc/cron.monthly"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0700/drwx------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/cron.monthly are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/cron.monthly are configured (Scored)")

    def crondperm_5_1_7(self):
        cmdOne = r"stat /etc/cron.d"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0700/drwx------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/cron.d are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/cron.d are configured (Scored)")

    def atcron_5_1_8(self):
        cmdOne = r"stat /etc/cron.deny"
        cmdTwo = r"stat /etc/at.deny"
        cmdThree = r"stat /etc/cron.allow"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)
        outputThree = self.caller(cmdThree)

        if (
                "No such file or directory" in outputOne and
                "No such file or directory" in outputTwo and
                "Access: (0640/-rw-r-----)  Uid: (    0/    root)   Gid: (    0/    root)"
        ):
            self.Compliant("Ensure at/cron is restricted to authorized users (Scored)")
        else:
            self.NotCompliant("Ensure at/cron is restricted to authorized users (Scored)")

    def sshdconfig_5_2_1(self):
        cmdOne = r"stat /etc/ssh/sshd_config"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/ssh/sshd_config are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/ssh/sshd_config are configured (Scored)")

    def sshone_5_2_4(self):
        cmdOne = r"""sshd -T | grep -Ei '^\s*protocol\s+(1|1\s*,\s*2|2\s*,\s*1)\s*' """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == ""
        ):
            self.Compliant("Ensure SSH Protocol is not set to 1 (Scored)")
        else:
            self.NotCompliant("Ensure SSH Protocol is not set to 1 (Scored)")

    def sshloglevel_5_2_5(self):
        cmdOne = r"sshd -T | grep loglevel"
        outputOne = self.caller(cmdOne)

        if (
                "LogLevel VERBOSE" in outputOne or
                "loglevel INFO" in outputOne
        ):
            self.Compliant("Ensure SSH LogLevel is appropriate (Scored)")
        else:
            self.NotCompliant("Ensure SSH LogLevel is appropriate (Scored)")

    def sshx11_5_2_6(self):
        cmdOne = r"sshd -T | grep x11forwarding"
        outputOne = self.caller(cmdOne)

        if (
                "X11Forwarding no" in outputOne
        ):
            self.Compliant("Ensure SSH X11 forwarding is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH X11 forwarding is disabled (Scored)")

    def sshmaxauth_5_2_7(self):
        cmdOne = r"sshd -T | grep maxauthtries"
        outputOne = self.caller(cmdOne)

        if "MaxAuthTries" in outputOne:
            temp = outputOne.split()
            try:
                tries = int(temp[1])
                if tries <= 4:
                    self.Compliant("Ensure SSH MaxAuthTries is set to 4 or less (Scored)")
                else:
                    self.NotCompliant("Ensure SSH MaxAuthTries is set to 4 or less (Scored)")
            except:
                self.NotCompliant("Ensure SSH MaxAuthTries is set to 4 or less (Scored)")
        else:
            self.NotCompliant("Ensure SSH MaxAuthTries is set to 4 or less (Scored)")

    def sshignorerhost_5_2_8(self):
        cmdOne = r"sshd -T | grep ignorerhosts"
        outputOne = self.caller(cmdOne)

        if (
                "IgnoreRhosts yes" in outputOne
        ):
            self.Compliant("Ensure SSH IgnoreRhosts is enabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH IgnoreRhosts is enabled (Scored)")

    def sshhostbased_5_2_9(self):
        cmdOne = r"sshd -T | grep hostbasedauthentication"
        outputOne = self.caller(cmdOne)

        if (
                "HostbasedAuthentication no" in outputOne
        ):
            self.Compliant("Ensure SSH HostbasedAuthentication is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH HostbasedAuthentication is disabled (Scored)")

    def sshrootlogin_5_2_10(self):
        cmdOne = r"sshd -T | grep permitrootlogin"
        outputOne = self.caller(cmdOne)

        if (
                "PermitRootLogin no" in outputOne
        ):
            self.Compliant("Ensure SSH root login is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH root login is disabled (Scored)")

    def sshempty_5_2_11(self):
        cmdOne = r"sshd -T | grep permitemptypasswords"
        outputOne = self.caller(cmdOne)

        if (
                "PermitEmptyPasswords no" in outputOne
        ):
            self.Compliant("Ensure SSH PermitEmptyPasswords is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH PermitEmptyPasswords is disabled (Scored)")

    def sshuserenv_5_2_12(self):
        cmdOne = r"sshd -T | grep permituserenvironment"
        outputOne = self.caller(cmdOne)

        if (
                "PermitUserEnvironment no" in outputOne
        ):
            self.Compliant("Ensure SSH PermitUserEnvironment is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH PermitUserEnvironment is disabled (Scored)")

    def sshstrongcipher_5_2_13(self):
        cmdOne = r"sshd -T | grep ciphers"
        outputOne = self.caller(cmdOne)
        found = False
        weak = "3des-cbc,aes128-cbc,aes192-cbc,aes256-cbc,arcfour,arcfour128,arcfour256," + \
               "blowfish-cbc,cast128-cbc,rijndael-cbc@lysator.liu.se"
        weak = weak.split(",")

        for i in weak:
            if i in outputOne:
                found = True

        if not found and "command not found" not in outputOne:
            self.Compliant("Ensure only strong Ciphers are used (Scored)")
        else:
            self.NotCompliant("Ensure only strong Ciphers are used (Scored)")

    def strongmac_5_2_14(self):
        cmdOne = r"""sshd -T | grep -i "MACs" """
        outputOne = self.caller(cmdOne)
        found = False

        weak = "hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-sha1,hmac-sha1-96,umac-64@openssh.com,umac-128@openssh.com," + \
               "hmac-md5-etm@openssh.com,hmac-md5-96-etm@openssh.com,hmac-ripemd160-etm@openssh.com," + \
               "hmac-sha1-etm@openssh.com,hmac-sha1-96-etm@openssh.com," + \
               "umac-64-etm@openssh.com,umac-128-etm@openssh.com"
        weak = weak.split(',')

        for i in weak:
            if i in outputOne:
                found = True
        if not found and "command not found" not in outputOne:
            self.Compliant("Ensure only strong MAC algorithms are used (Scored)")
        else:
            self.NotCompliant("Ensure only strong MAC algorithms are used (Scored)")

    def strongkex_5_2_15(self):
        cmdOne = r"sshd -T | grep kexalgorithms"
        outputOne = self.caller(cmdOne)

        found = False
        weak = r"diffie-hellman-group1-sha1,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1"
        weak = weak.split(",")

        for i in weak:
            if i in outputOne:
                found = True
        if not found and "command not found" not in outputOne:
            self.Compliant("Ensure only strong Key Exchange algorithms are used (Scored)")
        else:
            self.NotCompliant("Ensure only strong Key Exchange algorithms are used (Scored)")

    def sshidle_5_2_16(self):
        cmdOne = r"sshd -T | grep clientaliveinterval"
        cmdTwo = r"sshd -T | grep clientalivecountmax"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                "ClientAliveInterval 300" in outputOne and
                "ClientAliveCountMax 0" in outputTwo
        ):
            self.Compliant("Ensure SSH Idle Timeout Interval is configured (Scored)")
        else:
            self.NotCompliant("Ensure SSH Idle Timeout Interval is configured (Scored)")

    def sshlogingrace_5_2_17(self):
        cmdOne = r"sshd -T | grep logingracetime"
        outputOne = self.caller(cmdOne)

        try:
            graceTime = int(outputOne.split(" "))
            if (graceTime > 1 and graceTime <= 60):
                self.Compliant("Ensure SSH LoginGraceTime is set to one minute or less (Scored)")
            else:
                self.NotCompliant("Ensure SSH LoginGraceTime is set to one minute or less (Scored)")
        except:
            self.NotCompliant("Ensure SSH LoginGraceTime is set to one minute or less (Scored)")

    def sshbanner_5_2_19(self):
        cmdOne = r"sshd -T | grep banner"
        outputOne = self.caller(cmdOne)

        if (
                "Banner /etc/issue.net" in outputOne
        ):
            self.Compliant("Ensure SSH warning banner is configured (Scored)")
        else:
            self.NotCompliant("Ensure SSH warning banner is configured (Scored)")

    def sshpam_5_2_20(self):
        cmdOne = r"sshd -T | grep -i usepam"
        outputOne = self.caller(cmdOne)

        if (
                "usepam yes" in outputOne or
                "usePAM yes" in outputOne
        ):
            self.Compliant("Ensure SSH PAM is enabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH PAM is enabled (Scored)")

    def sshtcp_5_2_21(self):
        cmdOne = r"sshd -T | grep -i allowtcpforwarding"
        outputOne = self.caller(cmdOne)

        if (
                "AllowTcpForwarding no" in outputOne
        ):
            self.Compliant("Ensure SSH AllowTcpForwarding is disabled (Scored)")
        else:
            self.NotCompliant("Ensure SSH AllowTcpForwarding is disabled (Scored)")

    def sshmax_5_2_22(self):
        cmdOne = r"sshd -T | grep -i maxstartups"
        outputOne = self.caller(cmdOne)

        if (
                "maxstartups 10:30:60" in outputOne
        ):
            self.Compliant("Ensure SSH MaxStartups is configured (Scored)")
        else:
            self.NotCompliant("Ensure SSH MaxStartups is configured (Scored)")

    def sshmaxsessions_5_2_23(self):
        cmdOne = r"sshd -T | grep -i maxsessions"
        outputOne = self.caller(cmdOne)

        try:
            maxSessions = int(outputOne.split(" "))
            if maxSessions[1] <= 10:
                self.Compliant("Ensure SSH MaxSessions is limited (Scored)")
            else:
                self.NotCompliant("Ensure SSH MaxSessions is limited (Scored)")
        except:
            self.NotCompliant("Ensure SSH MaxSessions is limited (Scored)")

    def pwdreqs_5_3_1(self):
        cmdOne = r"grep '^\s*minlen\s*' /etc/security/pwquality.conf"
        cmdTwo = r"grep '^\s*minclass\s*' /etc/security/pwquality.conf"

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        cmdThree = r"grep -E '^\s*[duol]credit\s*' /etc/security/pwquality.conf"
        outputThree = self.caller(cmdThree)

        if (
                (
                        "minlen = 14" in outputOne and
                        "minclass = 4" in outputTwo
                ) or
                (
                        "dcredit = -1" in outputThree and
                        "ucredit = -1" in outputThree and
                        "lcredit = -1" in outputThree and
                        "ocredit = -1" in outputThree
                )
        ):
            self.Compliant("Ensure password creation requirements are configured (Scored)")
        else:
            self.NotCompliant("Ensure password creation requirements are configured (Scored)")

    def lockout_5_3_2(self):
        cmdOne = r"""grep "pam_tally2" /etc/pam.d/common-auth"""
        cmdTwo = r"""grep -E "pam_(tally2|deny)\.so" /etc/pam.d/common-account"""
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                "auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900" in outputOne and
                "pam_deny.so" in outputTwo and
                "pam_tally2.so"
        ):
            self.Compliant("Ensure lockout for failed password attempts is configured (Scored)")

        else:
            self.NotCompliant("Ensure lockout for failed password attempts is configured (Scored)")

    def passreuse_5_3_3(self):
        cmdOne = r"grep -E '^password\s+required\s+pam_pwhistory.so' /etc/pam.d/common-password"
        outputOne = self.caller(cmdOne)

        try:
            if (
                    "password required pam_pwhistory.so remember=5" in outputOne or
                    int(outputOne[-1]) >= 5
            ):
                self.Compliant("Ensure password reuse is limited (Scored)")
            else:
                self.NotCompliant("Ensure password reuse is limited (Scored)")
        except:
            self.NotCompliant("Ensure password reuse is limited (Scored)")

    def passhashing_5_3_4(self):
        cmdOne = r"""grep -E '^\s*password\s+(\S+\s+)+pam_unix\.so\s+(\S+\s+)*sha512\s*(\S+\s*)*(\s+#.*)?$ ' /etc/pam.d/common-password """
        outputOne = self.caller(cmdOne)

        if (
                "sha512" in outputOne
        ):
            self.Compliant("Ensure password hashing algorithm is SHA-512 (Scored)")
        else:
            self.NotCompliant("Ensure password hashing algorithm is SHA-512 (Scored)")

    def passexp_5_4_1_1(self):
        cmdOne = r"grep PASS_MAX_DAYS /etc/login.defs"
        outputOne = self.caller(cmdOne)

        days = int(outputOne.split("\n")[1].split("\t")[1])
        if (
                days <= 365
        ):
            self.Compliant("Ensure password expiration is 365 days or less (Scored)")
        else:
            self.NotCompliant("Ensure password expiration is 365 days or less (Scored)")

    def passmindays_5_4_1_2(self):
        cmdOne = r"grep PASS_MIN_DAYS /etc/login.defs"
        outputOne = self.caller(cmdOne)

        days = int(outputOne.split("\n")[1].split("\t")[1])

        if (
                days >= 1
        ):
            self.Compliant("Ensure minimum days between password changes is configured (Scored)")
        else:
            self.NotCompliant("Ensure minimum days between password changes is configured (Scored)")

    def passexpwarn_5_4_1_3(self):
        cmdOne = r"grep PASS_WARN_AGE /etc/login.defs"
        outputOne = self.caller(cmdOne)

        days = int(outputOne.split("\n")[1].split("\t")[1])

        if (
                days >= 7
        ):
            self.Compliant("Ensure password expiration warning days is 7 or more (Scored)")
        else:
            self.NotCompliant("Ensure password expiration warning days is 7 or more (Scored)")

    def inactivepass_5_4_1_4(self):
        cmdOne = r"useradd -D | grep INACTIVE"
        outputOne = self.caller(cmdOne)

        try:
            days = int(outputOne.split("=")[1])
            if (days <= 30):
                self.Compliant("Ensure inactive password lock is 30 days or less (Scored)")
            else:
                self.NotCompliant("Ensure inactive password lock is 30 days or less (Scored)")
        except:
            self.NotCompliant("Ensure inactive password lock is 30 days or less (Scored)")

    def lastpasschange_5_4_1_5(self):
        cmdOne = r"""for usr in $(cut -d: -f1 /etc/shadow); do [[ $(chage --list $usr | grep '^Last password change' | cut -d: -f2) > $(date) ]] && echo "$usr :$(chage --list $usr | grep '^Last password change' | cut -d: -f2)"; done"""
        outputOne = self.caller(cmdOne)

        if (
                outputOne == ""
        ):
            self.Compliant("Ensure all users last password change date is in the past (Scored)")
        else:
            self.NotCompliant("Ensure all users last password change date is in the past (Scored)")

    def sysaccs_5_4_2(self):
        cmdOne = r"""awk -F: '($1!="root" && $1!="sync" && $1!="shutdown" && $1!="halt" && $1!~/^\+/ && $3<'"$(awk '/^\s*UID_MIN/{print $2}' /etc/login.defs)"' && $7!="'"$(which nologin)"'" && $7!="/bin/false") {print}' /etc/passwd """
        cmdTwo = r"""awk -F: '($1!="root" && $1!~/^\+/ && $3<'"$(awk '/^\s*UID_MIN/{print $2}' /etc/login.defs)"') {print $1}' /etc/passwd | xargs -I '{}' passwd -S '{}' | awk '($2!="L" && $2!="LK") {print $1}' """

        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                outputOne == "" and
                outputTwo == ""
        ):
            self.Compliant("Ensure system accounts are secured (Scored)")
        else:
            self.NotCompliant("Ensure system accounts are secured (Scored)")

    def defgroupid_5_4_3(self):
        cmdOne = r"""grep "^root:" /etc/passwd | cut -f4 -d:"""
        outputOne = self.caller(cmdOne)

        if (
                "0" in outputOne
        ):
            self.Compliant("Ensure default group for the root account is GID 0 (Scored)")
        else:
            self.NotCompliant("Ensure default group for the root account is GID 0 (Scored)")

    def umask_5_4_4(self):
        cmdOne = r"""grep "umask" /etc/bash.bashrc"""
        cmdTwo = r"""grep "umask" /etc/profile /etc/profile.d/*.sh"""
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        try:
            perm = int(outputOne.split(" ")[1])
            perm2 = int(outputTwo.split("")[1])
            if (
                    perm >= 27 or
                    perm2 >= 27
            ):
                self.Compliant("Ensure default user umask is 027 or more restrictive (Scored)")
            else:
                self.NotCompliant("Ensure default user umask is 027 or more restrictive (Scored)")

        except:
            self.NotCompliant("Ensure default user umask is 027 or more restrictive (Scored)")

    def shelltimeout_5_4_5(self):
        cmdOne = r"""grep "^TMOUT" /etc/bash.bashrc """
        cmdTwo = r"""grep "^TMOUT" /etc/profile /etc/profile.d/*.sh """
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                "TMOUT=900" in outputOne and
                "TMOUT=900" in outputTwo
        ):
            self.Compliant("Ensure default user shell timeout is 900 seconds or less (Scored)")
        else:
            self.NotCompliant("Ensure default user shell timeout is 900 seconds or less (Scored)")

    def sucmd_5_6(self):
        cmdOne = r"grep pam_wheel.so /etc/pam.d/su"
        outputOne = self.caller(cmdOne)

        if (
                "auth required pam_wheel.so use_uid group=" in outputOne
        ):
            self.Compliant("Ensure access to the su command is restricted (Scored)")
        else:
            self.NotCompliant("Ensure access to the su command is restricted (Scored)")

    def passwdperm_6_1_2(self):
        cmdOne = r"stat /etc/passwd"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/passwd are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/passwd are configured (Scored)")

    def gshadowperm_6_1_3(self):
        cmdOne = r"stat /etc/gshadow-"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0640/-rw-r-----)  Uid: (    0/    root)   Gid: (    0/    root)"
        ):
            self.Compliant("Ensure permissions on /etc/gshadow- are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/gshadow- are configured (Scored)")

    def shadowperm_6_1_4(self):
        cmdOne = r"stat /etc/shadow"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0640/-rw-r-----)  Uid: (    0/    root)   Gid: (   42/  shadow)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/shadow are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/shadow are configured (Scored)")

    def groupperm_6_1_5(self):
        cmdOne = r"stat /etc/group"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/group are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/group are configured (Scored)")

    def etcpasswdperm_6_1_6(self):
        cmdOne = r"stat /etc/passwd-"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/passwd- are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/passwd- are configured (Scored)")

    def etcshadow_6_1_7(self):
        cmdOne = r"stat /etc/shadow-"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (   42/  shadow)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/shadow- are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/shadow- are configured (Scored)")

    def etcgroup_6_1_8(self):
        cmdOne = r"stat /etc/group-"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/group- are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/group- are configured (Scored)")

    def etcgshadow_6_1_9(self):
        cmdOne = r"stat /etc/gshadow"
        outputOne = self.caller(cmdOne)

        if (
                "Access: (0640/-rw-r-----)  Uid: (    0/    root)   Gid: (   42/  shadow)" in outputOne
        ):
            self.Compliant("Ensure permissions on /etc/gshadow are configured (Scored)")
        else:
            self.NotCompliant("Ensure permissions on /etc/gshadow are configured (Scored)")

    def wwfiles_6_1_10(self):
        cmdOne = r"df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type f -perm -0002"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no world writable files exist (Scored)")
        else:
            self.NotCompliant("Ensure no world writable files exist (Scored)")

    def unowned_6_1_11(self):
        cmdOne = r"df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nouser"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no unowned files or directories exist (Scored)")
        else:
            self.NotCompliant("Ensure no unowned files or directories exist (Scored)")

    def ungrouped_6_1_12(self):
        cmdOne = r"df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -nogroup"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no ungrouped files or directories exist (Scored)")

        else:
            self.NotCompliant("Ensure no ungrouped files or directories exist (Scored)")

    def passwdnotempty_6_2_1(self):
        cmdOne = r"""awk -F: '($2 == "" ) { print $1 " does not have a password "}' /etc/shadow """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure password fields are not empty (Scored)")
        else:
            self.NotCompliant("Ensure password fields are not empty (Scored)")

    def nolegacy_6_2_2(self):
        cmdOne = r"grep '^\+:' /etc/passwd"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no legacy \"+\" entries exist in /etc/passwd (Scored)")
        else:
            self.NotCompliant("Ensure no legacy \"+\" entries exist in /etc/passwd (Scored)")

    def userhome_6_2_3(self):
        cmdOne = r"""
            #!/bin/bash
            grep -E -v '^(halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read -r user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            fi
            done
        """

        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure all users' home directories exist (Scored)")
        else:
            self.NotCompliant("Ensure all users' home directories exist (Scored)")

    def nolegacy_6_2_4(self):
        cmdOne = r"grep '^\+:' /etc/shadow"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no legacy \"+\" entries exist in /etc/shadow (Scored)")
        else:
            self.NotCompliant("Ensure no legacy \"+\" entries exist in /etc/shadow (Scored)")

    def nolegacygroup_6_2_5(self):
        cmdOne = r"grep '^\+:' /etc/group"
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure no legacy \"+\" entries exist in /etc/group (Scored)")
        else:
            self.NotCompliant("Ensure no legacy \"+\" entries exist in /etc/group (Scored)")

    def rootuid_6_2_6(self):
        cmdOne = r"awk -F: '($3 == 0) { print $1 }' /etc/passwd"
        outputOne = self.caller(cmdOne)

        if (
                "root" in outputOne
        ):
            self.Compliant("Ensure root is the only UID 0 account (Scored)")
        else:
            self.NotCompliant("Ensure root is the only UID 0 account (Scored)")

    def rootpathintegrity_6_2_7(self):
        cmdOne = r"""
            #!/bin/bash
            if echo $PATH | grep -q "::" ; then
                echo "Empty Directory in PATH (::)"
            fi
            if echo $PATH | grep -q ":$" ; then
                echo "Trailing : in PATH"
            fi
            for x in $(echo $PATH | tr ":" " ") ; do
                if [ -d "$x" ] ; then
                    ls -ldH "$x" | awk '
                $9 == "." {print "PATH contains current working directory (.)"}
                $3 != "root" {print $9, "is not owned by root"}
            substr($1,6,1) != "-" {print $9, "is group writable"}
            substr($1,9,1) != "-" {print $9, "is world writable"}'
                else
                    echo "$x is not a directory"
                fi
            done
        """
        outputOne = self.caller(cmdOne)
        if (
                outputOne == "" or
                len(outputOne) == 0
        ):
            self.Compliant("Ensure root PATH Integrity (Scored)")

        else:
            self.NotCompliant("Ensure root PATH Integrity (Scored)")

    def userhomeperm_6_2_8(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                dirperm=$(ls -ld $dir | cut -f1 -d" ")
                if [ $(echo $dirperm | cut -c6) != "-" ]; then
                    echo "Group Write permission set on the home directory ($dir) of user $user"
                fi
                if [ $(echo $dirperm | cut -c8) != "-" ]; then
                echo "Other Read permission set on the home directory ($dir) of user $user"
                fi
                if [ $(echo $dirperm | cut -c9) != "-" ]; then
                    echo "Other Write permission set on the home directory ($dir) of user $user"
                fi
                if [ $(echo $dirperm | cut -c10) != "-" ]; then
                    echo "Other Execute permission set on the home directory ($dir) of user $user"
                fi
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure users' home directories permissions are 750 or more restrictive (Scored)")
        else:
            self.NotCompliant("Ensure users' home directories permissions are 750 or more restrictive (Scored)")

    def usershome_6_2_9(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                owner=$(stat -L -c "%U" "$dir")
            if [ "$owner" != "$user" ]; then
                echo "The home directory ($dir) of user $user is owned by $owner."
            fi
        fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure users own their home directories (Scored)")
        else:
            self.NotCompliant("Ensure users own their home directories (Scored)")

    def userdotfile_6_2_10(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                for file in $dir/.[A-Za-z0-9]*; do
                    if [ ! -h "$file" -a -f "$file" ]; then
                        fileperm=$(ls -ld $file | cut -f1 -d" ")
                        if [ $(echo $fileperm | cut -c6) != "-" ]; then
                            echo "Group Write permission set on file $file"
                        fi
                        if [ $(echo $fileperm | cut -c9) != "-" ]; then
                            echo "Other Write permission set on file $file"
                        fi
                    fi
                done
            fi
        done
        """

        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure users' dot files are not group or world writable (Scored)")
        else:
            self.NotCompliant("Ensure users' dot files are not group or world writable (Scored)")

    def nouserforward_6_2_11(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(root|halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                if [ ! -h "$dir/.forward" -a -f "$dir/.forward" ]; then
                    echo ".forward file $dir/.forward exists"
                fi
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no users have .forward files (Scored)")
        else:
            self.NotCompliant("Ensure no users have .forward files (Scored)")

    def nousernetrc_6_2_12(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(root|halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                if [ ! -h "$dir/.netrc" -a -f "$dir/.netrc" ]; then
                    echo ".netrc file $dir/.netrc exists"
                fi
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no users have .netrc files (Scored)")
        else:
            self.NotCompliant("Ensure no users have .netrc files (Scored)")

    def usernetrc_6_2_13(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(root|halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                for file in $dir/.netrc; do
                    if [ ! -h "$file" -a -f "$file" ]; then
                        fileperm=$(ls -ld $file | cut -f1 -d" ")
                        if [ $(echo $fileperm | cut -c5) != "-" ]; then
                            echo "Group Read set on $file"
                        fi
                        if [ $(echo $fileperm | cut -c6) != "-" ]; then
                            echo "Group Write set on $file"
                        fi
                        if [ $(echo $fileperm | cut -c7) != "-" ]; then
                            echo "Group Execute set on $file"
                        fi
                        if [ $(echo $fileperm | cut -c8) != "-" ]; then
                            echo "Other Read set on $file"
                        fi
                        if [ $(echo $fileperm | cut -c9) != "-" ]; then
                            echo "Other Write set on $file"
                        fi
                        if [ $(echo $fileperm | cut -c10) != "-" ]; then
                            echo "Other Execute set on $file"
                        fi
                    fi
                done
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure users' .netrc Files are not group or world accessible (Scored)")
        else:
            self.NotCompliant("Ensure users' .netrc Files are not group or world accessible (Scored)")

    def nouserrhosts_6_2_14(self):
        cmdOne = r"""
        #!/bin/bash
        grep -E -v '^(root|halt|sync|shutdown)' /etc/passwd | awk -F: '($7 != "'"$(which nologin)"'" && $7 != "/bin/false") { print $1 " " $6 }' | while read user dir; do
            if [ ! -d "$dir" ]; then
                echo "The home directory ($dir) of user $user does not exist."
            else
                for file in $dir/.rhosts; do
                    if [ ! -h "$file" -a -f "$file" ]; then
                        echo ".rhosts file in $dir"
                    fi
                done
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no users have .rhosts files (Scored)")
        else:
            self.NotCompliant("Ensure no users have .rhosts files (Scored)")

    def groupsetcpasswd_6_2_15(self):
        cmdOne = r"""
        #!/bin/bash
        for i in $(cut -s -d: -f4 /etc/passwd | sort -u); do
            grep -q -P "^.*?:[^:]*:$i:" /etc/group
            if [ $? -ne 0 ]; then
                echo "Group $i is referenced by /etc/passwd but does not exist in
        /etc/group"
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure all groups in /etc/passwd exist in /etc/group (Scored)")
        else:
            self.NotCompliant("Ensure all groups in /etc/passwd exist in /etc/group (Scored)")

    def noduplicateuid_6_2_16(self):
        cmdOne = r"""
        #!/bin/bash
        cut -f3 -d":" /etc/passwd | sort -n | uniq -c | while read x; do
            [ -z "$x" ] && break
            set - $x
            if [ $1 -gt 1 ]; then
                users=$(awk -F: '($3 == n) { print $1 }' n=$2 /etc/passwd | xargs)
                echo "Duplicate UID ($2): $users"
            fi
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no duplicate UIDs exist (Scored)")
        else:
            self.NotCompliant("Ensure no duplicate UIDs exist (Scored)")

    def noduplicategid_6_2_17(self):
        cmdOne = r"""
        #!/bin/bash
        cut -d: -f3 /etc/group | sort | uniq -d | while read x; do
            echo "Duplicate GID ($x) in /etc/group"
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no duplicate GIDs exist (Scored)")
        else:
            self.NotCompliant("Ensure no duplicate GIDs exist (Scored)")

    def noduplicateusernames_6_2_18(self):
        cmdOne = r"""
        #!/bin/bash
        cut -d: -f1 /etc/passwd | sort | uniq -d | while read x; do
            echo "Duplicate login name ${x} in /etc/passwd"
        done
        """

        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no duplicate user names exist (Scored)")
        else:
            self.NotCompliant("Ensure no duplicate user names exist (Scored)")

    def noduplicategroupname_6_2_19(self):
        cmdOne = r"""
        #!/bin/bash
        cut -d: -f1 /etc/group | sort | uniq -d | while read x; do
            echo "Duplicate group name ${x} in /etc/group"
        done
        """
        outputOne = self.caller(cmdOne)

        if (
                outputOne == "" or
                len(outputOne) <= 2
        ):
            self.Compliant("Ensure no duplicate group names exist (Scored)")
        else:
            self.NotCompliant("Ensure no duplicate group names exist (Scored)")

    def emptyshadow_6_2_20(self):
        cmdOne = r"grep ^shadow:[^:]*:[^:]*:[^:]+ /etc/group"
        cmdTwo = r"""awk -F: '($4 == "<shadow-gid>") { print }' /etc/passwd"""
        outputOne = self.caller(cmdOne)
        outputTwo = self.caller(cmdTwo)

        if (
                (
                        outputOne == "" or
                        len(outputOne) <= 2
                ) and
                (
                        outputTwo == "" or
                        len(outputTwo) <= 2
                )
        ):
            self.Compliant("Ensure shadow group is empty (Scored)")
        else:
            self.NotCompliant("Ensure shadow group is empty (Scored)")
