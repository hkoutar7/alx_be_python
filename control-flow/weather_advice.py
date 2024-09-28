def get_weather_advice(weather: str) -> str:
    """
    Provide clothing recommendations based on the weather input.

    Args:
        weather (str): The current weather condition ("sunny", "rainy", "cold").

    Returns:
        str: Clothing recommendation for the given weather, or an error message if the input is invalid.
    """
    
    weather = weather.strip().lower()  # Stripping and converting to lowercase for consistency

    if weather == "sunny":  # Check for sunny weather
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":  # Check for rainy weather
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":  # Check for cold weather
        return "Make sure to wear a warm coat and a scarf."
    else:  # Handle unexpected inputs
        return "Sorry, I don't have recommendations for this weather."


def main():
    """
    Main function to prompt the user for the weather and print appropriate clothing advice.
    """
    
    user_weather = input("What's the weather like today? (sunny/rainy/cold): ")
    
    advice = get_weather_advice(user_weather)  # Call the advice function with user input
    
    print(advice)  # Print the advice


if __name__ == "__main__":
    main()
