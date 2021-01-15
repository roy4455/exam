pipeline {
   
   agent {
        docker {
            image 'python:3'
            args '-u root'
        }
    }
   environment {
        GITHUB_CREDENTIALS = credentials('github_token')
   }
    stages {
        stage('Create tag') {

            steps {
                script {
                    def latest_commit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                    echo "${latest_commit}"
                       sh '''
                        
                        python3 -m venv env
                        pip3 install pygithub
                        python github_tags.py ''' + latest_commit + ''' '''
                       
                    }
                }
            }
        }
    }
    
    


