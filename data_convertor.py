import json
import pandas as pd


def json_to_spreadsheet(json_file, output_file, excel_template='data/Untitled spreadsheet.xlsx', ):
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Load the existing spreadsheet to get the exact structure and format
    existing_sheet = pd.read_excel(excel_template)
    columns = existing_sheet.columns

    # Create a new DataFrame with the same structure as the existing sheet
    new_data = {col: [] for col in columns}

    # Fill the new DataFrame with the extracted JSON data
    for keyword in data['keywords']:
        # Initialize a new row with None values
        row = {col: None for col in columns}
        row['Keyword'] = keyword['kw']
        row['Avg. Search Volume (Last Known Values)'] = keyword['sv']
        row['CPC/USD'] = keyword.get('cpc', None)
        row['PPC'] = keyword['ppc']

        for msv in keyword['msv']:
            year, month, value = msv
            col_name = f'Search Volume {month}/{year}'
            if col_name in row:
                row[col_name] = value

        # Append row values to new_data dictionary
        for col in columns:
            new_data[col].append(row[col])

    # Create a new DataFrame
    new_df = pd.DataFrame(new_data)

    # Save the new DataFrame to an Excel file
    new_df.to_excel(output_file, index=False)


if __name__ == "__main__":
    # Paths to the input and output files
    json_file = 'json/data-قیمت روز آهن آلات.json'
    excel_template = 'data/Untitled spreadsheet.xlsx'
    output_file = 'data/new_spreadsheet2.xlsx'

    # Convert JSON to spreadsheet
    json_to_spreadsheet(json_file, excel_template, output_file)
