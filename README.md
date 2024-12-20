# DHI Feedback Management System

Last-moment feedback solution.

## Overview

DHI Feedback is a easy lazy way to provide feedback designed to make you even more lazy.

## Prerequisites

- **Operating System**: Linux (x86_64), windows (not tested, not recommended)
- **Python Environment**: Conda
- **Dependencies**: Specified in `environment.yml`

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/bharathpofficial/dhi-feedback.git
cd dhi-feedback
```

### 2. Create Conda Environment

```bash
conda env create --file environment.yml -y
conda activate dhi-feedback
```

**Note**: Ensure you have Conda installed before running these commands.

### 3. WebDriver Configuration

**Geckodriver Installation**:
- Download geckodriver for your specific OS
- Follow platform-specific installation instructions
- Ensure geckodriver is accessible in system PATH

## Running the Application

After activating the conda environment, execute the main script:

```bash
python dhifeedback.py
```

## Troubleshooting

- Verify conda environment activation
- Check geckodriver compatibility with your browser version
- Ensure all dependencies are correctly installed
- If in future dhi change codebase, revision has to be conducted.

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the terms specified in the `LICENSE` file located in the repository root. Please refer to the `LICENSE` file for complete licensing details.
