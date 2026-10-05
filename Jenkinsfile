pipeline {
    agent any

    environment{
        IMAGE_NAME = 'devops-project'
        DOCKER_UNAME = 'bee17'
        TAG_VERSION = 'V2'
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
                echo "This is the env variable 1: ${IMAGE_NAME} "
                echo "This is the env variable 2: ${TAG_VERSION} "
                bat "docker build -t ${IMAGE_NAME}  ."
            }
        }

        stage('Push docker image') {
            steps{
                    withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'dockerPwd', usernameVariable: 'dockerUname')]) {
                    bat "docker login -u ${dockerUname} -p ${dockerPwd}"
                    echo "login to ${dockerUname} is successfull using ${dockerPwd}"
                    bat "docker tag ${IMAGE_NAME} ${DOCKER_UNAME}/devops-project:${TAG_VERSION}"
                    bat "docker push ${DOCKER_UNAME}/${IMAGE_NAME}:${TAG_VERSION}"
                }
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