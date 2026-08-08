# Name: Torin DeBlieck
# OSU Email: debliect@oregonstate.edu
# Course: CS361 - Software Engineering I
# Assignment: Assignment 9: Big Pool Implementation, Integration (Milestone #3) [Portfolio]
# Due Date: 8/10/2026

import time
import os

while True:
    try:
        with open("file_checker.txt", "r") as file:
            filename = file.read().strip()
            time.sleep(0.5)

        if filename and "CHECK_DONE" not in filename:
            if os.path.exists(filename): # Check if the requested text file exists.
                response = "Text file is found."
            else:
                response = "Text file not found."

            with open("file_checker.txt", "w") as file:
                file.write("CHECK_DONE\n") # Sends back Check Done back to program.
                file.write(response + "\n") # Appends the status answer below.
    except FileNotFoundError:
        # If the file is deleted, safely skip and do not crash
        pass
    time.sleep(0.1)