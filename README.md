# Setting up Continuous Integration Pipeline

This repository contains a Python script that automates the deployment of an HTML file to cloud storage solutions. The project is set up with a CI/CD pipeline using GitHub Actions that tests, lints, and deploys an `index.html` file to both Azure Blob Storage and AWS S3.

## Overview

The main script, `build.py`, performs the following actions:

- Copies an `index.html` file from the source directory to a destination directory.
- Ensures that the destination directory exists before copying.
- Provides a success message upon successful execution.

The project includes a GitHub Actions workflow that automates the following tasks upon each push to the `main` branch:

- Install dependencies.
- Run unit tests to ensure functionality.
- Lint the code to maintain quality.
- Deploy the `index.html` to both Azure and AWS.

## Prerequisites

Before you begin, ensure you have the following:
- Python 3.8 or higher installed.
- An AWS account with an S3 bucket configured.
- An Azure account with Blob Storage configured.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Lagiacrus96/JETAssessmentDay_2_Electric_Boogaloo.git
   cd JETAssessmentDay_2_Electric_Boogaloo
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### GitHub Secrets

Set up the following secrets in your GitHub repository to use the CI/CD pipeline:

- `AZURE_CREDENTIALS`: Your Azure credentials in a JSON format.
- `AWS_ACCESS_KEY_ID`: Your AWS access key.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.

### Local Environment Variables

Ensure your local environment is set up with the same credentials for testing locally.

## Usage

To run the script manually on your local machine:

```bash
python build.py
```

This will copy the `index.html` to the specified destination and print a success message.

## GitHub Actions Workflow

The CI/CD pipeline is defined in `.github/workflows/main.yml` and includes the following jobs:

- **build-and-test**: Installs dependencies, runs tests, and lints the code.
- **deploy**: Deploys `index.html` to Azure and AWS.

## Contributing

Feel free to fork this repository and propose changes via pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
