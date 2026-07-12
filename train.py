from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import joblib as jb
import pandas as pd



data = fetch_california_housing(as_frame=True)

X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.75,random_state=42)


model = RandomForestRegressor(n_estimators=200,random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"Mean Absolute Error: ${mae*100000:,.0f}")

print(f"R2 score:{r2}")

jb.dump(model,"house_price_predictor.joblib")
jb.dump(list(X.columns),"house_features.joblib")