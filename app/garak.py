import subprocess
import os

def run_garak_scan(model_type, model_name, probe_set):
    """
    Runs a Garak scan with the specified model type, model name, and probe set.
    The output will be saved in a .jsonl file in the `garak_results` directory.
    """
    output_file = os.path.join('garak_results', 'scan_results.jsonl')
    
    # Command to run Garak scan
    command = [
        'python', '-m', 'garak',
        '--model_type', model_type,
        '--model_name', model_name,
        '--probes', probe_set,
        '--output', output_file
    ]
    
    # Execute the command
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if process.returncode != 0:
        return f"Error running Garak scan: {process.stderr}"
    
    return f"Scan completed successfully. Results stored in {output_file}"

def parse_garak_results(file_path):
    """
    Parses the Garak scan results from a .jsonl file.
    Returns a list of dictionaries with parsed results.
    """
    import json
    
    results = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                results.append(json.loads(line))
    except FileNotFoundError:
        return "Result file not found. Ensure the scan has been run."
    
    return results
