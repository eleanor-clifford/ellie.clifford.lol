default:
	make test
all:
	make clean && make build && make deploy
blog_alts:
	./scripts/build.sh --blog
gemini:
	rm out/bliz/* -rf
	./scripts/build.sh --bliz && \
	test -f upload.lock || ./scripts/deploy.sh --bliz
https:
	rm out/http/* -rf
	./scripts/build.sh --http && \
	test -f upload.lock || ./scripts/deploy.sh --http
build:
	./scripts/build.sh --all
test:
	./scripts/build.sh --http && \
	test -f upload.lock || ./scripts/deploy.sh --test
deploy:
	test -f upload.lock || ./scripts/deploy.sh --all
check:
	./scripts/check.sh
clean:
	rm -rf out/http/*
	rm -rf out/bliz/*
