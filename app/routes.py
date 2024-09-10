from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.garak import run_garak_scan, parse_garak_results

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/run_scan', methods=['POST'])
def run_scan():
    # Capture the form data
    model_type = request.form.get('model_type')
    model_name = request.form.get('model_name')
    probe_set = request.form.get('probe_set')
    
    if not model_type or not model_name or not probe_set:
        return jsonify({'status': 'Missing input data. Please fill out all fields.'}), 400
    
    # Run Garak scan
    try:
        scan_results = run_garak_scan(model_type, model_name, probe_set)
        # Redirect to results page after running the scan
        return jsonify({'status': 'Scan initiated successfully. Check results page.'})
    except Exception as e:
        return jsonify({'status': f'Error: {str(e)}'}), 500

@main_bp.route('/results')
def results():
    try:
        # Parse the latest Garak scan results
        parsed_results = parse_garak_results()
        return render_template('results.html', results=parsed_results)
    except FileNotFoundError:
        # Handle case where results are not found
        return render_template('results.html', results=[], error="No results found. Please run a scan first.")
    except Exception as e:
        return render_template('results.html', results=[], error=f"An error occurred: {str(e)}")
