pipeline {

  agent {
    label 'prod'
  }

  stages {
     stage('Build') { 
            steps {
                sh "pip install --install-dir  /home/danba_abdelhadi/install-dir/  -e ."
            }
        }
  }
}
