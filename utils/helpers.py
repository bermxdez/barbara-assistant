def greet_user(name):
    return f"Hi, {name}! How can I help you today?"

def is_valid_city(city):
    city = city.strip()
    return (
        city != ""
        and all(char.isalpha() or char.isspace() for char in city)
        and len(city.replace(" ", "")) >= 2
    )


def is_valid_name(name):
    return name.strip() != "" and all(x.isalpha() or x.isspace() for x in name)
