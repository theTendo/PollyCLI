from boto3 import client
import argparse
import subprocess
import os

def aws_polly_tts(input_msg, voice_id, index):
    polly = client('polly', region_name='eu-west-1')

    response = polly.synthesize_speech(
            Text=input_msg,
            Engine='neural',
            OutputFormat='mp3',
            VoiceId=voice_id)

    stream = response.get('AudioStream')

    with open('/tmp/polly_' + str(index) + '.mp3', 'wb') as f:
        data = stream.read()
        f.write(data)

def input_splitter(input_msg, voice_id):
    split_size = 3000

    # split input_msg into 3000 characters string variables and store them in an array
    input_msg_split = [input_msg[i:i + split_size] for i in range(0, len(input_msg), split_size)]

    # for each item in input_msg_split call aws_polly_tts
    for i, item in enumerate(input_msg_split):
        aws_polly_tts(item, voice_id, i)
        subprocess.call(['mpv', '/tmp/polly_' + str(i) + '.mp3'])

    os.system('cls' if os.name == 'nt' else 'clear')

def input_parser():
    print("Enter text (use Ctrl-D to send it):")
    contents = []

    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    # convert list to string
    return ''.join(contents)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Amazon Polly Text-to-Speech in the terminal')
    parser.add_argument('--voice', help='Select a voice')
    args = parser.parse_args()
    input_msg = input_parser()
    if args.voice:
        print("Voice: " + args.voice)
        input_splitter(input_msg, args.voice)
    else:
        print("Voice: Salli")
        input_splitter(input_msg, 'Salli')