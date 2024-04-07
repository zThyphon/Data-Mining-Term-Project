from getData import get_data
from train import train
from test import test
from count import count
from draw import * 

#Training dataset path
global train_dataset_path
train_dataset_path = "Bank_Credit_Data_Train_Set.csv"

#Attributes of the dataset
global attribute_names
attribute_names = [
    "Age",
    "Sex",
    "Job",
    "Housing",
    "Saving accounts",
    "Checking account",
    "Credit amount",
    "Duration",
    "Purpose"
]

#Target attribute that we want to predict
global target_class
target_class = "Purpose"

#Target dataset path
global test_dataset_path
test_dataset_path = "Bank_Credit_Data_Test_Set.csv"

def main():
    #Get the training dataset from csv file
    train_dataset = get_data(train_dataset_path,attribute_names)

    #Specifying attribute types for creating decision tree
    train_dataset["Sex"] = train_dataset["Sex"].astype(str)
    train_dataset["Housing"] = train_dataset["Housing"].astype(str)
    train_dataset["Saving accounts"] = train_dataset["Saving accounts"].astype(str)
    train_dataset["Checking account"] = train_dataset["Checking account"].astype(str)

    #Get the testing dataset from csv file
    test_dataset = get_data(test_dataset_path,attribute_names)
    #Specifying attribute types for creating decision tree
    test_dataset["Age"] = test_dataset["Age"].astype(int)
    test_dataset["Sex"] = test_dataset["Sex"].astype(str)
    test_dataset["Housing"] = test_dataset["Housing"].astype(str)
    test_dataset["Saving accounts"] = test_dataset["Saving accounts"].astype(str)
    test_dataset["Checking account"] = test_dataset["Checking account"].astype(str)

    #Test test dataset according to decision tree 
    #Note: (decision tree is initialized in the test.py file)
    test(test_dataset)

    credit_purpose_options = [
        "car",
        "education",
        "furniture/equipment",
        "radio/TV",
        "business",
        "domestic appliances\n",
        "vacations"
    ]

    #Show Graphs According to Values
    credit_purpose_distribution = [222,49,129,197,68,8,10]

    draw_bar_chart(credit_purpose_options, credit_purpose_distribution, "Credit Purpose", "Number of Creditors", "Bar Chart of the Creditor Distribution According to Credit Purpose")

    genders = ["male","female"]
    gender_credit_purpose_distribution = [484,214]
    draw_bar_chart(genders, gender_credit_purpose_distribution, "Sex", "Number of Creditors", "Bar Chart of the Credit Purpose Distribution According to Sex")
    
    male_credit_purpose_distribution_percentage = [161/7,31/7,79/7,143/7,54/7,6/7,10/7]

    draw_pie_chart(credit_purpose_options, male_credit_purpose_distribution_percentage, "Pie Chart of the Male Creditor Purpose Distribution")

    female_credit_purpose_distribution_percentage = [64/7,20/7,53/7,57/7,14/7,5/7,3/7]
    
    draw_pie_chart(credit_purpose_options, female_credit_purpose_distribution_percentage, "Pie Chart of the Female Credit Purpose Distribution")

    creditor_age_intervals = ["20-30","31-40","41-50","51-60","61-70"]
    creditor_age_credit_purpose_distribution = [294,221,101,48,36]

    draw_bar_chart(creditor_age_intervals,creditor_age_credit_purpose_distribution,"Creditor Age Interval","Number of Creditors", "Bar Chart of the Credit Purpose Distribution According to Age Intervals")
    
    credit_purpose_distribution_20_30_percentage = [92/7,11/7,65/7,91/7,27/7,5/7,3/7]
    draw_pie_chart(credit_purpose_options,credit_purpose_distribution_20_30_percentage,"Pie Chart of 20 to 30 Years Old Creditor Purpose Distribution")

    credit_purpose_distribution_31_40_percentage = [85/7,20/7,26/7,58/7,26/7,2/7,4/7]
    draw_pie_chart(credit_purpose_options,credit_purpose_distribution_31_40_percentage,"Pie Chart of 31 to 40 Years Old Creditor Purpose Distribution")


    credit_purpose_distribution_41_50_percentage = [33/7,9/7,23/7,28/7,7/7,1/7,0]
    draw_pie_chart(credit_purpose_options,credit_purpose_distribution_41_50_percentage,"Pie Chart of 41 to 50 Years Old Creditor Purpose Distribution")

    credit_purpose_distribution_51_60_percentage = [19/7,3/7,7/7,13/7,3/7,0,3/7]
    draw_pie_chart(credit_purpose_options,credit_purpose_distribution_51_60_percentage,"Pie Chart of 51 to 60 Years Old Creditor Purpose Distribution")

    credit_purpose_distribution_61_70_percentage = [12/7,7/7,7/7,5/7,5/7,0,0]
    draw_pie_chart(credit_purpose_options,credit_purpose_distribution_61_70_percentage,"Pie Chart of 61 to 70 Years Old Creditor Purpose Distribution")    
if __name__ == "__main__":
    main()