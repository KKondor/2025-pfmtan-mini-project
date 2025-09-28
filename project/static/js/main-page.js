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

            let setup = joke.setup;
            let punchline = joke.punchline;

            // Update DOM
            setupEl.textContent = setup;
            punchlineEl.textContent = punchline;

            // Enable rating buttons
            likeBtn.dataset.id = joke.id;
            dislikeBtn.dataset.id = joke.id;
            buttonsDiv.dataset.rating = "0";

            likeBtn.disabled = false;
            dislikeBtn.disabled = false;
        }
        catch (err) {
            console.error("Failed to load joke:", err);
        }
    });

    // Send rating to backend
    async function rateJoke(jokeId, value) {
        try {
            const response = await fetch(`/joke/${jokeId}/rate`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ value })
            });
            if (!response.ok) throw new Error("Rating request failed");
            
            const ratingEl = document.querySelector(".rating");
            if (ratingEl) {
                ratingEl.textContent = parseInt(ratingEl.textContent || "0") + value;
            }
        } catch (err) {
            console.error("Failed to rate joke:", err);
        }
    }

    // Like button logic
    likeBtn.addEventListener("click", () => {
        const currentRating = parseInt(buttonsDiv.dataset.rating);
        const jokeId = likeBtn.dataset.id;
        let value = 0;

        if (currentRating === 0) {
            value = 1;
            buttonsDiv.dataset.rating = "1";
        } else if (currentRating === 1) {
            value = -1; // undo like
            buttonsDiv.dataset.rating = "0";
        } else if (currentRating === -1) {
            // from dislike to like
            rateJoke(jokeId, 1); 
            value = 1;
            buttonsDiv.dataset.rating = "1";
        }

        if (value !== 0) {
        rateJoke(jokeId, value);
        }
});

    // Dislike button logic
    dislikeBtn.addEventListener("click", () => {
        const currentRating = parseInt(buttonsDiv.dataset.rating);
        const jokeId = dislikeBtn.dataset.id;
        let value = 0;

        if (currentRating === 0) {
            value = -1;
            buttonsDiv.dataset.rating = "-1";
        } else if (currentRating === -1) {
            value = 1; // undo dislike
            buttonsDiv.dataset.rating = "0";
        } else if (currentRating === 1) {
            // from like to dislike
            rateJoke(jokeId, -1); 
            value = -1;
            buttonsDiv.dataset.rating = "-1";
        }

        if (value !== 0) {
        rateJoke(jokeId, value);
        }
    });

});
