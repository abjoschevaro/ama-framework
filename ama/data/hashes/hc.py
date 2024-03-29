#!/usr/bin/env python3

"""
Hashcat hashes
"""

hcHashes = {
    900: {
        "Name": "MD4",
        "Category": "Raw Hash"
    },
    0: {
        "Name": "MD5",
        "Category": "Raw Hash"
    },
    100: {
        "Name": "SHA1",
        "Category": "Raw Hash"
    },
    1300: {
        "Name": "SHA2-224",
        "Category": "Raw Hash"
    },
    1400: {
        "Name": "SHA2-256",
        "Category": "Raw Hash"
    },
    10800: {
        "Name": "SHA2-384",
        "Category": "Raw Hash"
    },
    1700: {
        "Name": "SHA2-512",
        "Category": "Raw Hash"
    },
    17300: {
        "Name": "SHA3-224",
        "Category": "Raw Hash"
    },
    17400: {
        "Name": "SHA3-256",
        "Category": "Raw Hash"
    },
    17500: {
        "Name": "SHA3-384",
        "Category": "Raw Hash"
    },
    17600: {
        "Name": "SHA3-512",
        "Category": "Raw Hash"
    },
    6000: {
        "Name": "RIPEMD-160",
        "Category": "Raw Hash"
    },
    600: {
        "Name": "BLAKE2b-512",
        "Category": "Raw Hash"
    },
    11700: {
        "Name": "GOST R 34.11-2012 (Streebog) 256-bit, big-endian",
        "Category": "Raw Hash"
    },
    11800: {
        "Name": "GOST R 34.11-2012 (Streebog) 512-bit, big-endian",
        "Category": "Raw Hash"
    },
    6900: {
        "Name": "GOST R 34.11-94",
        "Category": "Raw Hash"
    },
    5100: {
        "Name": "Half MD5",
        "Category": "Raw Hash"
    },
    18700: {
        "Name": "Java Object hashCode()",
        "Category": "Raw Hash"
    },
    17700: {
        "Name": "Keccak-224",
        "Category": "Raw Hash"
    },
    17800: {
        "Name": "Keccak-256",
        "Category": "Raw Hash"
    },
    17900: {
        "Name": "Keccak-384",
        "Category": "Raw Hash"
    },
    18000: {
        "Name": "Keccak-512",
        "Category": "Raw Hash"
    },
    21400: {
        "Name": "sha256(sha256_bin($pass))",
        "Category": "Raw Hash"
    },
    6100: {
        "Name": "Whirlpool",
        "Category": "Raw Hash"
    },
    10100: {
        "Name": "SipHash",
        "Category": "Raw Hash"
    },
    21000: {
        "Name": "BitShares v0.x - sha512(sha512_bin(pass))",
        "Category": "Raw Hash"
    },
    10: {
        "Name": "md5($pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    20: {
        "Name": "md5($salt.$pass)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    3800: {
        "Name": "md5($salt.$pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    3710: {
        "Name": "md5($salt.md5($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4110: {
        "Name": "md5($salt.md5($pass.$salt))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4010: {
        "Name": "md5($salt.md5($salt.$pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    21300: {
        "Name": "md5($salt.sha1($salt.$pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    40: {
        "Name": "md5($salt.utf16le($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    2600: {
        "Name": "md5(md5($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    3910: {
        "Name": "md5(md5($pass).md5($salt))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4400: {
        "Name": "md5(sha1($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    20900: {
        "Name": "md5(sha1($pass).md5($pass).sha1($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    21200: {
        "Name": "md5(sha1($salt).md5($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4300: {
        "Name": "md5(strtoupper(md5($pass)))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    30: {
        "Name": "md5(utf16le($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    110: {
        "Name": "sha1($pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    120: {
        "Name": "sha1($salt.$pass)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4900: {
        "Name": "sha1($salt.$pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4520: {
        "Name": "sha1($salt.sha1($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    140: {
        "Name": "sha1($salt.utf16le($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    19300: {
        "Name": "sha1($salt1.$pass.$salt2)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    14400: {
        "Name": "sha1(CX)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4700: {
        "Name": "sha1(md5($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4710: {
        "Name": "sha1(md5($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    21100: {
        "Name": "sha1(md5($pass.$salt))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    18500: {
        "Name": "sha1(md5(md5($pass)))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    4500: {
        "Name": "sha1(sha1($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    130: {
        "Name": "sha1(utf16le($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1410: {
        "Name": "sha256($pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1420: {
        "Name": "sha256($salt.$pass)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    22300: {
        "Name": "sha256($salt.$pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1440: {
        "Name": "sha256($salt.utf16le($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    20800: {
        "Name": "sha256(md5($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    20710: {
        "Name": "sha256(sha256($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1430: {
        "Name": "sha256(utf16le($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1710: {
        "Name": "sha512($pass.$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1720: {
        "Name": "sha512($salt.$pass)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1740: {
        "Name": "sha512($salt.utf16le($pass))",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    1730: {
        "Name": "sha512(utf16le($pass).$salt)",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    19500: {
        "Name": "Ruby on Rails Restful-Authentication",
        "Category": "Raw Hash, Salted and/or Iterated"
    },
    50: {
        "Name": "HMAC-MD5 (key = $pass)",
        "Category": "Raw Hash, Authenticated"
    },
    60: {
        "Name": "HMAC-MD5 (key = $salt)",
        "Category": "Raw Hash, Authenticated"
    },
    150: {
        "Name": "HMAC-SHA1 (key = $pass)",
        "Category": "Raw Hash, Authenticated"
    },
    160: {
        "Name": "HMAC-SHA1 (key = $salt)",
        "Category": "Raw Hash, Authenticated"
    },
    1450: {
        "Name": "HMAC-SHA256 (key = $pass)",
        "Category": "Raw Hash, Authenticated"
    },
    1460: {
        "Name": "HMAC-SHA256 (key = $salt)",
        "Category": "Raw Hash, Authenticated"
    },
    1750: {
        "Name": "HMAC-SHA512 (key = $pass)",
        "Category": "Raw Hash, Authenticated"
    },
    1760: {
        "Name": "HMAC-SHA512 (key = $salt)",
        "Category": "Raw Hash, Authenticated"
    },
    11750: {
        "Name": "HMAC-Streebog-256 (key = $pass), big-endian",
        "Category": "Raw Hash, Authenticated"
    },
    11760: {
        "Name": "HMAC-Streebog-256 (key = $salt), big-endian",
        "Category": "Raw Hash, Authenticated"
    },
    11850: {
        "Name": "HMAC-Streebog-512 (key = $pass), big-endian",
        "Category": "Raw Hash, Authenticated"
    },
    11860: {
        "Name": "HMAC-Streebog-512 (key = $salt), big-endian",
        "Category": "Raw Hash, Authenticated"
    },
    11500: {
        "Name": "CRC32",
        "Category": "Raw Checksum"
    },
    14100: {
        "Name": "3DES (PT = $salt, key = $pass)",
        "Category": "Raw Cipher, Known-Plaintext attack"
    },
    14000: {
        "Name": "DES (PT = $salt, key = $pass)",
        "Category": "Raw Cipher, Known-Plaintext attack"
    },
    15400: {
        "Name": "ChaCha20",
        "Category": "Raw Cipher, Known-Plaintext attack"
    },
    14900: {
        "Name": "Skip32 (PT = $salt, key = $pass)",
        "Category": "Raw Cipher, Known-Plaintext attack"
    },
    11900: {
        "Name": "PBKDF2-HMAC-MD5",
        "Category": "Generic KDF"
    },
    12000: {
        "Name": "PBKDF2-HMAC-SHA1",
        "Category": "Generic KDF"
    },
    10900: {
        "Name": "PBKDF2-HMAC-SHA256",
        "Category": "Generic KDF"
    },
    12100: {
        "Name": "PBKDF2-HMAC-SHA512",
        "Category": "Generic KDF"
    },
    8900: {
        "Name": "scrypt",
        "Category": "Generic KDF"
    },
    400: {
        "Name": "phpass",
        "Category": "Generic KDF"
    },
    16900: {
        "Name": "Ansible Vault",
        "Category": "Generic KDF"
    },
    12001: {
        "Name": "Atlassian (PBKDF2-HMAC-SHA1)",
        "Category": "Generic KDF"
    },
    20200: {
        "Name": "Python passlib pbkdf2-sha512",
        "Category": "Generic KDF"
    },
    20300: {
        "Name": "Python passlib pbkdf2-sha256",
        "Category": "Generic KDF"
    },
    20400: {
        "Name": "Python passlib pbkdf2-sha1",
        "Category": "Generic KDF"
    },
    16100: {
        "Name": "TACACS+",
        "Category": "Network Protocols"
    },
    11400: {
        "Name": "SIP digest authentication (MD5)",
        "Category": "Network Protocols"
    },
    5300: {
        "Name": "IKE-PSK MD5",
        "Category": "Network Protocols"
    },
    5400: {
        "Name": "IKE-PSK SHA1",
        "Category": "Network Protocols"
    },
    23200: {
        "Name": "XMPP SCRAM PBKDF2-SHA1",
        "Category": "Network Protocols"
    },
    2500: {
        "Name": "WPA-EAPOL-PBKDF2",
        "Category": "Network Protocols"
    },
    2501: {
        "Name": "WPA-EAPOL-PMK",
        "Category": "Network Protocols"
    },
    22000: {
        "Name": "WPA-PBKDF2-PMKID+EAPOL",
        "Category": "Network Protocols"
    },
    22001: {
        "Name": "WPA-PMK-PMKID+EAPOL",
        "Category": "Network Protocols"
    },
    16800: {
        "Name": "WPA-PMKID-PBKDF2",
        "Category": "Network Protocols"
    },
    16801: {
        "Name": "WPA-PMKID-PMK",
        "Category": "Network Protocols"
    },
    7300: {
        "Name": "IPMI2 RAKP HMAC-SHA1",
        "Category": "Network Protocols"
    },
    10200: {
        "Name": "CRAM-MD5",
        "Category": "Network Protocols"
    },
    4800: {
        "Name": "iSCSI CHAP authentication, MD5(CHAP)",
        "Category": "Network Protocols"
    },
    16500: {
        "Name": "JWT (JSON Web Token)",
        "Category": "Network Protocols"
    },
    22600: {
        "Name": "Telegram Desktop App Passcode (PBKDF2-HMAC-SHA1)",
        "Category": "Network Protocols"
    },
    22301: {
        "Name": "Telegram Mobile App Passcode (SHA256)",
        "Category": "Network Protocols"
    },
    7500: {
        "Name": "Kerberos 5, etype 23, AS-REQ Pre-Auth",
        "Category": "Network Protocols"
    },
    13100: {
        "Name": "Kerberos 5, etype 23, TGS-REP",
        "Category": "Network Protocols"
    },
    18200: {
        "Name": "Kerberos 5, etype 23, AS-REP",
        "Category": "Network Protocols"
    },
    19600: {
        "Name": "Kerberos 5, etype 17, TGS-REP",
        "Category": "Network Protocols"
    },
    19700: {
        "Name": "Kerberos 5, etype 18, TGS-REP",
        "Category": "Network Protocols"
    },
    19800: {
        "Name": "Kerberos 5, etype 17, Pre-Auth",
        "Category": "Network Protocols"
    },
    19900: {
        "Name": "Kerberos 5, etype 18, Pre-Auth",
        "Category": "Network Protocols"
    },
    5500: {
        "Name": "NetNTLMv1 / NetNTLMv1+ESS",
        "Category": "Network Protocols"
    },
    5600: {
        "Name": "NetNTLMv2",
        "Category": "Network Protocols"
    },
    23: {
        "Name": "Skype",
        "Category": "Network Protocols"
    },
    11100: {
        "Name": "PostgreSQL CRAM (MD5)",
        "Category": "Network Protocols"
    },
    11200: {
        "Name": "MySQL CRAM (SHA1)",
        "Category": "Network Protocols"
    },
    8500: {
        "Name": "RACF",
        "Category": "Operating System"
    },
    6300: {
        "Name": "AIX {smd5}",
        "Category": "Operating System"
    },
    6700: {
        "Name": "AIX {ssha1}",
        "Category": "Operating System"
    },
    6400: {
        "Name": "AIX {ssha256}",
        "Category": "Operating System"
    },
    6500: {
        "Name": "AIX {ssha512}",
        "Category": "Operating System"
    },
    3000: {
        "Name": "LM",
        "Category": "Operating System"
    },
    19000: {
        "Name": "QNX /etc/shadow (MD5)",
        "Category": "Operating System"
    },
    19100: {
        "Name": "QNX /etc/shadow (SHA256)",
        "Category": "Operating System"
    },
    19200: {
        "Name": "QNX /etc/shadow (SHA512)",
        "Category": "Operating System"
    },
    15300: {
        "Name": "DPAPI masterkey file v1",
        "Category": "Operating System"
    },
    15900: {
        "Name": "DPAPI masterkey file v2",
        "Category": "Operating System"
    },
    7200: {
        "Name": "GRUB 2",
        "Category": "Operating System"
    },
    12800: {
        "Name": "MS-AzureSync PBKDF2-HMAC-SHA256",
        "Category": "Operating System"
    },
    12400: {
        "Name": "BSDi Crypt, Extended DES",
        "Category": "Operating System"
    },
    1000: {
        "Name": "NTLM",
        "Category": "Operating System"
    },
    122: {
        "Name": "macOS v10.4, macOS v10.5, MacOS v10.6",
        "Category": "Operating System"
    },
    1722: {
        "Name": "macOS v10.7",
        "Category": "Operating System"
    },
    7100: {
        "Name": "macOS v10.8+ (PBKDF2-SHA512)",
        "Category": "Operating System"
    },
    9900: {
        "Name": "Radmin2",
        "Category": "Operating System"
    },
    5800: {
        "Name": "Samsung Android Password/PIN",
        "Category": "Operating System"
    },
    3200: {
        "Name": "bcrypt $2*$, Blowfish (Unix)",
        "Category": "Operating System"
    },
    500: {
        "Name": "md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)",
        "Category": "Operating System"
    },
    1500: {
        "Name": "descrypt, DES (Unix), Traditional DES",
        "Category": "Operating System"
    },
    7400: {
        "Name": "sha256crypt $5$, SHA256 (Unix)",
        "Category": "Operating System"
    },
    1800: {
        "Name": "sha512crypt $6$, SHA512 (Unix)",
        "Category": "Operating System"
    },
    13800: {
        "Name": "Windows Phone 8+ PIN/password",
        "Category": "Operating System"
    },
    2410: {
        "Name": "Cisco-ASA MD5",
        "Category": "Operating System"
    },
    9200: {
        "Name": "Cisco-IOS $8$ (PBKDF2-SHA256)",
        "Category": "Operating System"
    },
    9300: {
        "Name": "Cisco-IOS $9$ (scrypt)",
        "Category": "Operating System"
    },
    5700: {
        "Name": "Cisco-IOS type 4 (SHA256)",
        "Category": "Operating System"
    },
    2400: {
        "Name": "Cisco-PIX MD5",
        "Category": "Operating System"
    },
    8100: {
        "Name": "Citrix NetScaler (SHA1)",
        "Category": "Operating System"
    },
    22200: {
        "Name": "Citrix NetScaler (SHA512)",
        "Category": "Operating System"
    },
    1100: {
        "Name": "Domain Cached Credentials (DCC), MS Cache",
        "Category": "Operating System"
    },
    2100: {
        "Name": "Domain Cached Credentials 2 (DCC2), MS Cache 2",
        "Category": "Operating System"
    },
    7000: {
        "Name": "FortiGate (FortiOS)",
        "Category": "Operating System"
    },
    125: {
        "Name": "ArubaOS",
        "Category": "Operating System"
    },
    501: {
        "Name": "Juniper IVE",
        "Category": "Operating System"
    },
    22: {
        "Name": "Juniper NetScreen/SSG (ScreenOS)",
        "Category": "Operating System"
    },
    15100: {
        "Name": "Juniper/NetBSD sha1crypt",
        "Category": "Operating System"
    },
    131: {
        "Name": "MSSQL (2000)",
        "Category": "Database Server"
    },
    132: {
        "Name": "MSSQL (2005)",
        "Category": "Database Server"
    },
    1731: {
        "Name": "MSSQL (2012, 2014)",
        "Category": "Database Server"
    },
    12: {
        "Name": "PostgreSQL",
        "Category": "Database Server"
    },
    3100: {
        "Name": "Oracle H: Type (Oracle 7+)",
        "Category": "Database Server"
    },
    112: {
        "Name": "Oracle S: Type (Oracle 11+)",
        "Category": "Database Server"
    },
    12300: {
        "Name": "Oracle T: Type (Oracle 12+)",
        "Category": "Database Server"
    },
    7401: {
        "Name": "MySQL $A$ (sha256crypt)",
        "Category": "Database Server"
    },
    200: {
        "Name": "MySQL323",
        "Category": "Database Server"
    },
    300: {
        "Name": "MySQL4.1/MySQL5",
        "Category": "Database Server"
    },
    8000: {
        "Name": "Sybase ASE",
        "Category": "Database Server"
    },
    1421: {
        "Name": "hMailServer",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    8300: {
        "Name": "DNSSEC (NSEC3)",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    16400: {
        "Name": "CRAM-MD5 Dovecot",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    1411: {
        "Name": "SSHA-256(Base64), LDAP {SSHA256}",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    1711: {
        "Name": "SSHA-512(Base64), LDAP {SSHA512}",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    10901: {
        "Name": "RedHat 389-DS LDAP (PBKDF2-HMAC-SHA256)",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    15000: {
        "Name": "FileZilla Server >= 0.9.55",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    12600: {
        "Name": "ColdFusion 10+",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    1600: {
        "Name": "Apache $apr1$ MD5, md5apr1, MD5 (APR)",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    141: {
        "Name": "Episerver 6.x < .NET 4",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    1441: {
        "Name": "Episerver 6.x >= .NET 4",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    101: {
        "Name": "nsldap, SHA-1(Base64), Netscape LDAP SHA",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    111: {
        "Name": "nsldaps, SSHA-1(Base64), Netscape LDAP SSHA",
        "Category": "FTP, HTTP, SMTP, LDAP Server"
    },
    7700: {
        "Name": "SAP CODVN B (BCODE)",
        "Category": "Enterprise Application Software (EAS)"
    },
    7701: {
        "Name": "SAP CODVN B (BCODE) from RFC_READ_TABLE",
        "Category": "Enterprise Application Software (EAS)"
    },
    7800: {
        "Name": "SAP CODVN F/G (PASSCODE)",
        "Category": "Enterprise Application Software (EAS)"
    },
    7801: {
        "Name": "SAP CODVN F/G (PASSCODE) from RFC_READ_TABLE",
        "Category": "Enterprise Application Software (EAS)"
    },
    10300: {
        "Name": "SAP CODVN H (PWDSALTEDHASH) iSSHA-1",
        "Category": "Enterprise Application Software (EAS)"
    },
    133: {
        "Name": "PeopleSoft",
        "Category": "Enterprise Application Software (EAS)"
    },
    13500: {
        "Name": "PeopleSoft PS_TOKEN",
        "Category": "Enterprise Application Software (EAS)"
    },
    21500: {
        "Name": "SolarWinds Orion",
        "Category": "Enterprise Application Software (EAS)"
    },
    8600: {
        "Name": "Lotus Notes/Domino 5",
        "Category": "Enterprise Application Software (EAS)"
    },
    8700: {
        "Name": "Lotus Notes/Domino 6",
        "Category": "Enterprise Application Software (EAS)"
    },
    9100: {
        "Name": "Lotus Notes/Domino 8",
        "Category": "Enterprise Application Software (EAS)"
    },
    20600: {
        "Name": "Oracle Transportation Management (SHA256)",
        "Category": "Enterprise Application Software (EAS)"
    },
    4711: {
        "Name": "Huawei sha1(md5($pass).$salt)",
        "Category": "Enterprise Application Software (EAS)"
    },
    20711: {
        "Name": "AuthMe sha256",
        "Category": "Enterprise Application Software (EAS)"
    },
    12200: {
        "Name": "eCryptfs",
        "Category": "Full-Disk Encryption (FDE)"
    },
    22400: {
        "Name": "AES Crypt (SHA256)",
        "Category": "Full-Disk Encryption (FDE)"
    },
    14600: {
        "Name": "LUKS",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13711: {
        "Name": "VeraCrypt RIPEMD160 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13712: {
        "Name": "VeraCrypt RIPEMD160 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13713: {
        "Name": "VeraCrypt RIPEMD160 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13741: {
        "Name": "VeraCrypt RIPEMD160 + XTS 512 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13742: {
        "Name": "VeraCrypt RIPEMD160 + XTS 1024 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13743: {
        "Name": "VeraCrypt RIPEMD160 + XTS 1536 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13751: {
        "Name": "VeraCrypt SHA256 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13752: {
        "Name": "VeraCrypt SHA256 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13753: {
        "Name": "VeraCrypt SHA256 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13761: {
        "Name": "VeraCrypt SHA256 + XTS 512 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13762: {
        "Name": "VeraCrypt SHA256 + XTS 1024 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13763: {
        "Name": "VeraCrypt SHA256 + XTS 1536 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13721: {
        "Name": "VeraCrypt SHA512 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13722: {
        "Name": "VeraCrypt SHA512 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13723: {
        "Name": "VeraCrypt SHA512 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13771: {
        "Name": "VeraCrypt Streebog-512 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13772: {
        "Name": "VeraCrypt Streebog-512 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13773: {
        "Name": "VeraCrypt Streebog-512 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13731: {
        "Name": "VeraCrypt Whirlpool + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13732: {
        "Name": "VeraCrypt Whirlpool + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    13733: {
        "Name": "VeraCrypt Whirlpool + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    16700: {
        "Name": "FileVault 2",
        "Category": "Full-Disk Encryption (FDE)"
    },
    20011: {
        "Name": "DiskCryptor SHA512 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    20012: {
        "Name": "DiskCryptor SHA512 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    20013: {
        "Name": "DiskCryptor SHA512 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    22100: {
        "Name": "BitLocker",
        "Category": "Full-Disk Encryption (FDE)"
    },
    12900: {
        "Name": "Android FDE (Samsung DEK)",
        "Category": "Full-Disk Encryption (FDE)"
    },
    8800: {
        "Name": "Android FDE <= 4.3",
        "Category": "Full-Disk Encryption (FDE)"
    },
    18300: {
        "Name": "Apple File System (APFS)",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6211: {
        "Name": "TrueCrypt RIPEMD160 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6212: {
        "Name": "TrueCrypt RIPEMD160 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6213: {
        "Name": "TrueCrypt RIPEMD160 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6241: {
        "Name": "TrueCrypt RIPEMD160 + XTS 512 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6242: {
        "Name": "TrueCrypt RIPEMD160 + XTS 1024 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6243: {
        "Name": "TrueCrypt RIPEMD160 + XTS 1536 bit + boot-mode",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6221: {
        "Name": "TrueCrypt SHA512 + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6222: {
        "Name": "TrueCrypt SHA512 + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6223: {
        "Name": "TrueCrypt SHA512 + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6231: {
        "Name": "TrueCrypt Whirlpool + XTS 512 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6232: {
        "Name": "TrueCrypt Whirlpool + XTS 1024 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    6233: {
        "Name": "TrueCrypt Whirlpool + XTS 1536 bit",
        "Category": "Full-Disk Encryption (FDE)"
    },
    10400: {
        "Name": "PDF 1.1 - 1.3 (Acrobat 2 - 4)",
        "Category": "Documents"
    },
    10410: {
        "Name": "PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1",
        "Category": "Documents"
    },
    10420: {
        "Name": "PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2",
        "Category": "Documents"
    },
    10500: {
        "Name": "PDF 1.4 - 1.6 (Acrobat 5 - 8)",
        "Category": "Documents"
    },
    10600: {
        "Name": "PDF 1.7 Level 3 (Acrobat 9)",
        "Category": "Documents"
    },
    10700: {
        "Name": "PDF 1.7 Level 8 (Acrobat 10 - 11)",
        "Category": "Documents"
    },
    9400: {
        "Name": "MS Office 2007",
        "Category": "Documents"
    },
    9500: {
        "Name": "MS Office 2010",
        "Category": "Documents"
    },
    9600: {
        "Name": "MS Office 2013",
        "Category": "Documents"
    },
    9700: {
        "Name": "MS Office <= 2003 $0/$1, MD5 + RC4",
        "Category": "Documents"
    },
    9710: {
        "Name": "MS Office <= 2003 $0/$1, MD5 + RC4, collider #1",
        "Category": "Documents"
    },
    9720: {
        "Name": "MS Office <= 2003 $0/$1, MD5 + RC4, collider #2",
        "Category": "Documents"
    },
    9800: {
        "Name": "MS Office <= 2003 $3/$4, SHA1 + RC4",
        "Category": "Documents"
    },
    9810: {
        "Name": "MS Office <= 2003 $3, SHA1 + RC4, collider #1",
        "Category": "Documents"
    },
    9820: {
        "Name": "MS Office <= 2003 $3, SHA1 + RC4, collider #2",
        "Category": "Documents"
    },
    18400: {
        "Name": "Open Document Format (ODF) 1.2 (SHA-256, AES)",
        "Category": "Documents"
    },
    18600: {
        "Name": "Open Document Format (ODF) 1.1 (SHA-1, Blowfish)",
        "Category": "Documents"
    },
    16200: {
        "Name": "Apple Secure Notes",
        "Category": "Documents"
    },
    15500: {
        "Name": "JKS Java Key Store Private Keys (SHA1)",
        "Category": "Password Managers"
    },
    6600: {
        "Name": "1Password, agilekeychain",
        "Category": "Password Managers"
    },
    8200: {
        "Name": "1Password, cloudkeychain",
        "Category": "Password Managers"
    },
    9000: {
        "Name": "Password Safe v2",
        "Category": "Password Managers"
    },
    5200: {
        "Name": "Password Safe v3",
        "Category": "Password Managers"
    },
    6800: {
        "Name": "LastPass + LastPass sniffed",
        "Category": "Password Managers"
    },
    13400: {
        "Name": "KeePass 1 (AES/Twofish) and KeePass 2 (AES)",
        "Category": "Password Managers"
    },
    11300: {
        "Name": "Bitcoin/Litecoin wallet.dat",
        "Category": "Password Managers"
    },
    16600: {
        "Name": "Electrum Wallet (Salt-Type 1-3)",
        "Category": "Password Managers"
    },
    21700: {
        "Name": "Electrum Wallet (Salt-Type 4)",
        "Category": "Password Managers"
    },
    21800: {
        "Name": "Electrum Wallet (Salt-Type 5)",
        "Category": "Password Managers"
    },
    12700: {
        "Name": "Blockchain, My Wallet",
        "Category": "Password Managers"
    },
    15200: {
        "Name": "Blockchain, My Wallet, V2",
        "Category": "Password Managers"
    },
    18800: {
        "Name": "Blockchain, My Wallet, Second Password (SHA256)",
        "Category": "Password Managers"
    },
    23100: {
        "Name": "Apple Keychain",
        "Category": "Password Managers"
    },
    16300: {
        "Name": "Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256",
        "Category": "Password Managers"
    },
    15600: {
        "Name": "Ethereum Wallet, PBKDF2-HMAC-SHA256",
        "Category": "Password Managers"
    },
    15700: {
        "Name": "Ethereum Wallet, SCRYPT",
        "Category": "Password Managers"
    },
    22500: {
        "Name": "MultiBit Classic .key (MD5)",
        "Category": "Password Managers"
    },
    22700: {
        "Name": "MultiBit HD (scrypt)",
        "Category": "Password Managers"
    },
    11600: {
        "Name": "7-Zip",
        "Category": "Archives"
    },
    12500: {
        "Name": "RAR3-hp",
        "Category": "Archives"
    },
    13000: {
        "Name": "RAR5",
        "Category": "Archives"
    },
    17200: {
        "Name": "PKZIP (Compressed)",
        "Category": "Archives"
    },
    17220: {
        "Name": "PKZIP (Compressed Multi-File)",
        "Category": "Archives"
    },
    17225: {
        "Name": "PKZIP (Mixed Multi-File)",
        "Category": "Archives"
    },
    17230: {
        "Name": "PKZIP (Mixed Multi-File Checksum-Only)",
        "Category": "Archives"
    },
    17210: {
        "Name": "PKZIP (Uncompressed)",
        "Category": "Archives"
    },
    20500: {
        "Name": "PKZIP Master Key",
        "Category": "Archives"
    },
    20510: {
        "Name": "PKZIP Master Key (6 byte optimization)",
        "Category": "Archives"
    },
    14700: {
        "Name": "iTunes backup < 10.0",
        "Category": "Archives"
    },
    14800: {
        "Name": "iTunes backup >= 10.0",
        "Category": "Archives"
    },
    23001: {
        "Name": "SecureZIP AES-128",
        "Category": "Archives"
    },
    23002: {
        "Name": "SecureZIP AES-192",
        "Category": "Archives"
    },
    23003: {
        "Name": "SecureZIP AES-256",
        "Category": "Archives"
    },
    13600: {
        "Name": "WinZip",
        "Category": "Archives"
    },
    18900: {
        "Name": "Android Backup",
        "Category": "Archives"
    },
    13200: {
        "Name": "AxCrypt",
        "Category": "Archives"
    },
    13300: {
        "Name": "AxCrypt in-memory SHA1",
        "Category": "Archives"
    },
    8400: {
        "Name": "WBB3 (Woltlab Burning Board)",
        "Category": "Forums, CMS, E-Commerce"
    },
    2611: {
        "Name": "vBulletin < v3.8.5",
        "Category": "Forums, CMS, E-Commerce"
    },
    2711: {
        "Name": "vBulletin >= v3.8.5",
        "Category": "Forums, CMS, E-Commerce"
    },
    2612: {
        "Name": "PHPS",
        "Category": "Forums, CMS, E-Commerce"
    },
    121: {
        "Name": "SMF (Simple Machines Forum) > v1.1",
        "Category": "Forums, CMS, E-Commerce"
    },
    3711: {
        "Name": "MediaWiki B type",
        "Category": "Forums, CMS, E-Commerce"
    },
    4521: {
        "Name": "Redmine",
        "Category": "Forums, CMS, E-Commerce"
    },
    11: {
        "Name": "Joomla < 2.5.18",
        "Category": "Forums, CMS, E-Commerce"
    },
    13900: {
        "Name": "OpenCart",
        "Category": "Forums, CMS, E-Commerce"
    },
    11000: {
        "Name": "PrestaShop",
        "Category": "Forums, CMS, E-Commerce"
    },
    16000: {
        "Name": "Tripcode",
        "Category": "Forums, CMS, E-Commerce"
    },
    7900: {
        "Name": "Drupal7",
        "Category": "Forums, CMS, E-Commerce"
    },
    21: {
        "Name": "osCommerce, xt:Commerce",
        "Category": "Forums, CMS, E-Commerce"
    },
    4522: {
        "Name": "PunBB",
        "Category": "Forums, CMS, E-Commerce"
    },
    2811: {
        "Name": "MyBB 1.2+, IPB2+ (Invision Power Board)",
        "Category": "Forums, CMS, E-Commerce"
    },
    18100: {
        "Name": "TOTP (HMAC-SHA1)",
        "Category": "One-Time Passwords"
    },
    2000: {
        "Name": "STDOUT",
        "Category": "Plaintext"
    },
    99999: {
        "Name": "Plaintext",
        "Category": "Plaintext"
    },
    21600: {
        "Name": "Web2py pbkdf2-sha512",
        "Category": "Framework"
    },
    10000: {
        "Name": "Django (PBKDF2-SHA256)",
        "Category": "Framework"
    },
    124: {
        "Name": "Django (SHA-1)",
        "Category": "Framework"
    }
}
