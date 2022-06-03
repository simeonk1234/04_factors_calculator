# Main routine goes here

# Puts series of symbols at the start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer")
    print()
    print("This program assumes that images are being respresented in 24 bit colour (ie: 24 bits per pixel). For text we asume that ascii encoding is being used (8 bits per character) ")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    return ""

def num_check(question):

    valid = False
    while not valid:

        error = "Please enter a number that is more than one and less than 201"
    
        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if 0 < response < 201:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
        
def get_factors():
    print(24)

# Heading

statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the programme before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*" )
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
print()