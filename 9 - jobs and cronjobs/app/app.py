import time
import sys

if __name__ == "__main__":
    job_type = sys.argv[1] if len(sys.argv) > 1 else "job"
    if job_type == "job":
        print("Starting data processing...")
        time.sleep(2)
        print("Processing completed!")
    elif job_type == "cronjob":
        print("Running simulated backup...")
        time.sleep(2)
        print("Backup finished!")
    else:
        print(f"Unknown type: {job_type}")
