from boto3 import client
import argparse
import subprocess
import os

def aws_polly_tts(input_msg, index, voice_id, engine):
    polly = client('polly', region_name='eu-west-1')

    response = polly.synthesize_speech(
            Text=input_msg,
            Engine=engine,
            OutputFormat='mp3',
            VoiceId=voice_id)

    stream = response.get('AudioStream')

    with open('/tmp/polly_' + str(index) + '.mp3', 'wb') as f:
        data = stream.read()
        f.write(data)

def input_splitter(message, voice_id, engine, player, speed):
    split_size = 3000

    # split input_msg into 3000 characters string variables and store them in an array
    input_msg_split = [message[i:i + split_size] for i in range(0, len(message), split_size)]

    # for each item in input_msg_split call aws_polly_tts
    for i, item in enumerate(input_msg_split):
        aws_polly_tts(item, i, voice_id, engine)
        if player == 'mpv':
            subprocess.call([player, '--speed=' + speed, '/tmp/polly_' + str(i) + '.mp3'])
        else:
            subprocess.call([player, '/tmp/polly_' + str(i) + '.mp3'])

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
    parser = argparse.ArgumentParser(prog='polly-cli', description='Amazon Polly Text-to-Speech in the terminal')
    parser.add_argument('-e', '--engine', default='neural', help='Select an engine (standard or neural)')
    parser.add_argument('-p', '--player', default='mpv', help='Select a player (mpv, vlc, mplayer, etc.)')
    parser.add_argument('-s', '--speed', default='1', help='Select the playback speed (only supported by mpv))')
    parser.add_argument('-v', '--voice', default='Salli', help='Select a voice (voice list available at https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)')
    args = parser.parse_args()

    input_msg = input_parser()

    if args.voice:
        print("Voice: " + args.voice + " & " + "Engine: " + args.engine)
        input_splitter(input_msg, args.voice, args.engine, args.player, args.speed)
