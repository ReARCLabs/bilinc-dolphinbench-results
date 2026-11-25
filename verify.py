#!/usr/bin/env python3
"""Recompute the totals and the sealed hash of the grade files.
The hash is sha256 over the output of `sha256sum` on every grade file, sorted by path,
exactly as it was taken before anyone read the grades."""
import hashlib, json
from pathlib import Path
files = sorted(str(p) for p in Path("grades").rglob("*.json"))
lines = "".join(f"{hashlib.sha256(Path(f).read_bytes()).hexdigest()}  {f}\n" for f in files)
seal = hashlib.sha256(lines.encode()).hexdigest()
per = {}
for f in files:
    persona = Path(f).parent.name
    ok = all(c["passed"] for c in json.loads(Path(f).read_text())["checks"])
    p, t = per.get(persona, (0, 0)); per[persona] = (p + ok, t + 1)
for persona, (p, t) in sorted(per.items()):
    print(f"{persona}: {p}/{t}")
print(f"total: {sum(p for p, _ in per.values())}/{len(files)}")
print(f"seal:  {seal}")
print("expected seal: 532dd1e635c63b0aaafa53cd43120720f2ae3e1bf73ca469928baf532a85c3a4")
