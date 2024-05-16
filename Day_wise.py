import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r"E:\Python files\Spintly Data analysis\All-Data\Banglore_month_6.csv")

# Filter data for Bangalore and Gurugram centers
bangalore_data = df[df['Center'] == 'Bangalore']
gurugram_data = df[df['Center'] == 'Gurugram']

# Group the data by 'Day', 'eventinfo_direction', and count the occurrences
grouped_bangalore = bangalore_data.groupby(['S no','Month', 'eventinfo_direction']).size().unstack(fill_value=0)
grouped_gurugram = gurugram_data.groupby(['S no','Month', 'eventinfo_direction']).size().unstack(fill_value=0)

# Create a line plot to visualize the event counts over days for each event direction
fig, ax = plt.subplots(figsize=(12, 6))

# Plot Bangalore data as a green line
grouped_bangalore.plot(kind='line', marker='o', ax=ax, title='Event Counts by Event Direction Over Day (Bangalore vs. Gurugram)', color='green')

# Plot Gurugram data as a blue line
grouped_gurugram.plot(kind='line', marker='o', ax=ax, color='blue')

# Set labels and legend
plt.xlabel('Day')
plt.ylabel('Event Counts')
plt.legend(title='Event Direction', loc='upper left')
plt.grid(True)
plt.show()
