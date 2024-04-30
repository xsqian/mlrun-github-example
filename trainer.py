
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import mlrun
from mlrun.frameworks.sklearn import apply_mlrun

@mlrun.handler()
def train(context,
    dataset: pd.DataFrame,
    model_name: str = "lr_fit"
    ):
    
    x = dataset.drop('total_cup_points', axis=1)
    y = dataset['total_cup_points']
    X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

    model = LinearRegression()

    apply_mlrun(model=model, model_name=model_name, x_test=X_test, y_test=y_test)

    model.fit(X_train, y_train)
    print("******************** running with main branch git://github.com/xsqian/mlrun-github-example.git#main ********************")
