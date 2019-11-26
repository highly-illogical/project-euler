
var p=1, i=1;

function lcm(a,b) {
	var m = Math.max(a,b), n = Math.min(a,b);
	while (m%n) {
		var k = n;
		n = m%n;
		m = k;
	}
	return a*b/n;
}

while (i<=20) {
	p = lcm(p,i);
	i++;
}

alert(p);

