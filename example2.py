import requests

def curl_with_user_agent():
    try:
        url = "https://www.google.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Google homepage content received successfully.")
        else:
            print(f"Failed to curl Google. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


curl_with_user_agent()

# asdfasdfasdf