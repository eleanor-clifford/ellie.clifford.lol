function setCookie(name, value, days) {
	const expires = `; max-age=${days * 86400}`;
	document.cookie = `${name}=${encodeURIComponent(value || '')}${expires}; SameSite=Lax; path=/`;
}

const params = new URLSearchParams(location.search);

if (params.has('joe')) {
	setCookie('joemode', 'on', 365);
} else if (params.has('nojoe')) {
	setCookie('joemode', '', 0); // delete cookie
}

const sheets = document.querySelectorAll('link[rel="stylesheet"]');
const joe = ('; '+document.cookie).split(`; joemode=`).pop().split(';')[0];
if (joe === "on") {
	Array.from(sheets).find(sheet => sheet.href && sheet.href.includes("light.css")).media = '';
	Array.from(sheets).find(sheet => sheet.href && sheet.href.includes("main.css")).media = 'not all';
}
