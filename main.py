import smtplib
import datetime as dt
import pandas as pd

MY_EMAIL = "REPLACE WITH EMAIL"
MY_PASSWORD = "REPLACE WITH YOUR APP PASSWORD"

# Get the current date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read the tasks from the CSV file
data = pd.read_csv("tasks.csv")

# Create a dictionary with (month, day) tuples as keys and rows as values
tasks_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#Explaination of how dictionary is organized
'''
    - data.iterrows() iterates over each row in the DataFrame.
    - For each row, a tuple (data_row["month"], data_row["day"]) is created using the "month" and "day" columns.
    - The dictionary tasks_dict uses these tuples as keys.
    - The values for these keys are the entire rows (data_row) from the DataFrame.
'''
# Check if there is a task for today
if today_tuple in tasks_dict:
    task_details = tasks_dict[today_tuple]
    contents = task_details["task"]

    # Sending the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to your email
        connection.sendmail(
            from_addr=MY_EMAIL,  # From address
            to_addrs=MY_EMAIL,  # To address
            msg=f"Subject:REMINDER FOR TOMORROW!\n\n{contents}"  # Subject and task
        )
else:
    print("No task for today.")
