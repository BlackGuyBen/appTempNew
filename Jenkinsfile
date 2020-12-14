//pipeline
pipeline {
  agent { dockerfile { filename 'Dockerfile'
                      dir '/home/jdservice/flaskapi'
                     }
        }
  stages {
   stage('build') {
    steps {
      sh 'pip3 install --no-cache-dir -r requirements.txt' 
   }
  }
  stage('test') {
   steps {
     sh 'python3 test.py'
    } 
   }
  }
}
