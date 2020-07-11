import pandas as pd
from sklearn.tree import export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# load the data set
df = pd.read_csv('computer_purchase_data.csv')

# perform data encoding
lenc = LabelEncoder()
lenc.fit(['<=30', '31...40', '>40', 'High', 'Medium', 'Low', 'Fair', 'Excellent', 'Yes', 'No'])
raw_values = df.values.reshape(-1, 1)
encoded_values = lenc.transform(raw_values).reshape(-1, 5)

# define the attributes X and target y
X = encoded_values[:, 0:4]
y = encoded_values[:, 4:5]

# perform decision tree classification
tree_classifier = DecisionTreeClassifier(max_depth=10)
tree_classifier.fit(X, y)

# export as image
export_graphviz(
        tree_classifier,
        out_file="computer_purchase_decision_tree.dot",
        feature_names=df.columns.values[0:4].tolist(),
        class_names=['Buying (No)', 'Bying (Yes)'],
        rounded=True,
        filled=True
)



