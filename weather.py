import os
from datetime import datetime

def replaceemptystring(content):
    for i in range(len(content)):
        if content[i].strip() == '':
            content[i] = '0'

def read_weather_data(file_path):
    dates = []
    max_temp = []
    min_temp = []
    max_humidity = []

    with open(file_path, "r") as file:
        next(file)
        for line in file:
            content = line.split(',')
            replaceemptystring(content)
            
            date = content[0].strip()
            pmaxtemp = content[1].strip()
            pmin_temp = content[3].strip()
            pmax_humidity = content[7].strip()
            
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                dates.append(date)
                
                max_temp_value = float(pmaxtemp)
                max_temp.append(max_temp_value)
                
                min_temp_value = float(pmin_temp)
                min_temp.append(min_temp_value)
                
                max_humidity_value = float(pmax_humidity)
                max_humidity.append(max_humidity_value)
            
            except ValueError:
                continue

    return dates, max_temp, min_temp, max_humidity

def display_menu():
    print("\nWeather Data Menu")
    print("1. Find Max Temperature")
    print("2. Find Min Temperature")
    print("3. Find Highest Humidity")
    print("4. Show All Values")
    print("5. Exit")

def main():
    file_path = "Dubai_weather/Dubai_weather_2004_Aug.txt"
    
    dates, max_temp, min_temp, max_humidity = read_weather_data(file_path)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            max_value = max(max_temp)
            print(f"The maximum temperature is {max_value}°C")
        
        elif choice == '2':
            min_value = min(min_temp)
            print(f"The minimum temperature is {min_value}°C")
        
        elif choice == '3':
            max_humidity_value = max(max_humidity)
            print(f"The highest humidity is {max_humidity_value}%")
        
        elif choice == '4':
            max_value = max(max_temp)
            min_value = min(min_temp)
            max_humidity_value = max(max_humidity)
            print(f"Max Temperature: {max_value}")
            print(f"Min Temperature: {min_value}")
            print(f"Highest Humidity: {max_humidity_value}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
