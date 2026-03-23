async function uploadResume() {
    const job = document.getElementById("job").value;
    const fileInput = document.getElementById("resume");

    const formData = new FormData();
    formData.append("job_desc", job);
    formData.append("resume", fileInput.files[0]);

    const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

  document.getElementById("result").innerHTML = `
    <h3>📊 Match Score: ${data.score}%</h3>

    <div class="progress">
        <div class="progress-bar" style="width:${data.score}%"></div>
    </div>

    <div class="skills-section">
        <p>✅ Matched Skills</p>
        <div class="tags">
            ${data.matched.map(skill => `<span class="tag green">${skill}</span>`).join("")}
        </div>

        <p>❌ Missing Skills</p>
        <div class="tags">
            ${data.missing.length > 0 
                ? data.missing.map(skill => `<span class="tag red">${skill}</span>`).join("")
                : `<span class="tag gray">None 🎉</span>`}
        </div>
    </div>
`;
}