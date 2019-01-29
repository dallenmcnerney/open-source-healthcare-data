import urllib
import os


def save_web_file(url, output_name, file_destination=None):
    if file_destination is None:
        file_destination = os.getcwd()
    file = urllib.request.urlopen(url)
    data = file.read()
    with open(os.path.join(file_destination, output_name), 'wb') as write_file:
        write_file.write(data)
