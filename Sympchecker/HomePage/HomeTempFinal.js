var auth = firebase.auth();
//Assigning the Authentication Library.
var user = firebase.auth().currentUser;
//Getting the Current User who is logged in.
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
		//window.location.href = "http://localhost:8080/Sympchecker/cards.html";
    }
    ).catch(error=>{
        console.log(error);
    }
    )
}
auth.onAuthStateChanged(function(user) {
    if (user) {
        //Returning the email of the currently logged in user.
        email = user.email;
        name = user.displayName;
        console.log("Logged in as : " + email);
        //Displaying Email on Console
        console.log("Name is : " + name);
        //Displaying the Name of the Logged in User on Console.
        //document.getElementById("DisplayName").innerHTML = UserNmail;
        //Displaying the Email of the User on Website.
        //Retirving The Data of the user.
        console.log("Getting the information of the user");
        var db = firebase.firestore();
        db = db.collection("Users").doc(email);
        db.get().then(function(doc) {
            if (doc.exists) {
                console.log("Document data:", doc.data());
                document.getElementById("DisplayMail").innerHTML = email;
				//document.getElementById("DisplayMail").innerHTML = doc.data().email;
                //Code for Display in HTML.
            } else {
                // doc.data() will be undefined in this case
                console.log("No such document!");
            }
        }).catch(function(error) {
            console.log("Error getting document:", error);
        });
    } else {// When no user is Logged-in then Else part of this code will be executed.
    }
})

