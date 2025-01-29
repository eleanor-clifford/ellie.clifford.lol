translate() {
	# black -> white
	sed 's|000000|TMP-WHITE-TMP|' | \
	sed 's|0, 0, 0|TMPR-WHITE-TMPR|'   | \
	# white -> black
	sed 's|ffffff|TMP-BLACK-TMP|' | \
	sed 's|255, 255, 255|TMPR-BLACK-TMPR|' | \
	# bg -> white
	sed 's|40, *42, *54|250, 250, 250|'   | \
	sed 's|282a36|fafafa|i' | \
	# fg -> black
	sed 's|248, *248, *242|56, 58, 66|'   | \
	sed 's|f8f8f2|383a42|i' | \
	# cyan -> cyan
	sed 's|139, *233, *253|1, 132, 188|'   | \
	sed 's|8be9fd|0184bc|i' | \
	# green -> green
	sed 's|80, *250, *123|79, 135, 161|'   | \
	sed 's|50fa7b|4f87a1|i' | \
	# orange -> orange 2
	sed 's|255, *184, *108|203, 119, 1|'   | \
	sed 's|ffb86c|cb7701|i' | \
	# pink -> blue
	sed 's|255, *121, *198|242, 94, 173|'  | \
	sed 's|ff79c6|f25ead|i' | \
	# purple -> purple
	sed 's|189, *147, *249|166, 38, 164|'  | \
	sed 's|bd93f9|a626a4|i' | \
	# red -> red 2
	sed 's|255, *85, *85|202, 18, 67|'     | \
	sed 's|ff5555|ca1243|i' | \
	# yellow -> red 1
	sed 's|241, *250, *140|228, 86, 73|'   | \
	sed 's|f1fa8c|e45649|i' | \
	# darker background
	sed 's|252525|eeeeee|' | \
	# lighter background
	sed 's|44475a|cfd0d1|' | \
	# resolve black and white
	sed 's|TMP-WHITE-TMP|ffffff|' | \
	sed 's|TMP-BLACK-TMP|000000|' | \
	sed 's|TMPR-WHITE-TMPR|255, 255, 255|' | \
	sed 's|TMPR-BLACK-TMPR|0, 0, 0|'
}

<http/static/main.css translate > out/http/light.css

