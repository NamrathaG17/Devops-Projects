pipeline {
    agent any

    environment{
        IMAGE_NAME = 'devops-project'
        DOCKER_UNAME = 'bee17'
        TAG_VERSION = 'V3'
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
            cleanWs()
            deleteDir()
            bat 'docker logout'
            echo 'Cleaning up resources...'
        }
        success {
            echo 'Pipeline completed successfully!'
            mail to: 'transformer1assemble@gmail.com',
                    subject: "Jenkins build successfulNotification: ${currentBuild.fullDisplayName}",
                    body: """
                    The build finished with status: ${currentBuild.currentResult}
                    Project: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    URL: ${env.BUILD_URL}
                    """,
                    from: 'jenkins-admin@gmail.com',
                    mimeType: 'text/html'
            
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}