# prometheus-operator

```sh
# TODO: upgrade to Helm 3
kubectl create clusterrolebinding kube-system:tiller:cluster-admin --clusterrole cluster-admin --serviceaccount=kube-system:tiller
kubectl create serviceaccount tiller -n kube-system
helm init --service-account tiller --override 'spec.template.spec.containers[0].args={/tiller,--listen=localhost:44134}'
kubectl get namespace prometheus-operator || kubectl create namespace prometheus-operator
kubectl label namespace prometheus-operator istio-injection=enabled --overwrite
helm upgrade --install prometheus-operator --namespace prometheus-operator --values values.txt stable/prometheus-operator
```
