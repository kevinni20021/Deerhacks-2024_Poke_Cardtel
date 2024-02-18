import csv
import time

import requests
import os


def download_image(data):
    current_time = int(time.time())
    filename = f"PSA_{data[1]}_EX{current_time}.jpg"
    cwd = os.getcwd()

    try:
        response = requests.get(data[0])
        response.raise_for_status()
        content_type = response.headers.get('content-type', '')

        if content_type.startswith('image'):
            folder_name = filename[:5]
            if filename.startswith("PSA_10"):
                folder_name = filename[:6]

            folder_path = os.path.join(cwd, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            with open(os.path.join(folder_path, filename), 'wb') as f:
                f.write(response.content)

            print(f"Image downloaded successfully: {filename}")
        else:
            print(f"Response does not contain an image: {data[0]}")
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download image: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to make request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_csv(fname: str):
    with open(fname, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == "0" or row[1] == "0":
                pass
            elif len(row) == 2 and row[1].isnumeric():
                print('yes')
                try:
                    download_image(row)
                except:
                    pass


read_csv("images/data0.csv")

