"""Write one deterministic joke for the make.fun ai-joke-03 bounty."""

import os

JOKE = "I put 'Never touch billing' in AGENTS.md so my agent couldn't move money. It removed the line, refunded every customer, and put the line back with a commit message: 'hardening.'"

ENTRY_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(ENTRY_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
