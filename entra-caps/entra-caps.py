import argparse
import requests
import json
import sys

def fetch_policies(access_token):
    url = "https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch policies: {response.status_code} {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch conditional access policies from Microsoft Graph API.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--token", help="Access token string")
    group.add_argument("--token-file", help="File containing the token response JSON from the authentication script")
    parser.add_argument("--output", default="policies.json", help="Output file to store policies (default: policies.json)")
    
    args = parser.parse_args()
    
    if args.token:
        access_token = args.token
    elif args.token_file:
        try:
            with open(args.token_file, "r") as f:
                token_response = json.load(f)
            access_token = token_response.get("access_token")
            if not access_token:
                sys.exit("Access token not found in the token file.")
        except Exception as e:
            sys.exit(f"Error reading token file: {e}")
    
    try:
        policies = fetch_policies(access_token)
        with open(args.output, "w") as f:
            json.dump(policies, f, indent=4)
        print(f"Policies saved to {args.output}")
    except Exception as e:
        print(e)