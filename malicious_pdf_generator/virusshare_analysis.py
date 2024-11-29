import hashlib
import requests
import os
import sys
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def compute_file_hash(file_path, hash_algorithm='sha256'):
    """Compute the hash of a file using the specified hash algorithm."""
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        file_hash = hash_func.hexdigest()
        return file_hash
    except Exception as e:
        print(f"[ERROR] Failed to compute hash for {file_path}: {e}")
        sys.exit(1)

def check_virusshare(file_hash):
    """Submit the file hash to VirusShare API and return the results."""
    api_key = os.getenv('VIRUSSHARE_API_KEY')
    if not api_key:
        print("[ERROR] VIRUSSHARE_API_KEY is not set.")
        sys.exit(1)
    
    # Construct the API URL
    request_type = 'file_report'  # Assuming 'file_report' is the correct request
    api_url = f"https://virusshare.com/apiv2/{request_type}?apikey={api_key}&hash={file_hash}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            # Parse the response (assuming JSON)
            result = response.json()
            return result
        else:
            print(f"[ERROR] VirusShare API returned status code {response.status_code}: {response.text}")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Failed to connect to VirusShare API: {e}")
        sys.exit(1)
        
def analyze_virusshare_results(result, log_file_path):
    """Analyze the VirusShare results and log them."""
    if not result:
        print("[ERROR] No result received from VirusShare API.")
        return
    
    # Assuming the result contains a 'response_code' and 'verbose_msg'
    response_code = result.get('response_code')
    verbose_msg = result.get('verbose_msg')
    
    with open(log_file_path, 'a') as log_file:
        log_file.write("\n[VirusShare Report]\n")
        
        if response_code == 1:
            # File is known and has been analyzed
            print("[INFO] VirusShare has records of this file.")
            log_file.write("VirusShare has records of this file.\n")
            
            # Extract additional information (assuming keys exist)
            positives = result.get('positives')
            total = result.get('total')
            scans = result.get('scans', {})
            
            print(f"Detections: {positives}/{total}")
            log_file.write(f"Detections: {positives}/{total}\n")
            
            # Optionally, list the antivirus results
            print("Antivirus Results:")
            log_file.write("Antivirus Results:\n")
            for av_name, av_result in scans.items():
                detected = av_result.get('detected')
                result_str = av_result.get('result', 'Clean')
                print(f"{av_name}: {'Detected' if detected else 'Clean'} - {result_str}")
                log_file.write(f"{av_name}: {'Detected' if detected else 'Clean'} - {result_str}\n")
        elif response_code == 0:
            # File is unknown to VirusShare
            print("[INFO] VirusShare has no records of this file. It may be a new or unknown file.")
            log_file.write("VirusShare has no records of this file. It may be new or unknown.\n")
        else:
            # Some error occurred
            print(f"[ERROR] VirusShare API error: {verbose_msg}")
            log_file.write(f"VirusShare API error: {verbose_msg}\n")
