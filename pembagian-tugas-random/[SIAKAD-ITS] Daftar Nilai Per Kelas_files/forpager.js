/* fungsi umum */

var isMenuOpened = false;

function goSubmit() {
	document.getElementById("sipform").submit();
}

function goNew() {
	document.getElementById("sipform").action = filedetail+'add';
	document.getElementById("key").value = '';
	goSubmit();
}

function goDetail(key) {
	document.getElementById("sipform").action = filedetail+key;
	document.getElementById("key").value = key;
	goSubmit();
}

/* fungsi untuk paging */

function initButton(isfirst,islast) {
	if(isfirst) {
		document.getElementById("firstButton").disabled = 1;
		document.getElementById("prevButton").disabled = 1;
		document.getElementById("firstButton").src = "images/first2.gif";
		document.getElementById("prevButton").src = "images/prev2.gif";
		document.getElementById("firstButton").style.cursor = null;
		document.getElementById("prevButton").style.cursor = null;
	} else {
		document.getElementById("firstButton").disabled = 0;
		document.getElementById("prevButton").disabled = 0;
		document.getElementById("firstButton").src = "images/first.gif";
		document.getElementById("prevButton").src = "images/prev.gif";
	} if (islast) {
		document.getElementById("nextButton").disabled = 1;
		document.getElementById("lastButton").disabled = 1;
		document.getElementById("nextButton").src = "images/next2.gif";
		document.getElementById("lastButton").src = "images/last2.gif";
		document.getElementById("nextButton").style.cursor = null;
		document.getElementById("lastButton").style.cursor = null;
	} else {
		document.getElementById("nextButton").disabled = 0;
		document.getElementById("lastButton").disabled = 0;
		document.getElementById("nextButton").src = "images/next.gif";
		document.getElementById("lastButton").src = "images/last.gif";
	}
}

function goFirst(curr) {
	//alert('forpager');
	if(curr > 1 && !document.getElementById("firstButton").disabled) {
		document.getElementById("page").value = 1;
		goSubmit();
	}
}

function goPrev(curr) {
	if(curr > 1 && !document.getElementById("prevButton").disabled) {
		document.getElementById("page").value = (curr - 1);
		goSubmit();
	}
}

function goNext(curr,last) {
	//alert('curr' + curr);
	//alert('last' + last);
	//alert(document.getElementById("nextButton").disabled);
	if(curr < last && !document.getElementById("nextButton").disabled) {
		document.getElementById("page").value = (curr + 1);
		goSubmit();
	}
}

function goLast(curr,last) {
	if(curr < last && !document.getElementById("lastButton").disabled) {
		document.getElementById("page").value = last;
		goSubmit();
	}
}

function goPage(pageno) {
	document.getElementById("page").value = pageno;
	goSubmit();
}

function goRefresh() {
	document.getElementById("page").value = 1;
	document.getElementById("sort").value = "";
	document.getElementById("filter").value = "";
	goSubmit();
}

/* fungsi ex (filter dan sorting berdasarkan header) */

function goSort(direction) {
	if (gParam) {
		arrParam = gParam.split(":");
		document.getElementById("sort").value = arrParam[0] + ' ' + direction;	
		goSubmit();
	}
}

function goFilter(filterOn) {
	if (!filterOn) {
		// reset filter
		document.getElementById("page").value = 1;
		document.getElementById("sort").value = "";
		document.getElementById("filter").value = "";
		goSubmit();
	}
	else 
	{
		if (document.getElementById("popPaging")) { // tampilkan teksboks filter
			if (ns6) 
			{
				document.getElementById("popFilter").style.left = document.getElementById("popPaging").style.left;
				document.getElementById("popFilter").style.top = document.getElementById("popPaging").style.top;
			} 
			else
			{
				document.getElementById("popFilter").style.left = document.getElementById("popPaging").style.pixelLeft;
				document.getElementById("popFilter").style.top = document.getElementById("popPaging").style.pixelTop;
			}
			
			document.getElementById("popFilter").style.display = "inline";
			document.getElementById("popPaging").style.display = "none" ;
			document.getElementById("txtFilter").value = "";
			document.getElementById("txtFilter").focus();
		}
	}
}

function doFilter(e) {
	var ev = (window.event) ? window.event: e;
	var key = (ev.keyCode) ? ev.keyCode : ev.which;
	
	if (key==13 && gParam) // jika ditekan tombol enter
	{
		// processing filter
		arrParam = gParam.split(":");
		var columnFilter = arrParam[0];
		var columnType = arrParam[1];
		var retval;
		retval = document.getElementById("txtFilter").value;
		if (retval)
		{
			if (document.getElementById("filter").value)  // tambah kriteria filter
				document.getElementById("filter").value = document.getElementById("filter").value + ':';
			document.getElementById("filter").value = document.getElementById("filter").value + columnFilter  + ':' + retval + ':' + columnType;
			document.getElementById("page").value = 1;	
			goSubmit();
		}
	} 
	else if (key==27) // jika ditekan tombol escape
		document.getElementById("popFilter").style.display = "none";
}

/* fungsi popup menu */

// Popup Menu SECTION START  ---------------------------------

// mouse position

function checkS(e){ 
// capture the mouse position must be called at body onload
    if (!e) var e = window.event; 
    if (e.pageX || e.pageY) 
    { 
		mouseX = e.pageX-10;
		mouseY =  e.pageY;
    } 
    else if (e.clientX || e.clientY) 
    { 
        mouseX =  event.clientX-10+document.body.scrollLeft;
        mouseY = event.clientY+document.body.scrollTop;
    } 
} 

function getLikeElements(tagName, attrName, attrValue) {
    var startSet;
    var endSet = new Array( );
    if (tagName) {
        startSet = document.getElementsByTagName(tagName);    
    } else {
        startSet = (document.all) ? document.all : 
            document.getElementsByTagName("*");
    }
    if (attrName) {
        for (var i = 0; i < startSet.length; i++) {
            if (startSet[i].getAttribute(attrName)) {
                if (attrValue) {
                    if (startSet[i].getAttribute(attrName).substring(0,attrValue.length) == attrValue) {
                        endSet[endSet.length] = startSet[i];
                    }
                } else {
                    endSet[endSet.length] = startSet[i];
                }
            }
        }
    } else {
        endSet = startSet;
    }
    return endSet;
}

function ClosePopup(e)
{
	if( isMenuOpened )
	{
    	if( overpopupmenu == false )
    	{
			isMenuOpened = false ;
			overpopupmenu = false;
			var arrDiv = getLikeElements("div","id","pop");
			for (i=0;i<arrDiv.length;i++) { // close all popup windows
				if(arrDiv[i].id == 'popFilter') continue; // skip popFilter :D
				arrDiv[i].style.display = "none";
			}
			return true ;
    	}
    	return true ;
  	}
  	return false;
}

function PopupMenu(pMenu,pParam)
{
	var popUp = document.getElementById(pMenu);
	gParam = pParam;
	if (ns6)
	{
		popUp.style.left = mouseX;
		popUp.style.top = mouseY;
	} else {
		popUp.style.pixelLeft = mouseX;
		popUp.style.pixelTop = mouseY;
	}
	popUp.style.display = "";
	isMenuOpened = true;
	return false ;
}

if(window.addEventListener){ // Mozilla, Netscape, Firefox
	document.addEventListener('mousedown', ClosePopup, false);
} else { // IE
	document.attachEvent('onmousedown', ClosePopup);
}
