#### The exercise produces a voter registration application asking the user a few
##### simple questions followed by a confirmation of registration,
##### provided the user is eligible.

# List of valid U.S. state abbreviations
valid_states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID',
    'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
    'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
    'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
    'WI', 'WY'
]


# Function to validate user inputs
def get_input(prompt, error_msg=None, validation_func=None):
    while True:
        user_input = input( prompt )
        if validation_func and not validation_func( user_input ):
            print( error_msg or "Invalid input, please try again." )
        else:
            return user_input


# Function to validate age
def validate_age(age):
    try:
        age = int( age )
        return 18 <= age <= 120  # Valid if age is between 18 and 120
    except ValueError:
        return False


# Function to validate U.S. state
def validate_state(state):
    return state.upper() in valid_states


# Function to validate zipcode (assuming U.S. zipcodes)
def validate_zipcode(zipcode):
    return zipcode.isdigit() and len( zipcode )==5


# Main function for voter registration
def voter_registration():
    print( "Welcome to the Voter Registration System!" )
    print( "You can type 'exit' at any time to cancel the registration process." )

    # Collect user information
    first_name = get_input( "Enter your first name: " )
    last_name = get_input( "Enter your last name: " )
    age = get_input( "Enter your age: ")
    # Validate age for voting eligibility
    age = int( age )
    if age < 18:
        print( "You are not eligible to vote. You must be at least 18 years old." )
        return

    country = get_input( "Enter your country of citizenship: " )

    # Validate U.S. citizenship
    if country.lower()!='us' and country.lower()!='usa' and country.lower()!='united states':
        print( "You are not eligible to vote in the U.S. You must be a U.S. citizen." )
        return

    # Collect remaining information
    state = get_input( "Enter your state of residence (2-letter abbreviation): ",
                       "Please enter a valid U.S. state abbreviation (e.g., CA, TX).", validate_state )
    zipcode = get_input( "Enter your zipcode (5 digits): ",
                         "Please enter a valid 5-digit U.S. zipcode.", validate_zipcode )

    # Registration successful
    print( "\nCongratulations! You have successfully registered to vote." )
    print( f"Summary of your registration:" )
    print( f"Name: {first_name} {last_name}" )
    print( f"Age: {age}" )
    print( f"Country: {country}" )
    print( f"State: {state}" )
    print( f"Zipcode: {zipcode}" )
    print( "Thank you for registering to vote!" )


# Running the voter registration program
if __name__=="__main__":
    voter_registration()