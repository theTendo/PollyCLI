# Polly CLI

This tool allows the interaction with the Amazon Polly TTS service from a Linux command line.

```
usage: polly.py [-h] [--voice VOICE]

Amazon Polly Text-to-Speech in the terminal

options:
  -h, --help     show this help message and exit
  --voice VOICE  Select a voice
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
