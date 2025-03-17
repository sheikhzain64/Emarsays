pipeline {
    agent any

    environment {
        PYTHON_IMAGE = 'python:3.9'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sheikhzain64/Emarsays'
                sh 'ls -lah'  // Debugging step to verify files
            }
        }
        
        stage('Debug Workspace') {
            steps {
                sh 'ls -lah'  // Extra check to confirm files exist
            }
        }

        stage('Setup Python') {
            steps {
                sh 'docker pull ${PYTHON_IMAGE}'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    docker run --rm -v "$PWD":/app -w /app ${PYTHON_IMAGE} \
                    sh -c "pip install --upgrade pip && pip install -r requirements.txt || echo 'No requirements.txt found, skipping.'"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm -v "$PWD":/app -w /app ${PYTHON_IMAGE} python calculate_due_date.py
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                    docker run --rm -v "$PWD":/app -w /app ${PYTHON_IMAGE} \
                    sh -c "pip install flake8 && flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || echo 'Linting issues found.'"
                '''
            }
        }

        stage('Deploy (Placeholder)') {
            steps {
                echo 'Deployment step (to be implemented)'
            }
        }
    }
}
