const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const messagesDiv = document.getElementById("messages");

sendBtn.addEventListener("click", async () => {
    const userMessage = userInput.value;
    if (!userMessage) return;

    messagesDiv.innerHTML += `<p><b>You:</b> ${userMessage}</p>`;
    userInput.value = "";

    messagesDiv.scrollTop = messagesDiv.scrollHeight; // auto scroll

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        messagesDiv.innerHTML += `<p><b>Assistant:</b> ${data.message}</p>`;
        console.log(data);
        

        messagesDiv.scrollTop = messagesDiv.scrollHeight; // auto scroll again
    }
    catch (error) {
        messagesDiv.innerHTML += `<p><b>Assistant:</b> Sorry, there was an error processing your request.</p>`;
        console.error("Error:", error);
    }
});

userInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        sendBtn.click();
    }
});