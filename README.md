# HoloMonitorAnalysis - rescaling procedure 
In notebook "holomonitor_summary_20231120.ipynb", we are trying to rescale intensity values in images obtained using HoloMonitor in order to get physical values for the optical thickness of the cells. 

To run the notebook, create the following directory path in the repo: "HoloMonitor Beta TIFF/September 2023/MDCK Edna_06.09.23-B1-1_100ul" with images of MDCK cells. You can of course use any images that you would like - just make sure to adjust the directory path for the images. The metadata needed to run this notebook is already cointained in this repo under "Metadata Analysis" folder. 

"reading_metadata.py" is a script we made to read the metadata of the images from the Holomonitor, and extract the min and max pixel values in each image. The script reads the metadata and saves the min and max values as a new .csv file. 
