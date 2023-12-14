import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from colorama import *
import argparse
import json
import sys

root = tk.Tk()
root.withdraw()
init(autoreset=True)
link_type_default = True

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


with open('settings.json') as json_file:
    # Load the JSON data
    data = json.load(json_file)

type_types = []
filepath = data['filepath']
types = []

def sort_large_text_file(input_file, chunk_size=1000000):
    with open(input_file, 'rb') as infile:
        lines = infile.readlines()

    lines = [line.decode('utf-8', errors='ignore') for line in lines]
    lines.sort()

    with open(input_file, 'wb') as outfile:
        outfile.writelines(line.encode('utf-8') for line in lines)

def logext():
    global type_types
    global link_type_default

    print(f"""
{Fore.BLUE}
               __                             
  ____ ___  __/ /_____  ____ _________  ____ 
 / __ `/ / / / __/ __ \/ __ `/ ___/ _ \/ __ |
/ /_/ / /_/ / /_/ /_/ / /_/ / /  /  __/ /_/ /
\__,_/\__,_/\__/\____/\__, /_/   \___/ .___/ 
                     /____/         /_/      
{Style.RESET_ALL}
    """)

    file = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        initialdir=filepath,
    )
    if not file:
        print(f"[{Fore.RED}ERROR{Style.RESET_ALL}] FILE PATH NOT SPECIFIED")
        exit()

    print(f"[{Fore.GREEN}INFO{Style.RESET_ALL}] {file} selected")
    
    for subtype in data['types']['premade'].keys():
        type_types.append(subtype)
    print(f"[{Fore.CYAN}ACTION{Style.RESET_ALL}] Choose an option \n")
    for i in range(len(type_types)):
        print(f"{i+1}. {type_types[i].capitalize()}")

    option = int(input("> "))
    option = option-1

    selected_option = type_types[option]
    print(f"The {selected_option} set is selected!")
    premade_types = data['types']['premade'][selected_option]

    time.sleep(0.5)
    serial_number = int(time.time())
    os.makedirs(f"{filepath}/{serial_number}")
    if data['verbose'] == "True":
    
        print(f"[{Fore.RED}DEBUG{Style.RESET_ALL}] FILE_PATH = {file} ") 
        print(f"[{Fore.RED}DEBUG{Style.RESET_ALL}] FOLDER_NAME = {serial_number} ")
        print(f"[{Fore.RED}DEBUG{Style.RESET_ALL}] SELECTED_TYPE = {selected_option} ")
        if len(types) == 0:
            print(f"[{Fore.RED}DEBUG{Style.RESET_ALL}] SELFMADE_TYPES = Empty ")
        else:
            print(f"[{Fore.RED}DEBUG{Style.RESET_ALL}] SELFMADE_TYPES = {types} ")
    elif data['verbose'] == "False":
        pass
    else:
        print(f"[{Fore.RED}ERROR{Style.RESET_ALL}] SELFMADE_TYPES = {types} ")
    if link_type_default == False:
        for type_index in range(len(types)):
            print(f"[{Fore.GREEN}INFO{Style.RESET_ALL}] Start {Fore.CYAN}{types[type_index]}{Style.RESET_ALL} grepping...")
            if os.name == "nt":
                baseStr = f'grep -a "{premade_types[type_index]}" {os.path.basename(file)} > {filepath}/{serial_number}/{premade_types[type_index]}.txt'
                os.system(f"{baseStr}")
            else:
                os.system(f'grep -a "{premade_types[type_index]}" {os.path.basename(file)} > {filepath}/{serial_number}/{premade_types[type_index]}.txt')

        print(f"[{Fore.RED}EXIT{Style.RESET_ALL}] Program")
        time.sleep(1)
    else:
        for type_index in range(len(premade_types)):
            print(f"[{Fore.GREEN}INFO{Style.RESET_ALL}] Start {Fore.CYAN}{premade_types[type_index]}{Style.RESET_ALL} grepping...")
            if os.name == "nt":
                baseStr = f'grep -a "{premade_types[type_index]}" {os.path.basename(file)} > {filepath}/{serial_number}/{premade_types[type_index]}.txt'
                os.system(f"{baseStr}")
            else:
                os.system(f'grep -a "{premade_types[type_index]}" {os.path.basename(file)} > {filepath}/{serial_number}/{premade_types[type_index]}.txt')

        print(f"[{Fore.GREEN}COMPLETE{Style.RESET_ALL}] Closing Program...")
        time.sleep(1)
try:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description='Sort a large text file in-place.')
        parser.add_argument('input_file', type=str, help='Path to the input text file')
        args = parser.parse_args()

        input_file = args.input_file
        sort_large_text_file(input_file)
        print("Sorting file...")
        logext()
    else:
        logext()
except KeyboardInterrupt:
    exit()