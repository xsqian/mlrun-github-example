import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression

def coffeerating_data_generator(context):
    raw = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv")
    df = pd.DataFrame(raw)
    coffee = pd.DataFrame(df[
        [
            "total_cup_points",
            "aroma",
            "flavor",
            "sweetness",
            "acidity",
            "body",
            "uniformity",
            "balance",
        ]
    ])
    print("******************** running with main branch git://github.com/xsqian/mlrun-github-example.git#main ********************")
    # mlrun expr 
    context.log_dataset("coffee_dataset", df=coffee, format='parquet', index=False, artifact_path=context.artifact_subpath('coffee-dataset'))
    # context.log_artifact('coffee_dataset', body=raw, format='csv')
    return coffee, 'outcome'
