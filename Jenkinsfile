pipeline {
    agent any
    environment {
        // UBAH DENGAN USERNAME DOCKER HUB KAMU!
        IMAGE_NAME = 'USERNAME_DOCKERHUB_KAMU/simple-app'
        REGISTRY = 'https://index.docker.io/v1/'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Melakukan checkout dari SCM...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Mulai build aplikasi'
                bat 'echo Build selesai'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Membangun Docker image...'
                    docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    echo 'Push image ke Docker Hub...'
                    docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }
        stage('Deploy & Run Container') {
            steps {
                script {
                    echo 'Menjalankan container...'
                    bat 'docker stop app-container 2>NUL || exit 0'
                    bat 'docker rm app-container 2>NUL || exit 0'
                    bat "docker run -d -p 5001:5001 --name app-container ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                }
            }
        }
    }
    post {
        always {
            echo 'Selesai build'
        }
    }
}