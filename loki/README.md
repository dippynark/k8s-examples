# Loki

```sh
helm repo add loki https://grafana.github.io/loki/charts
helm repo update
kubectl get namespace loki || kubectl create namespace loki
kubectl label namespace loki istio-injection=enabled
helm upgrade --install loki loki/loki-stack --namespace loki \
  --set loki.extraArgs."log\.level"=warn
```
