import argparse
import requests

def get_token_response(tenant_id, client_id, client_secret):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials"
    }
    
    response = requests.post(token_url, data=token_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to obtain token: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Authenticate against Microsoft Graph using client credentials and print the access token (and refresh token if available)."
    )
    parser.add_argument("--tenant", required=True, help="Your Azure AD tenant ID")
    parser.add_argument("--client", required=True, help="Your Azure AD client ID")
    parser.add_argument("--secret", required=True, help="Your Azure AD client secret")
    
    args = parser.parse_args()
    
    try:
        token_response = get_token_response(args.tenant, args.client, args.secret)
        access_token = token_response.get("access_token")
        refresh_token = token_response.get("refresh_token")
        
        print("Access token:")
        print(access_token)
        if refresh_token:
            print("\nRefresh token:")
            print(refresh_token)
        else:
            print("\nNo refresh token provided. (This is expected for client credentials flow.)")
    except Exception as e:
        print(e)