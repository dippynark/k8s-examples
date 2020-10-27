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

generate:
	$(ISTIOCTL) manifest generate -f operator.yaml > charts/istio/templates/istioctl.yaml
	sed -i '' -e 's/{{/~~/g; s/}}/{{ "}}" }}/g; s/~~/{{ "{{" }}/g' charts/istio/templates/istioctl.yaml
	rm -Rf manifests
	jx gitops helmfile template \
		--args="--include-crds" \
		--output-dir manifests
