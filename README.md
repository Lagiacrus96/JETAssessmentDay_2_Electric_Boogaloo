# Project Repository: Cloud Deployment Automation

## Overview

This repository includes essential tools and configurations for automating the deployment of a static "Hello, World!" web page to both AWS and Azure cloud platforms. It features Python scripts for file management, automated testing, and Terraform configurations tailored for each cloud provider.

### Repository Structure

- **Python Scripts**: Automate file copying and provide utility functions.
- **HTML Files**: Contains a simple "Hello, World!" page used for deployment.
- **Terraform Configurations**:
  - `aws/`: Configurations for AWS deployments using S3 and other resources.
  - `azure/`: Configurations for Azure deployments using resource groups and storage accounts.
- **GitHub Actions Workflows**:
  - **AWS**: Automates build, test, and deployment processes to AWS.
  - **Azure**: Handles build, test, and deployment to Azure, with ongoing adjustments for authentication issues.

## Getting Started

### Prerequisites

- Python 3.8+
- Terraform
- AWS CLI (configured with user credentials)
- Azure CLI (configured with user credentials)

### Installation

Clone the repository to your local system:

```bash
git clone https://github.com/your-username/your-repository.git
```

Navigate to the repository directory:

```bash
cd your-repository
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Build Script

To copy `index.html` to the designated distribution directory:

```bash
python build.py
```

### Deploying to Cloud Services

Initialize and apply Terraform configurations within the respective cloud directories:

```bash
# For AWS
cd aws
terraform init
terraform apply

# For Azure
cd azure
terraform init
terraform apply
```

### Testing

Ensure the functionality of the scripts by running:

```bash
pytest
```

## GitHub Actions Workflows

### AWS Workflow

This workflow automates the process of testing, building, and deploying to AWS. It handles configuration of AWS credentials, executes Terraform scripts, and uploads the resulting `index.html` to an S3 bucket.

### Azure Workflow

Handles testing and building, and manages deployment to Azure. Due to ongoing authentication adjustments, check the latest runs for updates on authentication configurations and deployment success.

## Contributing

Contributions are welcome! Please adhere to the following workflow:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
