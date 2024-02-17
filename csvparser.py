import csv
import time

import requests
import os


def download_image(data):
    current_time = int(time.time())  # Get current timestamp
    filename = f"PSA_{data[1]}_EX{current_time}.jpg"
    cwd = os.getcwd()

    response = requests.get(data[0])
    folder_name = filename[:5]  # Default to first 5 characters
    if filename.startswith("PSA_10"):
        folder_name = filename[:6]  # Use first 6 characters if filename starts with "PSA_10"

    try:
        folder_path = os.path.join(cwd, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(os.path.join(folder_path, filename), 'wb') as f:
            f.write(response.content)

        print(f"Image downloaded successfully: {filename}")
    except Exception as e:
        print(f"Failed to download image: {e}")


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


read_csv("C:\\Users\\KAIXI\\PycharmProjects\\WebscraperV2\\data1.csv")

