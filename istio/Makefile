export ISTIO_VERSION = 1.7.3
export ISTIOCTL := $(CURDIR)/istio-$(ISTIO_VERSION)/bin/istioctl

init:
	curl -L https://istio.io/downloadIstio | sh -

install:
	$(ISTIOCTL) manifest install -f operator.yaml
	kubectl apply \
		-f certificates.yaml \
		-f gateway.yaml \
		-f ingressgateway-service.yaml
