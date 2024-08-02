# Task Reminder Email Automation

## Overview

This project automates the process of sending task reminders via email. The script reads tasks from a CSV file and sends an email reminder if a task is scheduled for the current day.

## Features

- Reads tasks from a CSV file.
- Sends an email reminder for tasks scheduled for today.
- Uses the `smtplib` library to send emails via SMTP.

## Prerequisites

- Python 3.6 or higher
- `pandas` library
- A Gmail account with an app-specific password enabled

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SREERAJRAJEEV/Task-Reminder-Email-Automation.git
   cd Task-Reminder-Email-Automation
   ```

2. Install the required Python packages:

   ```bash
   pip install pandas
   ```

## Setup

1. Prepare the `tasks.csv` file with your tasks. The file should have the following structure:

   ```csv
   month,day,task
   7,13,Finish the report
   7,14,Meeting with the team
   7,15,Doctor appointment
   ```

2. Update the `main.py` script with your email and app-specific password:

   ```python
   MY_EMAIL = "YOUR_EMAIL@gmail.com"
   MY_PASSWORD = "YOUR_APP_PASSWORD"
   ```

## Usage

Run the script:

```bash
python main.py
```

The script will check if there are any tasks scheduled for today and send an email reminder if any tasks are found.

## Automating the Script

To run the script automatically every day, you can use Windows Task Scheduler:

1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at a specific time.
3. Set the action to start a program, and specify the path to `python.exe` and the path to your script (`main.py`).

For detailed instructions, refer to [this guide](https://www.jcchouinard.com/python-automation-using-task-scheduler/).

## License

This project is licensed under the MIT License.

## Contributing

If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## Contact

For any questions or issues, please contact:

- Sreeraj Rajeev - sreerajrajeevasiet@gmail.com

## Acknowledgments

- This project uses the `smtplib` and `pandas` libraries.
```
