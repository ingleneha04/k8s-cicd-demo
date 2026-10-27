
param(
    [string]$ImageTag = "latest"
)

$ErrorActionPreference = "Stop"

$image = "ingleneha123/k8s-cicd-demo:$ImageTag"
$deployment = "k8s-cicd-demo"

Write-Host "Checking Minikube..."
minikube status --profile=devops
if ($LASTEXITCODE -ne 0) {
    throw "Minikube is not running."
}

Write-Host "Checking Kubernetes..."
kubectl get nodes
if ($LASTEXITCODE -ne 0) {
    throw "Cannot connect to Kubernetes."
}

Write-Host "Updating deployment image to $image..."
kubectl set image "deployment/$deployment" "k8s-cicd-demo=$image"
if ($LASTEXITCODE -ne 0) {
    throw "Failed to update image."
}

Write-Host "Waiting for rollout..."
kubectl rollout status "deployment/$deployment" --timeout=180s
if ($LASTEXITCODE -ne 0) {
    throw "Deployment failed."
}

Write-Host "Current pods:"
kubectl get pods

Write-Host "Deployed image:"
kubectl get deployment $deployment -o jsonpath="{.spec.template.spec.containers[0].image}"
Write-Host ""

Write-Host "Deployment completed successfully."
