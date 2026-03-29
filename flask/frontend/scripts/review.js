import workedExample from '../scripts/example.js';

export default function codeReview() {
    const codeReviewButton = document.getElementById("codeReview");

    if (!codeReviewButton) {
        console.log("Code Review button not found.");
        return;
    }

    // Prevent stacking multiple listeners if Run Feedback is clicked again
    codeReviewButton.replaceWith(codeReviewButton.cloneNode(true));
    const freshButton = document.getElementById("codeReview");

    freshButton.addEventListener("click", async () => {
        const task = document.getElementById("task").value;

        let reviewHTML = `
        <p class="review">Code Review</p>
        <p class="worked-example" id="review-response">Running...</p>
        `;

        const reviewContainer = document.getElementById("js-review-container");
        reviewContainer.innerHTML = reviewHTML;

        const reviewResponse = document.getElementById("review-response");

        try {
            const response = await fetch("/run-review", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ task })
            });

            const data = await response.json();
            reviewResponse.innerHTML = data.output;

        } catch (error) {
            reviewResponse.innerHTML = "Error: Could not get code review<br>" + error.message;
        }

       reviewResponse.innerHTML += `
        <p class="worked-example-question">Would you like a worked example?</p>
        <button class="worked-example-button" id="workedExample">Worked Example</button>
        `;

        workedExample();


    });
}