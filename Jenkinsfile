pipeline {

  agent {
    label 'prod'
  }

  stages {
     stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh "pip install -e ."
            }
        }
  }
}
