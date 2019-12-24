function sendMail(contactForm){
    emailjs.send("gmail", "unicorn_attractor", {
        "sender": contactForm.sender.value,
        "sender_email": contactForm.sender_email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response){
            alert("MESSAGE SENT", response);
        },
        function(error){
            alert("FAILED", error);
        }
    );
    return false;
}