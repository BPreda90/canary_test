import file_collector

# This script can be used to run the main task in the background without using the application interface.
# Once this is running, the user can manually add files to the tmp folder.
# Once there are 10 files, the script will archive the files and clean up the tmp folder.

file_collector.run_file_collection_in_background()
