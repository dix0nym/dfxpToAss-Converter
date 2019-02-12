﻿import argparse
import os
import re

from bs4 import BeautifulSoup as bs

__author__ = 'EngelEatos'

header = """
[Script Info]
; Script generated by Aegisub 3.0.4
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes
Video Zoom: 6
Scroll Position: 828
Active Line: 748
YCbCr Matrix: TV.601
Video Zoom Percent: 1
Aegisub Scroll Position: 81
Aegisub Active Line: 87
Aegisub Video Zoom Percent: 1.000000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Chinacat,68,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,3,1.5,2,15,15,15,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def main():
    """main"""
    parser = argparse.ArgumentParser(description="convert dfxp to ass")
    parser.add_argument(
        "-i",
        dest="input",
        required=True,
        help="input dfxp file",
        metavar="INPUT")
    parser.add_argument(
        "-o",
        dest="output",
        required=True,
        help="output ass file",
        metavar="OUTPUT")
    args = parser.parse_args()
    if not os.path.isfile(args.input):
        parser.error("input file {} does not exists!".format(args.input))
    with open(args.input, 'r') as input_file:
        input_data = input_file.read()
    soup = bs(input_data, 'html.parser')
    p_elements = soup.find('div', attrs={'xml:lang': 'de'}).find_all('p')
    with open(args.output, 'w+') as output_file:
        output_file.write(header)
        for element in p_elements:
            output = "Dialogue: 0,{},{},Main Dialog,,0,0,0,,{}\n".format(
                element.get('begin'), element.get('end'),
                re.sub(r"\s+", " ", element.text).strip())
            output_file.write(output)


if __name__ == '__main__':
    main()
