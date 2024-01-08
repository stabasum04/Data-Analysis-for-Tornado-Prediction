data <- read.csv("1950-2021_actual_tornadoes.csv", sep="\t")
# Summary statistics for 'mo'
summary(data$mo)

# Visualization for 'mo'
hist(data$mo, main="Tornado Occurrences by Month", xlab="Month")
# Summary statistics for 'st'
table(data$st)

# Visualization for 'st'
barplot(table(data$st), main="Tornado Occurrences by State", xlab="State", ylab="Count")
# Summary statistics for 'time'
summary(data$time)

# Visualization for 'time' (requires further data transformation)
# Convert 'time' to a time-of-day format
data$time <- as.POSIXct(data$time, format="%H:%M:%S")
hist(data$time, main="Tornado Occurrences by Time", xlab="Time of Day")
# Summary statistics for 'mag'
summary(data$mag)

# Visualization for 'mag'
hist(data$mag, main="Tornado Magnitude Distribution", xlab="Magnitude")
# Filter the data for F5 (mag == 5) tornados
f5_tornados <- subset(data, mag == 5)

# Count the occurrences of F5 tornados by month
f5_month_counts <- table(f5_tornados$mo)
months_with_most_f5 <- names(f5_month_counts)[which.max(f5_month_counts)]
cat("Months with the most F5 Tornados:", months_with_most_f5, "\n")
# Group data by state and calculate the average injuries and fatalities
state_injuries_fatalities <- aggregate(cbind(inj, fat) ~ st, data, mean)

# Find the state with the most average injuries and fatalities
state_most_avg_injuries <- state_injuries_fatalities[which.max(state_injuries_fatalities$inj), "st"]
state_most_avg_fatalities <- state_injuries_fatalities[which.max(state_injuries_fatalities$fat), "st"]
cat("State with the Most Average Injuries:", state_most_avg_injuries, "\n")
cat("State with the Most Average Fatalities:", state_most_avg_fatalities, "\n")
# Calculate the correlation between 'mag' and 'loss'
correlation <- cor(data$mag, data$loss)
cat("Correlation between Magnitude (mag) and Property Loss (loss):", correlation, "\n")

