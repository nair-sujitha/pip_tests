import sys
import time

def main():
    print("Running the teardown tc0001 scripts")

    time.sleep(1)  # Simulate some work

    # Exit with 0 or 1 based on command-line argument
    if len(sys.argv) > 1 and sys.argv[1] == "fail":
        print("Script execution failed. "
              "Exiting with code 1 (simulated failure).")
        sys.exit(1)
    else:
        print("Successful script execution.. "
              "Exiting with code 0 (success).")
        sys.exit(0)

if __name__ == "__main__":
    main()
