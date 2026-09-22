# Password Security

[Latviski](README.lv.md) · **English**

**Evidence-backed guidance for users, product teams and service owners.**

This repository separates **user advice** from **service requirements**. The English edition is written for a global audience. The Latvian edition is a language/localisation layer, not a claim that Latvian law defines the global password baseline.

> **Core principle:** a secure password strategy is not a symbol recipe. Prefer phishing-resistant authentication where available; otherwise use long, unique, unpredictable passwords, a password manager, and service-side controls that reject common or compromised passwords.

## What this project covers

- password and passphrase guidance for people;
- password-manager and account-recovery practices;
- the role of spaces in passwords and passphrases;
- modern service-side password policy;
- NIST SP 800-63B and OWASP ASVS 5.0 alignment notes;
- passkeys, MFA and the limits of passwords against phishing.

## The space-in-passwords question

**Yes, spaces should be accepted. No, a space is not a magic security character.** NIST's current guidance says password verifiers should accept the space character and support passphrases. It also explains that repeated spaces add little effective strength. Security comes from the whole secret: length, unpredictability, uniqueness and the controls around authentication.

See [Space in passwords: myth vs reality](docs/en/space-in-passwords.md).

## Quick guidance

1. Prefer passkeys or another phishing-resistant method when available.
2. Use a different password for every account.
3. Use a password manager.
4. When you must remember a password, prefer a long, unpredictable passphrase.
5. Do not treat spaces or special characters as magic.
6. Do not rotate passwords just because a calendar says so.
7. Protect your primary email and recovery channels.
8. If compromise is suspected, change the affected password and revoke old sessions where possible.

Service owners should also read [Password policy for services](docs/en/service-policy.md).

## Evidence model

`source → claim → guidance → validation`

Claims in `data/guidance.*.json` cite source IDs from `data/sources.json`. CI verifies language parity, source references and editorial safety constraints.

## Important distinction

NIST's **15-character minimum** is a verifier requirement for passwords used as a **single authentication factor**. It is not a universal statement that every human-chosen password in every context must be exactly 15+ characters. NIST permits a minimum of 8 when the password is only one factor in MFA. Services should still support at least 64 characters.

## Repository structure

- `docs/en/` — global English guidance;
- `docs/lv/` — Latvian guidance;
- `data/` — machine-readable guidance and source registry;
- `scripts/` — validation and link-health checks;
- `tests/` — regression tests.

## Sources

Primary sources include NIST SP 800-63B and OWASP ASVS 5.0. Supporting guidance includes UK NCSC and ENISA. Exact URLs and verification date are in [`data/sources.json`](data/sources.json).

## Scope

This is educational and engineering guidance, not legal advice and not a certification of any product or service.

## Author

**Zigmārs Ancveirs** — technology leader, software engineer and independent cybersecurity researcher.

## Licence

Documentation and data: **CC BY 4.0**. Code and automation: **MIT**. See [LICENSE.md](LICENSE.md).
