# external-dns

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm fetch bitnami/external-dns --version 3.5.0
tar xvzf external-dns-3.5.0.tgz

kubectl create ns external-dns --dry-run=client -o yaml \
  | kubectl apply -f -
# https://github.com/helm/charts/blob/master/stable/external-dns/values.yaml
helm template external-dns \
  -n external-dns \
  ./external-dns \
  -f values-secret.yaml \
  | tee external-dns-secret.yaml | kubectl apply -n external-dns -f -
```
