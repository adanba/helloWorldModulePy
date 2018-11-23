pipeline {

  agent {
    label 'prod'
  }

  stages {
     stage('Build') { 
            agent {
                label 'prod'
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
