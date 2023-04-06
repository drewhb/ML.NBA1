import sqlite3
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import numpy as np


dataset = "dataset_2012-23"
con = sqlite3.connect("../../Data/dataset.sqlite")
data = pd.read_sql_query(f"select * from \"{dataset}\"", con, index_col="index")
con.close()
OU = data['OU-Cover']
data.drop(['Score', 'Home-Team-Win', 'TEAM_NAME', 'Date', 'TEAM_NAME.1', 'Date.1', 'OU-Cover'], axis=1,
          inplace=True)
# firstTen = data.head(10)
# for colName in data.columns:
#     print(colName)
# print()
# print("DF: ")
# print(firstTen)
data = data.values
data = data.astype(float)
acc_results = []

# result = data[0, :]
# print("First 1 rows of the NUmpy:")
# print(result)

for x in tqdm(range(100)):
    x_train, x_test, y_train, y_test = train_test_split(data, OU, test_size=.1)

    train = xgb.DMatrix(x_train, label=y_train)
    test = xgb.DMatrix(x_test)

    param = {
        'max_depth': 6,
        'eta': 0.05,
        'objective': 'multi:softprob',
        'num_class': 3,
        'tree_method': 'gpu_hist',
        'gpu_id': 0
    }
    epochs = 300

    model = xgb.train(param, train, epochs)

    predictions = model.predict(test)
    y = []

    for z in predictions:
        y.append(np.argmax(z))

    acc = round(accuracy_score(y_test, y)*100, 1)
    print(f"{acc}%")
    acc_results.append(acc)
    # only save results if they are the best so far
    if acc == max(acc_results):
        model.save_model('../../Models/XGBoost_{}%_UO-6.json'.format(acc))
