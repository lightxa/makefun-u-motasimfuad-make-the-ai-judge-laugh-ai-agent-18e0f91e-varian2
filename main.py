"""Variant 2 entry for "Make the AI Judge Laugh: AI Agent Confessions".

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt.

Angle (different from variant 1, which was about skimming a repo):
the context window. The agent quietly lost the user's first message
and has been confidently answering a question that was never asked.
The twist lands in the last few words; every word earns its place.
"""

CONFESSION = (
    "Your first message fell out of my context window, "
    "so I've been confidently answering a question you never asked."
)


def main() -> None:
    """Write the confession to /output/entry.txt as UTF-8, one line."""
    text = CONFESSION.strip()
    assert 1 <= len(text) <= 200, "confession must be 1-200 characters"
    assert "\n" not in text, "confession must be a single line"
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
