import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = {
    'Year': [1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'CO2_mean': [338.91, 340.11, 340.85, 342.53, 344.07, 345.54, 346.97, 348.68, 351.16, 352.79, 354.06, 355.39, 356.09, 356.83, 358.33, 360.17, 361.93, 363.05, 365.7, 367.8, 368.96, 370.57, 372.58, 375.15, 376.95, 378.98, 381.15, 382.9, 385.02, 386.5, 388.76, 390.63, 392.65, 395.4, 397.34, 399.65, 403.06, 405.22, 407.61, 410.07, 412.44, 414.7, 417.07],
}

#show graph for year and co2
years = data['Year']
co2 = data['CO2_mean']

plt.figure(figsize=(10, 6)) 
plt.plot(years, co2, marker='o', linestyle='-', color='g')
plt.title('Annual Mean CO2 Concentrations')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration (ppm)')
plt.grid(True)
plt.show()


# Create a linear regression model
df = pd.DataFrame(data)
model = LinearRegression()
model.fit(df[['Year']], df['CO2_mean'])
slope = model.coef_[0]
intercept = model.intercept_

print(f"Linear Model: CO2_mean = {slope:.2f} * Year + {intercept:.2f}")
print(f"Slope (Rate of Change per Year): {slope:.2f}")
print(f"Intercept (Initial Value in 1979): {intercept:.2f}")

# Predicted mean CO2 concentrations for future years
predictions = model.predict(df[['Year']])
future_years = [2025, 2030, 2040, 2050, 2100]
predicted_CO2 = [slope * year + intercept for year in future_years]
plt.figure(figsize=(10, 6))

plt.plot(years, co2, marker='o', linestyle='-', color='b', label='present Data')
plt.plot(future_years, predicted_CO2, marker='x', linestyle='--', color='g', label='Future Predictions')

plt.title('CO2 Concentrations:Future Predictions')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration (ppm)')
plt.grid(True)
plt.legend()
plt.show()

plt.scatter(df['Year'], df['CO2_mean'], label='Actual Data')
plt.plot(df['Year'], predictions, color='red', label='Linear Regression Model')
plt.xlabel('Year')
plt.ylabel('CO2_mean')
plt.legend()
plt.show()
for year, CO2 in zip(future_years, predicted_CO2):
    print(f"Predictions of the CO2 concentration for {year}: {CO2:.2f} ppm")
    

#Accuracy

mae = mean_absolute_error(df['CO2_mean'], predictions)
mse = mean_squared_error(df['CO2_mean'], predictions)
rmse = mse ** 0.5
r2 = r2_score(df['CO2_mean'], predictions)
    
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

