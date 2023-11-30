from database import init_db

def main():
    """
    Main entry point for the CRM application.

    This function initializes the database and then starts the main
    application logic. It is the starting point of the CRM application.
    Here, you can integrate the logic for user input handling, 
    application navigation, and other high-level application functionalities.
    """
    # Initialize the database
    init_db()


if __name__ == '__main__':
    main()
