# Due Date Calculator Microservice CI/CD

## Project Overview

A solution that implements a due date calculator in an issuetracking system.

-  Input: Takes the submit date/time and turnaround time.
-  Output: Returns the date/time when the issue is resolved.

## Jenkins Pipeline

The pipeline follows these steps:

1. **Checkout Code**: Clones the repository from GitHub.
2. **Setup Python**: Ensures Python and necessary dependencies are available.
3. **Install Dependencies**: Installs required Python packages.
4. **Run Tests**: Executes unit tests to validate functionality.
5. **Lint Code**: Checks for code quality issues using `flake8`.
6. **Deploy (Placeholder)**: Reserved for future deployment steps.

## Jenkinsfile

Below is the Jenkinsfile implementing the pipeline:

```groovy
pipeline {
    agent any
    
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sheikhzain64/Emarsays'
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'apt update && apt install -y python3 python3-pip'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirements.txt || echo "No requirements.txt found, skipping."'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s . -p "*.py"'
            }
        }
        
        stage('Lint Code') {
            steps {
                sh 'pip3 install flake8'
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || echo "Linting issues found."'
            }
        }
        
        
        stage('Deploy (Placeholder)') {
            steps {
                echo 'Deployment step (to be implemented)'
            }
        }
    }
}
```

## Prerequisites

Before running the pipeline, ensure the following:

- Jenkins is installed and running.
- Your GitHub repository is public or accessible by Jenkins.

## Running the Pipeline

1. You can clone this repo.
2. Configure Jenkins to use this `Jenkinsfile`. For that you can chose ocean blue. You need to put your github username and PAT for
   password. Then select the cloned repo. Give it a unique name.
3. Run the pipeline and monitor execution.

## Deployment (Future Scope)

The deployment stage is currently a placeholder and can be extended to include Kubernetes deployments, AWS ECS, or other cloud solutions.

---

This README provides a comprehensive overview of the project and pipeline. Let me know if any modifications are needed! 🚀

