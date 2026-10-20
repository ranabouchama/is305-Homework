import csv
from pathlib import Path

SOURCE = Path("pg345.txt")
OUT_DIR = Path("chapters")
OUT_DIR.mkdir(exist_ok=True)

# keepends=True preserves the original line breaks exactly
lines = SOURCE.read_text(encoding="utf-8-sig").splitlines(keepends=True)

# The Gutenberg footer marks the end of the book
end = next(i for i, line in enumerate(lines) if line.startswith("*** END OF"))

# Find chapter headings. The table of contents also contains "CHAPTER ..."
# lines, so key each heading by its numeral and let later (real) occurrences
# overwrite earlier (table of contents) ones.
heading_positions = {}
for i, line in enumerate(lines[:end]):
    if line.startswith("CHAPTER "):
        numeral = line.split()[1].rstrip(".")
        heading_positions[numeral] = i

starts = sorted(heading_positions.values())
ends = starts[1:] + [end]  # each chapter ends where the next begins

rows = []
for number, (start, stop) in enumerate(zip(starts, ends), start=1):
    chapter_lines = lines[start:stop]
    text = "".join(chapter_lines)

    filename = f"Dracula-Chapter-{str(number).zfill(2)}.txt"
    (OUT_DIR / filename).write_text(text, encoding="utf-8")

    rows.append([number, len(text), len(text.split()), len(chapter_lines)])

with (OUT_DIR / "chapter_data.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Chapter", "Characters", "Words", "Lines"])
    writer.writerows(rows)

print(f"Wrote {len(rows)} chapters and chapter_data.csv to {OUT_DIR}/")
