# Load the data
library(tidyverse)
tornadoes <- read.csv("1950-2021_actual_tornadoes.csv")
# Display a few records
head(tornadoes)
# Display appropriate and labeled summary statistics and visualizations for:
# Month (mo) of tornado occurrences
ggplot(tornadoes, aes(x = factor(mo))) +
  geom_bar() +
  labs(title = "Number of Tornadoes by Month",
       x = "Month",
       y = "Number of Tornadoes")
# State (st) of tornado occurrences
ggplot(tornadoes, aes(x = factor(st))) +
  geom_bar() +
  labs(title = "Number of Tornadoes by State",
       x = "State",
       y = "Number of Tornadoes")
# Time (time) tornado occurrences
ggplot(tornadoes, aes(x = factor(time))) +
  geom_bar() +
  labs(title = "Number of Tornadoes by Time",
       x = "Time",
       y = "Number of Tornadoes")
# Size (mag) tornado occurrences
ggplot(tornadoes, aes(x = factor(mag))) +
  geom_bar() +
  labs(title = "Number of Tornadoes by Size",
       x = "Size",
       y = "Number of Tornadoes")
# Which months (mo) had the most F5 (mag) tornados?
tornadoes %>%
  filter(mag == "F5") %>%
  group_by(mo) %>%
  summarise(n = n()) %>%
  arrange(desc(n))
# Which states (st) had the most average injuries (inj) and fatalities (fat) from tornados?
tornadoes %>%
  group_by(st) %>%
  summarise(mean_inj = mean(inj), mean_fat = mean(fat)) %>%
  arrange(desc(mean_inj), desc(mean_fat))
# The relationship between magnitude (mag) and property loss (loss)
ggplot(tornadoes, aes(x = mag, y = loss)) +
  geom_point() +
  labs(title = "Relationship between Magnitude and Property Loss",
       x = " Magnitude",
       y = "Property Loss")