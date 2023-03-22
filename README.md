# Polly CLI

This tool allows the interaction with the Amazon Polly TTS service from a Linux command line.

```
usage: polly-cli [-h] [-e ENGINE] [-p PLAYER] [-s SPEED] [-v VOICE]

Amazon Polly Text-to-Speech in the terminal

options:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        Select an engine (standard or neural)
  -p PLAYER, --player PLAYER
                        Select a player (mpv, vlc, mplayer, etc.)
  -s SPEED, --speed SPEED
                        Select the playback speed (only supported by mpv))
  -v VOICE, --voice VOICE
                        Select a voice (voice list available at https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)
```

https://user-images.githubusercontent.com/2078392/211122803-04dd8c27-b5dc-41ef-931c-55932676f442.mp4

## Installation

### AWS Configuration
You need to have an AWS account and configure your credentials. You can do this by running the following command:

`aws configure`

Then install the required libraries with:

`pip install -r requirements.txt`

## Tip

You can create a file `/usr/bin/polly` with the following content:

`python3 /path/to/script/polly.py $1 $2`

And use it by calling `polly` from the command line.
