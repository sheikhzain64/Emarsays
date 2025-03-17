pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sheikhzain64/Emarsays'
                sh 'ls -lah'  // Debugging step to verify files
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv  # Create a virtual environment
                    source venv/bin/activate  # Activate it
                    python3 -m pip install --upgrade pip  # Upgrade pip inside venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    if [ -f "requirements.txt" ]; then
                        python3 -m pip install -r requirements.txt
                    else
                        echo "No requirements.txt found, skipping dependencies installation."
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 calculate_due_date.py
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                    source venv/bin/activate
                    python3 -m pip install flake8
                    python3 -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
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
