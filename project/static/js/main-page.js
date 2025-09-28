document.addEventListener("DOMContentLoaded", () => {
    const jokeBtn = document.getElementById("joke-btn");
    const setupEl = document.getElementById("setup");
    const punchlineEl = document.getElementById("punchline");
    const likeBtn = document.querySelector(".like-btn");
    const dislikeBtn = document.querySelector(".dislike-btn");
    const buttonsDiv = document.querySelector(".buttons");

    // Fetch a new joke from the backend
    jokeBtn.addEventListener("click", async () => {
        try {
            const response = await fetch("/joke");
            if (!response.ok) throw new Error("Error while fetching a joke");

            const joke = await response.json();

            // If text contains a separator, split into setup and punchline
            let setup = joke.text;
            let punchline = "";
            if (joke.text.includes("|")) {
                const [s, p] = joke.text.split("|");
                setup = s.trim();
                punchline = p ? p.trim() : "";
            }
        } 
    });
