pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                script {
                    currentBuild.displayName = 'Insider web site test'
                    currentBuild.description = 'Insider website working status test'
                }
                sh 'python --version'
            }
        }
    }
}
