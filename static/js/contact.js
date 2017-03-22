
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

$(document).ready(function(){
	$('#contactForm').bootstrapValidator({
		fields: {
			firstName: {
				validators:{
					notEmpty: {
						message: 'Hi, my name is Naomi! And you are...?'
					}
				}
			},
			lastName: {
				validators: {
					notEmpty: {
						message: "You might as well give me your entire name while you are here"
					}
				}
			},
			email: {
				validators: {
					notEmpty: {
						message: "Your email is required so I can respond. It will remain private and never be sold!"
					},
					emailAddress: {
						message: "Ummm, I don't think that email is valid, so lets try again"
					}
				}
			},
			subject: {
				validators: {
					notEmpty: {
						message: "A email without a subject is like a present without a bow"
					}
				}
			},
			comments: {
				validators: {
					notEmpty: {
						message: "Tell me something so I can tell you something in return"
					}
				}
			}
		}
	});
});

