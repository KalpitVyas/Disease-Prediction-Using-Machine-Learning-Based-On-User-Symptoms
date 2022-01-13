console.log("Welcome to the Login Page. Here the user can choose either to login via Email ID, Password or via Gooogle Account, or the user can alo create account and can also Request for Password Reset.");
var auth = firebase.auth();
var db = firebase.firestore(); 
//Following Function is For Login purpose.
function Login(){
	var email = document.getElementById("email");
	var password = document.getElementById("password");
	  var promise = auth.signInWithEmailAndPassword(email.value,password.value);
	  promise.catch(e => alert(e.message));
}
//Following Function is for Create Account and Make the entry of the user in the firestore.
//Create Account.
function SignUp(){
	console.log("Account Creation in Process....");
	var Name = document.getElementById("NewName").value;
	var email = document.getElementById("NewEmailID").value;
	var Age = document.getElementById("NewAge").value;
	var Gender = document.getElementById("GetGender").value;
	const Password = document.getElementById("NewPassword").value;
	const ConfirmPassword = document.getElementById("ConfirmNewPassword").value;
	//const password = document.getElementById("CreatePassword").value;
	var PhoneNumber = document.getElementById("NewPhoneNumber").value;
	var Address = document.getElementById("NewAddress").value;
	var BloodGroup = document.getElementById("BloodGroup").value;
	var City = document.getElementById("NewCity").value;
	var State = document.getElementById("NewState").value;
	var PinCode = document.getElementById("NewPinCode").value;
	if(Name === ""){ //Name Validation.
		document.getElementById("NameError").innerHTML = "Please Enter Name";
	}
	else{
		document.getElementById("NameError").innerHTML = "";
	}
	if(Age === ""){ //Age Validation.
		document.getElementById("AgeError").innerHTML = "Please Enter Valid Age";
	}
	else{
		document.getElementById("AgeError").innerHTML = "";
	}
	if(PhoneNumber === ""){ //PhoneNumber Validation
		document.getElementById("PhoneNumberError").innerHTML = "Please Enter Phone Number";
	}
	else{
		document.getElementById("PhoneNumberError").innerHTML = "";
	}
	if(Address === ""){ //Address Validation
		document.getElementById("AddressError").innerHTML = "Please Enter The Address";
	}
	else{
		document.getElementById("AddressError").innerHTML = "";
	}
	if(City === ""){ //City Validation
		document.getElementById("CityError").innerHTML = "Please Enter City Name";
	}
	else{
		document.getElementById("CityError").innerHTML = "";
	}
	if(State === ""){ //State Validation
		document.getElementById("StateError").innerHTML = "Please Enter State Name";
	}
	else{
		document.getElementById("StateError").innerHTML = "";
	}
	if(PinCode === ""){ //PinCode Validation
		document.getElementById("PinCodeError").innerHTML = "Please Enter The PinCode";
	}
	else{
		document.getElementById("PinCodeError").innerHTML = "";
	}
	//Verifying if the values are missing then don't pass the data to the firebase instead return nothing and stop the execution. 
	var authName = Name;
	var authAge = Age;
	var authAddress = Address;
	var authPhoneNumber = PhoneNumber;
	var authCity = City;
	var authState = State;
	var authPinCode = PinCode;
	if(authName.trim().length === 0 || authAge.trim().length === 0 || authAddress.trim().length === 0){
		console.log("SOMETHING IS WRONG");
		alert("Some Values are missing please complete the form");
		return;
	}
	else{
		console.log("NOTHING WENT WRONG");
	  const promise = auth.createUserWithEmailAndPassword(email,Password);
	  promise.catch(e => alert(e.message));
	  var Email = email.value;	
	}
	  //alert("Accout Creation Successfull" + email.value);
	//Code below is used to make the entry of new user in the firestore.
	db.collection("Users").doc(email).set({
    UserName: Name,
	UserEmail: email,
	UserAge: Age,
	UserAddress : Address,
	UserCity : City,
	UserState : State,
	UserPinCode : PinCode,
	UserPhoneNumber : PhoneNumber,
	UserGender : Gender,
	UserBloodGroup: BloodGroup
})
.then(function() {
    console.log("Document successfully written!");
		//alert("You're account has been created. Please Login to proceed.")
})
.catch(function(error) {
    console.error("Error writing document: ", error);
});	
}
//Following Function is for Forgot password.
function ForgotPassword(){
	console.log("Link for Password Reset Sent Successfully");
	const GetEmail = document.getElementById("ResetEmail");
	const Reset = GetEmail.value;
	firebase.auth().sendPasswordResetEmail(Reset);
	alert("Password reset link has been sent to your email address!");
}
//After Login the user is redirected to the Home Page.
var user = firebase.auth().currentUser;
var email;
auth.onAuthStateChanged(function(user){
	if(user){
		//Returning the email of the currently logged in user.
		email = user.email;
		const URL = "http://localhost:8080/Sympchecker/HomePage/index.html";
		console.log("Redirecting User to : " + URL);
		const win = window.open(URL, "_blank");
		const closeURL = "http://localhost:8080/Sympchecker/HomePage/LoginUser.html"; 
		window.close(closeURL);
	}
	else{
		// When no user is Logged-in then Else part of this code will be executed.
	}
})
function GoogleAccount(){
	console.log("Google Authentication Started");
	var provider = new firebase.auth.GoogleAuthProvider();
	firebase.auth().signInWithPopup(provider).then(function(result) {
  // This gives you a Google Access Token. You can use it to access the Google API.
  var token = result.credential.accessToken;
  // The signed-in user info.
  var user = result.user;
		console.log(user);	
		const URL = "http://localhost:8080/Sympchecker/HomePage/index.html";
		console.log("Redirecting User to : " + URL);
		//const win = window.open(URL, "_blank");
		const closeURL = "http://localhost:8080/Sympchecker/HomePage/LoginUser.html"; 
		window.close(closeURL);
})
}
