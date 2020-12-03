import os
import win32com.shell.shell as shell

# Checks if potentially outdated report already exists 
# if os.path.exists("group-policy.inf"):
#   os.remove("group-policy.inf")

# Generates new GP report 
# command = 'D: && cd Work\Capstone\oscarQ\OSCRQ && secedit /export /cfg group-policy2.inf /log export.log'
# shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)


policyRep = open('group-policy.inf','rb')
RepRead = policyRep.read()
GPR = RepRead.decode('utf-16')
GPRsplit = GPR.split()

COMPLIANT = []
NONCOMPLIANT = []
NOTCONFIGURED = []
# for idx, word in enumerate(GPRsplit):
#     if (GPRsplit[idx] == "LockoutBadCount"):
#         print(GPRsplit[idx+2])
# print(GPRsplit.find("LockoutBadCount"))

# 1.1.1 (L1) Ensure 'Enforce password history' is set to '24 or more
# password(s)' (Automated)
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "PasswordHistorySize"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 24:
            COMPLIANT.append("PasswordHistorySize")
        else:
            NONCOMPLIANT.append("PasswordHistorySize")
        break
if(found == 0):
    NONCOMPLIANT.append("PasswordHistorySize")
    NOTCONFIGURED.append("PasswordHistorySize")


# 1.1.2 (L1) Ensure 'Maximum password age' is set to '60 or fewer days,
# but not 0' (Automated)
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MaximumPasswordAge"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal <= 60:
            COMPLIANT.append("MaximumPasswordAge")
        else:
            NONCOMPLIANT.append("MaximumPasswordAge")
        break
if(found == 0):
    NONCOMPLIANT.append("MaximumPasswordAge")
    NOTCONFIGURED.append("MaximumPasswordAge")

# 1.1.3 (L1) Ensure 'Minimum password age' is set to '1 or more day(s)'
# (Automated)
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MinimumPasswordAge"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 1:
            COMPLIANT.append("MinimumPasswordAge")
        else:
            NONCOMPLIANT.append("MinimumPasswordAge")
        break
if(found == 0):
    NONCOMPLIANT.append("MinimumPasswordAge")
    NOTCONFIGURED.append("MinimumPasswordAge")

# 1.1.4 (L1) Ensure 'Minimum password length' is set to '14 or more
# character(s)' (Automated)
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MinimumPasswordLength"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 14:
            COMPLIANT.append("MinimumPasswordLength")
        else:
            NONCOMPLIANT.append("MinimumPasswordLength")
        break
if(found == 0):
    NONCOMPLIANT.append("MinimumPasswordLength")
    NOTCONFIGURED.append("MinimumPasswordLength")

# 1.1.5 (L1) Ensure 'Password must meet complexity requirements' is set
# to 'Enabled' (Automated)
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "PasswordComplexity"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal == 1:
            COMPLIANT.append("PasswordComplexity")
        else:
            NONCOMPLIANT.append("PasswordComplexity")
        break
if(found == 0):
    NONCOMPLIANT.append("PasswordComplexity")
    NOTCONFIGURED.append("PasswordComplexity")


# 1.1.6 (L1) Ensure 'Relax minimum password length limits' is set to
# 'Enabled' (Automated)

# MACHINE\System\CurrentControlSet\Control\SAM\RelaxMinimumPasswordLengthLimits=4,1

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "RelaxMinimumPasswordLengthLimits"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal == 1:
            COMPLIANT.append("RelaxMinimumPasswordLengthLimits")
        else:
            NONCOMPLIANT.append("RelaxMinimumPasswordLengthLimits")
        break
    else:
        pathStr = GPRsplit[idx]
        if (pathStr[0:7] == "MACHINE"):
            # pathStr.split('\)
            print(pathStr)
            break
if(found == 0):
    NONCOMPLIANT.append("RelaxMinimumPasswordLengthLimits")
    NOTCONFIGURED.append("RelaxMinimumPasswordLengthLimits")

# 1.1.7 (L1) Ensure 'Store passwords using reversible encryption' is set to
# 'Disabled' (Automated)

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "ClearTextPassword"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal == 0:
            COMPLIANT.append("ClearTextPassword")
        else:
            NONCOMPLIANT.append("ClearTextPassword")
        break
if(found == 0):
    NONCOMPLIANT.append("ClearTextPassword")
    NOTCONFIGURED.append("ClearTextPassword")

# 1.2.1 (L1) Ensure 'Account lockout duration' is set to '15 or more
# minute(s)' (Automated)

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "LockoutDuration"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 15:
            COMPLIANT.append("LockoutDuration")
        else:
            NONCOMPLIANT.append("LockoutDuration")
        break
if(found == 0):
    NONCOMPLIANT.append("LockoutDuration")
    NOTCONFIGURED.append("LockoutDuration")

# 1.2.2 (L1) Ensure 'Account lockout threshold' is set to '10 or fewer
# invalid logon attempt(s), but not 0' (Automated)

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "LockoutBadCount"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 1 and benchVal <=10:
            COMPLIANT.append("LockoutBadCount")
        else:
            NONCOMPLIANT.append("LockoutBadCount")
        break
if(found == 0):
    NONCOMPLIANT.append("LockoutBadCount")
    NOTCONFIGURED.append("LockoutBadCount")

# 1.2.3 (L1) Ensure 'Reset account lockout counter after' is set to '15 or
# more minute(s)' (Automated)

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "ResetLockoutCount"):
        found = 1
        benchVal = int(GPRsplit[idx+2])
        if benchVal >= 15:
            COMPLIANT.append("ResetLockoutCount")
        else:
            NONCOMPLIANT.append("ResetLockoutCount")
        break
if(found == 0):
    NONCOMPLIANT.append("ResetLockoutCount")
    NOTCONFIGURED.append("ResetLockoutCount")

# Local Policies

# https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
# S-1-0	Null Authority
# S-1-1-0	Everyone
# S-1-0-0	Nobody
# S-1-5-32-544	Administrators
# S-1-5-32-545	Users
# S-1-5-32-551	Backup Operators
# S-1-5-19	NT Authority	Local Service
# S-1-5-20	NT Authority	Network Service
# S-1-5-32-555	Builtin\Remote Desktop Users
# S-1-5-6	Service
# S-1-5-32-546	Guests
# S-1-5-18	Local System
# S-1-5-90-0	Windows Manager\Windows Manager Group
# S-1-5-32-559	Builtin\Performance Log Users
# S-1-5-83-0	NT Virtual Machine\Virtual Machines

# 2.2.1 (L1) Ensure 'Access Credential Manager as a trusted caller' is set to
# 'No One' (Automated)

# SeTrustedCredManAccessPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeTrustedCredManAccessPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeTrustedCredManAccessPrivilege")
        else:
            NONCOMPLIANT.append("SeTrustedCredManAccessPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeTrustedCredManAccessPrivilege")
    NOTCONFIGURED.append("SeTrustedCredManAccessPrivilege")

# 2.2.2 (L1) Ensure 'Access this computer from the network' is set to
# 'Administrators, Remote Desktop Users' (Automated)

# SeNetworkLogonRight = *S-1-5-32-544,*S-1-5-32-555

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeNetworkLogonRight"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544,*S-1-5-32-555":
            COMPLIANT.append("SeNetworkLogonRight")
        else:
            NONCOMPLIANT.append("SeNetworkLogonRight")
        break
if(found == 0):
    NONCOMPLIANT.append("SeNetworkLogonRight")
    NOTCONFIGURED.append("SeNetworkLogonRight")

# 2.2.3 (L1) Ensure 'Act as part of the operating system' is set to 'No One'
# (Automated)

# SeTcbPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeTcbPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeTcbPrivilege")
        else:
            NONCOMPLIANT.append("SeTcbPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeTcbPrivilege")
    NOTCONFIGURED.append("SeTcbPrivilege")

# 2.2.4 (L1) Ensure 'Adjust memory quotas for a process' is set to
# 'Administrators, LOCAL SERVICE, NETWORK SERVICE' (Automated)

# SeIncreaseQuotaPrivilege

# 2.2.5 (L1) Ensure 'Allow log on locally' is set to 'Administrators, Users'
# (Automated)

# SeInteractiveLogonRight

# 2.2.6 (L1) Ensure 'Allow log on through Remote Desktop Services' is set
# to 'Administrators, Remote Desktop Users' (Automated)

# SeRemoteInteractiveLogonRight

# 2.2.7 (L1) Ensure 'Back up files and directories' is set to 'Administrators'
# (Automated)

# SeBackupPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeBackupPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeBackupPrivilege")
        else:
            NONCOMPLIANT.append("SeBackupPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeBackupPrivilege")
    NOTCONFIGURED.append("SeBackupPrivilege")

# 2.2.8 (L1) Ensure 'Change the system time' is set to 'Administrators,
# LOCAL SERVICE' (Automated)

# SeSystemtimePrivilege

# 2.2.9 (L1) Ensure 'Change the time zone' is set to 'Administrators, LOCAL
# SERVICE, Users' (Automated)

# SeTimeZonePrivilege

# 2.2.10 (L1) Ensure 'Create a pagefile' is set to 'Administrators'
# (Automated)

# SeCreatePagefilePrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeCreatePagefilePrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeCreatePagefilePrivilege")
        else:
            NONCOMPLIANT.append("SeCreatePagefilePrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeCreatePagefilePrivilege")
    NOTCONFIGURED.append("SeCreatePagefilePrivilege")

# 2.2.11 (L1) Ensure 'Create a token object' is set to 'No One' (Automated)

# SeCreateTokenPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeCreateTokenPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeCreateTokenPrivilege")
        else:
            NONCOMPLIANT.append("SeCreateTokenPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeCreateTokenPrivilege")
    NOTCONFIGURED.append("SeCreateTokenPrivilege")

# 2.2.12 (L1) Ensure 'Create global objects' is set to 'Administrators,
# LOCAL SERVICE, NETWORK SERVICE, SERVICE' (Automated)

# SeCreateGlobalPrivilege

# 2.2.13 (L1) Ensure 'Create permanent shared objects' is set to 'No One'
# (Automated)

# SeCreatePermanentPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeCreatePermanentPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeCreatePermanentPrivilege")
        else:
            NONCOMPLIANT.append("SeCreatePermanentPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeCreatePermanentPrivilege")
    NOTCONFIGURED.append("SeCreatePermanentPrivilege")

# 2.2.14 (L1) Configure 'Create symbolic links' (Automated)

# SeCreateSymbolicLinkPrivilege

# 2.2.15 (L1) Ensure 'Debug programs' is set to 'Administrators'
# (Automated)

# SeDebugPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeDebugPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeDebugPrivilege")
        else:
            NONCOMPLIANT.append("SeDebugPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeDebugPrivilege")
    NOTCONFIGURED.append("SeDebugPrivilege")

# 2.2.16 (L1) Ensure 'Deny access to this computer from the network' to
# include 'Guests, Local account' (Automated)

# SeDenyNetworkLogonRight

# 2.2.17 (L1) Ensure 'Deny log on as a batch job' to include 'Guests'
# (Automated)

# SeDenyBatchLogonRight

# 2.2.18 (L1) Ensure 'Deny log on as a service' to include 'Guests'
# (Automated)

# SeDenyServiceLogonRight

# 2.2.19 (L1) Ensure 'Deny log on locally' to include 'Guests' (Automated)

# SeDenyInteractiveLogonRight

# 2.2.20 (L1) Ensure 'Deny log on through Remote Desktop Services' to
# include 'Guests, Local account' (Automated)

# SeDenyRemoteInteractiveLogonRight

# 2.2.21 (L1) Ensure 'Enable computer and user accounts to be trusted for
# delegation' is set to 'No One' (Automated)

# SeEnableDelegationPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeEnableDelegationPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeEnableDelegationPrivilege")
        else:
            NONCOMPLIANT.append("SeEnableDelegationPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeEnableDelegationPrivilege")
    NOTCONFIGURED.append("SeEnableDelegationPrivilege")

# 2.2.22 (L1) Ensure 'Force shutdown from a remote system' is set to
# 'Administrators' (Automated)

# SeRemoteShutdownPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeRemoteShutdownPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeRemoteShutdownPrivilege")
        else:
            NONCOMPLIANT.append("SeRemoteShutdownPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeRemoteShutdownPrivilege")
    NOTCONFIGURED.append("SeRemoteShutdownPrivilege")

# 2.2.23 (L1) Ensure 'Generate security audits' is set to 'LOCAL SERVICE,
# NETWORK SERVICE' (Automated)

# SeAuditPrivilege

# 2.2.24 (L1) Ensure 'Impersonate a client after authentication' is set to
# 'Administrators, LOCAL SERVICE, NETWORK SERVICE, SERVICE'
# (Automated)

# SeImpersonatePrivilege

# 2.2.25 (L1) Ensure 'Increase scheduling priority' is set to 'Administrators,
# Window Manager\Window Manager Group' (Automated)

# SeIncreaseBasePriorityPrivilege

# 2.2.26 (L1) Ensure 'Load and unload device drivers' is set to
# 'Administrators' (Automated)

# SeLoadDriverPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeLoadDriverPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeLoadDriverPrivilege")
        else:
            NONCOMPLIANT.append("SeLoadDriverPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeLoadDriverPrivilege")
    NOTCONFIGURED.append("SeLoadDriverPrivilege")

# 2.2.27 (L1) Ensure 'Lock pages in memory' is set to 'No One'
# (Automated)

# SeLockMemoryPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeLockMemoryPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeLockMemoryPrivilege")
        else:
            NONCOMPLIANT.append("SeLockMemoryPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeLockMemoryPrivilege")
    NOTCONFIGURED.append("SeLockMemoryPrivilege")

# 2.2.28 (L2) Ensure 'Log on as a batch job' is set to 'Administrators'
# (Automated)

# SeBatchLogonRight = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeBatchLogonRight"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeBatchLogonRight")
        else:
            NONCOMPLIANT.append("SeBatchLogonRight")
        break
if(found == 0):
    NONCOMPLIANT.append("SeBatchLogonRight")
    NOTCONFIGURED.append("SeBatchLogonRight")

# 2.2.29 (L2) Configure 'Log on as a service' (Automated)

# SeServiceLogonRight

# 2.2.30 (L1) Ensure 'Manage auditing and security log' is set to
# 'Administrators' (Automated)

# SeSecurityPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeSecurityPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeSecurityPrivilege")
        else:
            NONCOMPLIANT.append("SeSecurityPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeSecurityPrivilege")
    NOTCONFIGURED.append("SeSecurityPrivilege")

# 2.2.31 (L1) Ensure 'Modify an object label' is set to 'No One'
# (Automated)

# SeRelabelPrivilege = *S-1-0-0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeRelabelPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-0-0":
            COMPLIANT.append("SeRelabelPrivilege")
        else:
            NONCOMPLIANT.append("SeRelabelPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeRelabelPrivilege")
    NOTCONFIGURED.append("SeRelabelPrivilege")

# 2.2.32 (L1) Ensure 'Modify firmware environment values' is set to
# 'Administrators' (Automated)

# SeSystemEnvironmentPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeSystemEnvironmentPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeSystemEnvironmentPrivilege")
        else:
            NONCOMPLIANT.append("SeSystemEnvironmentPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeSystemEnvironmentPrivilege")
    NOTCONFIGURED.append("SeSystemEnvironmentPrivilege")


# 2.2.33 (L1) Ensure 'Perform volume maintenance tasks' is set to
# 'Administrators' (Automated)

# SeManageVolumePrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeManageVolumePrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeManageVolumePrivilege")
        else:
            NONCOMPLIANT.append("SeManageVolumePrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeManageVolumePrivilege")
    NOTCONFIGURED.append("SeManageVolumePrivilege")

# 2.2.34 (L1) Ensure 'Profile single process' is set to 'Administrators'
# (Automated)

# SeProfileSingleProcessPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeProfileSingleProcessPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeProfileSingleProcessPrivilege")
        else:
            NONCOMPLIANT.append("SeProfileSingleProcessPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeProfileSingleProcessPrivilege")
    NOTCONFIGURED.append("SeProfileSingleProcessPrivilege")

# 2.2.35 (L1) Ensure 'Profile system performance' is set to 'Administrators,
# NT SERVICE\WdiServiceHost' (Automated)

# SeSystemProfilePrivilege

# 2.2.36 (L1) Ensure 'Replace a process level token' is set to 'LOCAL
# SERVICE, NETWORK SERVICE' (Automated)

# SeAssignPrimaryTokenPrivilege

# 2.2.37 (L1) Ensure 'Restore files and directories' is set to 'Administrators'
# (Automated)

# SeRestorePrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeRestorePrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeRestorePrivilege")
        else:
            NONCOMPLIANT.append("SeRestorePrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeRestorePrivilege")
    NOTCONFIGURED.append("SeRestorePrivilege")

# 2.2.38 (L1) Ensure 'Shut down the system' is set to 'Administrators,
# Users' (Automated)

# SeShutdownPrivilege

# 2.2.39 (L1) Ensure 'Take ownership of files or other objects' is set to
# 'Administrators' (Automated)

# SeTakeOwnershipPrivilege = *S-1-5-32-544

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "SeTakeOwnershipPrivilege"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "*S-1-5-32-544":
            COMPLIANT.append("SeTakeOwnershipPrivilege")
        else:
            NONCOMPLIANT.append("SeTakeOwnershipPrivilege")
        break
if(found == 0):
    NONCOMPLIANT.append("SeTakeOwnershipPrivilege")
    NOTCONFIGURED.append("SeTakeOwnershipPrivilege")

# Security Options

# 2.3.1.1 (L1) Ensure 'Accounts: Administrator account status' is set to
# 'Disabled' (Automated)
# EnableAdminAccount = 0

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "EnableAdminAccount"):
        found = 1
        benchVal = GPRsplit[idx+2]
        if benchVal == "0":
            COMPLIANT.append("EnableAdminAccount")
        else:
            NONCOMPLIANT.append("EnableAdminAccount")
        break
if(found == 0):
    NONCOMPLIANT.append("EnableAdminAccount")
    NOTCONFIGURED.append("EnableAdminAccount")

# 2.3.1.2 (L1) Ensure 'Accounts: Block Microsoft accounts' is set to 'Users
# can't add or log on with Microsoft accounts' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\NoConnectedUser=4,3

for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\NoConnectedUser=4,3"):
        found = 1
        COMPLIANT.append("NoConnectedUser")
        break
if(found == 0):
    NONCOMPLIANT.append("NoConnectedUser")
    NOTCONFIGURED.append("NoConnectedUser")

# 2.3.1.3 (L1) Ensure 'Accounts: Guest account status' is set to 'Disabled'
# (Automated)
EnableGuestAccount = 0
# 2.3.1.4 (L1) Ensure 'Accounts: Limit local account use of blank
# passwords to console logon only' is set to 'Enabled' (Automated)

# MACHINE\System\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse=4,1"):
        found = 1
        COMPLIANT.append("LimitBlankPasswordUse")
        break
if(found == 0):
    NONCOMPLIANT.append("LimitBlankPasswordUse")
    NOTCONFIGURED.append("LimitBlankPasswordUse")

# 2.3.1.5 (L1) Configure 'Accounts: Rename administrator account'
# (Automated)
NewAdministratorName = "Administrator"
# 2.3.1.6 (L1) Configure 'Accounts: Rename guest account' (Automated)
NewGuestName = "Guest"

# 2.3.2 Audit

# 2.3.2.1 (L1) Ensure 'Audit: Force audit policy subcategory settings
# (Windows Vista or later) to override audit policy category settings' is set
# to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy=4,1"):
        found = 1
        COMPLIANT.append("SCENoApplyLegacyAuditPolicy")
        break
if(found == 0):
    NONCOMPLIANT.append("SCENoApplyLegacyAuditPolicy")
    NOTCONFIGURED.append("SCENoApplyLegacyAuditPolicy")

# MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy=4,1

# 2.3.2.2 (L1) Ensure 'Audit: Shut down system immediately if unable to
# log security audits' is set to 'Disabled' (Automated)

# MACHINE\System\CurrentControlSet\Control\Lsa\CrashOnAuditFail=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\CrashOnAuditFail=4,0"):
        found = 1
        COMPLIANT.append("CrashOnAuditFail")
        break
if(found == 0):
    NONCOMPLIANT.append("CrashOnAuditFail")
    NOTCONFIGURED.append("CrashOnAuditFail")

# 2.3.4 Devices

# 2.3.4.1 (L1) Ensure 'Devices: Allowed to format and eject removable
# media' is set to 'Administrators and Interactive Users' (Automated)
# MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\AllocateDASD=1,"2"
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == 'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\AllocateDASD=1,"2"'):
        found = 1
        COMPLIANT.append("AllocateDASD")
        break
if(found == 0):
    NONCOMPLIANT.append("AllocateDASD")
    NOTCONFIGURED.append("AllocateDASD")

# 2.3.4.2 (L2) Ensure 'Devices: Prevent users from installing printer drivers'
# is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Control\Print\Providers\LanMan Print Services\Servers\AddPrinterDrivers=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Print\Providers\LanMan Print Services\Servers\AddPrinterDrivers=4,1"):
        found = 1
        COMPLIANT.append("AddPrinterDrivers")
        break
if(found == 0):
    NONCOMPLIANT.append("AddPrinterDrivers")
    NOTCONFIGURED.append("AddPrinterDrivers")

# 2.3.6 Domain member

# 2.3.6.1 (L1) Ensure 'Domain member: Digitally encrypt or sign secure
# channel data (always)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal=4,1"):
        found = 1
        COMPLIANT.append("RequireSignOrSeal")
        break
if(found == 0):
    NONCOMPLIANT.append("RequireSignOrSeal")
    NOTCONFIGURED.append("RequireSignOrSeal")

# 2.3.6.2 (L1) Ensure 'Domain member: Digitally encrypt secure channel
# data (when possible)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\SealSecureChannel=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\SealSecureChannel=4,1"):
        found = 1
        COMPLIANT.append("SealSecureChannel")
        break
if(found == 0):
    NONCOMPLIANT.append("SealSecureChannel")
    NOTCONFIGURED.append("SealSecureChannel")

# 2.3.6.3 (L1) Ensure 'Domain member: Digitally sign secure channel data
# (when possible)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\SignSecureChannel=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\SignSecureChannel=4,1"):
        found = 1
        COMPLIANT.append("SignSecureChannel")
        break
if(found == 0):
    NONCOMPLIANT.append("SignSecureChannel")
    NOTCONFIGURED.append("SignSecureChannel")

# 2.3.6.4 (L1) Ensure 'Domain member: Disable machine account
# password changes' is set to 'Disabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\DisablePasswordChange=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\DisablePasswordChange=4,0"):
        found = 1
        COMPLIANT.append("DisablePasswordChange")
        break
if(found == 0):
    NONCOMPLIANT.append("DisablePasswordChange")
    NOTCONFIGURED.append("DisablePasswordChange")

# 2.3.6.5 (L1) Ensure 'Domain member: Maximum machine account
# password age' is set to '30 or fewer days, but not 0' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\MaximumPasswordAge=4,29
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\MaximumPasswordAge=4,29"):
        found = 1
        COMPLIANT.append("MaximumPasswordAge")
        break
if(found == 0):
    NONCOMPLIANT.append("MaximumPasswordAge")
    NOTCONFIGURED.append("MaximumPasswordAge")

# 2.3.6.6 (L1) Ensure 'Domain member: Require strong (Windows 2000 or
# later) session key' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireStrongKey=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireStrongKey=4,1"):
        found = 1
        COMPLIANT.append("RequireStrongKey")
        break
if(found == 0):
    NONCOMPLIANT.append("RequireStrongKey")
    NOTCONFIGURED.append("RequireStrongKey")

# 2.3.7 Interactive logon

# 2.3.7.1 (L1) Ensure 'Interactive logon: Do not require CTRL+ALT+DEL' is
# set to 'Disabled' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableCAD=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableCAD=4,0"):
        found = 1
        COMPLIANT.append("DisableCAD")
        break
if(found == 0):
    NONCOMPLIANT.append("DisableCAD")
    NOTCONFIGURED.append("DisableCAD")

# 2.3.7.2 (L1) Ensure 'Interactive logon: Don't display last signed-in' is set
# to 'Enabled' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\DontDisplayLastUserName=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\DontDisplayLastUserName=4,1"):
        found = 1
        COMPLIANT.append("DontDisplayLastUserName")
        break
if(found == 0):
    NONCOMPLIANT.append("DontDisplayLastUserName")
    NOTCONFIGURED.append("DontDisplayLastUserName")

# 2.3.7.3 (BL) Ensure 'Interactive logon: Machine account lockout
# threshold' is set to '10 or fewer invalid logon attempts, but not 0'
# (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\MaxDevicePasswordFailedAttempts=4,9

# Has to be configured 
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\MaxDevicePasswordFailedAttempts=4,9"):
        found = 1
        COMPLIANT.append("MaxDevicePasswordFailedAttempts")
        break
if(found == 0):
    NONCOMPLIANT.append("MaxDevicePasswordFailedAttempts")
    NOTCONFIGURED.append("MaxDevicePasswordFailedAttempts")

# 2.3.7.4 (L1) Ensure 'Interactive logon: Machine inactivity limit' is set to
# '900 or fewer second(s), but not 0' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\InactivityTimeoutSecs=4,899

# Need to reconfigure 
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\InactivityTimeoutSecs=4,899"):
        found = 1
        COMPLIANT.append("InactivityTimeoutSecs")
        break
if(found == 0):
    NONCOMPLIANT.append("InactivityTimeoutSecs")
    NOTCONFIGURED.append("InactivityTimeoutSecs")

# 2.3.7.5 (L1) Configure 'Interactive logon: Message text for users
# attempting to log on' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeText=7,Configured
# Caption can be anything, need to reconfigure test
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeText=7,Configured"):
        found = 1
        COMPLIANT.append("LegalNoticeText")
        break
if(found == 0):
    NONCOMPLIANT.append("LegalNoticeText")
    NOTCONFIGURED.append("LegalNoticeText")

# 2.3.7.6 (L1) Configure 'Interactive logon: Message title for users
# attempting to log on' (Automated)
# MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeCaption=1,"Configured"

# Caption can be anything, need to reconfigure test 
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == 'MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeCaption=1,"Configured"'):
        found = 1
        COMPLIANT.append("LegalNoticeCaption")
        break
if(found == 0):
    NONCOMPLIANT.append("LegalNoticeCaption")
    NOTCONFIGURED.append("LegalNoticeCaption")

# 2.3.7.7 (L2) Ensure 'Interactive logon: Number of previous logons to
# cache (in case domain controller is not available)' is set to '4 or fewer
# logon(s)' (Automated)
# MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount=1,"3"
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == 'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount=1,"3"'):
        found = 1
        COMPLIANT.append("CachedLogonsCount")
        break
if(found == 0):
    NONCOMPLIANT.append("CachedLogonsCount")
    NOTCONFIGURED.append("CachedLogonsCount")

# 2.3.7.8 (L1) Ensure 'Interactive logon: Prompt user to change password
# before expiration' is set to 'between 5 and 14 days' (Automated)
# MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\PasswordExpiryWarning=4,13
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\PasswordExpiryWarning=4,13"):
        found = 1
        COMPLIANT.append("PasswordExpiryWarning")
        break
if(found == 0):
    NONCOMPLIANT.append("PasswordExpiryWarning")
    NOTCONFIGURED.append("PasswordExpiryWarning")

# 2.3.7.9 (L1) Ensure 'Interactive logon: Smart card removal behavior' is
# set to 'Lock Workstation' or higher (Automated)
# MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ScRemoveOption=1,"1"
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == 'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ScRemoveOption=1,"1"'):
        found = 1
        COMPLIANT.append("ScRemoveOption")
        break
if(found == 0):
    NONCOMPLIANT.append("ScRemoveOption")
    NOTCONFIGURED.append("ScRemoveOption")

# 2.3.8 Microsoft network client

# 2.3.8.1 (L1) Ensure 'Microsoft network client: Digitally sign
# communications (always)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1"):
        found = 1
        COMPLIANT.append("RequireSecuritySignature")
        break
if(found == 0):
    NONCOMPLIANT.append("RequireSecuritySignature")
    NOTCONFIGURED.append("RequireSecuritySignature")

# 2.3.8.2 (L1) Ensure 'Microsoft network client: Digitally sign
# communications (if server agrees)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanmanWorkstation\Parameters\EnableSecuritySignature=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanmanWorkstation\Parameters\EnableSecuritySignature=4,1"):
        found = 1
        COMPLIANT.append("EnableSecuritySignature")
        break
if(found == 0):
    NONCOMPLIANT.append("EnableSecuritySignature")
    NOTCONFIGURED.append("EnableSecuritySignature")

# 2.3.8.3 (L1) Ensure 'Microsoft network client: Send unencrypted
# password to third-party SMB servers' is set to 'Disabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanmanWorkstation\Parameters\EnablePlainTextPassword=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanmanWorkstation\Parameters\EnablePlainTextPassword=4,0"):
        found = 1
        COMPLIANT.append("EnablePlainTextPassword")
        break
if(found == 0):
    NONCOMPLIANT.append("EnablePlainTextPassword")
    NOTCONFIGURED.append("EnablePlainTextPassword")

# 2.3.9 Microsoft network server

# 2.3.9.1 (L1) Ensure 'Microsoft network server: Amount of idle time
# required before suspending session' is set to '15 or fewer minute(s)'
# (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\AutoDisconnect=4,14
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\AutoDisconnect=4,14"):
        found = 1
        COMPLIANT.append("AutoDisconnect")
        break
if(found == 0):
    NONCOMPLIANT.append("AutoDisconnect")
    NOTCONFIGURED.append("AutoDisconnect")

# 2.3.9.2 (L1) Ensure 'Microsoft network server: Digitally sign
# communications (always)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RequireSecuritySignature=4,1"):
        found = 1
        COMPLIANT.append("RequireSecuritySignature")
        break
if(found == 0):
    NONCOMPLIANT.append("RequireSecuritySignature")
    NOTCONFIGURED.append("RequireSecuritySignature")

# 2.3.9.3 (L1) Ensure 'Microsoft network server: Digitally sign
# communications (if client agrees)' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableSecuritySignature=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableSecuritySignature=4,1"):
        found = 1
        COMPLIANT.append("EnableSecuritySignature")
        break
if(found == 0):
    NONCOMPLIANT.append("EnableSecuritySignature")
    NOTCONFIGURED.append("EnableSecuritySignature")

# 2.3.9.4 (L1) Ensure 'Microsoft network server: Disconnect clients when
# logon hours expire' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableForcedLogOff=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableForcedLogOff=4,1"):
        found = 1
        COMPLIANT.append("EnableForcedLogOff")
        break
if(found == 0):
    NONCOMPLIANT.append("EnableForcedLogOff")
    NOTCONFIGURED.append("EnableForcedLogOff")

# 2.3.9.5 (L1) Ensure 'Microsoft network server: Server SPN target name
# validation level' is set to 'Accept if provided by client' or higher
# (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\SmbServerNameHardeningLevel=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\SmbServerNameHardeningLevel=4,1"):
        found = 1
        COMPLIANT.append("SmbServerNameHardeningLevel")
        break
if(found == 0):
    NONCOMPLIANT.append("SmbServerNameHardeningLevel")
    NOTCONFIGURED.append("SmbServerNameHardeningLevel")

# 2.3.10 Network access

# 2.3.10.1 (L1) Ensure 'Network access: Allow anonymous SID/Name
# translation' is set to 'Disabled' (Automated)
LSAAnonymousNameLookup = 0
# 2.3.10.2 (L1) Ensure 'Network access: Do not allow anonymous
# enumeration of SAM accounts' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymousSAM=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymousSAM=4,1"):
        found = 1
        COMPLIANT.append("RestrictAnonymousSAM")
        break
if(found == 0):
    NONCOMPLIANT.append("RestrictAnonymousSAM")
    NOTCONFIGURED.append("RestrictAnonymousSAM")

# 2.3.10.3 (L1) Ensure 'Network access: Do not allow anonymous
# enumeration of SAM accounts and shares' is set to 'Enabled'
# (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymous=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymous=4,1"):
        found = 1
        COMPLIANT.append("RestrictAnonymous")
        break
if(found == 0):
    NONCOMPLIANT.append("RestrictAnonymous")
    NOTCONFIGURED.append("RestrictAnonymous")

# 2.3.10.4 (L1) Ensure 'Network access: Do not allow storage of
# passwords and credentials for network authentication' is set to
# 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\DisableDomainCreds=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\DisableDomainCreds=4,1"):
        found = 1
        COMPLIANT.append("DisableDomainCreds")
        break
if(found == 0):
    NONCOMPLIANT.append("DisableDomainCreds")
    NOTCONFIGURED.append("DisableDomainCreds")

# 2.3.10.5 (L1) Ensure 'Network access: Let Everyone permissions apply to
# anonymous users' is set to 'Disabled' (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\EveryoneIncludesAnonymous=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\EveryoneIncludesAnonymous=4,0"):
        found = 1
        COMPLIANT.append("EveryoneIncludesAnonymous")
        break
if(found == 0):
    NONCOMPLIANT.append("EveryoneIncludesAnonymous")
    NOTCONFIGURED.append("EveryoneIncludesAnonymous")

# 2.3.10.6 (L1) Ensure 'Network access: Named Pipes that can be accessed
# anonymously' is set to 'None' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionPipes=7,
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionPipes=7,"):
        found = 1
        COMPLIANT.append("NullSessionPipes")
        break
if(found == 0):
    NONCOMPLIANT.append("NullSessionPipes")
    NOTCONFIGURED.append("NullSessionPipes")

# 2.3.10.7 (L1) Ensure 'Network access: Remotely accessible registry
# paths' (Automated)
# MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedExactPaths\Machine=7,System\CurrentControlSet\Control\ProductOptions,System\CurrentControlSet\Control\Server Applications,Software\Microsoft\Windows NT\CurrentVersion
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedExactPaths\Machine=7,System\CurrentControlSet\Control\ProductOptions,System\CurrentControlSet\Control\Server Applications,Software\Microsoft\Windows NT\CurrentVersion"):
        found = 1
        COMPLIANT.append("AllowedExactPaths")
        break
if(found == 0):
    NONCOMPLIANT.append("AllowedExactPaths")
    NOTCONFIGURED.append("AllowedExactPaths")

# 2.3.10.8 (L1) Ensure 'Network access: Remotely accessible registry paths
# and sub-paths' (Automated)
# MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedPaths\Machine=7,System\CurrentControlSet\Control\Print\Printers,System\CurrentControlSet\Services\Eventlog,Software\Microsoft\OLAP Server,Software\Microsoft\Windows NT\CurrentVersion\Print,Software\Microsoft\Windows NT\CurrentVersion\Windows,System\CurrentControlSet\Control\ContentIndex,System\CurrentControlSet\Control\Terminal Server,System\CurrentControlSet\Control\Terminal Server\UserConfig,System\CurrentControlSet\Control\Terminal Server\DefaultUserConfiguration,Software\Microsoft\Windows NT\CurrentVersion\Perflib,System\CurrentControlSet\Services\SysmonLog
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedPaths\Machine=7,System\CurrentControlSet\Control\Print\Printers,System\CurrentControlSet\Services\Eventlog,Software\Microsoft\OLAP Server,Software\Microsoft\Windows NT\CurrentVersion\Print,Software\Microsoft\Windows NT\CurrentVersion\Windows,System\CurrentControlSet\Control\ContentIndex,System\CurrentControlSet\Control\Terminal Server,System\CurrentControlSet\Control\Terminal Server\UserConfig,System\CurrentControlSet\Control\Terminal Server\DefaultUserConfiguration,Software\Microsoft\Windows NT\CurrentVersion\Perflib,System\CurrentControlSet\Services\SysmonLog"):
        found = 1
        COMPLIANT.append("AllowedPaths")
        break
if(found == 0):
    NONCOMPLIANT.append("AllowedPaths")
    NOTCONFIGURED.append("AllowedPaths")

# 2.3.10.9 (L1) Ensure 'Network access: Restrict anonymous access to
# Named Pipes and Shares' is set to 'Enabled' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RestrictNullSessAccess=4,1
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RestrictNullSessAccess=4,1"):
        found = 1
        COMPLIANT.append("RestrictNullSessAccess")
        break
if(found == 0):
    NONCOMPLIANT.append("RestrictNullSessAccess")
    NOTCONFIGURED.append("RestrictNullSessAccess")

# 2.3.10.10 (L1) Ensure 'Network access: Restrict clients allowed to make
# remote calls to SAM' is set to 'Administrators: Remote Access: Allow'
# (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\RestrictRemoteSAM=1,"O:BAG:BAD:(A;;RC;;;BA)"
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == 'MACHINE\System\CurrentControlSet\Control\Lsa\RestrictRemoteSAM=1,"O:BAG:BAD:(A;;RC;;;BA)"'):
        found = 1
        COMPLIANT.append("RestrictRemoteSAM")
        break
if(found == 0):
    NONCOMPLIANT.append("RestrictRemoteSAM")
    NOTCONFIGURED.append("RestrictRemoteSAM")

# 2.3.10.11 (L1) Ensure 'Network access: Shares that can be accessed
# anonymously' is set to 'None' (Automated)
# MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionShares=7,
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionShares=7,"):
        found = 1
        COMPLIANT.append("NullSessionShares")
        break
if(found == 0):
    NONCOMPLIANT.append("NullSessionShares")
    NOTCONFIGURED.append("NullSessionShares")

# 2.3.10.12 (L1) Ensure 'Network access: Sharing and security model for
# local accounts' is set to 'Classic - local users authenticate as themselves'
# (Automated)
# MACHINE\System\CurrentControlSet\Control\Lsa\ForceGuest=4,0
for idx, word in enumerate(GPRsplit):
    found = 0
    if (GPRsplit[idx] == "MACHINE\System\CurrentControlSet\Control\Lsa\ForceGuest=4,0"):
        found = 1
        COMPLIANT.append("ForceGuest")
        break
if(found == 0):
    NONCOMPLIANT.append("ForceGuest")
    NOTCONFIGURED.append("ForceGuest")
    
print("Compliant",COMPLIANT,'\n')
print("Non Compliant",NONCOMPLIANT,'\n')
print("Not Configured",NOTCONFIGURED,'\n')

# 2.3.11 Network security
# ---------------------------------------------------------------------------
# 2.3.11.1 (L1) Ensure 'Network security: Allow Local System to use
# computer identity for NTLM' is set to 'Enabled' (Automated)

# 2.3.11.2 (L1) Ensure 'Network security: Allow LocalSystem NULL session
# fallback' is set to 'Disabled' (Automated)

# 2.3.11.3 (L1) Ensure 'Network Security: Allow PKU2U authentication
# requests to this computer to use online identities' is set to 'Disabled'
# (Automated)

# 2.3.11.4 (L1) Ensure 'Network security: Configure encryption types
# allowed for Kerberos' is set to 'AES128_HMAC_SHA1,
# AES256_HMAC_SHA1, Future encryption types' (Automated)

# 2.3.11.5 (L1) Ensure 'Network security: Do not store LAN Manager hash
# value on next password change' is set to 'Enabled' (Automated)

# 2.3.11.6 (L1) Ensure 'Network security: Force logoff when logon hours
# expire' is set to 'Enabled' (Manual)

# 2.3.11.7 (L1) Ensure 'Network security: LAN Manager authentication
# level' is set to 'Send NTLMv2 response only. Refuse LM & NTLM'
# (Automated)

# 2.3.11.8 (L1) Ensure 'Network security: LDAP client signing
# requirements' is set to 'Negotiate signing' or higher (Automated)

# 2.3.11.9 (L1) Ensure 'Network security: Minimum session security for
# NTLM SSP based (including secure RPC) clients' is set to 'Require
# NTLMv2 session security, Require 128-bit encryption' (Automated)

# 2.3.11.10 (L1) Ensure 'Network security: Minimum session security for
# NTLM SSP based (including secure RPC) servers' is set to 'Require
# NTLMv2 session security, Require 128-bit encryption' (Automated)

# 2.3.14 System cryptography

# 2.3.14.1 (L2) Ensure 'System cryptography: Force strong key protection
# for user keys stored on the computer' is set to 'User is prompted when
# the key is first used' or higher (Automated)

# 2.3.15 System objects

# 2.3.15.1 (L1) Ensure 'System objects: Require case insensitivity for nonWindows subsystems' is set to 'Enabled' (Automated)

# 2.3.15.2 (L1) Ensure 'System objects: Strengthen default permissions of
# internal system objects (e.g. Symbolic Links)' is set to 'Enabled'
# (Automated)

# 2.3.17 User Account Control

# 2.3.17.1 (L1) Ensure 'User Account Control: Admin Approval Mode for
# the Built-in Administrator account' is set to 'Enabled' (Automated)

# 2.3.17.2 (L1) Ensure 'User Account Control: Behavior of the elevation
# prompt for administrators in Admin Approval Mode' is set to 'Prompt
# for consent on the secure desktop' (Automated)

# 2.3.17.3 (L1) Ensure 'User Account Control: Behavior of the elevation
# prompt for standard users' is set to 'Automatically deny elevation
# requests' (Automated)

# 2.3.17.4 (L1) Ensure 'User Account Control: Detect application
# installations and prompt for elevation' is set to 'Enabled' (Automated)

# 2.3.17.5 (L1) Ensure 'User Account Control: Only elevate UIAccess
# applications that are installed in secure locations' is set to 'Enabled'
# (Automated)

# 2.3.17.6 (L1) Ensure 'User Account Control: Run all administrators in
# Admin Approval Mode' is set to 'Enabled' (Automated)

# 2.3.17.7 (L1) Ensure 'User Account Control: Switch to the secure desktop
# when prompting for elevation' is set to 'Enabled' (Automated)

# 2.3.17.8 (L1) Ensure 'User Account Control: Virtualize file and registry
# write failures to per-user locations' is set to 'Enabled' (Automated)

# 5 System Services

# 5.1 (L2) Ensure 'Bluetooth Audio Gateway Service (BTAGService)' is set
# to 'Disabled' (Automated)

# 5.2 (L2) Ensure 'Bluetooth Support Service (bthserv)' is set to 'Disabled'
# (Automated)

# 5.3 (L1) Ensure 'Computer Browser (Browser)' is set to 'Disabled' or 'Not
# Installed' (Automated)

# 5.4 (L2) Ensure 'Downloaded Maps Manager (MapsBroker)' is set to
# 'Disabled' (Automated)

# 5.5 (L2) Ensure 'Geolocation Service (lfsvc)' is set to 'Disabled'
# (Automated)

# 5.6 (L1) Ensure 'IIS Admin Service (IISADMIN)' is set to 'Disabled' or 'Not
# Installed' (Automated)

# 5.7 (L1) Ensure 'Infrared monitor service (irmon)' is set to 'Disabled' or
# 'Not Installed' (Automated)

# 5.8 (L1) Ensure 'Internet Connection Sharing (ICS) (SharedAccess)' is set
# to 'Disabled' (Automated)

# 5.9 (L2) Ensure 'Link-Layer Topology Discovery Mapper (lltdsvc)' is set to
# 'Disabled' (Automated)

# 5.10 (L1) Ensure 'LxssManager (LxssManager)' is set to 'Disabled' or 'Not
# Installed' (Automated)

# 5.11 (L1) Ensure 'Microsoft FTP Service (FTPSVC)' is set to 'Disabled' or
# 'Not Installed' (Automated)

# 5.12 (L2) Ensure 'Microsoft iSCSI Initiator Service (MSiSCSI)' is set to
# 'Disabled' (Automated)

# 5.13 (L1) Ensure 'OpenSSH SSH Server (sshd)' is set to 'Disabled' or 'Not
# Installed' (Automated)

# 5.14 (L2) Ensure 'Peer Name Resolution Protocol (PNRPsvc)' is set to
# 'Disabled' (Automated)

# 5.15 (L2) Ensure 'Peer Networking Grouping (p2psvc)' is set to 'Disabled'
# (Automated)

# 5.16 (L2) Ensure 'Peer Networking Identity Manager (p2pimsvc)' is set to
# 'Disabled' (Automated)

# 5.17 (L2) Ensure 'PNRP Machine Name Publication Service
# (PNRPAutoReg)' is set to 'Disabled' (Automated)

# 5.18 (L2) Ensure 'Problem Reports and Solutions Control Panel Support
# (wercplsupport)' is set to 'Disabled' (Automated)

# 5.19 (L2) Ensure 'Remote Access Auto Connection Manager (RasAuto)' is
# set to 'Disabled' (Automated)

# 5.20 (L2) Ensure 'Remote Desktop Configuration (SessionEnv)' is set to
# 'Disabled' (Automated)

# 5.21 (L2) Ensure 'Remote Desktop Services (TermService)' is set to
# 'Disabled' (Automated)

# 5.22 (L2) Ensure 'Remote Desktop Services UserMode Port Redirector
# (UmRdpService)' is set to 'Disabled' (Automated)

# 5.23 (L1) Ensure 'Remote Procedure Call (RPC) Locator (RpcLocator)' is
# set to 'Disabled' (Automated)

# 5.24 (L2) Ensure 'Remote Registry (RemoteRegistry)' is set to 'Disabled'
# (Automated)

# 5.25 (L1) Ensure 'Routing and Remote Access (RemoteAccess)' is set to
# 'Disabled' (Automated)

# 5.26 (L2) Ensure 'Server (LanmanServer)' is set to 'Disabled' (Automated)

# 5.27 (L1) Ensure 'Simple TCP/IP Services (simptcp)' is set to 'Disabled' or
# 'Not Installed' (Automated)

# 5.28 (L2) Ensure 'SNMP Service (SNMP)' is set to 'Disabled' or 'Not
# Installed' (Automated)

# 5.29 (L1) Ensure 'Special Administration Console Helper (sacsvr)' is set to
# 'Disabled' or 'Not Installed' (Automated)

# 5.30 (L1) Ensure 'SSDP Discovery (SSDPSRV)' is set to 'Disabled'
# (Automated)

# 5.31 (L1) Ensure 'UPnP Device Host (upnphost)' is set to 'Disabled'
# (Automated)

# 5.32 (L1) Ensure 'Web Management Service (WMSvc)' is set to 'Disabled'
# or 'Not Installed' (Automated)

# 5.33 (L2) Ensure 'Windows Error Reporting Service (WerSvc)' is set to
# 'Disabled' (Automated)

# 5.34 (L2) Ensure 'Windows Event Collector (Wecsvc)' is set to 'Disabled'
# (Automated)

# 5.35 (L1) Ensure 'Windows Media Player Network Sharing Service
# (WMPNetworkSvc)' is set to 'Disabled' or 'Not Installed' (Automated)

# 5.36 (L1) Ensure 'Windows Mobile Hotspot Service (icssvc)' is set to
# 'Disabled' (Automated)

# 5.37 (L2) Ensure 'Windows Push Notifications System Service
# (WpnService)' is set to 'Disabled' (Automated)

# 5.38 (L2) Ensure 'Windows PushToInstall Service (PushToInstall)' is set to
# 'Disabled' (Automated)

# 5.39 (L2) Ensure 'Windows Remote Management (WS-Management)
# (WinRM)' is set to 'Disabled' (Automated)

# 5.40 (L1) Ensure 'World Wide Web Publishing Service (W3SVC)' is set to
# 'Disabled' or 'Not Installed' (Automated)

# 5.41 (L1) Ensure 'Xbox Accessory Management Service (XboxGipSvc)' is
# set to 'Disabled' (Automated)

# 5.42 (L1) Ensure 'Xbox Live Auth Manager (XblAuthManager)' is set to
# 'Disabled' (Automated)

# 5.43 (L1) Ensure 'Xbox Live Game Save (XblGameSave)' is set to
# 'Disabled' (Automated)

# 5.44 (L1) Ensure 'Xbox Live Networking Service (XboxNetApiSvc)' is set to
# 'Disabled' (Automated)

# 9 Windows Firewall with Advanced Security

# 9.1 Domain Profile

# 9.1.1 (L1) Ensure 'Windows Firewall: Domain: Firewall state' is set to 'On
# (recommended)' (Automated)

# 9.1.2 (L1) Ensure 'Windows Firewall: Domain: Inbound connections' is
# set to 'Block (default)' (Automated)

# 9.1.3 (L1) Ensure 'Windows Firewall: Domain: Outbound connections' is
# set to 'Allow (default)' (Automated)

# 9.1.4 (L1) Ensure 'Windows Firewall: Domain: Settings: Display a
# notification' is set to 'No' (Automated)

# 9.1.5 (L1) Ensure 'Windows Firewall: Domain: Logging: Name' is set to
# '%SystemRoot%\System32\logfiles\firewall\domainfw.log' (Automated)

# 9.1.6 (L1) Ensure 'Windows Firewall: Domain: Logging: Size limit (KB)' is
# set to '16,384 KB or greater' (Automated)

# 9.1.7 (L1) Ensure 'Windows Firewall: Domain: Logging: Log dropped
# packets' is set to 'Yes' (Automated)

# 9.1.8 (L1) Ensure 'Windows Firewall: Domain: Logging: Log successful
# connections' is set to 'Yes' (Automated)

# 9.2 Private Profile

# 9.2.1 (L1) Ensure 'Windows Firewall: Private: Firewall state' is set to 'On
# (recommended)' (Automated)

# 9.2.2 (L1) Ensure 'Windows Firewall: Private: Inbound connections' is set
# to 'Block (default)' (Automated)

# 9.2.3 (L1) Ensure 'Windows Firewall: Private: Outbound connections' is
# set to 'Allow (default)' (Automated)

# 9.2.4 (L1) Ensure 'Windows Firewall: Private: Settings: Display a
# notification' is set to 'No' (Automated)

# 9.2.5 (L1) Ensure 'Windows Firewall: Private: Logging: Name' is set to
# '%SystemRoot%\System32\logfiles\firewall\privatefw.log' (Automated)

# 9.2.6 (L1) Ensure 'Windows Firewall: Private: Logging: Size limit (KB)' is
# set to '16,384 KB or greater' (Automated)

# 9.2.7 (L1) Ensure 'Windows Firewall: Private: Logging: Log dropped
# packets' is set to 'Yes' (Automated)

# 9.2.8 (L1) Ensure 'Windows Firewall: Private: Logging: Log successful
# connections' is set to 'Yes' (Automated)

# 9.3 Public Profile

# 9.3.1 (L1) Ensure 'Windows Firewall: Public: Firewall state' is set to 'On
# (recommended)' (Automated)

# 9.3.2 (L1) Ensure 'Windows Firewall: Public: Inbound connections' is set
# to 'Block (default)' (Automated)

# 9.3.3 (L1) Ensure 'Windows Firewall: Public: Outbound connections' is
# set to 'Allow (default)' (Automated)

# 9.3.4 (L1) Ensure 'Windows Firewall: Public: Settings: Display a
# notification' is set to 'No' (Automated)

# 9.3.5 (L1) Ensure 'Windows Firewall: Public: Settings: Apply local firewall
# rules' is set to 'No' (Automated)

# 9.3.6 (L1) Ensure 'Windows Firewall: Public: Settings: Apply local
# connection security rules' is set to 'No' (Automated)

# 9.3.7 (L1) Ensure 'Windows Firewall: Public: Logging: Name' is set to
# '%SystemRoot%\System32\logfiles\firewall\publicfw.log' (Automated)

# 9.3.8 (L1) Ensure 'Windows Firewall: Public: Logging: Size limit (KB)' is
# set to '16,384 KB or greater' (Automated)

# 9.3.9 (L1) Ensure 'Windows Firewall: Public: Logging: Log dropped
# packets' is set to 'Yes' (Automated)

# 9.3.10 (L1) Ensure 'Windows Firewall: Public: Logging: Log successful
# connections' is set to 'Yes' (Automated)

# 17 Advanced Audit Policy Configuration

# 17.1 Account Logon

# 17.1.1 (L1) Ensure 'Audit Credential Validation' is set to 'Success and
# Failure' (Automated)

# 17.2 Account Management

# 17.2.1 (L1) Ensure 'Audit Application Group Management' is set to
# 'Success and Failure' (Automated)

# 17.2.2 (L1) Ensure 'Audit Security Group Management' is set to include
# 'Success' (Automated)

# 17.2.3 (L1) Ensure 'Audit User Account Management' is set to 'Success
# and Failure' (Automated)

# 17.3 Detailed Tracking

# 17.3.1 (L1) Ensure 'Audit PNP Activity' is set to include 'Success'
# (Automated)

# 17.3.2 (L1) Ensure 'Audit Process Creation' is set to include 'Success'
# (Automated)

# 17.5 Logon/Logoff

# 17.5.1 (L1) Ensure 'Audit Account Lockout' is set to include 'Failure'
# (Automated)

# 17.5.2 (L1) Ensure 'Audit Group Membership' is set to include 'Success'
# (Automated)

# 17.5.3 (L1) Ensure 'Audit Logoff' is set to include 'Success' (Automated)

# 17.5.4 (L1) Ensure 'Audit Logon' is set to 'Success and Failure'
# (Automated)

# 17.5.5 (L1) Ensure 'Audit Other Logon/Logoff Events' is set to 'Success
# and Failure' (Automated)

# 17.5.6 (L1) Ensure 'Audit Special Logon' is set to include 'Success'
# (Automated)

# 17.6 Object Access

# 17.6.1 (L1) Ensure 'Audit Detailed File Share' is set to include 'Failure'
# (Automated)

# 17.6.2 (L1) Ensure 'Audit File Share' is set to 'Success and Failure'
# (Automated)

# 17.6.3 (L1) Ensure 'Audit Other Object Access Events' is set to 'Success
# and Failure' (Automated)

# 17.6.4 (L1) Ensure 'Audit Removable Storage' is set to 'Success and
# Failure' (Automated)

# 17.7 Policy Change

# 17.7.1 (L1) Ensure 'Audit Audit Policy Change' is set to include 'Success'
# (Automated)

# 17.7.2 (L1) Ensure 'Audit Authentication Policy Change' is set to include
# 'Success' (Automated)

# 17.7.3 (L1) Ensure 'Audit Authorization Policy Change' is set to include
# 'Success' (Automated)

# 17.7.4 (L1) Ensure 'Audit MPSSVC Rule-Level Policy Change' is set to
# 'Success and Failure' (Automated)

# 17.7.5 (L1) Ensure 'Audit Other Policy Change Events' is set to include
# 'Failure' (Automated)

# 17.8 Privilege Use

# 17.8.1 (L1) Ensure 'Audit Sensitive Privilege Use' is set to 'Success and
# Failure' (Automated)

# 17.9 System

from pymongo import MongoClient 
from datetime import datetime
import uuid,re,platform

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

macAdd = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
platVer = platform.version()
  
try: 
    conn = MongoClient("mongodb+srv://Sanya:4wUubuaMachwQ9rn@cluster0.9w3mr.mongodb.net/OSCARQ?retryWrites=true&w=majority") 
    print("Connected to OSCARQ Database") 
except Exception as e:   
    print("Could not connect ", e) 
  
db = conn.OSCARQ 
collection = db.Windows
  
emp_rec1 = { 
        "Message":"This is a test! ~Vaibhav",
        "DeviceID":macAdd,
        "Platform":platVer,
        "TestTime":dt_string,
        "Compliant":COMPLIANT,
        "Non Compliant":NONCOMPLIANT,
        "Not Configured":NOTCONFIGURED
        } 
  
rec_id1 = collection.insert_one(emp_rec1) 
  
print("Data inserted with record id",rec_id1) 
  
cursor = collection.find() 
for record in cursor: 
    print(record) 
