pipeline {

  agent {
    label 'prod'
  }

  stages {
     stage('Build') { 
            steps {
                sh "pip install -e ."
            }
        }
  }
}
