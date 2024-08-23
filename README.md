SPIP Unauthenticated RCE Exploit

Remote Code Execution (RCE) vulnerability in SPIP versions up to and including 4.2.12. The vulnerability arises from SPIP’s templating system, where it incorrectly handles user-supplied input, allowing an attacker to inject and execute arbitrary PHP code.

Usage: python3 spip_exploit.py

Example: python3 spip_exploit.py https://example.org

Reference: https://thinkloveshare.com/hacking/spip_preauth_rce_2024_part_1_the_feather/
