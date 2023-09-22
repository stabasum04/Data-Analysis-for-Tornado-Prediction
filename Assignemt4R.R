# Loading the CSV file into a dataframe
d<- read.csv("1950-2021_actual_tornadoes.csv")
#displaying a few records
head(d)
# Summary statistics for monthly tornadoes(mo)
summary(d$mo)
#visualization
hist(d$mo, main="Monthly Tornado Occurrences", xlab="Month", col="lightblue")

# Summary statistics for Tornadoes by states(st)
table(d$st)
# Visualization
barplot(table(d$st), main="Tornado Occurrences by State", xlab="State",ylab = "Frequency",col="blue")

# Summary statistics for Time of the day 'time'
summary(d$time)

# Visualization
d$time <- as.POSIXct(d$time, format="%H:%M:%S")
hist(d$time, main="Tornado Occurrences - Time of the Day", xlab="Time of the Day", 
     breaks="hours", format="%H:%M:%S", col="orange")

# Summary statistics for Magnitude(mag) of Tornadoes
summary(d$mag)
# Visualization
hist(d$mag, main="Tornado Magnitude Distribution", xlab="Magnitude",col="red")

#Displaying the months that have most F5(mag)tornados
#taking the magnitudes which have 5
tornadoesF5<- subset(d, mag == 5)
#takings months
month<- table(tornadoesF5$mo)
#sorting the months in descending order
sort_month <- sort(month, decreasing = TRUE)
#taking the top 3 highest months
top_3_months <- head(names(sort_month), 3)
mag_values <- as.numeric(sort_month[1:3])
top_3_months <- data.frame(Month = top_3_months, Mag_Value = mag_values)
cat("Top 3 Months with the Most F5 Tornadoes with their Magnitude Values:\n")
print(top_3_months)

#states with most avg injuries and fatalities
#taking mean
inj_fat <- aggregate(cbind(inj, fat) ~ st, d, mean)
#max injuries
inj <- inj_fat[which.max(inj_fat$inj), "st"]
#max fatalities
fat<- inj_fat[which.max(inj_fat$fat), "st"]
cat("State with the Most Average Injuries is -", inj, "\n")
cat("State with the Most Average Fatalities is -", avg_fat, "\n")


#Relation between Magnitude and Property Loss
plot(d$mag, d$loss, main="Magnitude and Property Loss Correlation",
     xlab="Magnitude", ylab="Property Loss", pch=16)

# Calculate the correlation between 'mag' and 'loss'
correlation <- cor(d$loss, d$mag)
cat("Correlation between Magnitude and Property Loss:", correlation, "\n")
