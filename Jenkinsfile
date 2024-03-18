pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yashigupta5108/my-flask-app'
    }

    stages {
        stage('Build') {
            steps {
                // Clone the repository
                git 'https://github.com/Yashi5108/devOps_app.git'

                // Build Docker image
                script {
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }
        stage('Push to Registry') {
            steps {
                // Push Docker image to registry
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image(env.DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                // Deploy to Minikube using Kubeconfig
                script {
                    kubernetesDeploy(
                        kubeconfigId: 'minikube-kubeconfig',
                        configs: 'deployment.yaml',
                        enableConfigSubstitution: true
                    )
                }
            }
        }
    }
}
