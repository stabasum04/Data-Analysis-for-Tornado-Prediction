ds = spark.read.csv("dbfs:/FileStore/shared_uploads/sshaik20@gmu.edu/ScreenTime.csv", header=True, inferSchema=True)
# Convert Dataset to RDD(does the parallelize and collect function)
csv_rdd = ds.rdd

# Display the first few rows of the RDD
print(csv_rdd.take(5))

# Count the number of rows in the RDD
print("Total number of rows in RDD:", csv_rdd.count())

# Filter data based on a condition in RDD and display the first 5 rows
filtered_rdd = csv_rdd.filter(lambda row: int(row["ElGrade"]) > 10)
filtered_rdd.take(5)

# Map and transform data in RDD
squared_rdd = csv_rdd.map(lambda row: (row["ElGrade"], int(row["MealSkip"]) ** 2))
squared_rdd.take(5)

# Reduce and calculate the total sum in RDD
total_sum = csv_rdd.map(lambda row: int(row["MealSkip"])).reduce(lambda x, y: x + y)
print("Total sum in RDD:", total_sum)

# Sort the RDD in ascending order and display the first 5 rows
sorted_rdd = csv_rdd.sortBy(lambda row: int(row["MealSkip"]), ascending=True)
sorted_rdd.take(5)

# Group by and aggregate in RDD, then display the result
grouped_rdd = csv_rdd.groupBy(lambda row: row["ElGrade"])
sums_by_group = grouped_rdd.map(lambda x: (x[0], sum(int(row["MealSkip"]) for row in x[1])))
sums_by_group.take(5)
