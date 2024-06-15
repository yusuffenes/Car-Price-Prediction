import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('clean_car.csv')
df = dataset.copy()
from sklearn.model_selection import train_test_split

X = df.drop('Price', axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=43)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import HistGradientBoostingRegressor
hgbr = HistGradientBoostingRegressor()
num_features = X.select_dtypes(include=['int64']).columns
cat_features = X.select_dtypes(include='object').columns
transformer = ColumnTransformer(transformers=[('num', StandardScaler(), num_features),('cat', OneHotEncoder(sparse_output=False), cat_features)])
pipe = Pipeline(steps=[('preprocessor', transformer), ('model', hgbr)])

pipe.fit(X_train, y_train)

import streamlit as st

def price(companyName,modelName,modelYear,locaiton,mileage,engineType,engineCapacity,color,assembly,bodyType,transmissionType,registrationStatus):
  input_data = pd.DataFrame({
      'Company Name':[companyName],
      'Model Name':[modelName],
      'Model Year':[modelYear],
      'Location':[locaiton],
      'Mileage':[mileage],
      'Engine Type':[engineType],
      'Engine Capacity':[engineCapacity],
      'Color':[color],
      'Assembly':[assembly],
      'Body Type':[bodyType],
      'Transmission Type':[transmissionType],
      'Registration Status':[registrationStatus]
  })
  prediction=pipe.predict(input_data)[0]
  return prediction
st.title('Car Price Prediction :car: :arrow_forward: :dollar: @yusufenes')
st.write('Please Chose Car Specifications')
companyName = st.selectbox('Company Name',df['Company Name'].unique())
modelName = st.selectbox('Model Name',df[df['Company Name']==companyName]['Model Name'].unique())
modelYear = st.selectbox('Model Year',df[(df['Company Name']==companyName)&(df['Model Name'] == modelName)]['Model Year'].unique())
locaiton = st.selectbox('Location',df['Location'].unique())
mileage = st.number_input('Mileage',df['Mileage'].min(),df['Mileage'].max())
engineType = st.selectbox('Engine Type',df['Engine Type'].unique())
engineCapacity = st.number_input('Engine Capacity',df['Engine Capacity'].min(),df['Engine Capacity'].max())
color = st.selectbox('Color',df['Color'].unique())
assembly = st.selectbox('Assembly',df['Assembly'].unique())
bodyType = st.selectbox('Body Type',df['Body Type'].unique())
transmissionType = st.selectbox('Transmission Type',df['Transmission Type'].unique())
registrationStatus = st.selectbox('Registration Status',df['Registration Status'].unique())
if st.button('Predict'):
  pred=price(companyName,modelName,modelYear,locaiton,mileage,engineType,engineCapacity,color,assembly,bodyType,transmissionType,registrationStatus)
  st.success(f'The predicted price is :red_car: {pred.round(2)} :heavy_dollar_sign:')
  st.balloons()