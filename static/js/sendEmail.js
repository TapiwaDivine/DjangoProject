function sendMail(contactForm){
    emailjs.send("gmail", "unicorn_attractor", {
        "sender": contactForm.sender.value,
        "sender_email": contactForm.sender_email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response){
            swal("Good job!", "You clicked the button!", "success");
        },
        function(error){
            alert("FAILED", error);
        }
    );
    return false;
}