pipeline {
    agent any

    environment {
        IMAGE_NAME = "jerald04/CiCd"
        IMAGE_TAG = "latest"
    }

    stages {
	stage('Fix Docker Socket Permission') {
            steps {
                sh 'sudo chmod 666 /var/run/docker.sock'
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/jerald-04/CiCd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ./app"
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push $IMAGE_NAME:$IMAGE_TAG"
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "docker run -d -p 5000:5000 --name CiCd $IMAGE_NAME:$IMAGE_TAG || true"
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished!'
        }
    }
}

