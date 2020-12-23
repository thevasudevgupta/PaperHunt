# __author__ = "Vasudev Gupta"

import os
import pickle
import webbrowser

def save_pickle(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def load_pickle(path="database/database.pickle"):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def open_link(link):
    print(f"opening {link} in your default browser")
    webbrowser.open(link)

def makedirs(directory):
    if directory not in os.listdir():
        os.makedirs(directory)
