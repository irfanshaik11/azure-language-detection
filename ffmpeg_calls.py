# FFMPEG is an open source audio/video file processing tool
# This file contains all the calls to FFMPEG

import subprocess
import os

import logging
logging.basicConfig(filename='./logs/example.log',level=logging.DEBUG)
# Log format
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

#dtermines the length of an input file
def retrieve_len(filepath):
    log.info("Retrieving length for " + filepath)
    temp = float(subprocess.check_output(["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(filepath)]))
    return int(temp)

#Creates a shortened file given an input file, an output filename, and a text file containing cutpoints
# This is used to cut multiple segments out of a video/audio file
def create_shortened_file(cutpoints_file_directory, target_directory, outputfile, cutpoints_filename="cutpoints.txt"):
    cutpoints_filepath = cutpoints_file_directory + "/" + cutpoints_filename
    output_filepath = target_directory + "/" + outputfile
    log.info("Ran command")
    log.info("ffmpeg -f concat -i "+ cutpoints_filepath + " " + output_filepath + " -y")
    subprocess.check_output(["ffmpeg", "-f", "concat", "-i", cutpoints_filepath, output_filepath, "-y"])
#Dumps information on stream number and type to a text file given an input file
def dump_streams_metadata(filepath, WAV_directory):
    # print("ffmpeg is calling" + filepath)
    # os.system("ffmpeg -i \"" + str(filepath) + "\" &>streams.txt")  #

    command = ['ffprobe', '-i', filepath]
    p = subprocess.Popen(command, stderr=subprocess.PIPE)
    text = p.stderr.readlines()
    w = open(WAV_directory + "/" +"streams.txt", "w+")
    for l in text:
        w.write(str(l) + "\n")
    w.close()

# Shortens a given file given a startime and a length
# This is used to cut out one segment out of a video/audio file
def shorten_file(end_directory, starttime, filename, cuttosize, i, outfile_name = None):
    strm = "0:" + i

    if outfile_name == None:
        end_file = end_directory + "/" + i + "output.wav"
    else:
        end_file = end_directory + "/" + outfile_name


    print ("ffmpeg -ss " + str(starttime) + " -i \"" + str(filename) + "\" -t " + str(
        cuttosize) + " -map " + strm + " " + end_file + " -y")

    axws = "ffmpeg -ss " + str(starttime) + " -i \"" + str(filename) + "\" -t " + str(
        cuttosize) + " -map " + strm + " " + end_file + " -y"
    os.system(axws)

def shorten_file_with_specified_outfile(starttime, filename, cuttosize, i, outfile):
    strm = "0:" + i
    axws = "ffmpeg -ss " + str(starttime) + " -i \"" + str(filename) + "\" -t " + str(
        cuttosize) + " -map " + strm + " " + "" + outfile + " -y"
    os.system(axws)
