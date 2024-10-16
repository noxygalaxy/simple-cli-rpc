import argparse
from pypresence import Presence
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Set Discord RPC details.")
    parser.add_argument('--details', type=str, help='Details (First line) for Discord RPC.')
    parser.add_argument('--state', type=str, help='State (Second line) for Discord RPC.')
    parser.add_argument('--appid', type=str, help='Application ID for Discord RPC.')
    parser.add_argument('--image', type=str, help='Name of the image to display in Discord RPC.')
    return parser.parse_args()

def get_user_input():
    rpc_details = input("Enter the details (First line): ")
    rpc_state = input("Enter the state (Second line): ")
    rpc_application_id = input("Enter the application ID: ")
    rpc_image = input("Enter the image name (optional, press enter to skip): ")
    return rpc_details, rpc_state, rpc_application_id, rpc_image

def main():
    args = parse_arguments()

    if not (args.details and args.state and args.appid):
        rpc_details, rpc_state, rpc_application_id, rpc_image = get_user_input()
    else:
        rpc_details = args.details
        rpc_state = args.state
        rpc_application_id = args.appid
        rpc_image = args.image

    rpc = Presence(rpc_application_id)  
    print("Starting up RPC...")
    
    rpc.connect()
    print("Connected to Discord RPC! ( Press Ctrl+C to Disconnect from RPC )")

    if rpc_image:
        rpc.update(state=rpc_state, details=rpc_details, large_image=rpc_image)
    else:
        rpc.update(state=rpc_state, details=rpc_details)
    
    print("RPC Updated.")

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Disconnecting from Discord RPC...")
        rpc.clear()
        print("Disconnected.")

if __name__ == "__main__":
    main()
