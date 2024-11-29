def analyze_alerts(alerts, pdf_name, log_file_path):
    """Analyze alerts and output results."""
    if not alerts:
        print("[INFO] No alerts found. The PDF is undetected.")
        with open(log_file_path, 'w') as log_file:
            log_file.write("Result: Undetected\n")
    else:
        print("[INFO] Alerts detected:")
        with open(log_file_path, 'w') as log_file:
            log_file.write("Result: Detected\n")
            for alert in alerts:
                # Extract relevant information
                alert_description = alert['_source'].get('signal', {}).get('rule', {}).get('description', 'N/A')
                impacted_assets = alert['_source'].get('host', {}).get('name', 'N/A')
                evidence = alert['_source'].get('process', {}).get('entity_id', 'N/A')
                timestamp = alert['_source'].get('@timestamp', 'N/A')

                # Output to console
                print(f"\n[ALERT]")
                print(f"Timestamp: {timestamp}")
                print(f"Description: {alert_description}")
                print(f"Impacted Assets: {impacted_assets}")
                print(f"Evidence: {evidence}")

                # Write to log file
                log_file.write(f"\n[ALERT]\n")
                log_file.write(f"Timestamp: {timestamp}\n")
                log_file.write(f"Description: {alert_description}\n")
                log_file.write(f"Impacted Assets: {impacted_assets}\n")
                log_file.write(f"Evidence: {evidence}\n")
