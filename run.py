import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from internetarchive import get_item
from queue import Queue

def check_website_availability(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Website is available.")
                return True
            else:
                print(f"Website is not responding properly. Status code: {response.status_code}")
                print("Retrying in 1 minute...")
                time.sleep(60)  # Wait for 1 minute before retrying
        except Exception as e:
            print(f"Error occurred while checking website availability: {str(e)}")
            print("Retrying in 1 minute...")
            time.sleep(60)  # Wait for 1 minute before retrying

def download_file(item, file, output_directory, retry_attempts=5):
    file_name = file['name']
    file_path = os.path.join(output_directory, file_name)
    
    for attempt in range(retry_attempts):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)  # Remove the existing file to ensure overwrite
                print(f"Removed existing file: {file_path}")
                
            print(f"Downloading {file_name} (attempt {attempt+1})...")
            item.download(files=[file_name], destdir=output_directory, verbose=True)
            print(f"Download of {file_name} successful!")
            return True
        except Exception as e:
            print(f"Download failed: {str(e)}. Retrying in 10 seconds...")
            time.sleep(10)
    print(f"Failed to download {file_name} after {retry_attempts} attempts.")
    return False

def download_cdlc_collection():
    website_url = 'https://archive.org/details/rocksmithcdlccollection'
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist

    print("Checking website availability...")
    while not check_website_availability(website_url):
        pass  # Keep retrying until website is available

    print("Starting download process...")
    try:
        item = get_item('rocksmithcdlccollection')
        files = item.files
        files_to_download = [file for file in files if file['format'] != 'Metadata']

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_file = {executor.submit(download_file, item, file, output_directory): file for file in files_to_download}
            for future in as_completed(future_to_file):
                file = future_to_file[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"Exception occurred while downloading {file['name']}: {e}")
        
        print("All downloads completed!")
    except Exception as e:
        print(f"Download failed: {str(e)}")

# Call the function to start the download attempt
download_cdlc_collection()
