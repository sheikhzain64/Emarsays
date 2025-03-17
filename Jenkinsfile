pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/sheikhzain64/Emarsays'
                sh 'ls -lah'  // Debugging step to verify files
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    if [ -f "requirements.txt" ]; then
                        pip install --upgrade pip && pip install -r requirements.txt
                    else
                        echo "No requirements.txt found, skipping dependencies installation."
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python calculate_due_date.py'
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                    pip install flake8
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
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
