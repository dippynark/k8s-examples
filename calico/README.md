# Calico

```sh
curl -O https://docs.projectcalico.org/archive/v3.15/manifests/calico.yaml
# Replace /usr/libexec/kubernetes/kubelet-plugins/volume/exec/nodeagent~uds
# with /var/lib/kubelet/volume-plugins/nodeagent~uds to match controller-manager
kubectl apply -f calico.yaml
```
