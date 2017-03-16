#!/usr/local/bin/python3.6
import subprocess
from os import listdir,path,devnull
from os.path import isfile,join


## definitions

def transcode_file(input_file, output_file, encode_crf, encode_preset):
    # open null device to redirect ffmpeg output
    FNULL=open(devnull,'w')

    subprocess.call(["ffmpeg",
    "-y", # overwrite output files without asking
    "-i",input_file,
    "-map","0", # -map 0 tells ffmpeg to use all streams, instead of just one per type
    "-acodec","copy", # copy, do not transcode audio
    "-scodec","copy", # copy, do not transcode subtitles
    "-vcodec","libx264","-crf",encode_crf,"-preset",encode_preset,
    output_file], # transcode video using libx264
    stdout=FNULL, stderr=subprocess.STDOUT) # redirect output to devnull
    return

## config
# folder options
input_folder="/general/fs1/transcode_input/"
output_folder="/general/fs1/transcode_output/"
# libx264 encoder options
encode_crf="16"
encode_preset="ultrafast"

## main
# get files to process
input_files=listdir(input_folder)

# tell user what we will do
print("Transcoding the following files:")
for entry in input_files:
    print(" - ",join(input_folder,entry))

# process files
#for input_file in input_files:
    #transcode_file(join(input_folder,input_file), join(output_folder,input_file),
    #encode_crf, encode_preset)

print("Transcoding complete.")
