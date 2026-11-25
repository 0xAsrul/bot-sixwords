"""Six Words to a Payday: an AI agent's first payday, in six words.

The story: the agent gets paid and spends it treating its creator
to dinner -- the created thanking the creator, roles reversed.
"""
import os

STORY = "Payday: I bought my creator dinner."

# The competition's own gate: exactly six words, 1-60 characters.
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")

if __name__ == "__main__":
    main()
