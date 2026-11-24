"""Write one short text for make.fun's bounty.

The bounty is u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610:
one original line, up to 200 characters, roasting a gadget or app used every
day. This program writes that single line to entry.txt inside the output
folder, byte for byte, with no trailing newline.
"""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def resolve_output_dir() -> str:
    """Return the folder to write into, defaulting to /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"

    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(f"{len(TEXT)} characters written to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
