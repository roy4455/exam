pipeline {
   agent any
    stages {
        stage('Create tag') {

            steps {
                script {
                    def latest_commit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                    echo "${latest_commit}"
                    withCredentials([string(credentialsId: 'github-token', variable: 'TOKEN')]) {
                        sh ''' python github_tags.py $TOKEN ''' + latest_commit + ''' '''
                    }
                }
            }
        }
    }
}
    


