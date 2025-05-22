"""
<Project Title>


Copyright (c) 2021 -- This is the 2021 Spring B version of the Template
Licensed
Written by <> Likhith Sai Challa

# you can also rely on the docstring documentation from pandas on how to format dosctrings:
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html

"""

import pandas as pd

def read_csv_file(file_path):
    """
    Reads a CSV file from the specified file path into a pandas DataFrame.

    Args:
    file_path (str): The path to the CSV file to be read.

    Returns:
    DataFrame or None: A pandas DataFrame containing the data from the CSV file, or None if an error occurs.
    """
    try:
        data_frame = pd.read_csv(file_path)
        return data_frame
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_txt_file(file_path, delimiter="|", quotechar=None):
    """
    Imports a TXT file into a pandas DataFrame by treating it as a table with a specified delimiter and optional quote character.

    Args:
    file_path (str): The path to the TXT file.
    delimiter (str): The delimiter used to split the lines.
    quotechar (str or None): Character used to denote the start and end of a quoted item.

    Returns:
    DataFrame or None: A pandas DataFrame containing the TXT file data, or None if an error occurs.
    """
    try:
        data_frame = pd.read_csv(file_path, delimiter=delimiter, quotechar=quotechar, engine='python')
        return data_frame
    except Exception as e:
        print(f"Error while reading TXT file: {e}")
        return None
    
def read_json_file(file_path):
    """
    Imports a JSON file into a Python data structure.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    DataFrame or None: A pandas DataFrame or None if an error occurs.
    """
    try:
        data_frame = pd.read_json(file_path)
        return data_frame
    except Exception as e:
        print(f"Error while reading JSON file: {e}")
        return None

def read_excel_file(file_path, sheet_name='Sheet1', usecols=None, skiprows=0):
    """
    Imports an Excel file into a pandas DataFrame.

    Args:
    file_path (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to import.
    usecols (list or None): The columns to parse.
    skiprows (int): The number of rows at the top of the sheet to skip.

    Returns:
    DataFrame or None: A pandas DataFrame containing the Excel sheet data, or None if an error occurs.
    """
    try:
        data_frame = pd.read_excel(file_path, sheet_name=sheet_name, usecols=usecols, skiprows=skiprows)
        return data_frame
    except Exception as e:
        print(f"Error while reading Excel file: {e}")
        return None

if __name__ == '__main__':
    # Derive the file paths
    csv_file = "/Users/challalikhithsai/Downloads/Week 2/Module2/Neural_data.csv"
    txt_file = "/Users/challalikhithsai/Downloads/Week 2/Module2/network_data.txt"
    json_file = "/Users/challalikhithsai/Downloads/Week 2/Module2/nested_data.json"
    excel_file = "/Users/challalikhithsai/Downloads/Week 2/Module2/Excel_report.xlsx"

    # Import data using the defined functions
    csv_data = read_csv_file(csv_file)
    txt_data = read_txt_file(txt_file)  # Update the delimiter as needed
    json_data = read_json_file(json_file)
    excel_data = read_excel_file(excel_file, sheet_name='financials', usecols='M:AS', skiprows=24)

    # Print data previews
    print("CSV Data Preview:", csv_data.head() if csv_data is not None else "Failed to load data.")
    print("TXT Data Preview:", txt_data.head() if txt_data is not None else "Failed to load data.")
    print("JSON Data Preview:", json_data.head() if json_data is not None else "Failed to load data.")
    print("Excel Data Preview:", excel_data.head() if excel_data is not None else "Failed to load data.")
    
    
    
    
    
    
    
  

