pipeline {
    agent any
    parameters {
        string(name: 'BUILD_NAME', defaultValue: 'Build_Name_1', description: 'Insider website working status test')
    }
    stages {
        stage('build') {
            steps {
                script {
                    currentBuild.displayName = 'Insider web site test'
                    currentBuild.description = 'Insider website working status test'
                }
                sh 'python3 run.py'
            }
        }
    }
}
