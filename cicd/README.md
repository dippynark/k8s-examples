# CI/CD

- Push code
- ArgoCD watching GitHub applies config containing hash
- Knative Eventing watches configmap
- Sends event to endpoint to run Workflow to build code
- Final Workflow step applies Application to change Helm parameters for new image version plus hash of repo commit
- ArgoCD syncs automatically

## Argo CD

```sh
kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v1.7.8/manifests/install.yaml
kubectl port-forward -n argocd svc/argocd-server 8080:80
# admin
# argocd-server-5bc896856-28nvx
```

## GoCD

```sh
helm repo add gocd https://gocd.github.io/helm-chart
#helm search repo gocd/gocd
kubectl create ns gocd
helm upgrade --install gocd \
  --namespace gocd gocd/gocd \
  --version 1.31.0 \
  -f values.yaml
helm status gocd -n gocd
```
