import re
# We delcare a boolean in default condition to be used within the function.
final_goodbye = False
output_message = "SPEAK UP, KID!"

def deaf_grandma(output = ""):
    # If we are overriding the default value then let's use it.
    if output == "":
        message = "HEY KID!"
    else:
        message = output
    # Now that we know what we want to say, let's say it
    user_input = input(f"{message}\n")
    # Handle the input from the user
    handle_next_question(user_input)

# This function simply processes the input from the user and then prepares the next question.
def handle_next_question(user_input):
    global output_message
    global final_goodbye
    if (user_input == ""):
        output_message = "WHAT?!"
    elif (re.match("GOODBYE", user_input)):
        # Is final_goodbye true?
        if (final_goodbye):
            # We can just print here since this is the last case, and will close anyway.
            print("LATER, SKATER!")
            exit()
        # This has to be the first goodbye you've said so set true
        output_message = "LEAVING SO SOON?"
        final_goodbye = True
    # Are any of the letters within the string a capital?
    elif (re.search("[A-Z]", user_input)):
        output_message = "NO, NOT SINCE 1946!"
    # Because our global variable remains the last assignment we need this catch case to return to default
    else:
        output_message = "SPEAK UP, KID!"
    # Call the main function for repeat
    deaf_grandma(output=output_message)




deaf_grandma()
