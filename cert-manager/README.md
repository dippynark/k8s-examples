# cert-manager

```sh
kubectl get namespace cert-manager || kubectl create namespace cert-manager
kubectl label namespace cert-manager istio-injection=enabled
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.0.1/cert-manager.yaml
```
