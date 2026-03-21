# Import required libraries
import os
import sys
import subprocess

def build_app():
    # Navigate to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Build the app for Android
    subprocess.run(['npx', 'react-native', 'android', 'build'])

def clean_app():
    # Navigate to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Clean the app build for Android
    subprocess.run(['npx', 'react-native', 'android', 'clean'])

def run_app():
    # Navigate to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Run the app for Android
    subprocess.run(['npx', 'react-native', 'run-android'])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "build":
            build_app()
        elif sys.argv[1] == "clean":
            clean_app()
        elif sys.argv[1] == "run":
            run_app()