import os
import re
import syncedlyrics

PREFIX_REGEX = re.compile(r"^\d+\.\s*")

directory = "."
view_mode = None

def should_view_lyrics():
    global view_mode
    if view_mode == "all":
        return True
    if view_mode == "skip":
        return False

    while True:
        choice = input("View lyrics? [y]es / [n]o / [a]ll / [s]kip all: ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        if choice in ("a", "all"):
            view_mode = "all"
            return True
        if choice in ("s", "skip"):
            view_mode = "skip"
            return False
        print("Invalid choice. Enter y, n, a, or s.")

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
            if should_view_lyrics():
                print(lrc_data)
        else:
            print(f"No lyrics found for: {clean_query}")
