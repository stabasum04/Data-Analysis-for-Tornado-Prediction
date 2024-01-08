import pandas as pd
import matplotlib.pyplot as plt
#Reading the CSV file
df = pd.read_csv('cleanedataset.csv')
df = pd.DataFrame(df)
#Age
age_data = pd.to_numeric(df['age'], errors='coerce')
# Remove rows with NaN (non-numeric) values
age_data = age_data.dropna()
# Define the bin
bin_edges = list(range(1, int(max(age_data)) + 11, 10))
# Create a histogram with the specified bin edges
plt.hist(age_data, bins=bin_edges, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution Histogram (Scales of 10)')
plt.show()
print(df['age'].describe())
# Summary statistics for 'gender'
gender_counts = df['gender'].value_counts()
print("\nGender Counts:")
print(gender_counts)
# Bar chart for gender distribution
plt.figure(figsize=(8, 6))
df['gender'].value_counts().plot(kind='pie')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
# Summary statistics for 'citizenship'
citizenship_counts = df['Citizenship_country'].value_counts()
print("\nCitizenship Counts:")
print(citizenship_counts)
#Visualizations
countries = df['Citizenship_country']
# Counting the occurrences of each unique value in the "Citizenship_country" column
country_counts = countries.value_counts()
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size as needed
country_counts.plot(kind='bar', ax=ax)
plt.xlabel('Citizenship Country')
plt.ylabel('Count')
plt.title('Bar Chart for Citizenship Country Distribution')
# Rotate and adjust x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ensure labels fit within the figure
# Display only a subset of labels if needed because long names are overlapping
n = len(country_counts)
if n > 20:
    step = n // 20  # Display every 20th label
    for i, label in enumerate(ax.get_xticklabels()):
        if i % step != 0:
            label.set_visible(False)
plt.show()
# Summary statistics for 'college degree'
degree_counts = df['Degree'].value_counts()
print("\nCollege Degree Counts:")
print(degree_counts)
#Visualizations
plt.figure(figsize=(8, 6))
df['Degree'].value_counts().plot(kind='bar',color='green')
plt.title('College Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.show()

