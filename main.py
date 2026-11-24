#!/usr/bin/env python3
"""Write a one-line office joke to entry.txt.

The joke is a single line of at most 200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
No trailing newline is written; the file is re-read after writing
to confirm its contents byte for byte.
"""

import os
import sys

JOKE = "The birthday card took six weeks to circle the office for signatures, and by the time it reached me, its owner had quit and joined the company next door."


def main():
    joke = JOKE
    if not joke or not joke.strip():
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(joke) > 200:
        print("error: joke exceeds 200 characters", file=sys.stderr)
        return 1
    data = joke.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: verification read mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(joke)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
