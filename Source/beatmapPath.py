import os
import pywinauto
import sys
from tqdm import tqdm

# ------------------
# Beatmap Path
# ------------------   
beatmap_path = ""
file = ""
print("Searching for beatmap...")

# Connect to Osu! application
app = pywinauto.Application(backend="uia").connect(title_re=".*osu!.*")
osu_window = app.top_window()

# Get the application name
app_name = osu_window.window_text()
# print(f"Application name: {app_name}")

# Get the user's home directory
user_home_dir = os.path.expanduser("~")

# Build the osu! Songs folder path
songs_folder_path = os.path.join(user_home_dir, "AppData", "Local", "osu!", "Songs")

# Extract the necessary information from the string
song_info = app_name
try:
    song_info_list = song_info.split(" - ")
    mapper_name, song_name, diff_name = song_info_list[1], song_info_list[2].split(" [")[0], song_info_list[2].split(" [")[1][:-1]
except IndexError:
    print("Error: Can't detect beatmap.")
    print("Please select in beatmap editor.\n")
    input("Press Enter to exit...")
    sys.exit()


# Loop through all subdirectories of the Songs folder
for root, dirs, files in tqdm(os.walk(songs_folder_path, topdown=True)):
    # Check if the name of the folder contains artist_name and song_name
    if mapper_name in root or song_name in root:
        # Check if the beatmap name is in any of the files in the current directory
        for file in files:
            if mapper_name in file and song_name in file and diff_name in file:
                # Print the full path to the beatmap file and stop searching
                beatmap_path = os.path.join(root, file)
                print()
                print("Beatmap found at:", beatmap_path)
                break
        else:
            # Continue searching in the next subdirectory
            continue
        # Stop searching if the beatmap was found
        break
else:
    # Print a message if the beatmap was not found
    print("Beatmap not found.")
