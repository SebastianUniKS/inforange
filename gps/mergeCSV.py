import pandas as pd
import os

# Directory containing your CSV files
# directory = '/home/jovyan/data/'

# def mergeFiles(directory):
#     df_list = []
#     # Loop through each file in the directory
#     for filename in os.listdir(directory):
#         if filename.endswith('.CSV'):
#             # Read the CSV file
#             file_path = os.path.join(directory, filename)
#             df = pd.read_csv(file_path)

#             # Add a new column 'id' with the filename (without .csv extension)
#             df['id'] = os.path.splitext(filename)[0]

#             # Append to list of DataFrames
#             df_list.append(df)

#     # Concatenate all DataFrames into one
#     merged_df = pd.concat(df_list, ignore_index=True)

#     # Save the merged DataFrame to a new CSV file
#     merged_df.to_csv(directory + 'merged_GPSfile.csv', index=False)

#     print("CSV files merged successfully!")

def append_dataframes(folder_path,filenames,target):
  gps_df = None
  for filename in filenames:
    if filename.endswith(".CSV") and os.stat(folder_path+'/'+filename).st_size > 0:
       try:
          df = pd.read_csv(folder_path+'/'+filename)
          if gps_df is None:
            gps_df = df.copy() 
          else:
            gps_df = pd.concat([gps_df, df])
       except Exception as e:
            print(f"Skipping {filename} due to error: {e}")
    
    
  if not gps_df.empty:
     gps_df.to_csv(target+'.CSV')
  else:
     print("Invalid or empty file")
  return gps_df

def mergeFiles(directory):
  foldernames = os.listdir(directory)
  foldernames = [item for item in foldernames if not item.startswith('.')]
  print("folderlist:",foldernames)
  for foldername in foldernames:
      print (foldername)
      path = os.path.join(directory,foldername)
      print(path)
      filenames = os.listdir(path)
      print ("filenames:",filenames)
      mergedGPSdata = append_dataframes(path,filenames,foldername)

def getOneFile(directory):
    # Directory containing your CSV files
    # List to store DataFrames
    df_list = []

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.CSV'):
            # Read the CSV file
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path)

            # Add a new column 'id' with the filename (without .csv extension)
            df['id'] = os.path.splitext(filename)[0]

            # Append to list of DataFrames
            df_list.append(df)

    # Concatenate all DataFrames into one
    merged_df = pd.concat(df_list, ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(directory + 'merged_GPSfile.csv', index=False)

    print("CSV files merged successfully!")

#mergeFiles('/home/sebastian/GIS/gps_data/Sololo/')
getOneFile('/home/sebastian/apps/inforange/gps/')