function sendEmail(contactForm) {
    emailjs.send("gmail", "pj_stickers", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "projectsummary": contactForm.projectsummary.value,
        "title": contactForm.title.value,
        "projectdescription": contactForm.projectdescription.value,
        "quantity": contactForm.quantity.value,
        "size": contactForm.size.value,
        "promo_code": contactForm.promo_code.value,
        
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