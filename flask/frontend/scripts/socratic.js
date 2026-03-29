import codeReview from '../scripts/review.js';

// When the user clicks run task, run this async function
document.getElementById("runBtn").addEventListener("click", async () => {

    // Get the selected value from the dropdown with id="task"
    const task = document.getElementById("task").value;

    let socraticResponseHTML = `
    <p class="socratic">Socratic Hint</p>
    <p class="concepts" id="socratic-response">Running...</p>
    `;

    const socraticContainer = document.getElementById("js-socratic-hint-container");
    socraticContainer.innerHTML = socraticResponseHTML;

    const ai_response = document.getElementById("socratic-response");

    try {
        // Send a POST request to your Flask route "/run-feedback"
        const response = await fetch("/run-socratic", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ task })
        });

        // Take the server response and convert it from JSON into a JS object
        const data = await response.json();

        // Put the returned backend output into the page
        ai_response.innerHTML = data.output;

    } catch (error) {
        ai_response.innerHTML = "Error: Could not get socratic hint<br>" + error.message;
        return;
    }

    // Add the code review button AFTER the hint is shown
    socraticContainer.innerHTML += `
    <p class="code-review-question">Would you like to try code review?</p>
    <button class="code-review-button" id="codeReview">Code Review</button>
    `;

    codeReview();
    
});