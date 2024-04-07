import decisionTree 

#Get decision tree with using build_decision_tree function 
#inside the decisionTree.py file
def train(data_set, attribute_names,target_class):
    decision_tree = decisionTree.build_decision_tree(data_set,attribute_names,target_class)
    return decision_tree
    