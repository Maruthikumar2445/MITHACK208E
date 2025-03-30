# Soil 3D Molecules Visualization

A web application for visualizing and analyzing molecular structures in 3D, built with Flask and RDKit.

## Features

- 3D molecular structure visualization
- DNA/RNA sequence to amino acid conversion
- SMILES string processing and visualization
- Interactive web interface

## Prerequisites

- Python 3.x
- Flask
- RDKit
- py3Dmol
- Gunicorn

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd soil-3d_molecules
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

- `app.py`: Main Flask application file
- `require.py`: Custom module for 3D molecule visualization
- `static/`: Directory containing static files (CSS, JavaScript)
- `templates/`: Directory containing HTML templates
- `requirements.txt`: List of Python dependencies

## Dependencies

- Flask: Web framework
- RDKit: Chemical informatics toolkit
- py3Dmol: 3D molecular visualization
- Gunicorn: WSGI HTTP server

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here] 