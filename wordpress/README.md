# Wordpress

```sh
kubectl get namespace wordpress || kubectl create namespace wordpress
#kubectl label namespace wordpress istio-injection=enabled --overwrite
kubectl apply -f pvs.yaml -f pvcs.yaml

helm repo add bitnami https://charts.bitnami.com/bitnami
helm upgrade --install wordpress --namespace wordpress \
  --set wordpressUsername=admin \
  --set wordpressPassword=admin \
  --set persistence.existingClaim=wordpress \
  --set mariadb.master.persistence.existingClaim=mariadb \
  bitnami/wordpress
```
