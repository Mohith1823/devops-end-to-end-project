pipeline {
    agent any

    environment {
        IMAGE_NAME = "dockermohith/flask-devops-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
                sh 'git --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                    docker logout
                    '''
                }
            }
        }
stage('Remove Old Container') {
    steps {
        sh '''
        docker stop flask-devops-app || true
        docker rm flask-devops-app || true
        '''
    }
}
stage('Deploy Container') {
    steps {
        sh '''
        docker run -d \
        --name flask-devops-app \
        -p 5000:5000 \
        dockermohith/flask-devops-app:${BUILD_NUMBER}
        '''
    }
}
stage('Verify Deployment') {
    steps {
        sh 'docker ps'
    }
} 
   }
}
