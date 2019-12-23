function sendMail(contactForm){
    emailjs.send("gmail", "unicorn_attractor", {
        "sender": contactForm.sender.value,
        "sender_email": contactForm.sender_email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response){
            console.log("Success", response);
        },
        function(error){
            console.log("Failed", error)
        })
}