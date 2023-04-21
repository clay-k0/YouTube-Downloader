# YouTube-Downloader
A command-line tool to download YouTube videos (shorts included) using the `pytube` library.

## Requirements

- Python 3.6 or later
- Run `pip install -r requirements.txt` to install the necessary dependencies

## Usage

`python downloader.py <link> [path]\`
or\
`python3 downloader.py <link> [path]`

`<link>`: Required. The link of the YouTube video to download.\
`[path]`: Optional. The path to the directory where the video will be downloaded. Default is the current working directory.

When you run the script, you will be prompted to choose between downloading the video or audio of the YouTube video.

## Example

`python3 downloader.py https://www.youtube.com/watch?v=Ekd9rPGzbVs Videos`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
