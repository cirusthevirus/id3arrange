# id3arrange.py
Simple maintenance program I quickly wrote to sort my music and rewrite id3 tags to make sure the music is properly organised before being uploaded to my phone.

## Description
Reads mp3 files in the source directory and rewrites id3 tags based on file name. Note that some filenames are flagged as invalid if some keywords are encountered. This was added to ensure no erroneous data is written to the id3 tags (as I can be distracted and forget to correct filenames when downloading music). The files are then reordered into subdirectories based on artist name. This follows the iTunes "convention" while omitting sub-ordering by album name.

### Note
The path of the source directory is hard-coded into the program and must be modified for each individual person. I did this as my music gets downloaded to a specific folder automatically and I therefore do not require to change this path on the fly.
