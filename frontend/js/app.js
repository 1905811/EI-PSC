const fileInput = document.getElementById("pdfFile");
const analyseButton = document.getElementById("analyseButton");

const statusSection = document.getElementById("statusSection");
const statusMessage = document.getElementById("statusMessage");

const resultsSection = document.getElementById("resultsSection");
const materialsContainer = document.getElementById("materialsContainer");


analyseButton.addEventListener("click", async () => {

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a PDF first.");
        return;
    }

    statusSection.classList.remove("hidden");
    resultsSection.classList.add("hidden");

    statusMessage.textContent = "Analysing paper...";

    const formData = new FormData();

    formData.append("file", file);


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyse",
            {
                method: "POST",
                body: formData
            }
        );


        if (!response.ok) {
            throw new Error("Analysis failed.");
        }


        const data = await response.json();


        statusMessage.textContent =
            `Analysis complete. ${data.materials.length} materials found.`;


        displayMaterials(data.materials);

        resultsSection.classList.remove("hidden");


    } catch (error) {

        statusMessage.textContent =
            "An error occurred while analysing the paper.";

        console.error(error);

    }

});


function displayMaterials(materials) {

    materialsContainer.innerHTML = "";


    materials.forEach(material => {

        const card = document.createElement("div");

        card.className = "material-card";


        const riskClass =
            material.risk === "HIGH"
                ? "risk-high"
                : "risk-unknown";


        card.innerHTML = `
            <h3>${material.name}</h3>

            <p>
                <strong>Matched alias:</strong>
                ${material.matched_alias || "N/A"}
            </p>

            <p>
                <strong>Role:</strong>
                ${material.role || "Unknown"}
            </p>

            <p>
                <strong>Risk:</strong>
                <span class="${riskClass}">
                    ${material.risk || "UNKNOWN"}
                </span>
            </p>

            <p>
                <strong>Source:</strong>
                ${material.source || "Unknown"}
            </p>

            <p>
                <strong>Confidence:</strong>
                ${material.confidence ?? "N/A"}
            </p>
        `;


        materialsContainer.appendChild(card);

    });

}