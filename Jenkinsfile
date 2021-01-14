pipeline {
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    agent {
        docker {
            image 'python:3'
            args '-u root'
        }
    }
    stages {
        stage('Create tag') {
            steps {
                script {
                    def latest_commit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                    
                    withCredentials([string(credentialsId: 'github-token', variable: 'TOKEN')]) {
                        sh ''' python github_tags.py $TOKEN ''' + latest_commit + ''' '''
                    }
                }
            }
        }
    }
}
    
    


