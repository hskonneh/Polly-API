import requests

class APIClient:
    def __init__(self, base_url):
        """
        Initializes the API client with a base URL for the API.

        Args:
            base_url (str): The base URL of the API (e.g., "http://localhost:8000").
        """
        self.base_url = base_url

    def register_user(self, username, password):
        """
        Registers a user by making a POST request to the /register endpoint.

        Args:
            username (str): The username to register.
            password (str): The password for the user.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/register"
        user_data = {"username": username, "password": password}
        try:
            response = requests.post(url, json=user_data)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def login(self, username, password):
        """
        Logs in a user to get a JWT token.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/login"
        login_data = {"username": username, "password": password}
        try:
            response = requests.post(url, data=login_data)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

if __name__ == "__main__":
    # Example usage:
    # Make sure your FastAPI server is running before executing this script.
    client = APIClient("http://localhost:8000")

    # --- Test User Registration ---
    test_username = "testuser2"
    test_password = "testpassword2"
    
    print(f"Attempting to register user: {test_username}")
    register_response = client.register_user(test_username, test_password)

    if register_response:
        print(f"Registration Status Code: {register_response.status_code}")
        if register_response.status_code == 200:
            print("User registered successfully!")
            print("Response JSON:", register_response.json())
        elif register_response.status_code == 400:
            print("Username already registered.")
            print("Response JSON:", register_response.json())
        else:
            print("An unexpected error occurred during registration.")
            print("Response Text:", register_response.text)
    
    print("\n" + "="*20 + "\n")

    # --- Test User Login ---
    print(f"Attempting to log in as user: {test_username}")
    login_response = client.login(test_username, test_password)

    if login_response:
        print(f"Login Status Code: {login_response.status_code}")
        if login_response.status_code == 200:
            print("Login successful!")
            print("Response JSON:", login_response.json())
        elif login_response.status_code == 400:
            print("Incorrect username or password.")
            print("Response JSON:", login_response.json())
        else:
            print("An unexpected error occurred during login.")
            print("Response Text:", login_response.text)
