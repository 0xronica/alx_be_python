from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  
    print(f"Current Date and Time: {formatted_date}")
    return current_date

    
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
    current_date = datetime.now()  # get the current date
    future_date = current_date + timedelta(days)
    formatted_future = future_date.strftime("%Y-%m-%d")  
    print(f"Date after {days} days: {formatted_future}")
    return future_date
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
      main()
    
