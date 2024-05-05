pipeline {
    agent any
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