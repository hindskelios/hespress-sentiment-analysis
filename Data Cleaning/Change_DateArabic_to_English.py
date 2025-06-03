import pandas as pd
import re
from datetime import datetime
import locale

# Set the locale to Arabic
locale.setlocale(locale.LC_TIME, 'ar')

# Load your dataset
# Assuming 'your_dataset.csv' is the CSV file containing your dataset
# Replace 'your_dataset.csv' with the actual filename or path
df = pd.read_excel('result_Sentim_Orange.xlsx')

# Define a mapping for Arabic month names
month_mapping = {
    'يناير': '01',
    'فبراير': '02',
    'مارس': '03',
    'إبريل': '04',
    'مايو': '05',
    'يونيو': '06',
    'يوليو': '07',
    'غشت': '08',
    'شتنبر': '09',
    'أكتوبر': '10',
    'نونبر': '11',
    'دجنبر': '12',
}

# Function to convert Arabic date to English date
def convert_arabic_date(arabic_date_string):
    match = re.search(r'(\d+) ([ء-ي]+) (\d+) - (\d+):(\d+)', arabic_date_string)
    day, month_arabic, year, hour, minute = match.groups()

    # Convert Arabic month name to English
    month_english = month_mapping.get(month_arabic, month_arabic)

    # Construct the English date string (excluding day of the week)
    english_date_string = f"{day} {month_english} {year} - {hour.zfill(2)}:{minute.zfill(2)}"

    # Parse the English date string
    english_date = datetime.strptime(english_date_string, "%d %m %Y - %H:%M")

    # Format the date in the desired format (YYYY/MM/DD)
    # desired_format = "%Y/%m/%d"
    # formatted_date = english_date.strftime(desired_format)
    # print(formatted_date)
    return english_date

# Apply the conversion function to the 'date' column in your dataset
df['Date'] = df['Date'].apply(lambda x: convert_arabic_date(x))
df.to_excel('result_Sentim_Orange.xlsx', index=False)