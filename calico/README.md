# Calico

```sh
curl https://docs.projectcalico.org/archive/v3.14/manifests/calico.yaml -O
# Replace /usr/libexec/kubernetes/kubelet-plugins/volume/exec/nodeagent~uds
# with /var/lib/kubelet/volume-plugins/nodeagent~uds to match controller-manager
kubectl apply -f calico.yaml
```
