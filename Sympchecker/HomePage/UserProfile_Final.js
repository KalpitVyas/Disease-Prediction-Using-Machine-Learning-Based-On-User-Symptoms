var auth = firebase.auth(); //Assigning the Authentication Library.
var user = firebase.auth().currentUser; //Getting the Current User who is logged in.
var email; var name; 
function SignOut() {
    auth.signOut().then(()=>{
        alert('You have been looged out successfully! Click on the "Ok" Button to continue.');
        URL = "http://localhost:8080/Sympchecker/cards.html";
        //const win = window.open(URL, "_blank");
		window.open(URL, "_blank");
		CloseURL = "http://localhost:8080/Sympchecker/HomePage/index.html";
		var SignoutMessage = "You've been logged out please login to continue!";
		document.getElementById("DisplayMail").innerHTML = SignoutMessage;
		window.close(CloseURL);
    }
    ).catch(error=>{
        console.log(error);
    }
    )
}
function ForgotPassword(){
	console.log("ChangePasswordModuleStarted:");
	const GetEmail = document.getElementById("ResetPass");
	const Reset = GetEmail.value;
	firebase.auth().sendPasswordResetEmail(Reset);	
}
function UpdateInfo(){
	console.log("Updating Profile");
	var auth = firebase.auth(); //Assigning the Authentication Library.
						var user = firebase.auth().currentUser; //Getting the Current User who is logged in.
						console.log("Updating the info");
						auth.onAuthStateChanged(function(user){
						if(user){
							var Name = document.getElementById("UpdateUserName").value;
							var Age = document.getElementById("UpdateAge").value;
							var Address = document.getElementById("UpdateAddress").value;
							var PhoneNumber = document.getElementById("UpdatePhoneNumber").value;
							var BloodGroup = document.getElementById("BloodGroup").value;
							var City = document.getElementById("UpdateCity").value;
							var PinCode = document.getElementById("UpdatePinCode").value;
							var db = firebase.firestore();
							db.collection("Users").doc(email).set({
							UserName: Name,
							UserAge: Age,
							UserAddress : Address,
							UserCity : City,
							UserPinCode : PinCode,
							UserPhoneNumber : PhoneNumber,
							UserBloodGroup: BloodGroup,
							UserEmail : user.email
						})
						.then(function() {
							console.log("Document successfully written!");
								alert("Data has been updated successfully please refresh the page!");
						})
						.catch(function(error) {
							console.error("Error writing document: ", error);
							alert("Sorry there was error while submitting you're data. Please Try Again!");
						});
					}
			})
	}
auth.onAuthStateChanged(function(user){
	if(user){
		//Returning the email of the currently logged in user.
		email = user.email;
		console.log(email);
		name = user.displayName;
		console.log("Logged in as : " + email);  //Displaying Email on Console
		//console.log("Name is : " + name); //Displaying the Name of the Logged in User on Console.
		document.getElementById("DisplayMail").innerHTML = user.email; //Displaying the Email of the User on Website.
		//Retirving The Data of the user.
		console.log("Getting the information of the user");
		var db = firebase.firestore();
		db = db.collection("Users").doc(email);
		db.get().then(function(doc) {
    	if (doc.exists) {
        	console.log("Document data:", doc.data());
			console.log("Profile Name : " + doc.data().UserName);
			document.getElementById("UserName").innerHTML = doc.data().UserName;
			document.getElementById("DisplayAge").innerHTML = doc.data().UserAge;
			document.getElementById("UserGender").innerHTML = doc.data().UserGender;
			document.getElementById("PhoneNumber").innerHTML = doc.data().UserPhoneNumber;
			document.getElementById("DisplayMailForModal").innerHTML = doc.data().UserEmail;
			document.getElementById("UserCity").innerHTML = doc.data().UserCity;
			document.getElementById("UserAddress").innerHTML = doc.data().UserAddress;
			document.getElementById("UpdateUserName").innerHTML = doc.data().UserEmail;
			document.getElementById("UserBloodGroup").innerHTML = doc.data().UserBloodGroup;
			document.getElementById("UserPinCode").innerHTML = doc.data().UserPinCode;
    	} else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
		}
		}).catch(function(error) {
    console.log("Error getting document:", error);
			alert("")
		});
	}
	else{
		// When no user is Logged-in then Else part of this code will be executed.
	}
})
