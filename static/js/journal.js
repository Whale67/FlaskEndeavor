// On Click Page Animations

$(document).ready(function(){
//	$("body").css("display", "none");

//	$("body").fadeIn(2000);

	$("a.transition").click(function(event){
		event.preventDefault();
		linkLocation = this.href;
		$("body").fadeOut(1000, redirectPage);
	});
  
    function redirectPage() {
		window.location.href = linkLocation;
	}
	
});

//Scroll to top
	if (document.body.scrollTop!=0 || document.documentElement.scrollTop!=0)
{

}
window.scrollBy(0,-50);
var timeOut;
    function scrollToTop() {
        if (document.body.scrollTop!=0 || document.documentElement.scrollTop!=0){
            window.scrollBy(0,-50);
            timeOut=setTimeout('scrollToTop()',10);
        }
        else clearTimeout(timeOut);
    }


//Delay going to website pages by 1 sec
function delayURL(URL) {
	setTimeout(function(){
		window.location.href = URL
	}, 1000);
}

