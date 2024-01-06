import requests
import subprocess
import time

# Prompt the user for the dynamic number
user_number = input("Enter the koth game id: ")
url = f"https://tryhackme.com/games/koth/data/{user_number}"

while True:
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Clear the console screen after X seconds as mentioned below and print's the response. 
        subprocess.call('clear', shell=True)

        # Check if the response status code is 200
        if response.status_code == 200:
            # Execute jq to process the JSON response directly
            jq_command = f'echo \'{response.text}\' | jq -r \'"the box name is: " + .box.title, "The game type is: " + .gameType, "Users:" + (.tableData[] | "  - " + .username)\''
            output = subprocess.check_output(jq_command, shell=True, text=True)
            
            # This print's the result with proper formatting
            print(output)
        # Check if the response status code is 302
        elif response.status_code == 302:
            print("The game is not started yet.")
        # If the response code is neither 200 nor 302, print "Mayday" and exit 😅
        else:
            print("Mayday")
            break
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from URL: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error running jq command: {e}")

    # Here It wait for 1 second before making the next request. You could tweek the delay be X seconds here. 
    time.sleep(1)
