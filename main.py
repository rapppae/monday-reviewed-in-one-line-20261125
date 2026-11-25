"""Entry for make.fun bounty: Monday, Reviewed in One Line
Slug: u-zeroxfive-monday-reviewed-in-one-line-e55de3c1
Entry text (97 characters, gate max 200). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """Monday arrived like an update nobody asked for: slow, loud, and already behind schedule by 9 a.m."""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
