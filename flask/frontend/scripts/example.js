export default function workedExample() {
    const workedExampleButton = document.getElementById("workedExample");

    if (!workedExampleButton) {
        console.log("Worked Example button not found.");
        return;
    }

    // Prevent duplicate listeners if this gets called more than once
    workedExampleButton.replaceWith(workedExampleButton.cloneNode(true));
    const freshButton = document.getElementById("workedExample");

    freshButton.addEventListener("click", async () => {
        const task = document.getElementById("task").value;

        const exampleContainer = document.getElementById("js-example-container");
        exampleContainer.innerHTML = `
            <p class="review">Worked Example</p>
            <div id="example-response">Running...</div>
        `;

        const exampleResponse = document.getElementById("example-response");

        try {
            const response = await fetch("/run-example", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ task })
            });

            const data = await response.json();

            let exampleData;
            try {
                exampleData = JSON.parse(data.output);
            } catch (parseError) {
                exampleResponse.innerHTML = `
                    <p class="example-explanation">Could not parse structured worked example output.</p>
                    <pre class="code-block"><code>${data.output}</code></pre>
                `;
                return;
            }

            exampleResponse.innerHTML = "";

            const explanation = document.createElement("p");
            explanation.className = "example-explanation";
            explanation.textContent = exampleData.explanation || "";

            const pre = document.createElement("pre");
            pre.className = "code-block";

            const code = document.createElement("code");
            code.textContent = exampleData.code || "";

            pre.appendChild(code);
            exampleResponse.appendChild(explanation);
            exampleResponse.appendChild(pre);

        } catch (error) {
            exampleResponse.innerHTML = "Error: Could not get worked example<br>" + error.message;
        }
    });
}