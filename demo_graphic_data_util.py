import random

# Define lists for countries and genders
countries = ["USA", "JAPAN", "CANADA", "INDIA", "SOUTH_AFRICA"]
genders = ["MALE", "FEMALE"]

# Mapping of countries to their respective states
states_mapping = {
    "USA": ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri"],
    "INDIA": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"],
    "CANADA": ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"],
    "JAPAN": ["Hokkaido", "Tohoku", "Kanto", "Chubu", "Kinki/Kansai", "Chugoku", "Shikoku", "Kyushu"],
    "SOUTH_AFRICA": ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "Northern Cape", "North West", "Western Cape"]
}

def get_country():
    """Returns a random country from the predefined list."""
    return random.choice(countries)

def get_state(country):
    """Returns a random state for a given country."""
    if country in states_mapping:
        return random.choice(states_mapping[country])
    return None

def get_age():
    """Returns a random age between 0 and 60."""
    return random.randint(0, 60)

def get_gender():
    """Returns a random gender from the predefined list."""
    return random.choice(genders)

def get_user_id():
    return random.randint(1, 100000)

if __name__ == "__main__":
    # Example usage
    country = get_country()
    print(f"Country: {country}")
    print(f"State: {get_state(country)}")
    print(f"Age: {get_age()}")
    print(f"Gender: {get_gender()}")
