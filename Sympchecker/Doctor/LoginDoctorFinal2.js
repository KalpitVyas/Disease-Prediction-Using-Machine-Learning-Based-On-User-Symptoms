var auth = firebase.auth();
//Following Function is For Login purpose.
function Login(){
	var email = document.getElementById("email");
	var password = document.getElementById("password");
	  var promise = auth.signInWithEmailAndPassword(email.value,password.value);
	  promise.catch(e => alert(e.message));
	
}
var user = firebase.auth().currentUser;
var email;
auth.onAuthStateChanged(function(user){
	if(user){
		//Returning the email of the currently logged in user.
		email = user.email;
		console.log("Logged in as : " + email);
		//If the user is already logged in the it will be redirected to the specified URL.
		const URL = "http://localhost:8080/Sympchecker/Doctor/doc_profile/profile.html";
		console.log("Redirecting User to : " + URL);
		window.open(URL);
		const closeURL = "http://localhost:8080/Sympchecker/Doctor/LoginUser_doc.html";
		window.close(closeURL);
	}
	else{
		// When no user is Logged-in then Else part of this code will be executed.
	}
})