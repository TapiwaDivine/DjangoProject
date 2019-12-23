function sendMail(contactForm){
    emailjs.send("gmail", "unicorn_attractor", {
        "sender": contactForm.sender.value,
        "sender_email": contactForm.sender_email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response){
            console.log("You message has been sent successfully, a response will be sent soon to you email", response);
        },
        function(error){
            console.log("There was a problem sending your message try again later", error)
        })
}