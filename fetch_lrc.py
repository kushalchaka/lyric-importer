import os
import re
import syncedlyrics

PREFIX_REGEX = re.compile(r"^\d+\.\s*")

directory = "."

for root, _, files in os.walk(directory):
    for file in files:
        if not file.endswith(".flac"):
            continue

        clean_query = PREFIX_REGEX.sub("", file)
        clean_query = os.path.splitext(clean_query)[0]

        lrc_filename = os.path.splitext(file)[0] + ".lrc"
        lrc_path = os.path.join(root, lrc_filename)

        print(f"Filename:  {lrc_filename}")
        print(f"Path: {lrc_filename}")

        if os.path.exists(lrc_path):
            print(f"Skipping (already exists): {lrc_filename}")
            continue

        print(f"Searching lyrics for: '{clean_query}'...")

        lrc_data = syncedlyrics.search(clean_query, save_path=lrc_path)

        if lrc_data:
            print(f"Successfully saved: {lrc_filename}")
        else:
            print(f"No lyrics found for: {clean_query}")
