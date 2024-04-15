find . -type f | grep -vP '^\./(\.git|out).*' | xargs grep -Pil "$1" | xargs -n1 file --mime | grep -v charset=binary | cut -d':' -f1
