pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/demoBlaze'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv demoblazeVENV'
                bat 'demoblazeVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'demoblazeVENV\\Scripts\\activate && pytest -v --html=report.html'
            }
        }
    }
}