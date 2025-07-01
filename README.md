# Project Documentation

This README documents the setup process, changes made to the codebase to resolve issues, and the steps to set up the development environment using `uv` for dependency management.

## Changes Made to the Codebase

1. **Dependency Conflict Resolution**:
   - Encountered dependency conflicts when installing libraries from `requirements.txt`.
   - Noticed that `crewai` version must not be changed as specified in `requirements.txt`.
   - Commented out other dependencies in `requirements.txt` and installed `crewai` independently.
   - Manually installed additional libraries deemed necessary based on code inspection.

2. **Agent Assignment Fixes**:
   - Identified that all tasks in the codebase were assigned to a single "doctor" agent.
   - Refactored the code to assign tasks to their respective agents for proper task-agent alignment.

3. **Uvicorn Application Error**:
   - Encountered an error when running `main.py` due to passing the app instance directly to Uvicorn, which caused issues with reload functionality.
   - Modified the code to use a string import path for the app, enabling Uvicorn to reload correctly during development.

4. **Blood Test Report Tool Refactoring**:
   - Identified improper usage of the `BloodTestReportTool`.
   - Replaced the standalone `async read_data_tool` method with a new `BloodTestReportTool` class that inherits from `BaseTool` (from `crewai.tools`).
   - Implemented PDF extraction using `pypdf.PdfReader` to standardize tool creation and ensure compatibility with the CrewAI framework.
   - Refactored other tools to follow the same `BaseTool` inheritance structure for consistency and integration with CrewAI.

5. **API Key and Tool Configuration**:
   - Set up API keys in a `.env` file for secure configuration.
   - Configured the `SerperDevTool` to integrate with the project.

## Setup Instructions

To set up the development environment and run the project, follow these steps:

### Prerequisites
- Ensure Python (version compatible with the project, e.g., Python 3.10+) is installed.
- Install `uv` for dependency management.

### Steps to Set Up the Environment

1. **Install `uv`**:
   - Install `uv` globally using pip:
     ```bash
     pipx install uv
     ```
   - Alternatively, follow the official `uv` installation instructions: [uv documentation](https://github.com/astral-sh/uv).

2. **Create a Virtual Environment**:
   - Navigate to the project directory:
     ```bash
     cd /path/to/project
     ```
   - Create a virtual environment using `uv`:
     ```bash
     uv venv .venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source .venv/bin/activate
       ```
     - On Windows:
       ```bash
       .venv\Scripts\activate
       ```

3. **Install Dependencies**:
   - Install the required dependencies from `requirements.txt`:
     ```bash
     uv pip install -r requirements.txt
     ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory.
   - Add necessary API keys (e.g., for `SerperDevTool` or other services) in the `.env` file:
     ```env
     GROQ_API_KEY = ""
     SERPER_API_KEY = ""
     ```
   - Ensure the `.env` file is loaded correctly in the application (e.g., using `python-dotenv` if required).

5. **Run the Application**:
   - Execute the main script:
     ```bash
     python3 main.py
     ```

### Additional Notes
- Verify that the `.env` file is correctly configured with all required API keys before running the application.
