export ISTIO_VERSION = 1.6.0
export ARCH = osx
export ISTIOCTL := $(CURDIR)/istio-$(ISTIO_VERSION)-$(ARCH)/bin/istioctl

init:
	ls istio-$(ISTIO_VERSION)-$(ARCH).tar.gz || curl -LO https://github.com/istio/istio/releases/download/$(ISTIO_VERSION)/istio-$(ISTIO_VERSION)-$(ARCH).tar.gz
	ls istio-$(ISTIO_VERSION)-$(ARCH) || (mkdir istio-$(ISTIO_VERSION)-$(ARCH) && tar xzf istio-$(ISTIO_VERSION)-$(ARCH).tar.gz -C istio-$(ISTIO_VERSION)-$(ARCH) --strip-components 1)

install: init
	$(ISTIOCTL) manifest apply -f operator.yaml
	kubectl apply -f kiali-secret.yaml -f kiali-config.yaml -f kiali-ingress.yaml
	kubectl delete pods -n istio-system -l app=kiali
