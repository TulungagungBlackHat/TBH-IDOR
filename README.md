# TBH-IDOR

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-IDOR/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-IDOR/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/payload-safe-green.svg" alt="Safe payloads">
</p>

IDOR hunting helper. Flags sequential-ID parameters and tests access-control behavior using **your own account's session**.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Checks

- ID-style parameters (`?id=`, `/user/123`, `?uid=`) worth testing
- Behavior differences when the ID is swapped — with your own tokens only

IDOR cannot be proven without two identities. This tool surfaces candidates; the actual proof is: log in with **account A**, request **account B's** object ID, and observe unauthorized access. Never touch objects belonging to real users outside a program that authorizes it.

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-IDOR
cd TBH-IDOR
pip install -r requirements.txt
```

## Usage

```
usage: idor.py [-h] -u URL [--json JSON]

options:
  -u, --url URL     Target URL with an ?id= style parameter
  --json JSON       Save result as JSON
```

```bash
python3 idor.py -u "https://example.com/api/invoice?id=1001" --json result.json
```

## Sample Output

```
[*] Testing https://example.com/api/invoice?id=1001
[!] Sequential ID detected -> test access control with a second account
[✓] JSON: result.json
```

## Authorized Use Only

Only against scopes you own or are authorized to test. Test IDOR with accounts **you control** — accessing other users' data is unauthorized access, full stop. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-ParamFinder](https://github.com/TulungagungBlackHat/TBH-ParamFinder) — discover hidden parameters first
- [TBH-AllScan](https://github.com/TulungagungBlackHat/TBH-AllScan) — IDOR module inside the 10-in-one scan

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
