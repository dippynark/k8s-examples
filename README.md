# k8s-examples

This repository contains a set of configuration examples for various systems and
applications on Kubernetes.

## Examples

```sh
# generate basic auth username/password
htpasswd -c auth dippynark
kubectl create secret generic basic-auth --from-file=auth -n $NAMEPSACE

# search lidarr for unmapped content
curl -H "X-Api-Key: $API_KEY" http://lidarr.lidarr.svc.cluster.local/api/v1/trackfile?unmapped=true | jq '.[].path' # | xargs -I {} rm -f {}
# search lidarr for incomplete albums
curl -H "X-Api-Key: $API_KEY" http://lidarr.lidarr.svc.cluster.local/api/v1/album | jq '.[] | select(.statistics.percentOfTracks != 100 and .statistics.percentOfTracks != 0 and .statistics.percentOfTracks != null) | .artist.path + "/" + .title'
```
