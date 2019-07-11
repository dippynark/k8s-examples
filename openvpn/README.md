# OpenVPN

https://firxworx.com/blog/it-devops/sysadmin/creating-certificates-and-keys-for-openvpn-server-with-easyrsa-on-macos/

```
cd ~/vpn/easyrsa
openvpn --genkey --secret pki/private/ta.key
kubectl create ns openvpn
kubectl create secret generic openvpn -n openvpn --from-file=~/vpn/easyrsa/pki/private/server.key \
    --from-file=~/vpn/easyrsa/pki/ca.crt \
    --from-file=~/vpn/easyrsa/pki/issued/server.crt \
    --from-file=~/vpn/easyrsa/pki/dh.pem \
    --from-file=~/vpn/easyrsa/pki/private/ta.key
    [--from-file=./crl.pem]

# https://github.com/helm/charts/blob/master/stable/openvpn/values.yaml
helm template /Users/luke/go/src/github.com/helm/charts/stable/openvpn -f values.yaml --name openvpn --namespace openvpn > openvpn.yaml

mkdir -p ~/.openvpn/home
cp -a ~/vpn/easyrsa/pki/dh.pem \
    ~/vpn/easyrsa/pki/ca.crt \
    ~/vpn/easyrsa/pki/private/ta.key \
    ~/vpn/easyrsa/pki/private/laptop.key \
    ~/vpn/easyrsa/pki/issued/laptop.crt \
    ~/.openvpn/home
```
