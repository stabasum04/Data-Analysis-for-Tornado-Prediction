#importing pandas for reading the CSV
#importing matplot for visualization
import pandas as ps
import matplotlib.pyplot as pt
# Loading the Seattle.csv into dataframe 
d=ps.read_csv('Seattle.csv')
# Displaying a few records
show=d.head()
print(show)
# Displaying the appropriate and labeled summary statistics and visualizations for:
# Bedrooms
print("Summary Statistics for # of Bedrooms:")
print(d['bedrooms'].describe())
pt.hist(d['bedrooms'],bins=20,color='pink')
pt.xlabel('Bedrooms')
pt.xlim(1,10)
pt.ylim(1000,14000)
pt.ylabel('Frequency')
pt.title('Histogram for Number of Bedrooms')
pt.show()
# Bathrooms
print("Summary Statistics for # of Bathrooms:")
print(d['bathrooms'].describe())
pt.hist(d['bathrooms'],bins=10,color='green')
pt.xlabel('Number of Bathrooms')
pt.ylabel('Frequency')
pt.title('Histogram for Number of Bathrooms')
pt.show()
# Condition
print("Summary Statistics for Condition:")
print(d['condition'].describe())
colors = ['red', 'green', 'blue','orange']
pt.bar(d['condition'].value_counts().index, d['condition'].value_counts(),color=colors)
pt.xlabel('Condition')
pt.ylabel('Frequency')
pt.title('Bar Chart for Condition')
pt.show()
# Year_built
print("Summary Statistics for Year Built:")
print(d['yr_built'].describe())
pt.hist(d['yr_built'], bins=20,color="orange")
pt.xlabel('Year Built')
pt.ylabel('Frequency')
pt.title('Histogram for Year Built')
pt.show()
#price of all houses
pt.hist(d['price'], bins=20)
pt.xlabel('Price')
pt.ylabel('Frequency')
pt.title('Distribution of House Prices')
pt.show()
pr = d['price'].describe()
print('The price summary is\n',pr)
house_price_sum = d['price'].sum()
print("Price of all houses:", house_price_sum)
#Price by Zipcode
price_zip = d.groupby('zipcode').agg({'price': ['mean', 'median', 'std', 'min', 'max']})
price_zip['price']['mean'].plot.bar()
pt.title('Mean House Price by Zip Code')
pt.xlabel('Zip Code')
pt.ylabel('Price')
pt.show()
p = d.groupby('zipcode')['price'].mean()
print(p)
#importing package seaborn  to display the scatterplot hue
import seaborn as sb
#Scatterplot for corr between price and sqft living
pt.figure(figsize=(20, 10))
sb.scatterplot(data=d, x='sqft_living', y='price', hue='zipcode')
pt.title('Relationship between Price and Living Space')
pt.xlabel('Living Space (sqft)')
pt.ylabel('Price')
pt.show()

