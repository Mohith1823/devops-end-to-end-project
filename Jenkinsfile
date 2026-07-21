pipeline {
    agent any

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
                sh 'docker build -t flask-devops-app:v1 .'
            }
        }

    }
}
