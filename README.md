# Password Strength Analyzer
**Course:** Introduction to Analysis of Algorithms | **B.Tech CSE** | **Python 3.9+** | **Group size: 5**

## Run
`python3 -m password_analyzer.app`

Use sample strings for the class demo, never a real account password.

## Tests
`python3 -m unittest discover -s tests -v`

## Runtime experiment
`python3 benchmark.py`
Creates `benchmark_results.csv` using synthetic strings of increasing lengths. Runtime varies by device and system load. Theoretical time complexity is O(n).

## Files
- `password_analyzer/app.py`: implementation
- `tests/test_app.py`: four unit tests
- `benchmark.py`: runtime measurement
- `benchmark_results.csv`: benchmark data from this build
- `complexity_graph.png`: runtime graph
- `report.pdf`: written project report
- `class_presentation.pptx`: 10-slide presentation
- `presentation_outline.md`: slide outline
- `sample_outputs.txt`: demo examples

## Limitations
This is an educational heuristic, not a professional security audit. The common-password list is small; simple patterns may miss weaknesses; entropy assumes random independent character choices. It does not check breached-password databases and does not save or transmit input.

## Web GUI (Flask)
The project includes a local browser interface.

1. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Start the web app:
   ```bash
   python3 web_app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

The web server binds to localhost only. Use sample strings, not real account passwords. The app does not persist the submitted password.
