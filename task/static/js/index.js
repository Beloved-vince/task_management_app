$(window).on("hashchange", function () {
	if (location.hash.slice(1) == "signup") {
		$(".page").addClass("extend");
		$("#login").removeClass("active");
		$("signup.html").addClass("active");
	} else {
		$(".page").removeClass("extend");
		$("#login").addClass("active");
		$("signup.html").removeClass("active");
	}
});
$(window).trigger("hashchange");



	function validatePassword() {
		var password = document.getElementById("ver_pass").value;
	
		if (password == "") {
			document.getElementById("errorMsg").innerHTML = "Please fill the required fields"
			return false;
		}
	
		else if (password.length < 8) {
			document.getElementById("errorMsg").innerHTML = "Your password must include atleast 8 characters"
			return false;
		}
		else {
			alert("Password Reset Successfully!");
			return true;
		}
	}