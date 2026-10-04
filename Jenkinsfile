pipeline {
    agent any

    environment{
        IMAGE_NAME = 'devops-project'
    }

    stages{
        stage('Install Dependencies') {
            steps{
                bat  " pip install -r requirements.txt "
            }
        }

        stage('Linting') {
            steps{
                bat """ ruff check .
                ruff check . --fix
                """
            }
        }

        stage('Testing Code') {
            steps{
                bat '''
                    pip install -U pytest
                    pytest -v
                    '''
            }
        }

        stage('Build docker image') {
            steps{
                bat 'docker build -t ${IMAGE_NAME}  .'
            }
        }

        stage('Push docker image') {
            steps{
                bat 'docker tag devops-project bee17/devops-project:${BUILD_NUMBER}'
                bat 'docker push bee17/devops-project:${BUILD_NUMBER}'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}