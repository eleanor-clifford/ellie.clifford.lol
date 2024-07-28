default:
	make test
clean:
	rm -rf out/http/*
	rm -rf out/bliz/*
build:
	./scripts/build.sh --all
deploy:
	test -f upload.lock || ./scripts/deploy.sh --all
all:
	make clean && make build && make deploy

check:
	./scripts/check.sh

gemini:
	rm out/bliz/* -rf
	./scripts/build.sh --bliz && \
	test -f upload.lock || ./scripts/deploy.sh --bliz
https:
	#rm out/http/* -rf
	./scripts/build.sh --http && \
	test -f upload.lock || ./scripts/deploy.sh --http

test:
	./scripts/build.sh --test

test_remote:
	./scripts/build.sh --test
	./scripts/deploy.sh --test

blog_alts:
	./scripts/build.sh --blog
