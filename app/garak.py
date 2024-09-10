import subprocess
import os
from datetime import datetime

# Define the directory for storing Garak scan results
GARAK_RESULTS_DIR = '/home/karan/.local/share/garak/garak_runs/'

# Function to ensure the results directory exists
def ensure_results_directory():
    if not os.path.exists(GARAK_RESULTS_DIR):
        os.makedirs(GARAK_RESULTS_DIR)

def run_garak_scan(model_type, model_name, probe_set):
    """
    Runs the Garak scan using the provided model type, model name, and probe set.
    Saves the results as an HTML file in the reports directory.
    """
    # Ensure the results directory exists before running the scan
    ensure_results_directory()

    # Generate a unique filename using timestamp to avoid conflicts
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f"{probe_set}_{timestamp}.html"
    output_path = os.path.join(GARAK_RESULTS_DIR, output_filename)

    # Correct command to run Garak
    command = [
        'python3', '-m', 'garak',
        '--model_type', model_type,
        '--model_name', model_name,
        '--probes', probe_set,
    ]

    try:
        # Execute the command and capture output
        subprocess.run(command, check=True)
        return output_filename  # Return the filename of the generated report
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error running Garak scan: {str(e)}")
