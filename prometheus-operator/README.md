# prometheus-operator

```sh
kubectl create clusterrolebinding kube-system:tiller:cluster-admin --clusterrole cluster-admin --serviceaccount=kube-system:tiller
kubectl create serviceaccount tiller -n kube-system
helm init --service-account tiller --override 'spec.template.spec.containers[0].args={/tiller,--listen=localhost:44134}'
helm upgrade --install prometheus-operator --namespace prometheus-operator --values values.yaml stable/prometheus-operator
```
