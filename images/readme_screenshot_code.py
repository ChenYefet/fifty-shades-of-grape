from datetime import datetime

def parse_event_logs(event_log_files):
    """
    Parses event log files to extract event details and their timestamps

    Parameters:
    event_log_files (list): A list of event log file names, e.g.
                            ["event123_20241127153000_START.log", "event456_20241127160000_START.log"]
    
    Returns:
    dict: A dictionary mapping event IDs (str) to event details (dict) with keys:
          - "timestamp" (datetime): The event's timestamp
          - "status" (str): The event's status (e.g. "START" or "END")
    """

    event_details = {}

    for filename in event_log_files:

        try:
            components = filename.split("_")
            if len(components) < 3:
                raise ValueError("Invalid file format")
            
            event_id = components[0].replace("event", "").strip()
            timestamp_str = components[1]
            status = components[2].replace(".log", "").strip().upper()
            timestamp = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")

            event_details[event_id] = {"timestamp": timestamp, "status": status}
        
        except (ValueError, IndexError) as e:
            print(f"Error processing file '{filename}': {e}")
            continue
    
    return event_details
