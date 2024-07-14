import pandas as pd


def combine_spreadsheets(file1, file2, output_file, key_column='Keyword'):
    # Load the Excel files into DataFrames
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge the DataFrames on the key column
    combined_df = pd.merge(df1, df2, on=key_column,
                           how='cross')

    # Save the combined DataFrame to a new Excel file
    combined_df.to_excel(output_file, index=False)

    print(f"Combined spreadsheet saved to {output_file}")


# Paths to the input and output files
file1 = 'out/data-آهن آلات.xlsx'
file2 = 'out/data-قیمت اهن.xlsx'
output_file = 'out/combined_spreadsheet.xlsx'

# Combine the spreadsheets
combine_spreadsheets(file1, file2, output_file)
