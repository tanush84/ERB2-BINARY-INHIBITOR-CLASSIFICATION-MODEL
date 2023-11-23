import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO
import argparse

def read_smi_file(file_path):
    try:
        with open(file_path, 'r') as smi_file:
            lines = smi_file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def smi_to_dataframe(file_path):
    smi_data = read_smi_file(file_path)
    if not smi_data:
        return None
    
    data = {'SMILES': smi_data}
    df = pd.DataFrame(data)
    return df
