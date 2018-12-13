
Audio Detection Project
======================
* This project was created to automate  language detection on NBC's video assets. Given a video file with multiple audio streams as input, this project will give a detected language and a confidence score for each audio stream in the video file. 
* This project uses an S3 Bucket to store the initial video file, an EC2 Instance to shorten the video file, and Microsoft Azure Video Indexer to retrieve langauge and confidence of the given file
* The files included with this readme are all executed by the EC2 instance, there is also an included Microsoft Azure Video Indexer API (API directory, azure_api.py file).

Getting Started
============
* Steps to Run Locally:
1. pip install requirements.txt
2. Put an MP4 file into S3-Files folder.
3. Run ./detection.py in terminal

* Steps to Run on AWS:


Prerequisites
===========
*Requirements to Run Locally:
1. Install all modules in Requirements.txt
2. Install Python 3.7

*Requirements to Run on AWS:


Built With
=========
* Azure Video Indexer - https://api-portal.videoindexer.ai
* Amazon EC2 Bucket
* Amazon EC3 Instance
* Voice Activity Detector (by Alexander Usoltsev) - https://github.com/marsbroshok/VAD-python

Basic Idea
==========
1. Convert Audio File to WAV File and Cut it into a 20 min - 2 Hour Segment at a random point
2. Run Voice Activity Detecor on WAV File to generate an array with voice acitivty clusters:
    * Steps to VAD:
    1. Convert Stero to Mono
    2. Move a window of 20 ms along the audio data
    3. Calculate the ration between energy of speech band and total energy for speech window
    4. If ratio is more than threshold (0.6 by default) label windows as speech
    5. Apply median fileter with length of 0.5s to smooth the detection speech regions
    6. Represend speech regions as intervals of time
3. Run a 20 second window along the array to determine the 20 sec segment with clearest audio
4. Combine top 15 clearest audio segments to generate a 5 minute clip
5. Feed clip to Azure to dertermine language
6. Store language and confidence to database

Authors
=========
Irfan Shaik (MediaTech Intern) - irfanshaik11@gmail.com
Sheik Hassan (CoreTech Engineer) - email
