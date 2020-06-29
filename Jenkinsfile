def workspace;
node
{

    stage ('SCM checkout')
    {
    
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '96f0d0b2-ee5f-4975-b6f7-c9d36738ce45', url: 'https://github.com/roy4455/exam']]])
        workspace = pwd()
        
    }
    
    stage ('Build')
    {
        echo "This is Build"
        
    }
    
    stage ('Deploy')
    
    {
        echo "This is Deployment stage"
    }
    
    
    

}
