properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'jenkins_host'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
    }
    environment {
        TELEGRAMBOT_IP="37.140.198.248"
        TELEGRAMBOT_PORT=8081
        WEBSITE_PORT_HTTPS=443
        WEBSITE_PORT_HTTP=80
    }
    stages {
        stage('git clone') {
            steps {
                git branch: "master", url: 'git@github.com:Asidrus/project_website.git', credentialsId: 'Github_ssh'
            }
        }
        stage('docker-compose up'){
            steps {
                withCredentials([string(credentialsId: 'SECRET_KEY', variable: 'SECRET_KEY')]) {
                    sh """
                    echo SECRET_KEY=$SECRET_KEY > .env
                    echo TELEGRAMBOT_IP=$TELEGRAMBOT_IP >> .env
                    echo TELEGRAMBOT_PORT=$TELEGRAMBOT_PORT >> .env
                    """
                }
                sh "sudo chmod -R 777 data"
                sh "docker-compose up -d --build"
            }
        }
        stage('migrate'){
            steps{
                sh "docker exec website_web_1 python manage.py migrate"
            }
        }
    }
}