import pandas as pd

#Get data from csv file
def get_data(dataset_path,attribute_names):
    data_set = pd.read_csv(dataset_path,skiprows=1,names=attribute_names)
    return data_set    

