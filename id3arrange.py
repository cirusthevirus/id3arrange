#!/usr/bin/env python3
'''Sets ID3 tags based on file name for artist and song title. Files are then
ordered based on artist.

Any songs containing the keywords 'original', 'audio', 'premiere' or
'official' are marked invalid and are stored in the directory './_invalid/'
for manual processing. (in order to remove any unwanted 'original mix'
descriptions)
'''

from mutagen.easyid3 import EasyID3
import re
import os

invalid = re.compile('audio|premiere|original|official|lyric', re.IGNORECASE)

def run():
    try:
        os.mkdir('./_invalid')
    except:
        print("_invalid directory already exists.")

    files = [f for f in os.listdir('.') if f[-4:] == ".mp3"]
    tag_list = {}

    for file in files:
        tags = re.split(' - ', file)
        if re.search(invalid, file) or len(tags) != 2:
            os.rename(file, "./_invalid/"+file)
            files.remove(file)
        else:
            tag_list[file] = EasyID3(file)
            tag_list[file]['artist'] = tags[0].strip()
            tag_list[file]['title'] = tags[1][:-4].strip()
            tag_list[file].save()
            try:
                os.mkdir('./'+tags[0])
            except:
                print("Artist folder \'%s\' already exists." % tags[0])
            os.rename(file, "./"+tags[0]+"/"+file)

if __name__ == "__main__":
    save_dir = os.getcwd()

    # Substitute the default path to which your music is downloaded
    directory = "/Users/user/path/to/music"
    os.chdir(directory)

    # Safeguard
    x = input("Working in: %s\nEnter 'continue' to continue.\n" % os.getcwd())
    if x == "continue":
        run()
    os.chdir(save_dir)
