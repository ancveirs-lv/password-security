# Password policy for services

This page is for product, identity and security teams. It describes a defensible baseline derived from NIST SP 800-63B and OWASP ASVS 5.0. It is not a substitute for a system-specific threat model.

## Baseline

1. If a password is the **only authentication factor**, require at least **15 characters**.
2. If a password is only one factor in MFA, NIST permits a shorter minimum but requires at least **8 characters**.
3. Permit at least **64 characters**.
4. Accept broad character sets, including **spaces**; do not arbitrarily truncate or case-transform the submitted password.
5. Do **not** require a fixed mix of uppercase, lowercase, digits and symbols.
6. Permit paste, browser password helpers and external password managers.
7. Reject common, expected and compromised passwords using an appropriate blocklist.
8. Do **not** require periodic password rotation without evidence of compromise.
9. Apply rate limiting and other controls against online guessing and credential stuffing.
10. Store passwords using a suitable salted, computationally expensive password-hashing scheme.
11. Offer stronger authentication; where risk requires it, prefer phishing-resistant methods.

## Why this matters

A password policy is a system control, not a test of whether a user can satisfy a character puzzle. Strong service-side controls reduce predictable user behaviour and make password managers and passphrases work as intended.

## Sources

See `nist_sp800_63b_4` and `owasp_asvs_5_v6_2` in [`../../data/sources.json`](../../data/sources.json).
