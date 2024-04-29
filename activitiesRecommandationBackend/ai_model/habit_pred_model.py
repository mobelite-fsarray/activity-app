import pandas as pd

data_file = pd.read_csv("habit_data_manually.csv",index_col=0)

# Parse textual data
data_file["gender_code"] = data_file['gender'].astype("category").cat.codes
data_file["ageGeneration_code"] = data_file['ageGeneration'].astype("category").cat.codes
data_file["profession_code"] = data_file['profession'].astype("category").cat.codes
data_file["partsOfTheDay_code"] = data_file['partsOfTheDay'].astype("category").cat.codes


#gender
#[0, 1]
#['Female', 'Male']

#ageGeneration_code
#[0, 1, 2, 3]
#['Baby Boomer', 'Gen X', 'Gen Z', 'Millennial']

#profession_code
#[0, 1, 2]
#['Marketing Manager', 'Software Engineer', 'Doctor']

#partsOfTheDay
#[0, 1, 2, 3, 4, 5]
#['morning', 'sunset', 'sunrise', 'noon', 'afternoon', 'night']

target = "category"
ignored_columns = ["gender",
                  "ageGeneration",
                  "profession",
                   "country",
                   "partsOfTheDay"
                  ]
ignored_columns.append(target)
input_columns = list(set(data_file.columns.array).difference(ignored_columns))
input_columns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = data_file.drop(columns=ignored_columns,axis=1)
y = data_file[target]

# we using 20% of our data to test this model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
train_data = X_train.join(y_train)
train_data.hist(figsize=(15,8))

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train.values, y_train)

predictions = model.predict(X_test.values)

score = accuracy_score(y_test, predictions)
print(score)

import pickle
# Save the model to disk
filename = 'habit_pred_model.pkl'
pickle.dump(model, open(filename, 'wb'))

predictions = model.predict([[1,2,1,5]])
print(predictions)
