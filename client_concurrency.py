import threading
import subprocess
import sys
import time
from client import run_client

# note I'm testing the program with multithreading
# currently it works better with 1-2 client thread

def run_single_client_1():
    run_client("example_concurrency_b.json")

def run_single_client_3():
    run_client("example_concurrency_b.json")
    
def run_single_client_2():
    run_client("example_concurrency_v.json")

def run_single_client_4():
    run_client("example_concurrency_v.json")

def main():
    # json_fpath_1 = "example_concurrency.json"
    # json_fpath_2 = "example_concurrency_2.json"

    # Create threads for the client scripts
    thread1 = threading.Thread(target=run_single_client_1)
    # thread2 = threading.Thread(target=run_single_client_2)
    # thread3 = threading.Thread(target=run_single_client_3)
    thread4 = threading.Thread(target=run_single_client_4)
    # thread2 = threading.Thread(target=run_single_client, args=(json_fpath_2))

    # Start the threads
    thread1.start()
    # thread2.start()

    time.sleep(5)
    # thread3.start()
    thread4.start()

    # Wait for both threads to complete
    thread1.join()
    # thread2.join()
    # thread3.join()
    thread4.join()

    print("All client scripts have finished executing.")

if __name__ == "__main__":
    # Define the endpoints and JSON data
    # try:
    #     json_fpath_1 = sys.argv[1]
    #     json_fpath_2 = sys.argv[2]
    # except:
    #     exit("Please specify twp input json files")
    main()

    