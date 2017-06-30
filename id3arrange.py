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
import shutil

invalid = re.compile('audio|premiere|original|official|lyric', re.IGNORECASE)
feat = re.compile(' feat | feat. | ft ', re.IGNORECASE)
feat_bis = re.compile('\(feat |\(feat. |\(ft ', re.IGNORECASE)

def run():
    # Scan files from input
    os.chdir(source)
    files = [f for f in os.listdir('.') if f[-4:] == ".mp3"]
    tag_list = {}

    try:
        os.mkdir(os.path.join(destination, '_invalid'))
    except:
        print("_invalid directory already exists.")

    for file in files:
        # Change file name and replace feat flag with 'ft.'
        os.rename(file, re.sub(feat, ' ft. ', file))
        file = re.sub(feat, ' ft. ', file)
        os.rename(file, re.sub(feat_bis, '(ft. ', file))
        file = re.sub(feat_bis, '(ft. ', file)

        tags = re.split(' - ', file)
        if re.search(invalid, file) or len(tags) != 2:
            os.rename(file, os.path.join(destination, "_invalid", file))
            files.remove(file)
        else:
            tag_list[file] = EasyID3(file)

            # Process artist name
            artist_name = tags[0].strip()
            tag_list[file]['artist'] = artist_name

            # Process song title
            title_name = tags[1].strip()
            tag_list[file]['title'] = title_name
            tag_list[file].save()

            try:
                os.mkdir(os.path.join(destination, tags[0]))
            except:
                print("Artist folder \'%s\' already exists." % tags[0])
            shutil.copy2(file, os.path.join(destination, tags[0], file))

if __name__ == "__main__":
    save_dir = os.getcwd()
    source = "/path/to/music/source"
    destination = "/path/to/music/destination"
    print("Working with source:\t\t %s" % source)
    print("Working with destination:\t %s" % destination)
    x = input("Enter 'continue' to continue.\n")
    if x == "continue":
        run()
    os.chdir(save_dir)
