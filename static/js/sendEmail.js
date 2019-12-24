function sendMail(contactForm){
    emailjs.send("gmail", "unicorn_attractor", {
        "sender": contactForm.sender.value,
        "sender_email": contactForm.sender_email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response){
            swal("Message Sent!", "We will be in touch soon!", "success");
        },
        function(error){
            swal("Sending Failed!", "Email us directly if it continue!", "success");
        }
    );
    return false;
}