import os
import re
import syncedlyrics

PREFIX_REGEX = re.compile(r"^\d+\.\s*")

directory = "."

for file in os.listdir(directory):
    if not file.endswith(".flac"):
        continue

    clean_query = PREFIX_REGEX.sub("", file)
    clean_query = os.path.splitext(clean_query)[0]

    lrc_filename = os.path.splitext(file)[0] + ".lrc"
    lrc_path = os.path.join(directory, lrc_filename)

    print(f"Filename:  {lrc_filename}")
    print(f"Path: {lrc_filename}")
