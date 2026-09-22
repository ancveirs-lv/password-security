# Space in passwords: myth vs reality

## The short answer

A space is a legitimate password character. It can be useful because it makes long passphrases easier to construct and remember. It is **not** a magic character that makes an otherwise weak password strong.

## What NIST says

Current NIST SP 800-63B guidance says verifiers should accept all printing ASCII characters **and the space character**, should support passwords of at least 64 characters, should not impose composition rules, and should not require arbitrary periodic password changes. Its appendix also notes that repeated spaces add little effective strength.

## What matters instead

- length;
- unpredictability;
- uniqueness per account;
- avoiding personal facts and common patterns;
- blocking common/compromised passwords;
- rate limiting and secure password storage on the service side;
- MFA/passkeys where appropriate.

## Good use of spaces

A space can help form a long passphrase made of unrelated words. The words still need to be hard to predict, and the phrase must not be reused elsewhere.

## Bad interpretation

Adding a space to `Password1!` does not turn it into a robust secret. Likewise, adding many repeated spaces is not a meaningful substitute for a better password.

## Source context

See `nist_sp800_63b_4` in [`../../data/sources.json`](../../data/sources.json).
