document.addEventListener("DOMContentLoaded", function () {
    const trigger = document.getElementById("rag-chatbot-trigger");
    const windowEl = document.getElementById("rag-chatbot-window");
    const closeBtn = document.getElementById("rag-chatbot-close");
    const input = document.getElementById("chatbot-input");
    const sendBtn = document.getElementById("chatbot-send");
    const messagesContainer = document.getElementById("chatbot-messages");
    const apiKeyOverlay = document.getElementById("chatbot-api-key-overlay");
    const apiKeyInput = document.getElementById("chatbot-api-key-input");
    const apiKeySaveBtn = document.getElementById("chatbot-api-key-save");

    let indexData = null;
    let apiKey = localStorage.getItem("gemini_api_key");

    // Toggle Chat
    trigger.addEventListener("click", () => {
        windowEl.classList.toggle("open");
        if (windowEl.classList.contains("open")) {
            input.focus();
            checkApiKey();
        }
    });

    closeBtn.addEventListener("click", () => {
        windowEl.classList.remove("open");
    });

    // API Key Handling
    function checkApiKey() {
        if (!apiKey) {
            apiKeyOverlay.classList.remove("hidden");
        } else {
            apiKeyOverlay.classList.add("hidden");
            if (!indexData) loadIndex();
        }
    }

    apiKeySaveBtn.addEventListener("click", () => {
        const key = apiKeyInput.value.trim();
        if (key) {
            apiKey = key;
            localStorage.setItem("gemini_api_key", apiKey);
            apiKeyOverlay.classList.add("hidden");
            loadIndex();
            addBotMessage("Hello! I'm integrated with this blog's content. Ask me anything!");
        }
    });

    // Load Search Index
    async function loadIndex() {
        if (indexData) return;
        try {
            const response = await fetch("rag_index.json");
            if (!response.ok) throw new Error("Index not found");
            indexData = await response.json();
            console.log("RAG Index loaded", indexData.length, "chunks");
        } catch (e) {
            console.error(e);
            addBotMessage("Error loading knowledge base. Please try refreshing.");
        }
    }

    // Chat Logic
    function addMessage(text, sender) {
        const div = document.createElement("div");
        div.className = `message ${sender}`;
        // Basic markdown-like rendering could go here, for now just text
        // Safety: textContent for user, innerHTML for bot (if we trust it or sanitize)
        // We'll use simple replacement for bold/newlines for bot
        if (sender === 'bot') {
            // Simple markdown converter
            let formatted = text
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                .replace(/\n/g, '<br>');
            div.innerHTML = formatted;
        } else {
            div.textContent = text;
        }
        messagesContainer.appendChild(div);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function addBotMessage(text) {
        addMessage(text, "bot");
    }

    async function handleSend() {
        const text = input.value.trim();
        if (!text) return;

        addMessage(text, "user");
        input.value = "";

        if (!apiKey) {
            checkApiKey();
            return;
        }

        const loadingDiv = document.createElement("div");
        loadingDiv.className = "message bot loading-dots";
        loadingDiv.textContent = "Thinking";
        messagesContainer.appendChild(loadingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        try {
            const context = retrieveContext(text);
            const response = await callGemini(text, context);
            messagesContainer.removeChild(loadingDiv);
            addBotMessage(response);
        } catch (e) {
            console.error(e);
            messagesContainer.removeChild(loadingDiv);
            addBotMessage("Sorry, I encountered an error. Check your API key or try again.");
            if (e.message.includes("401") || e.message.includes("key")) {
                localStorage.removeItem("gemini_api_key");
                apiKey = null;
                checkApiKey();
            }
        }
    }

    sendBtn.addEventListener("click", handleSend);
    input.addEventListener("keypress", (e) => {
        if (e.key === "Enter") handleSend();
    });

    // Simple Vector-less Search implementation
    // Ideally we'd use embeddings but for "free static", keyword matching + ranking is okay for small blogs
    function retrieveContext(query) {
        if (!indexData) return "";
        const terms = query.toLowerCase().split(/\s+/).filter(w => w.length > 3);

        const scored = indexData.map(chunk => {
            let score = 0;
            const contentLower = chunk.content.toLowerCase();
            terms.forEach(term => {
                if (contentLower.includes(term)) score += 1;
            });
            return { ...chunk, score };
        });

        scored.sort((a, b) => b.score - a.score);
        console.log("Top chunks:", scored.slice(0, 3));
        return scored.slice(0, 3).map(c => `Content: ${c.content}\nSource: ${c.title}`).join("\n\n");
    }

    async function callGemini(query, context) {
        const prompt = `
You are a helpful assistant for the "Nathemis" blog. Use the provided context to answer the user's question.
If the context doesn't contain the answer, say "I couldn't find that in the blog posts."
Context:
${context}

Question: ${query}
Answer:
`;

        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${apiKey}`;
        console.log("Requesting Gemini URL:", url.replace(apiKey, "HIDDEN_KEY"));

        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }]
            })
        });

        if (!response.ok) {
            const errText = await response.text();
            console.error("Gemini API Error Details:", errText);
            throw new Error(`Gemini API Error: ${response.status} ${response.statusText} - ${errText}`);
        }

        const data = await response.json();
        return data.candidates[0].content.parts[0].text;
    }
});
