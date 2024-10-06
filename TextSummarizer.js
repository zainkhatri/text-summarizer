async function summarizeText() {
    const inputText = document.getElementById("inputText").value;
    const loading = document.getElementById("loading");
    const outputContainer = document.getElementById("outputContainer");
    const summaryText = document.getElementById("summaryText");

    if (!inputText) {
        alert("Please enter some text to summarize.");
        return;
    }

    // Show loading indicator
    loading.style.display = "block";
    outputContainer.style.display = "none";

    try {
        // Make sure this is a POST request
        const response = await fetch("https://text-summarizer-production-ef4b.up.railway.app/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: inputText })
        });

        const data = await response.json();

        if (response.ok) {
            summaryText.textContent = data.summary;
        } else {
            summaryText.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        summaryText.textContent = `Error: ${error.message}`;
    }

    // Hide loading indicator and show output
    loading.style.display = "none";
    outputContainer.style.display = "block";
}
