import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r"E:\Python files\Spintly Data analysis\Madhapur-Hyderabad\CSV Data\Madhapur-Hyderabad_month_8.csv")

# Group the data by 'Time' and 'eventinfo_direction' and count the occurrences
grouped_data = df.groupby(['Time', 'eventinfo_direction']).size().unstack(fill_value=0)

# Create a line plot to visualize the event counts over time for each event direction

grouped_data.plot(kind='line', marker='o', figsize=(12, 6))

# Set plot title and labels 
plt.title('Event Counts by Event Direction Over Time')
plt.xlabel('Time')
plt.ylabel('Event Counts')

# Show the plot
plt.legend(title='Event Direction')
plt.grid(True)
plt.show()
