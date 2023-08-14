"""
This module demonstrates how to fetch data from a URL using the requests library.

Includes a single function that prints the response.
"""

import requests

class MyClass:
    """
    MyClass encapsulates the logic for fetching data from a URL.
    """

    def my_function(self):
        """
        Fetches data from a given URL and prints the response.
        """
        url = 'https://example.com'
        response = requests.get(url)
        print(response.text)

def main():
    """
    Main function to execute the logic.
    """
    obj = MyClass()
    obj.my_function()

if __name__ == "__main__":
    main()

