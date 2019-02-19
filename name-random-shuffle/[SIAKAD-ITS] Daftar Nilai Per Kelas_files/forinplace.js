/* fungsi umum */

function goSubmit() {
	document.getElementById("sipform").submit();
}

function initScroll(scrolln) {
	document.body.scrollTop = scrolln;
}

/* fungsi aksi */

function goDeleteIP(key,label) {
	var hapus;
	if(label)
		hapus = confirm('Apakah anda yakin akan menghapus data "' + label + '"?');
	else
		hapus = confirm('Apakah anda yakin akan menghapus data ini?');
		
	if(hapus) {
		document.getElementById("key").value = key;
		document.getElementById("act").value = "hapus";
		goSubmit();
	}
}

function goEditIP(key) {
	document.getElementById("key").value = key;
	document.getElementById("act").value = "sunting";
	goSubmit();
}

function goInsertIP() {
	document.getElementById("act").value = "insersi";
	goSubmit();
}

function goUpdateIP(key) {
	document.getElementById("key").value = key;
	document.getElementById("act").value = "update";
	goSubmit();
}

/* validasi input */

function cfAlert(id,alertmsg,stat) {
	if(!stat)
		return false;
	if(document.getElementById(id) != null && document.getElementById(id).value == "") {
		alert(alertmsg);
		document.getElementById(id).focus();
		return false;
	}
	return true;
}

function cfHighlight(csv) {
	var i, err = false;
	var aid = csv.split(",");
	
	if(aid.length > 1) {
		for(i=0;i<aid.length;i++) {
			e = document.getElementById(aid[i]);
			if(e != null && e.value == "") {
				e.className = "ControlErr";
				e.onfocus = function () { if(this.readOnly) this.className = "ControlStyleRO"; else this.className = "ControlStyle"; }
				err = true;
			}
		}
	}
	else {
		e = document.getElementById(aid);
		if(e != null && e.value == "") {
			e.className = "ControlErr";
			e.onfocus = function () { if(this.readOnly) this.className = "ControlStyleRO"; else this.className = "ControlStyle"; }
			err = true;
		}
	}
	
	if(err) {
		alert("Mohon mengisi isian-isian yang berwana kuning terlebih dahulu.");
		return false;
	}
	return true;
}

function onlyNumber(e,elem,dec) {
	var code = e.keyCode || e.which;
	if ((code > 57 && code < 96) || code > 105 || code == 32) {
		if(code == 190 && dec) {
			if(elem.value == "") // belum ada isinya, titik tidak boleh didepan
				return false;
			if(elem.value.indexOf(".") > -1) // udah ada titik, tidak boleh ada lagi
				return false;
			return true;
		}
		return false;
	}
}