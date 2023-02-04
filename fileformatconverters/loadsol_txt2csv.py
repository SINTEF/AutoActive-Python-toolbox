"""Script to convert loadsol txt-files to csv-files that can be imported in activity presenter"""

import pandas as pd
import os
import argparse
from pathlib import Path


def convert_file(file_name):
    df = pd.read_table(file_name, delimiter='\t', header=[2, 3])
    df = df.loc[df.iloc[:, 0].apply(lambda x: isinstance(x, float))]
    left_col = df.columns.get_level_values(0).str.contains('-L')
    left_col = [i for i, val in enumerate(left_col) if val]
    right_col = df.columns.get_level_values(0).str.contains('-R')
    right_col = [i for i, val in enumerate(right_col) if val]
    time = (1e6*df.iloc[:, 0]).astype(int)
    if right_col[0] < left_col[0]:
        right_df = df.iloc[:, [1, 2, 3]]
        right_df = right_df[sorted(right_df.columns)]
        right_df['sum'] = df.iloc[:, 4]
        left_df = df.iloc[:, [6, 7, 8]]
        left_df = left_df[sorted(left_df.columns)]
        left_df['sum'] = df.iloc[:, 9]
    elif right_col[0] > left_col[0]:
        left_df = df.iloc[:, [1, 2, 3]]
        left_df = left_df[sorted(left_df.columns)]
        left_df['sum'] = df.iloc[:, 4]
        right_df = df.iloc[:, [6, 7, 8]]
        right_df = right_df[sorted(right_df.columns)]
        right_df['sum'] = df.iloc[:, 9]
    else:
        print("Warning: could not determine correct column order. Leaving as is")
        df.to_csv(file_name[0:-4] + "unordered.csv", index=False)
        return
    df_sorted = pd.concat([time, left_df, right_df], 1)
    df_sorted.columns = ['time_us', 'left_heel', 'left_medial', 'left_lateral', 'left_sum', 'right_heel', 'right_medial', 'right_lateral', 'right_sum']
    df_sorted.to_csv(file_name[0:-3]+"csv", index=False)
    print("Exported file: " + file_name[0:-3]+"csv")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Converts loadsol txt-files to csv. Converts all txt-files if input is folder."
    )
    parser.add_argument("src_folder", help="Location of the file or folder with data file(s)", type=Path)

    args = parser.parse_args()
    if os.path.isfile(args.src_folder):
        convert_file(args.src_folder)
    elif os.path.isdir(args.src_folder):
        all_files = os.listdir(args.src_folder)
        [convert_file(os.path.join(args.src_folder, file)) for file in all_files if os.path.splitext(file)[1] == ".txt"]
    else:
        raise Exception("Input is neither a file nor folder")
