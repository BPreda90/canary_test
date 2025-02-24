import file_collector


# This script offers us a console interface that guides us on using the application using standard inputs
# Following the steps it provides, it creates 10 randomly named txt files inside the 'tmp' folder
# Afterward, it triggers the background method inside the file_collector
# At the end we enter a loop where we can create batches of 10 files inside while the loop is running.
# Once we're done we can call the quit method where the background task is stopped,
# and the application interface is closed.


def run_application_interface():
    print("Welcome to the file collection application.\n"
          "This interface can be used to run the file_collector script from a console interface.\n"
          "The file_collector does a few things:\n"
          "1. It will generate a tmp file in the working directory if there isn't one already.\n"
          "2. It will check every 0.5 seconds to see if there are at least 10 files in the 'tmp' folder.\n"
          "3. Once there are at least 10 files in the 'tmp folder, it will archive them in a \ntimestamped .tar.gz"
          " file, then it will delete the tmp folder and create a new one. \n"
          "Please note that the script will only check the tmp folder for files, it will ignore anything inside"
          " a sub directory\n")
    handle_first_user_input(
        "Before we start, shall we create 10 empty txt files inside the 'tmp' folder? \nyes or no\n")


def get_user_input(msg):
    user_input = input(msg).strip().lower()
    return user_input


def handle_first_user_input(msg):
    user_input = get_user_input(msg)
    if user_input not in {'yes', 'no'}:
        print("{} was not an expected reply\n\n".format(user_input))
        handle_first_user_input(
            "Let's try again.\nShall we create 10 empty txt files inside the 'tmp' folder?\nyes or no\n")
    elif user_input == 'yes':
        file_collector.create_10_empty_txt_files_in_tmp_folder()
        print("We've generated 10 empty txt files in the tmp folder \n")
        user_input = input("Shall we start the file_collector.py script \nyes or no\n")
        handle_user_input_for_running_the_file_collector(user_input)
    elif user_input == 'no':
        user_input = get_user_input("Then shall we start the file collector in the background\nyes or no\n")
        handle_user_input_for_running_the_file_collector(user_input)


def handle_user_input_for_running_the_file_collector(msg):
    if msg not in ('yes', 'no'):
        print("{} was not really expected\n\n".format(msg))
        user_input = get_user_input("Let's try again! Shall we start the file collector in the background\nyes or no\n")
        handle_user_input_for_running_the_file_collector(user_input)
    elif msg == 'yes':
        print("The tmp folder has been created. You can now add files in the folder. \n"
              "Once there are at least 10,"
              " the files will be collected and archived as per the previous instruction\n")
        file_collector.run_file_collection_in_background()
        handle_user_input_in_final_loop()
    elif msg == 'no':
        input("Alright, then you can just hit 'Enter' key and the application will close for you\n")
        handle_application_end()


def handle_user_input_in_final_loop():
    user_input = get_user_input(
        "Now I'm waiting for your input\n "
        "If you type 'create' and I'll create another batch of 10 files for you, or 'quit' and we can close the application.\n").strip().lower()
    if user_input not in ('create', 'quit'):
        print("I couldn't understand that, please try again \n\n")
        handle_user_input_in_final_loop()
    elif user_input == 'create':
        file_collector.create_10_empty_txt_files_in_tmp_folder()
        handle_user_input_in_final_loop()
    elif user_input == 'quit':
        handle_application_end()


def handle_application_end():
    print('Closing the application. Thank you for playing around with this interface!')
    file_collector.stop_event.set()  # Signal the background thread to stop
    exit(0)


run_application_interface()
