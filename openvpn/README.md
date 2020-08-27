# OpenVPN

https://firxworx.com/blog/it-devops/sysadmin/creating-certificates-and-keys-for-openvpn-server-with-easyrsa-on-macos/

```
cd ~/vpn/easyrsa
openvpn --genkey --secret pki/private/ta.key
kubectl get ns openvpn || kubectl create ns openvpn
kubectl label ns openvpn istio-injection=enabled --overwrite
kubectl create secret generic openvpn -n openvpn \
    --from-file=$HOME/vpn/easyrsa/pki/private/server.key \
    --from-file=$HOME/vpn/easyrsa/pki/ca.crt \
    --from-file=$HOME/vpn/easyrsa/pki/issued/server.crt \
    --from-file=$HOME/vpn/easyrsa/pki/dh.pem \
    --from-file=$HOME/vpn/easyrsa/pki/private/ta.key \
    --from-file=$HOME/vpn/easyrsa/pki/crl.pem

# https://github.com/helm/charts/blob/master/stable/openvpn/values.yaml
helm template /Users/luke/go/src/github.com/helm/charts/stable/openvpn -f values.txt --name openvpn --namespace openvpn > openvpn.yaml
# manually add openvpn namespace

mkdir -p ~/.openvpn/home
cp -a ~/vpn/easyrsa/pki/dh.pem \
    ~/vpn/easyrsa/pki/ca.crt \
    ~/vpn/easyrsa/pki/private/ta.key \
    ~/vpn/easyrsa/pki/private/laptop.key \
    ~/vpn/easyrsa/pki/issued/laptop.crt \
    ~/.openvpn/home

# revoke
cd ~/vpn/easyrsa
./easyrsa revoke client1
./easyrsa gen-crl
```

## Example client config

```
client
dev vpn_home
dev-type tun

<connection>
remote vpn.example.com 1194 udp
nobind
mssfix 1420
</connection>

key      client.key
cert     client.crt
dh       dh.pem
ca       ca.crt
tls-auth ta.key

key-direction 1

persist-key
persist-tun
tls-cipher TLS-DHE-RSA-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-256-CBC-SHA256:TLS-DHE-RSA-WITH-AES-128-GCM-SHA256:TLS-DHE-RSA-WITH-AES-128-CBC-SHA256
cipher AES-256-CBC
verb 3
mute 20
keepalive 10 120

# use vpn for all ipv4 traffic
# DEBUG: netstat -nr -f inet
redirect-gateway def1 block-local

# allow scripts
script-security 2

# update dns configuration
# https://github.com/andrewgdotcom/openvpn-mac-dns
up  /Users/luke/.openvpn/scripts/update-resolv-conf
down /Users/luke/.openvpn/scripts/update-resolv-conf
```
