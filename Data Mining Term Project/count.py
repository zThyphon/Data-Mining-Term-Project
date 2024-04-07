
#This function calculates how many data 
#Satisfies searched attribute

def count(dataset, attribute_name, 
          searched_attribute, target_attribute,
          searched_target_attribute):
    count = 0
    for index, row in dataset.iterrows():
        if (row[attribute_name] == searched_attribute) and (row[target_attribute] == searched_target_attribute):
            count += 1
    
    print(f"age: {searched_attribute} count: {count}")