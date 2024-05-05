pipeline {
    agent any
    stages {
        stage('version') {
            sh 'python3 --version'
        }
        stage('startTest') {
            sh 'python3 run.py'
        }
    }
}