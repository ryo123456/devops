def jenkins_path= "/var/lib/jenkins"
def tf_path = "${jenkins_path}/terraform"
def terraform = "/usr/local/bin/terraform"
 
node {
 
    stage('scm'){
        checkout scm
    }

    stage('terraform'){
        dir("${tf_path}"){
            sh "${terraform} apply -auto-approve"
        }
    }
 
}