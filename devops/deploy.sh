#!/bin/bash

# Move to the project root directory (from devops/)
cd "$(dirname "$0")/.." || exit

# Load environment variables from .env file
if [ -f devops/.env ]; then
    set -a  # Automatically export all variables
    source devops/.env
    set +a
else
    echo "⚠️  .env file not found!"
    exit 1
fi

# Git repository information
GIT_URL="https://${GITHUB_PAT}@github.com/saleck24"
repository="chatbot"

clone_repository() {
    ssh -p $SSH_PORT ${SSH_USER}@${DEPLOYMENT_SERVER} "
        mkdir -p ${PROJECT_DIR} &&
        docker network ls --format '{{.Name}}' | grep -wq '^$DOCKER_NETWORK$' || docker network create '$DOCKER_NETWORK'
    "
    ssh -p $SSH_PORT ${SSH_USER}@${DEPLOYMENT_SERVER} "
        cd ${PROJECT_DIR} &&
        [ -d '$repository' ] && zip -r \"\$(date +'%Y-%m-%d_%H-%M-%S')_${repository}.zip\" $repository && rm -rf $repository
    "
    ssh -p $SSH_PORT ${SSH_USER}@${DEPLOYMENT_SERVER} "
        cd ${PROJECT_DIR} && git clone -b ${BRANCH} ${GIT_URL}/${repository}.git
    "
}

copy_devops_and_configs() {
    # Ensure the remote `devops/` directory exists before copying files
    ssh -p $SSH_PORT ${SSH_USER}@${DEPLOYMENT_SERVER} "mkdir -p ${PROJECT_DIR}/$repository/devops"

    # Copy the necessary files
    scp -P $SSH_PORT devops/Dockerfile ${SSH_USER}@${DEPLOYMENT_SERVER}:${PROJECT_DIR}/$repository/devops/Dockerfile
    scp -P $SSH_PORT devops/compose.yml ${SSH_USER}@${DEPLOYMENT_SERVER}:${PROJECT_DIR}/$repository/devops/compose.yml
    scp -P $SSH_PORT devops/.env ${SSH_USER}@${DEPLOYMENT_SERVER}:${PROJECT_DIR}/$repository/devops/.env
}

build_and_run_compose() {
    ssh -p $SSH_PORT ${SSH_USER}@${DEPLOYMENT_SERVER} "
        cd ${PROJECT_DIR}/$repository/devops &&
        docker compose down &&
        docker compose build --no-cache &&
        docker compose up -d
    "
}

# Main execution
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 repository"
    exit 1
fi

repo_name="$1"

echo "🚀 Starting deployment of '$repo_name'..."

clone_repository "$repo_name"
copy_devops_and_configs "$repo_name"
build_and_run_compose "$repo_name"

echo "✅ Deployment of '$repo_name' completed successfully."

