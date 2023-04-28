import os
import pandas as pd

def list_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        # Skip the '.git' folder
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# Get the current working directory
directory_path = os.getcwd()
files = list_files_in_directory(directory_path)

# Create a pandas DataFrame
files_df = pd.DataFrame(files, columns=['file_path'])

# Save the DataFrame as a CSV file
files_df.to_csv('files_list.csv', index=False)

print("CSV file saved as 'files_list.csv'.")
