function toggleDark() {
    document.body.classList.toggle("dark-mode");
}

function clearText() {
    document.getElementById("emailText").value = "";
    document.getElementById("result").innerText = "";
    document.getElementById("confidence").innerText = "";
}

async function checkSpam() {
    const email = document.getElementById("emailText").value;
    const loader = document.getElementById("loader");
    const result = document.getElementById("result");
    const confidence = document.getElementById("confidence");

    loader.classList.remove("hidden");
    result.innerText = "";
    confidence.innerText = "";

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email })
    });

    const data = await response.json();
    loader.classList.add("hidden");

    result.classList.remove("spam", "not-spam");
    result.innerText = data.prediction || data.error;
    confidence.innerText = data.confidence ? `Confidence: ${data.confidence}` : "";

    if (data.prediction === "Spam") {
        result.classList.add("spam");
    } else if (data.prediction === "Not Spam") {
        result.classList.add("not-spam");
    }
}
