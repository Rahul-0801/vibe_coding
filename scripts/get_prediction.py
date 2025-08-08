import requests
import sys
import json
import os

def get_prediction():
    """
    Sends a sample payload to the FastAPI /predict endpoint and
    sets the prediction result as a GitHub Action output.
    """
    try:
        url = 'http://127.0.0.1:8000/predict'
        # This payload is for demonstration. You might want to make it dynamic.
        payload = {'files_changed': 10, 'test_pass_rate': 0.85, 'build_time_sec': 100}

        print("Sending sample input to /predict endpoint...")
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes

        prediction_data = response.json()
        print('Prediction Response:', prediction_data)

        # Assumes the API response is a JSON with a 'prediction' key.
        # e.g., {'prediction': 'low_risk'} or {'prediction': 'high_risk'}
        prediction_result = prediction_data.get('prediction', 'unknown')

        # Set the output for the GitHub Actions step
        if 'GITHUB_OUTPUT' in os.environ:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                print(f'prediction={prediction_result}', file=f)

    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}', file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Failed to decode JSON from response: {response.text}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_prediction()

