import csv
from pathlib import Path

SOURCE = Path("pg345.txt")
OUT_DIR = Path("frankenstein_chapters")
OUT_DIR.mkdir(exist_ok=True)

"""
Tutorial Part 1:
To begin with, we need to start with the obvious: importing csv as well as pathlib to be able to write a csv as well as to 
manipulate file paths. Next we establish the source file we're going to be using, in this case Project Gutenberg's plain text
version of Mary Shelly's Frankenstein. Then we name the directory we want all of our future code to go to, in this case I've 
named it "frankenstein_chapters", and finally we run a check to make sure that the directory already exists locally to be able
to run the code in the first place. This is all the groundwork and foundation to be able to do the real heavy lifting later
on.
"""

lines = SOURCE.read_text(encoding="utf-8-sig").splitlines(keepends=True)

end = next(i for i, line in enumerate(lines) if line.startswith("*** END OF"))

"""
Here we've begun to define some important variables that we'll call back to later in the code. For the "lines" variable, we
are splitting the text into lines based on where there are line breaks (\n) in the text. This is for when we write the lines
back in when we are creating the chapter text files later. 
"""

# Find chapter headings. The table of contents also contains "CHAPTER ..."
# lines, so key each heading by its numeral and let later (real) occurrences
# overwrite earlier (table of contents) ones.
heading_positions = {}
for i, line in enumerate(lines[:end]):
    if line.startswith("CHAPTER "):
        numeral = line.split()[1].rstrip(".")
        heading_positions[numeral] = i

starts = sorted(heading_positions.values())
ends = starts[1:] + [end]  # each chapter ends where the next begin

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
