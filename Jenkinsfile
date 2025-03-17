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
                    if [ -f "${WORKSPACE}/requirements.txt" ]; then
                        docker run --rm -v "${WORKSPACE}:/workspace" ${PYTHON_IMAGE} \
                        sh -c "pip install --upgrade pip && pip install -r /workspace/requirements.txt"
                    else
                        echo "No requirements.txt found, skipping dependencies installation."
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm -v "${WORKSPACE}:/workspace" ${PYTHON_IMAGE} \
                    python /workspace/calculate_due_date.py
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                    docker run --rm -v "${WORKSPACE}:/workspace" ${PYTHON_IMAGE} \
                    sh -c "pip install flake8 && flake8 /workspace --count --select=E9,F63,F7,F82 --show-source --statistics"
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
