# prometheus-operator

```sh
go get -d github.com/prometheus-community/helm-charts
cd github.com/prometheus-community/helm-charts/charts/kube-prometheus-stack/crds
kubectl apply -f .

kubectl create namespace kube-prometheus-stack --dry-run=client -o yaml | kubectl apply -f -
#kubectl label namespace kube-prometheus-stack istio-injection=enabled --overwrite
helm upgrade --install kube-prometheus-stack --namespace kube-prometheus-stack --values values.yaml prometheus-community/kube-prometheus-stack
```
