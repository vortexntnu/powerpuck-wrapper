import subprocess

def receive_verification_code(team_name, output_file):
    try:
        # Construct the curl command with your team's name
        url = f"http://192.168.123.132:5000/hello/{team_name}"
        command = f"curl -s {url}"  # Use the -s flag to suppress curl's progress output

        # Execute the curl command and capture the output
        output = subprocess.check_output(command, shell=True).decode().strip()

        # Write the output to the file
        with open(output_file, 'w') as file:
            file.write(output)

        print("Output saved to:", output_file)

    except subprocess.CalledProcessError as e:
        print("Error executing curl command:", str(e))
    except Exception as e:
        print("Error:", str(e))

team_name = "teamVORTEX" 

# Specify the file path to save the output
output_file = "output.txt"  # Replace with the desired file path

# Call the function to connect to the web service and receive the verification code
while True :
    receive_verification_code(team_name, output_file)
