var auth = firebase.auth(); //Assigning the Authentication Library.
var user = firebase.auth().currentUser; //Getting the Current User who is logged in.
var email; var name;
function SignOut() {
    auth.signOut().then(()=>{
        
        alert('You have been looged out successfully! Click on the "Ok" Button to continue.');
		const CloseURL = "http://localhost:8080/Sympchecker/cards.html";
		window.close(CloseURL);
    }
    ).catch(error=>{
        console.log(error);
    })
}
function Show(){
	console.log("Displaying the info");
					var list_patientName= [];
					var list_patientEmail = [];
					var list_Day = [];
					var list_Time = [];
					var Display = "";
					var Display_Email = "";
					var Display_Day = "";
					var Display_time = "";
						var verify = firebase.auth().currentUser;
						var db = firebase.firestore();
						var doc_name = verify.email;
						console.log(doc_name)
						db = db.collection(doc_name).get().then((querySnapshot) =>{
						querySnapshot.forEach((doc) =>{
							console.log(doc.id, " => ", doc.data());
							list_patientName.push(doc.data().UserName);
							list_patientEmail.push(doc.data().UserEmail);
							list_Day.push(doc.data().Date);	
							list_Time.push(doc.data().Time);
							//document.getElementById("EmailPatient").innerHTML = list_patientEmail + "<br>"
							//document.getElementById("Day").innerHTML = list_Day + "<br>"
						})	
						var i;
						for(i = 0; i<list_patientName.length;i++){
							Display += list_patientName[i] + "<br>";
						}
							for(i = 0; i<list_patientEmail.length;i++){
							Display_Email += list_patientEmail[i] + "<br>";
						}
							for(i = 0; i<list_Day.length;i++){
							Display_Day += list_Day[i] + "<br>";
						}
							for(i = 0; i<list_Time.length;i++){
							Display_time += list_Time[i] + "<br>";
						}
					console.log(Display_time);
					document.getElementById("NamePatient").innerHTML = Display;
					//console.log("Patient Name " + Display);
					document.getElementById("EmailPatient").innerHTML = Display_Email;
					document.getElementById("Day").innerHTML = Display_Day;
					document.getElementById("Time").innerHTML = Display_time;
				});
}
function ChangePassword(){
	console.log("ChangePasswordModuleStarted:");
	const GetEmail = document.getElementById("ResetPass");
	const Reset = GetEmail.value;
	firebase.auth().sendPasswordResetEmail(Reset);	
}
auth.onAuthStateChanged(function(user){
	if(user){
		//Returning the email of the currently logged in user.
		email = user.email;
		name = user.displayName;
		console.log("Logged in as : " + email);  //Displaying Email on Console
		console.log("Name is : " + name); //Displaying the Name of the Logged in User on Console.
		document.getElementById("DisplayMail").innerHTML = email; //Displaying the Email of the User on Website.
		//Retirving The Data of the user.
		console.log("Getting the information of the user");
		var db = firebase.firestore();
		db = db.collection("Doctors").doc(email);
		db.get().then(function(doc) {
    	if (doc.exists) {
        	console.log("Document data:", doc.data());
			console.log(doc.data().UserName);
			document.getElementById("DocName").innerHTML = doc.data().DocName;
			document.getElementById("DisplayAge").innerHTML = doc.data().DocAge;
			document.getElementById("UserGender").innerHTML = doc.data().DocGender;
			document.getElementById("PhoneNumber").innerHTML = doc.data().DocPhoneNumber;
			document.getElementById("UserCity").innerHTML = doc.data().DocCity;
			document.getElementById("UserAddress").innerHTML = doc.data().DocAddress;
			document.getElementById("UserBloodGroup").innerHTML = doc.data().DocBloodGroup;
			document.getElementById("DocYOE").innerHTML = doc.data().DocYOE;
			document.getElementById("DocQualification").innerHTML = doc.data().DocQualification;
    	} else {
        // doc.data() will be undefined in this case
        console.log("No such document!");
		}
		}).catch(function(error) {
    console.log("Error getting document:", error);
		});
	}
	else{
		// When no user is Logged-in then Else part of this code will be executed.
	}
})
