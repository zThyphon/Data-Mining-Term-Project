import decisionTree

#Declare and initialize decision tree
global decision_tree
decision_tree = decisionTree.get_decision_tree()

#Testing function
def test(test_data):
    #Assign an variable which contains number of correct predictions
    correct_predictions = 0
   
   #Start a loop for each item of test data
    for index, row in test_data.iterrows():
        #Get actual target attribute value
        actual_class = row["Purpose"]

        #Predict target attribute according to credit amount, age sex and job
        predicted_class = predict_class(row["Credit amount"],
                                        row["Age"],
                                        row["Sex"],
                                        row["Job"])
        
        #If actual class is equal to predicted class
        #It means that decision tree algorithm has predicted correctly
        if(actual_class == predicted_class):
            #Increase correct predictions +1
            correct_predictions+=1
    
    #Get test data size for calculating accuracy
    test_data_size = len(test_data)

    #Calculate accuracy percentage
    accuracy = float(correct_predictions/test_data_size)*100

    #Print the testing results
    print(f"Test Sample Size: {test_data_size}")
    print(f"Number of correct predictions: {correct_predictions}")
    print(f"Accuracy(%): {accuracy}")




def predict_class(credit_amount, age, sex, number_of_job):
    #According to decision tree and its optimization
    #The following rules has been found
    if(credit_amount == 1474):
        if(sex=="female"):
            return "furniture/equipment"
        else:
            return "car"
    
    elif (credit_amount == 2978):
        if("Saving accounts" == "little"):
            return "business"
        else: 
            return "furniture/equipment"
    
    elif (credit_amount == 2028):
        if(number_of_job == 1):
            return "furniture/equipment"
        else:
            return "car"
    else:
        #If target value has childs (if it has dictionary in it)
        #It means that there exists an nested dictionary, we need to 
        #check other attributes for describing value
        #(In all other situations credit amount and 
        #age is enough for getting target class)
        if(isinstance(decision_tree["Credit amount"][credit_amount],dict)):
            return decision_tree["Credit amount"][credit_amount]["Age"][age]
        
        #If target value has no child it means that
        #Credit amount is enough for getting target class
        else:
            return decision_tree["Credit amount"][credit_amount]
        

