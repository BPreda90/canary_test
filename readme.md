# canary_test
### This project contains a small application written in Python3 that:
- On startup make sure there is a “tmp” sub folder in the current directory.
- If one does not exist, it creates it.
- Repeatedly counts the number of files in the “tmp” folder.
- Whenever the number of files reaches 10, the script creates an archive “files.tar.gz” with
all 10 files from the “tmp” directory.
- The script should then empty the folder and print “files collected” to the console before
exiting.

## Design Decisions
### The project contains three files:
1. file_collector.py
   - This script does the heavy lifting, containing the logic that achieves the task requirements
   - To access the script's logic, use one or the other wrapper scripts below 
2. run_application_in_background.py
   - This script can be used to bypass the console interface and just have the file_collector run the task in the background. 
   - Once this script is triggered in a terminal, a tmp folder is generated, and you can add files it and see the archive created
3. run_with_console_interface.py
   - This script contains a console interface for the user to use the file_collector.py via a guided method
   - The interface uses the basic python input to listen to the user's commands
   - It also offers the user the option to automatically generate 10 files for them   

## Setup
### 1. Repository
Fork https://github.com/BPreda90/canary_test and clone it to your machine.

```$ git clone git@github.com:BPreda90/canary_test.git```

### 2. Python
You will need at least Python 3.9 installed on your machine.
- [Download and install](https://www.python.org/downloads/)

The scripts use only built-in modules, so there's no need to import anything extra to run 

## Run
- Open a new terminal in Linux or Mac environment or command prompt with admin rights if using a Windows environment
- Change the working directory to the `canary_test` folder

### There are two ways of running the task:

### 1. Run the task in background without an interface
- Using python call the `run_application_in_background.py` script.
- Now as the script is running in the background, manually add at least 10 files to the newly created `tmp` folder
- Observe that a new timestamped archive has been created and the `tmp` folder is empty  

### 2. Run the task in background using a console interface
- Using python call the `run_with_console_interface.py` script.
- Follow the instructions. It will guide you on starting the script in the background and generating 10 
txt files for you
  
