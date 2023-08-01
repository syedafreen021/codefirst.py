#weather data assignment 
weather_data = {
    "2023-07-30": {"temp": 28},
    "2023-07-31": {"temp": 25},
}

wind_speed_data = {
    "2023-07-30": {"wind_speed": 10},
    "2023-07-31": {"wind_speed": 15},
}

pressure_data = {
    "2023-07-30": {"pressure": 1012},
    "2023-07-31": {"pressure": 1010},
}

def get_weather(date):
    return weather_data.get(date, None)

def get_wind_speed(date):
    return wind_speed_data.get(date, None)

def get_pressure(date):
    return pressure_data.get(date, None)

def print_weather(date, weather):
    if weather:
        print(f"Temperature on {date}: {weather['temp']}°C")
    else:
        print("Data not available for the given date.")

def print_wind_speed(date, wind_speed):
    if wind_speed:
        print(f"Wind speed on {date}: {wind_speed['wind_speed']} km/h")
    else:
        print("Data not available for the given date.")

def print_pressure(date, pressure):
    if pressure:
        print(f"Pressure on {date}: {pressure['pressure']} hPa")
    else:
        print("Data not available for the given date.")

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            weather = get_weather(date)
            print_weather(date, weather)
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            print_wind_speed(date, wind_speed)
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            print_pressure(date, pressure)
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
