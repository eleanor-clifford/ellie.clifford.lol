default:
	make build
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
deploy:
	test -f upload.lock || ./scripts/deploy.sh --all
clean:
	rm -rf out/http/*
	rm -rf out/bliz/*
