from flask import Blueprint, render_template, request, jsonify, send_from_directory
from app.garak import run_garak_scan, GARAK_RESULTS_DIR
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Render the index page
    return render_template('index.html')

@main_bp.route('/run_scan', methods=['POST'])
def run_scan():
    model_type = request.form.get('model_type')
    model_name = request.form.get('model_name')
    probe_set = request.form.get('probe_set')

    try:
        # Run the Garak scan and get the report filename
        report_filename = run_garak_scan(model_type, model_name, probe_set)
        return jsonify({'status': f'Scan completed successfully. Report saved as {report_filename}.'})
    except RuntimeError as e:
        # Handle errors in running the Garak scan
        return jsonify({'status': str(e)}), 500

@main_bp.route('/reports')
def list_reports():
    # Ensure the results directory exists
    if not os.path.exists(GARAK_RESULTS_DIR):
        os.makedirs(GARAK_RESULTS_DIR)

    # List all HTML reports in the GARAK_RESULTS_DIR
    files = [f for f in os.listdir(GARAK_RESULTS_DIR) if f.endswith('.html')]
    return render_template('reports.html', files=files)

@main_bp.route('/reports/<filename>')
def view_report(filename):
    # Open the selected report in a new tab
    return send_from_directory(GARAK_RESULTS_DIR, filename)
