
def get_weather_advice(weather: str) -> str:
    """
        Provide clothing recommendations based on the weather input.

        Args:
            weather (str): The current weather condition ("sunny", "rainy", "cold").

        Returns:
            str: Clothing recommendation for the given weather, or an error message if the input is invalid.
    """

    weather = weather.strip().lower()

    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."


def main():
    """
        Main function to prompt the user for the weather and print appropriate clothing advice.
    """

    user_weather = input("What's the weather like today? (sunny/rainy/cold): ")
    
    advice = get_weather_advice(user_weather)
    
    print(advice)


if __name__ == "__main__":
    main()
