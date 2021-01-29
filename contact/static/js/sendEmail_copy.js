function sendMail(contactForm) {
    
    emailjs.send("service_yesouwh", "template_4zfydwi", {
        "from_name": contactForm.user_name.value,
        "from_email": contactForm.user_email.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}