pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'zipping files'

      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }   
    }
    stage('deploy') {
      steps {
         sh 'pwd'
         sh 'ls -las'
         sh 'gzip -r ** > flaskapi.gzip'
         //sh 'scp microblog.zip 192.168.56.105:.' 
      } 
    }
  }
}
