# OAuth 2

- luke@lukeaddison.co.uk [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)
- https://console.developers.google.com/apis/credentials/oauthclient/189522423084-6opace55ro8aeqqgjsajsm24p6qlis6e.apps.googleusercontent.com?authuser=1&folder=&organizationId=&project=general-253420

```sh
kubectl get namespace oauth2-proxy || kubectl create namespace oauth2-proxy
kubectl label namespace oauth2-proxy istio-injection=enabled --overwrite
helm upgrade --install oauth2-proxy -n oauth2-proxy .
```
