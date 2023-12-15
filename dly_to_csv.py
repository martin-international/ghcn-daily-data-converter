import os
import tkinter as tk
from tkinter import filedialog
import concurrent.futures
import logging

class GHCNDParser:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_file = os.path.join(output_folder, 'merged_data.csv')

    @staticmethod
    def parse_line(line, day):
        """
        Efficiently parses a single line from a .dly file and returns structured data.
        Converts values of -9999 to 'None'.
        """
        date = f"{line[11:15]}-{line[15:17]}-{str(day).zfill(2)}"
        value = line[21 + (day - 1) * 8:21 + (day - 1) * 8 + 5]
        value = 'None' if value == '-9999' else value
        return [line[0:11], date, line[17:21], value, line[21 + (day - 1) * 8 + 5],
                line[21 + (day - 1) * 8 + 6], line[21 + (day - 1) * 8 + 7]]

    def process_file(self, file_path):
        """
        Process a single .dly file and write the results to the CSV file in a streaming fashion.
        """
        with open(file_path, 'r') as file, open(self.output_file, 'a') as output:
            for line in file:
                for day in range(1, 32):
                    parsed_data = self.parse_line(line, day)
                    output.write(','.join(parsed_data) + '\n')

    def process_dly_files(self):
        """
        Process all .dly files in the input folder using concurrent processing.
        Writes header comments to the CSV file for clarity.
        """
        file_paths = [os.path.join(self.input_folder, f) for f in os.listdir(self.input_folder) if f.endswith('.dly')]
        
        # Write header to the CSV file
        header_comments = [
            "ID: Station identification code.",
            "Date: Date of observation in YYYY-MM-DD format.",
            "Element: Type of observation (e.g., PRCP for Precipitation).",
            "Value: Observation value (e.g., temperature in tenths of degrees C, 'None' if missing).",
            "MFlag: Measurement flag.",
            "QFlag: Quality flag.",
            "SFlag: Source flag.",
            "Refer to the GHCN Daily Readme for detailed descriptions: https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt"
        ]

        with open(self.output_file, 'w') as f:
            for comment in header_comments:
                f.write(f"# {comment}\n")
            f.write("ID,Date,Element,Value,MFlag,QFlag,SFlag\n")
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [executor.submit(self.process_file, file_path) for file_path in file_paths]
            concurrent.futures.wait(futures)

        logging.info("Data processing completed.")

def select_directory(title):
    """
    Opens a Tkinter dialog to select a directory.
    """
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()
    return folder_path

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    input_folder = select_directory("Select the Input Folder")
    output_folder = select_directory("Select the Output Folder")

    if input_folder and output_folder:
        parser = GHCNDParser(input_folder, output_folder)
        parser.process_dly_files()
    else:
        logging.info("Input folder or output file not selected. Exiting.")

if __name__ == '__main__':
    main()
