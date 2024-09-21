import pandas as pd

# Directory where the data has been downloaded
data_dir = "/home/student/workspace/lp-forecasting-bm/data"

data = pd.read_csv(data_dir +"/H1.csv")
# How to concatenate columns: https://datatofish.com/concatenate-values-python/
data["Date (Year and Week Number"] = data["ArrivalDateYear"].map(str) + data["ArrivalDateWeekNumber"].map(str)

# Filter out the cancelled bookings
cancelled_bookings_filter = data["IsCanceled"] == 1
cancelled_bookings = data[cancelled_bookings_filter]

cancelled_by_year_and_week = cancelled_bookings.filter(items = ["Date (Year and Week Number", "IsCancelled"]).groupby("Date (Year and Week Number")

#cancelled_by_year_and_week.size()
cancelled_by_year_and_week.value_counts()