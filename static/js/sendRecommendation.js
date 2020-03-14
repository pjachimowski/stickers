function sendRecommendation(contactForm) {
    emailjs.send("gmail", "pj_recommendation", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "recommendation": contactForm.recommendation.value,
        "rating": contactForm.rating.value,      
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