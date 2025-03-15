import requests
import time

def test_request():
    url = "http://localhost:5000/test"  # Adjust the port if necessary
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Test Passed: Query successfully processed.")
            print("Response:", response.text)
        else:
            print("Test Failed: Unexpected response status.", response.status_code)
    except Exception as e:
        print("Test Failed: Exception occurred.", str(e))

if __name__ == "__main__":
    print("Waiting for services to start...")
    time.sleep(10)  # Give services some time to start
    test_request()
