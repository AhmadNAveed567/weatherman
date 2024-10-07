import os
from datetime import datetime


def replace_empty_string(content):
    for i in range(len(content)):
        if content[i].strip() == "":
            content[i] = "0"


def read_weather_data(file_path):
    dates = []
    max_temp = []
    min_temp = []
    most_humidity = []

    with open(file_path, "r") as file:

        header1 = [col.strip().lower() for col in file.readline().strip().split(",")]
        header2 = [col.strip().lower() for col in file.readline().strip().split(",")]

        if "gst" in header1 or "pkt" in header1:
            header = header1
        elif "gst" in header2 or "pkt" in header2:
            header = header2
        else:
            return dates, max_temp, min_temp, most_humidity

        date_idx = (
            header.index("gst")
            if "gst" in header
            else header.index("pkt")
            if "pkt" in header
            else -1
        )
        max_temp_idx = (
            header.index("max temperaturec") if "max temperaturec" in header else -1
        )
        min_temp_idx = (
            header.index("min temperaturec") if "min temperaturec" in header else -1
        )
        humidity_idx = header.index("max humidity") if "max humidity" in header else -1

        for line in file:
            content = line.strip().split(",")
            if len(content) < max(humidity_idx, min_temp_idx, max_temp_idx) + 1:
                continue
            replace_empty_string(content)
            date = content[date_idx].strip()
            pmaxtemp = content[max_temp_idx].strip()
            pmin_temp = content[min_temp_idx].strip()
            pmost_humidity = content[humidity_idx].strip()

            try:
                datetime.strptime(date, "%Y-%m-%d")
                dates.append(date)
                max_temp.append(float(pmaxtemp))
                min_temp.append(float(pmin_temp))
                most_humidity.append(float(pmost_humidity))
            except ValueError:
                continue

    return dates, max_temp, min_temp, most_humidity


def display_menu():
    print("\nWeather Data Menu")
    print("1. Find Max Temperature")
    print("2. Find Min Temperature")
    print("3. Find Highest Humidity")
    print("4. Show All Values")
    print("5. Exit")


def list_weather_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith(".txt")]


def main():
    base_path = r"C:\Users\an030\OneDrive\Desktop\pythonprojests\weather"

    folder_map = {"1": "lahore_weather", "2": "Murree_weather", "3": "Dubai_weather"}

    while True:
        print("\nSelect a folder:")
        print("1: Lahore Weather")
        print("2: Murree Weather")
        print("3: Dubai Weather")
        print("0: Exit")

        choice = input("Enter your choice (1-3 or 0 to exit): ")

        if choice == "0":
            print("Exiting the program.")
            break

        if choice in folder_map:
            selected_folder = folder_map[choice]
            folder_path = os.path.join(base_path, selected_folder)
        else:
            print("Invalid choice, please try again.")
            continue

        weather_files = list_weather_files(folder_path)
        if not weather_files:
            print(f"No .txt files found in '{selected_folder}'.")
            continue

        all_dates, all_max_temp, all_min_temp, all_most_humidity = [], [], [], []
        for file in weather_files:
            file_path = os.path.join(folder_path, file)
            dates, max_temp, min_temp, most_humidity = read_weather_data(file_path)
            all_dates.extend(dates)
            all_max_temp.extend(max_temp)
            all_min_temp.extend(min_temp)
            all_most_humidity.extend(most_humidity)

        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                if all_max_temp:
                    print(f"The maximum temperature is {max(all_max_temp)}")
                else:
                    print("No maximum temperature data available.")

            elif choice == "2":
                if all_min_temp:
                    print(f"The minimum temperature is {min(all_min_temp)}")
                else:
                    print("No minimum temperature data available.")

            elif choice == "3":
                if all_most_humidity:
                    print(f"The highest humidity is {max(all_most_humidity)}")
                else:
                    print("No humidity data available.")

            elif choice == "4":
                if all_max_temp and all_min_temp and all_most_humidity:
                    print(f"Max Temperature: {max(all_max_temp)}")
                    print(f"Min Temperature: {min(all_min_temp)}")
                    print(f"Highest Humidity: {max(all_most_humidity)}")
                else:
                    print("Not enough data to display all values.")

            elif choice == "5":
                print("Returning to folder selection.")
                break

            else:
                print("Invalid choice, please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
