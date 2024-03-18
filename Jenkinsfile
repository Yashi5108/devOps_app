pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-docker-image-name'
    }

    stages {
        stage('Build') {
            steps {
                // Clone the repository
                git 'https://github.com/your-username/your-repo.git'

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
                    docker.withRegistry('https://your.registry.url', 'credentials-id-for-registry') {
                        docker.image(env.DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                // Deploy to Kubernetes
                script {
                    kubernetesDeploy(
                        kubeconfigId: 'your-kubeconfig-credentials-id',
                        configs: 'your-k8s-deployment-file.yml',
                        enableConfigSubstitution: true
                    )
                }
            }
        }
    }
}
