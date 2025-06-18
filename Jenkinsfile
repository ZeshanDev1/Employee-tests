pipeline {
    agent any

    environment {
        TEST_REPO_URL = 'https://github.com/ZeshanDev1/Employee-tests.git'
        IMAGE_NAME = 'selenium-tests'
        CONTAINER_NAME = 'selenium-test-runner'
    }

    stages {
        stage('Clone Test Repo') {
            steps {
                script {
                    echo '📥 Cloning Selenium test repository...'
                    sh 'rm -rf employee-tests || true'
                    sh 'git clone $TEST_REPO_URL employee-tests'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '🐳 Building Docker image with headless Chrome and test code...'
                    sh '''
                        cd employee-tests
                        docker build -t $IMAGE_NAME .
                    '''
                }
            }
        }

        stage('Run Tests in Container') {
            steps {
                script {
                    echo '🧪 Running Selenium tests in Docker container...'
                    sh '''
                        docker run --rm --name $CONTAINER_NAME $IMAGE_NAME
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Tests passed. Optionally send success email.'
        }
        failure {
            echo '❌ Tests failed. Optionally send failure email.'
            // Add this block if you have email configured:
            // mail to: 'you@example.com',
            //      subject: "❌ Selenium Test Pipeline Failed",
            //      body: "Please check Jenkins console output for details."
        }
        always {
            echo '📌 Test pipeline completed.'
        }
    }
}
