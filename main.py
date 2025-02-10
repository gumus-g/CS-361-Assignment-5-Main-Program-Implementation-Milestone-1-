import zmq
import json

# Quality attribute 1: Reliability
# Quality attribute 1 definition:
# Reliability refers to the ability of a system to perform its required functions 
#  under specified conditions for a specified period of time without failure.

# Quality attribute 2: Efficiency
# Quality attribute 2 definition:
# Efficiency is the ability of the system to provide adequate
#  performance given the number of resources used under specified conditions.

# Quality attribute 3: Usability
# Quality attribute 3 definition:
# Usability refers to the extent to which a system can be 
#  used to achieve specified goals effectively, efficiently, and 
#  satisfactorily by specified users in a specified context of use.

context = zmq.Context()

# Function to browse recipes
def browse_recipes():
    # Heuristic #1: Visibility of System Status
    # The function provides immediate feedback by returning the list of recipes
    # Quality attribute 1: Reliability: Connects to the correct server address to browse recipes
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555") # Address to connect for browsing recipes
    socket.send_string("browse")
    recipes = socket.recv_string()
    return json.loads(recipes)

# Function to search recipes
def search_recipes(keyword):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    socket.send_string(keyword)
    search_results = socket.recv_string()
    return json.loads(search_results)

# Function to view recipe details
def view_recipe_details(recipe_id):
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")
    socket.send_string(str(recipe_id))
    details = socket.recv_string()
    return json.loads(details)

# Function to display help
def display_help():
    # Heuristic #2: Match Between System and the Real World
    # The help text uses familiar language and concepts 
    # to align with user expectations
    # Quality attribute 3: Usability: Provides clear help instructions for users
    help_text = """
    Recipe Catalog App - Help Information

    1. Browse Recipes:
       - Select option 1 from the main menu to view a list of available recipes.
    2. Search Recipes:
       - Select option 2 from the main menu to search for recipes by keyword.
       - Enter the keyword and press enter to see the search results.
    3. View Recipe Details:
       - Select option 3 from the main menu to view detailed information about a specific recipe.
       - Enter the recipe ID to view its ingredients and steps.
    4. Help:
       - Select option 4 from the main menu to view this help guide.
    5. Exit:
       - Select option 5 from the main menu to exit the application.
    """
    print(help_text)

# Function to check if the user wants to save their work before exiting 
def check_unsaved_changes():
    # Heuristic #5: Error Prevention
    # This function prevents accidental data loss by checking for unsaved changes
    unsaved_changes = input("\nDo you have any unsaved changes? If you exit without saving, you may lose your work. Type 'yes' or 'no': ")
    if unsaved_changes.lower() == "yes":
        save = input("Would you like to save your changes before exiting? Type 'yes' or 'no': ")
        if save.lower() == "yes":
            print("Your changes have been saved.")
        else:
            print("You chose not to save your changes.")
    else:
        print("No unsaved changes to worry about.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nWelcome to Recipe Catalog App")
        print("\nAbout the Recipe App :")
        print("Our Recipe Catalog App lets you explore a variety of delicious recipes at your fingertips.")
        print("Whether you want to browse, search, or view detailed recipes, we've got you covered.")
        print("Use our intuitive interfa you your next favorite dish!!!\n")

        # Heuristic #6: Recognition Rather Than Recall
        # The main menu provides a list of options, reducing the need for users to remember commands
        # Explicit navigation instructions - Inclusivity Heuristics #1
        print("Please use the main menu options to navigate through the app:")
        print("1. Browse Recipes")
        print("2. Search Recipes")
        print("3. View Recipe Details")
        print("4. Help")
        print("5. Exit")

        # Heuristic #8: Aesthetic and Minimalist Design
        # Simplify and declutter the user interface by removing unnecessary 
        # information and focusing on key tasks.
        choice = input("Enter one of the numbers to discover: ")

        if choice == "1":
            recipes = browse_recipes()
            print("\nAvailable Recipes:")
            for recipe in recipes:
                print(f"- {recipe['name']} (Cuisine: {recipe['cuisine']})")

        elif choice == "2":
             # Usability: Allows users to retry if no recipes are foun          
             while True:
                keyword = input("\nEnter a keyword to search for recipes: ")
                search_results = search_recipes(keyword)
                if search_results:
                    print("\nSearch Results:")
                    for recipe in search_results:
                        print(f"- {recipe['name']} (Cuisine: {recipe['cuisine']})")
                    break
                else:
                    retry = input("\nNo recipes found matching the keyword. Do you want to try again? Type 'yes' or 'no': ")
                    if retry.lower() != "yes":
                        break

        elif choice == "3":
            recipe_id = int(input("\nEnter the recipe ID to view details: "))
            details = view_recipe_details(recipe_id)
            if details:
                # Heuristic #7: Flexibility and Efficiency of Use
                # Displays all details of the selected recipe to cater 
                #   to both novice and experienced users
                print(f"\nRecipe Details for {details['name']}:")
                print("Ingredients:")
                for ingredient in details["ingredients"]:
                    print(f"- {ingredient}")
                print("Steps:")
                for step in details["steps"]:
                    print(f"- {step}")
                # Display image URL of the recipe   
                #print(f"Image URL: {details['image_url']}")  
            else:
                print("\nRecipe not found.")

        elif choice == "4":
            display_help()

        elif choice == "5":
            # Check for unsaved changes before exiting-Inclusivity Heuristics #2
            # Heuristic #3: User Control and Freedom
            # Confirms exit and checks for unsaved changes to prevent accidental closure and data loss
            check_unsaved_changes()
            # Usability: Confirms exit to prevent accidental closure     
            confirm_exit = input("Are you sure you want to exit? Type 'yes' or 'no': ")
            if confirm_exit.lower() == "yes":
                print("Exiting the applicationn. Bye!!!")
                break
            else:
                print("\nExit cancelled.")

        else:
            print("\nInvalid choice. Please try again.")