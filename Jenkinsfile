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
