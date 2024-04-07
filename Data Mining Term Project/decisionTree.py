import numpy as np

#Calculates entropy according to an attribute
def calculate_entropy(data):
    classes, counts = np.unique(data, return_counts=True)
    probability = counts/len(data)
    entropy = -np.sum(probability * np.log2(probability))

    return entropy

#calculates information gain according to an attribute
def calculate_information_gain(data, feature_name, class_name):
    total_entropy = calculate_entropy(data[class_name])

    feature_values, feature_counts = np.unique(data[feature_name], return_counts=True)
    weighted_entropy = np.sum([(feature_counts[i] / len(data)) * 
                               calculate_entropy(data[data[feature_name] 
                                                      == feature_values[i]][class_name]) 
                                                      for i in range(len(feature_values))])

    information_gain = total_entropy - weighted_entropy

    return information_gain

#Builds decision tree according to data, attributes and target attribute
def build_decision_tree(data, features, class_name):
    # If all samples have the same class label, return a leaf node with that class label
    if len(np.unique(data[class_name])) == 1:
        return np.unique(data[class_name])[0]
    
    # If there are no more features to split on, return the most common class label
    if len(features) == 0:
        return np.unique(data[class_name])[np.argmax(np.unique(data[class_name], 
                                                               return_counts=True)[1])]

    # Find the feature that provides the highest information gain
    information_gains = [calculate_information_gain(data, feature, class_name) 
                         for feature in features]
    best_feature_index = np.argmax(information_gains)
    best_feature = features[best_feature_index]

    #Create a decision tree in dictionary data structure
    decision_tree = {best_feature: {}}
    features = [feature for feature in features if feature != best_feature]

    for value in np.unique(data[best_feature]):
        subdata = data[data[best_feature] == value]
        subtree = build_decision_tree(subdata, features, class_name)
        decision_tree[best_feature][value] = subtree

    return decision_tree


#Get decision tree from txt file
def get_decision_tree():
    with open("decision_tree.txt", "r") as file:
        decision_tree_string = file.read()
        decision_tree = eval(decision_tree_string)
        return decision_tree