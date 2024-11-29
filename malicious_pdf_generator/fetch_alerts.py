from elasticsearch import Elasticsearch
from datetime import datetime, timedelta
import json
import sys
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()


def fetch_alerts(elastic_host, elastic_port, username, password, pdf_name):
    """Fetch alerts from Elastic Stack related to the specified PDF in the last 10 minutes."""
    try:
        api_key = os.getenv('ELASTIC_API_KEY')

        es = Elasticsearch(
            hosts=[{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
            api_key=api_key,
            verify_certs=False  # Set to True if you're using proper certificates
        )

        # Calculate time range (last 10 minutes)
        now = datetime.utcnow()
        start_time = now - timedelta(minutes=10)

        # Convert times to ISO format
        now_iso = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        start_time_iso = start_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        # Define the index pattern for alerts
        index_pattern = '.siem-signals*'  # Adjust based on your setup

        # Build the query
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match_phrase": {
                                "file.name": pdf_name
                            }
                        },
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": start_time_iso,
                                    "lte": now_iso,
                                    "format": "strict_date_optional_time"
                                }
                            }
                        }
                    ]
                }
            }
        }

        # Execute the search
        response = es.search(
            index=index_pattern,
            body=query
        )

        # Return the hits
        hits = response['hits']['hits']
        return hits

    except Exception as e:
        print(f"[ERROR] Failed to fetch alerts from Elastic Stack: {e}")
        sys.exit(1)
