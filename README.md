# Rocksmith Custom DLC Downloader

This program allows users to download over 62,000 custom songs for Rocksmith from the Internet Archive. It ensures robust downloading with retries and concurrent downloads to speed up the process.

## Features

- Downloads over 62,000 custom songs for Rocksmith.
- Concurrent downloads to speed up the process.
- Automatic retries for failed downloads.
- Removes existing files before downloading to ensure the latest version is obtained.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `internetarchive`, `concurrent.futures`

You can install the required packages using the following command:

```bash
pip install requests internetarchive
```

## Usage

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed.
3. Install the required Python packages as mentioned above.
4. Run the `run.py` script to start the download process.

### Running the Script

You can run the script using the following command:

```bash
python run.py
```

The script will:

1. Check the availability of the Internet Archive page.
2. Download the custom songs to the `output` directory.

## Credit

This program utilizes the Rocksmith Custom DLC Collection hosted on the Internet Archive by Deus Deceptor. You can visit their profile [here](https://archive.org/details/@deusdeceptor).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This tool is intended for personal use only. Please respect the rights of the content creators and the terms of service of the Internet Archive.
