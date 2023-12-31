from PIL import Image
from PIL.ExifTags import TAGS
import glob
import os
import csv

#Define directory paths for your data - here I have one for september and october since I want to compare the two to see if my code works for both

directory_path = "./HoloMonitor Beta TIFF/September 2023/MDCK Edna_06.09.23-B1-1_100ul"
# directory_path = "./HoloMonitor Beta TIFF/October 2023/MDCK 17.10.23/B2-1"
last_directory = directory_path.split("/")[-1]
two_last_directories = directory_path.split("/")[-2]
image_files = glob.glob(os.path.join(directory_path, "*.tiff"))

#access the metada for each image in the directory and save the data as a list
data_list = []
for image_file in image_files:
    image = Image.open(image_file)
    exifdata = image.getexif()
    data=exifdata.get(40092)
    data = data.decode('utf-16')

    data_list.append(data)
    # Close the image to release resources
    image.close()

#the metadata that we want is stored as strings, but I would like to turn it into floats so that I can do calculations with it
max_values_strings = []
min_values_strings = []

#slicing the strings to get the values that we want (min and max values)
for i in range(len(data_list)):
    max_values_strings.append(data_list[i][35:46])
    min_values_strings.append(data_list[i][10:20]) #need to make this more robust and dynamic, ask someone for help...

max_values_floats = []
min_values_floats = []

#convert desired min and max values from strings to floats while stripping away strange characters that are not numbers
for i in range(len(max_values_strings)):
    max_values_strings[i] = float(max_values_strings[i].strip('\x00'))
    min_values_strings[i] = float(min_values_strings[i].strip('\x00'))
    
    max_values_floats.append(max_values_strings[i])
    min_values_floats.append(min_values_strings[i])

#printing for sanity check ;) 
print("min values: ", min_values_floats)
print("    ")
print("max values: ", max_values_floats)

#now, time to save the float min and max values for each image in a csv file - I am not the biggest fan of my naming convention yet, but it works for now 
#save in a new directory called "Metadata Analysis" and make a new folder called "Raw Data" to save the raw data in

if not os.path.exists("Metadata Analysis"):
    os.makedirs("Metadata Analysis")

# Specify the path of the parent folder where you want to create a new folder
parent_folder = './Metadata Analysis'

# Specify the name of the new folder you want to create
new_folder_name = 'Raw Data'

# Create the path for the new folder
new_folder_path = os.path.join(parent_folder, new_folder_name)

# Check if the folder already exists
if not os.path.exists(new_folder_path):
    # Create the new folder
    os.mkdir(new_folder_path)
    
file_name = two_last_directories + "_" + last_directory + "_minmaxvalues_rawHM.csv"
file_name = file_name.replace(" ", "_")

#save Raw Data folder in the Metadata Analysis folder
with open("Metadata Analysis/Raw Data/" + file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["min_values", "max_values"])
    for i in range(len(max_values_floats)):
        writer.writerow([min_values_floats[i], max_values_floats[i]])
