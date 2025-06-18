from storage.history import save_to_history, view_history
from api.weather import get_weather
from utils.helpers import greet_user, is_valid_city, is_valid_name

def start_assistant():
    print("👋 Welcome to Barbara Assistant")

    while True:
        name = input("What's your name? ")
        if is_valid_name(name):
            break
        print("Please enter a valid name")

    print(greet_user(name))

    while True:
        print("\nWhat would you like to do?")
        print("1. Check the weather")
        print("2. View search history")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            while True:
              city = input("Which city do you want the weather for? ")

              if not is_valid_city(city):
                  print("Invalid input. Please enter a real city name.")
                  continue
        

              weather = get_weather(city)
    
              if "City not found" in weather or "Unable to retrieve" in weather:
                  print(weather)
                  continue
      
    
              print(weather)
              save_to_history(city, name)
              break

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("\nGoodbye! 👋")
            break

        else:
            print("Invalid option. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    start_assistant()