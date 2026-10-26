import csv
from pathlib import Path

SOURCE = Path("pg345.txt")
OUT_DIR = Path("frankenstein_chapters")
OUT_DIR.mkdir(exist_ok=True)

"""
Tutorial Part 1:
To begin with, we need to start with the obvious: importing csv as well as pathlib to be able to write a csv as well as to manipulate file paths. Csv is needed to create and write the file and pathlib to, once again, manipulate file paths and decide on what directory they will belong to. In this case “frankenstein_chapters”. Next we establish the source file we're going to be using, in this case Project Gutenberg's plain text version of Mary Shelly's Frankenstein. Then we name the directory we want all of our future code to go to, in this case I've named it "frankenstein_chapters", and finally we run a check to make sure that the directory already exists locally to be able to run the code in the first place, and if it doesn’t, it creates the directory anyway. This is all the groundwork and foundation to be able to do the real heavy lifting later
on.
"""

lines = SOURCE.read_text(encoding="utf-8-sig").splitlines(keepends=True)

end = next(i for i, line in enumerate(lines) if line.startswith("*** END OF"))

"""
Tutorial Part 2:
Here we've begun to define some important variables that we'll call back to later in the code. For the "lines" variable, we are splitting the text into lines based on where there are line breaks (\n) in the text. This is for when we write the lines back in when we are creating the chapter text files later. Something that was initially difficult was knowing when to stop enumerating/at what point there is no more text to split. As it turns out, in checking the Project Gutenberg file, we know that we’ve reached the end of the text once we see the “END OF” line, as such we have an if statement that checks for that to stop enumerating.
"""

header_position = {}
for i, line in enumerate(lines[:end]):
    if line.startswith("CHAPTER "):
        numeral = line.split()[1].rstrip(".")
        header_position[numeral] = i

"""
Tutorial Part 3:
As the previous part handles the lines of every chapter, this part creates a dictionary that finds where every chapter starts. The first line “for i, line in enumerate(lines[:end]):” tells python to only enumerate from the beginning to the “END OF” line as described earlier. Then, there is the problem of knowing when chapters start. Checking the Project Gutenberg file we know that chapters are marked by “CHAPTER [number]” at the beginning. Thusly, we check for that with the if statement. Once that requirement has been met we strip the line of any periods following the chapter number. This is, fairly obviously, to keep the chapter titles all neat and tidy within the dictionary. In the same line we define a variable to contain the chapter numbers as “numeral” (as Project Gutenberg tends to use roman numerals). Finally, we use that chapter number as the value position for every chapter within the dictionary index. 
"""

starts = sorted(header_position.values())
ends = starts[1:] + [end]

"""
Tutorial Part 4:
These lines are fairly straightforward. Naturally, I want the chapters to be sorted by their number values, that is typically how a book is structured. Thus, we have the “starts” line to sort the chapters by numerical values. The “ends” line, predictably, then figures out when the chapter should end. Shifting the position by one after the “CHAPTER” start. This is to solve a problem with the very end of the previous chapter being paired with the next. This way, the chapter ends right when the next begins.
"""

rows = []
for number, (start, stop) in enumerate(zip(starts, ends), start=1):
    chapter_lines = lines[start:stop]
    text = "".join(chapter_lines)

"""
Tutorial Part 5:
This part of the code is concerned with taking the groundwork we established in the previous sections and taking the chapter lines and joining them together into one massive text block. Essentially, this takes the individual chapter lines and sticks them back together into one large chapter block. This isn’t all this block is doing, however, the “rows” line collects the data for the csv spreadsheet in a list. This will be called upon later on within the for loop. 
"""

    filename = f"Dracula-Chapter-{str(number).zfill(2)}.txt"
    (OUT_DIR / filename).write_text(text, encoding="utf-8")

"""
Tutorial Part 6:
Here we are adding leading zeroes to the chapter titles, this is to prevent ordering issues with “1” and “10”, for instance, which would be read as identical and come one after another. Doing it this way, we avoid that problem and have each chapter ordered as they’re meant to be! The next line simply takes the chapter text and writes them into a text file in our “frankenstein_chapters” file directory from earlier.
"""

    rows.append([number, len(text), len(text.split()), len(chapter_lines)])

"""
Tutorial Part 7:
This then calls on the rows list from earlier and appends the data into our csv spreadsheet. Specifically it adds the chapter number, the length of the chapter (both the number of characters as well as splitting the chapter text into individual words for an estimated word count), as well as the number lines of text in the chapter. 
"""

with (OUT_DIR / "chapter_counts.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Chapter", "Characters", "Words", "Lines"])
    writer.writerows(rows)

"""
Tutorial Part 8:
This, I think is the part of the code I can explain the least. As this part of it is that I essentially copied and pasted from my notes, both from this class and IS 205, and changed slightly to suit the purposes of this assignment. Essentially, we need to create/open the csv in our target directory so that we can write in the files we’ve created. This also creates the row headers/titles for our data so that we can tell what the numbers in each row signify instead of having a bunch of random unlabeled data in the spreadsheet.
"""

print(f"You did it! {len(rows)} chapters and chapter_counts.csv were written to {OUT_DIR}/")

"""
Tutorial Part 9: This final part of the code just lets me know that everything previously was successful and that the code was properly executed. 
"""
