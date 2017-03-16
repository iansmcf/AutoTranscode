#!/usr/local/bin/python3.6
import subprocess
from os import listdir,path,devnull
from os.path import isfile,join
from email_alert import email_alert
import time


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
# email target
recipient_email = open('./email.txt', 'r').read()
sender_name="Recall"
timestamp=time.strftime('%b %d, %H:%M')

## main
# get files to process
input_files=listdir(input_folder)

# tell user what we will do
alert_string="\n"


print("Transcoding the following files:")
for entry in input_files:
    print(" - ",join(input_folder,entry))
    # also add the files to the list
    alert_string=alert_string+entry+"\n"

# send email about the start of the transcode
email_alert(recipient_email,sender_name,"Transcode starting " + timestamp,
            "Beginning transcode for the following files:\n"+alert_string)

# process files
for input_file in input_files:
    transcode_file(join(input_folder,input_file), join(output_folder,input_file),
    encode_crf, encode_preset)

print("Transcoding complete.")
email_alert(recipient_email,sender_name,"Transcode starting " + timestamp,
            "Finished transcode for the following files:\n"+alert_string)
