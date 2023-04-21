"""
Author: Clayton King
Date: Fri 21 Apr 2023 09:02:00
Description: A simple YouTube video downloader.
"""

import argparse
import os
from time import sleep

from pytube import YouTube
import pytube.exceptions


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("link", type=str, help="Video Link")
    parser.add_argument("path", type=str, nargs="?", default=os.getcwd(),
                        help="Video Download (default is cwd)")
    args = parser.parse_args()
    return args.link, args.path


def get_user_choice(message, valid_choices):
    """Asks the user for input and returns it if it's a valid choice."""

    user_choice = input(message)
    while user_choice not in valid_choices:
        print("\nPlease enter a valid choice.")
        user_choice = input(message)
    return user_choice


def create_directory(path):
    """Creates a directory if it doesn't exist."""

    if not os.path.exists(path):
        print(f"\nCould not find the directory {path}")

        choice = get_user_choice(
            "Would you like to create it? (y/n) ", ['y', 'Y', 'n', 'N'])

        if choice in {"y", "Y"}:
            print("\nAttempting to create directory...")
            try:
                os.makedirs(path)
                sleep(1)
                print(f"Created {path}")
            except OSError:
                print(f"Failed to create {path}")
                exit(1)
        elif choice in {"n", "N"}:
            print("\nYou chose not to create the directory. Exiting...")
            exit(1)

    else:
        print(f"\nFound directory {path}")

def download_video(stream, path):
    print(f"\nDownloading Video...")
    stream.download(output_path=path)
    print(f"Successfully Downloaded Video To {path}")

def process_video(path, yt, choice):
    """Download video or audio based on user's choice."""
    try:
        if int(choice) == 1:
            download_video(yt.streams.get_highest_resolution(), path)
        elif int(choice) == 2:
            download_video(yt.streams.get_audio_only(), path)

    except pytube.exceptions.VideoUnavailable as e:
        print(f"Error: {e}")




def main():
    link, path = parse_arguments()

    try:
        yt = YouTube(link)
        create_directory(path)
        choice = get_user_choice(f"\nChoose An Option:\n"
                        "1. Download Video\n"
                        "2. Download Audio\n"
                        "=> ", ['1', '2'])
        process_video(path, yt, choice)
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable) as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
