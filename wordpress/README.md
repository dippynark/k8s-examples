# Wordpress

```sh
kubectl get namespace wordpress || kubectl create namespace wordpress
#kubectl label namespace wordpress istio-injection=enabled --overwrite
kubectl apply -f pvs.yaml -f pvcs.yaml -f ingress.yaml

helm repo add bitnami https://charts.bitnami.com/bitnami
# Danny
helm upgrade --install danny --namespace wordpress \
  --set wordpressUsername=admin \
  --set wordpressPassword=admin \
  --set mariadb.rootUser.password=mariadb \
  --set mariadb.db.password=mariadb \
  --set persistence.existingClaim=danny-wordpress \
  --set mariadb.master.persistence.existingClaim=danny-mariadb \
  --set service.type=ClusterIP \
  --set resources.requests.memory=128Mi \
  --set resources.requests.cpu=100m \
  --set mariadb.resources.requests.memory=128Mi \
  --set mariadb.resources.requests.cpu=100m \
  --set wordpressScheme=https \
  --version 9.3.10 \
  bitnami/wordpress
```
