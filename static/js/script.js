// Shopping Cart Functionality
let totalPrice = 0;

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        const price = parseInt(button.getAttribute('data-price'));
        const productName = button.previousElementSibling.previousElementSibling.textContent;

        // Add product to cart list
        const cartItems = document.getElementById('cart-items');
        const listItem = document.createElement('li');
        listItem.textContent = productName + ' - ₹' + price;
        cartItems.appendChild(listItem);

        // Update total price
        totalPrice += price;
        document.getElementById('total-price').textContent = totalPrice;
    });
});

// Chatbot Functionality

// Function to get CSRF token (for Django or similar frameworks)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Chatbot toggle
document.getElementById("chatbotToggle").addEventListener("click", function () {
    const chatWindow = document.getElementById("chatWindow");
    chatWindow.style.display = chatWindow.style.display === "block" ? "none" : "block";
});

// Close chat button
document.getElementById("closeChat").addEventListener("click", function () {
    document.getElementById("chatWindow").style.display = "none";
});

// Chatbot message handling 
document.getElementById("sendBtn").addEventListener("click", function () {
    const userInput = document.getElementById("userInput");
    const chatBody = document.getElementById("chatBody");

    if (userInput.value.trim()) {
        // Append user message
        const userMessage = document.createElement("div");
        userMessage.classList.add("message", "user-message");

        const userText = document.createElement("p");
        userText.textContent = "User: " + userInput.value;

        userMessage.appendChild(userText);
        chatBody.appendChild(userMessage);

        // Send the user message to the server
        fetch("/", {  // Point to the index view
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken")  // Include CSRF token
            },
            body: "user_message=" + encodeURIComponent(userInput.value)
        })
        .then(response => response.json())
        .then(data => {
            // Append bot's response
            const botResponse = document.createElement("div");
            botResponse.classList.add("message", "bot-message");

            const botText = document.createElement("p");
            botText.textContent = "Bot: " + data.response;

            botResponse.appendChild(botText);
            chatBody.appendChild(botResponse);

            // Scroll to bottom of chat
            chatBody.scrollTop = chatBody.scrollHeight;
        })
        .catch(error => {
            console.error("Error in fetch:", error);
        });

        // Clear input field after submission
        userInput.value = "";
    }
});

// Add "Enter to Send" functionality
document.getElementById("userInput").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Prevent form submission or other default actions
        // The message sending logic is already in the click handler, so no need to call sendMessage() again.
    }
});
