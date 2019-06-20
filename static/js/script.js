function modal() {
	document.getElementById('modal').classList.add('active');
	setTimeout(function() {
		document.getElementById('modal').classList.add('opacity');
	}, 500);
}

function cerrarModal() {
	document.getElementById('modal').classList.remove('opacity');
	setTimeout(function() {
		document.getElementById('modal').classList.remove('active');
	}, 500);
}