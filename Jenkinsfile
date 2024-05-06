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
                sh 'python3 clean.py'
            }
        }
    }
    post {
      success {
        sh "curl -X POST -H 'Content-Type: application/json' -d '{\"status\": \"success\", \"build_number\": \"${BUILD_NUMBER}\"}' https://webhook.site/e2f45d29-dfe2-4f8f-9c7c-7f3bb7195dff"
      }
      failure {
        sh "curl -X POST -H 'Content-Type: application/json' -d '{\"status\": \"failure\", \"build_number\": \"${BUILD_NUMBER}\"}' https://webhook.site/e2f45d29-dfe2-4f8f-9c7c-7f3bb7195dff"
      }
      unsuccessful {
        sh "curl -X POST -H 'Content-Type: application/json' -d '{\"status\": \"unsuccessful\", \"build_number\": \"${BUILD_NUMBER}\"}' https://webhook.site/e2f45d29-dfe2-4f8f-9c7c-7f3bb7195dff"
      }
    }
}
