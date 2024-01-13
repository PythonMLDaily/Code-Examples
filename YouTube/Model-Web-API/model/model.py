import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import joblib


def create_model(current_dir):
    df = pd.read_csv(os.path.join(current_dir, 'salaries-2023.csv'))

    allowed_languages = ['php', 'js', '.net', 'java']
    df = df[df['language'].isin(allowed_languages)]

    vilnius_names = ['Vilniuj', 'Vilniua', 'VILNIUJE', 'VILNIUS', 'vilnius', 'Vilniuje']
    condition = df['city'].isin(vilnius_names)
    df.loc[condition, 'city'] = 'Vilnius'

    kaunas_names = ['KAUNAS', 'kaunas', 'Kaune']
    condition = df['city'].isin(kaunas_names)
    df.loc[condition, 'city'] = 'Kaunas'

    allowed_cities = ['Vilnius', 'Kaunas']
    df = df[df['city'].isin(allowed_cities)]

    df = df[df['salary'] <= 6000]

    one_hot = pd.get_dummies(df['language'], prefix='lang')
    df = df.join(one_hot)
    df = df.drop('language', axis=1)

    one_hot = pd.get_dummies(df['city'], prefix='city')
    df = df.join(one_hot)
    df = df.drop('city', axis=1)

    x = df.iloc[:, 0:2].values
    y = df.iloc[:, 2].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(x_train, y_train)

    joblib.dump(model, os.path.join(current_dir, 'model.pkl'))


def predict_salary(experience, level):
    current_dir = os.path.dirname(__file__)

    # Check if model exists, if not - create it
    if not os.path.isfile(os.path.join(current_dir, 'model.pkl')):
        create_model(current_dir)

    # Load the saved model
    model = joblib.load(os.path.join(current_dir, 'model.pkl'))
    # Use the loaded model to make predictions
    salaries = model.predict([[int(level), int(experience)]])

    print(salaries[0])

    return salaries[0]
