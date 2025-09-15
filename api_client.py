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

    def cast_vote(self, poll_id, option_id, token):
        """
        Casts a vote on a poll.

        Args:
            poll_id (int): The ID of the poll to vote on.
            option_id (int): The ID of the option to vote for.
            token (str): The JWT token for authentication.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls/{poll_id}/vote"
        headers = {"Authorization": f"Bearer {token}"}
        vote_data = {"option_id": option_id}
        try:
            response = requests.post(url, headers=headers, json=vote_data)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def get_poll_results(self, poll_id):
        """
        Retrieves the results for a specific poll.

        Args:
            poll_id (int): The ID of the poll.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls/{poll_id}/results"
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def get_all_polls(self, skip=0, limit=10):
        """
        Retrieves all polls.

        Args:
            skip (int): Number of items to skip.
            limit (int): Max number of items to return.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls?skip={skip}&limit={limit}"
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def create_poll(self, question, options, token):
        """
        Creates a new poll.

        Args:
            question (str): The poll question.
            options (list): A list of strings for poll options.
            token (str): The JWT token for authentication.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls"
        headers = {"Authorization": f"Bearer {token}"}
        poll_data = {"question": question, "options": options}
        try:
            response = requests.post(url, headers=headers, json=poll_data)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def get_specific_poll(self, poll_id):
        """
        Retrieves a specific poll by ID.

        Args:
            poll_id (int): The ID of the poll to retrieve.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls/{poll_id}"
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

    def delete_poll(self, poll_id, token):
        """
        Deletes a poll by ID.

        Args:
            poll_id (int): The ID of the poll to delete.
            token (str): The JWT token for authentication.

        Returns:
            requests.Response: The response object from the API call.
        """
        url = f"{self.base_url}/polls/{poll_id}"
        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = requests.delete(url, headers=headers)
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            return None

if __name__ == "__main__":
    # Example usage:
    # Make sure your FastAPI server is running before executing this script.
    client = APIClient("http://localhost:8000")

    # --- Test User Registration ---
    test_username = "testuser4"
    test_password = "testpassword4"
    
    print(f"Attempting to register user: {test_username}")
    register_response = client.register_user(test_username, test_password)

    if register_response:
        print(f"Registration Status Code: {register_response.status_code}")
        if register_response.status_code == 200:
            print("User registered successfully!")
        else:
            print(f"Registration failed. Status: {register_response.status_code}, Response: {register_response.text}")

    print("\n" + "="*20 + "\n")

    # --- Test User Login ---
    print(f"Attempting to log in as user: {test_username}")
    login_response = client.login(test_username, test_password)
    access_token = None

    if login_response:
        print(f"Login Status Code: {login_response.status_code}")
        if login_response.status_code == 200:
            print("Login successful!")
            access_token = login_response.json().get("access_token")
        else:
            print(f"Login failed. Status: {login_response.status_code}, Response: {login_response.text}")

    print("\n" + "="*20 + "\n")

    # --- Poll ID for testing ---
    # NOTE: You will need to have a poll available in your database for the following tests to work.
    # Replace this with an actual poll ID from your database.
    poll_id_to_test = 1

    # --- Test Casting a Vote ---
    if access_token:
        # NOTE: You will need to have an option available for the poll in your database.
        # Replace this with an actual option ID from your database.
        option_id_to_vote = 1

        print(f"Attempting to cast a vote on poll {poll_id_to_test} for option {option_id_to_vote}")
        vote_response = client.cast_vote(poll_id_to_test, option_id_to_vote, access_token)

        if vote_response:
            print(f"Vote Casting Status Code: {vote_response.status_code}")
            if vote_response.status_code == 200:
                print("Vote cast successfully!")
            else:
                print(f"Vote casting failed. Status: {vote_response.status_code}, Response: {vote_response.text}")
    else:
        print("Skipping vote casting test because login failed or no access token was received.")

    print("\n" + "="*20 + "\n")

    # --- Test Retrieving Poll Results ---
    print(f"Attempting to retrieve results for poll {poll_id_to_test}")
    results_response = client.get_poll_results(poll_id_to_test)

    if results_response:
        print(f"Poll Results Status Code: {results_response.status_code}")
        if results_response.status_code == 200:
            print("Poll results retrieved successfully!")
            print("Response JSON:", results_response.json())
        elif results_response.status_code == 404:
            print("Poll not found.")
        else:
            print(f"An unexpected error occurred while retrieving poll results. Status: {results_response.status_code}, Response: {results_response.text}")

    print("\n" + "="*20 + "\n")

    # --- Test Get All Polls ---
    print("Attempting to retrieve all polls")
    all_polls_response = client.get_all_polls()

    if all_polls_response:
        print(f"Get All Polls Status Code: {all_polls_response.status_code}")
        if all_polls_response.status_code == 200:
            print("All polls retrieved successfully!")
            print("Response JSON:", all_polls_response.json())
        else:
            print(f"Failed to retrieve all polls. Status: {all_polls_response.status_code}, Response: {all_polls_response.text}")

    print("\n" + "="*20 + "\n")

    # --- Test Create a Poll ---
    if access_token:
        new_poll_question = "What is your favorite color?"
        new_poll_options = ["Red", "Blue", "Green"]
        print(f"Attempting to create a poll: '{new_poll_question}' with options {new_poll_options}")
        create_poll_response = client.create_poll(new_poll_question, new_poll_options, access_token)

        if create_poll_response:
            print(f"Create Poll Status Code: {create_poll_response.status_code}")
            if create_poll_response.status_code == 200:
                print("Poll created successfully!")
                created_poll = create_poll_response.json()
                print("Created Poll JSON:", created_poll)
                poll_id_to_test = created_poll.get("id") # Update poll_id_to_test with the newly created poll's ID
            else:
                print(f"Poll creation failed. Status: {create_poll_response.status_code}, Response: {create_poll_response.text}")
    else:
        print("Skipping poll creation test because login failed or no access token was received.")

    print("\n" + "="*20 + "\n")

    # --- Test Get a Specific Poll ---
    if poll_id_to_test:
        print(f"Attempting to retrieve poll {poll_id_to_test}")
        specific_poll_response = client.get_specific_poll(poll_id_to_test)

        if specific_poll_response:
            print(f"Get Specific Poll Status Code: {specific_poll_response.status_code}")
            if specific_poll_response.status_code == 200:
                print("Specific poll retrieved successfully!")
                print("Response JSON:", specific_poll_response.json())
            elif specific_poll_response.status_code == 404:
                print("Specific poll not found.")
            else:
                print(f"An unexpected error occurred while retrieving specific poll. Status: {specific_poll_response.status_code}, Response: {specific_poll_response.text}")
    else:
        print("Skipping get specific poll test because no poll ID is available.")

    print("\n" + "="*20 + "\n")

    # --- Test Delete a Poll ---
    if access_token and poll_id_to_test:
        print(f"Attempting to delete poll {poll_id_to_test}")
        delete_poll_response = client.delete_poll(poll_id_to_test, access_token)

        if delete_poll_response:
            print(f"Delete Poll Status Code: {delete_poll_response.status_code}")
            if delete_poll_response.status_code == 204:
                print("Poll deleted successfully!")
            elif delete_poll_response.status_code == 404:
                print("Poll not found or not authorized to delete.")
            else:
                print(f"An unexpected error occurred while deleting poll. Status: {delete_poll_response.status_code}, Response: {delete_poll_response.text}")
    else:
        print("Skipping delete poll test because login failed, no access token, or no poll ID is available.")

    print("\n" + "="*20 + "\n")
