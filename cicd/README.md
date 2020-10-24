# CI/CD

- Push code
- ArgoCD updates Application object
- Argo Events picks up change
- Revision is parsed and used to run build Workflow
- Final Workflow updates Application to change Helm parameters for new image version
- ArgoCD syncs automatically

## Knative Eventing

```sh
# https://knative.dev/docs/install/any-kubernetes-cluster/#installing-the-eventing-component
kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/eventing-crds.yaml
kubectl apply --filename https://github.com/knative/eventing/releases/download/v0.18.0/eventing-core.yaml
```

## Argo

```sh
kubectl create namespace argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/v2.11.6/manifests/install.yaml
```

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
