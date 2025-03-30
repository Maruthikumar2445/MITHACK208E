import streamlit.cli as stcli
import sys
import os

def main():
    # Get the absolute path to the dashboard.py file
    dashboard_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "frontend",
        "dashboard.py"
    )
    
    # Run the Streamlit app
    sys.argv = ["streamlit", "run", dashboard_path]
    stcli.main()

if __name__ == "__main__":
    main()