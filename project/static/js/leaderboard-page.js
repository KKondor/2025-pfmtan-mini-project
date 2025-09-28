document.addEventListener("DOMContentLoaded", async () => {
    const leaderboardList = document.getElementById("leaderboard-list");

    try {
        const response = await fetch("/leaderboard");
        if (!response.ok) throw new Error("Failed to fetch leaderboard");

        const jokes = await response.json();

        // Clear old list
        leaderboardList.innerHTML = "";

        // Add jokes to the leaderboard
        jokes.forEach(joke => {
            let setup = joke.text;
            let punchline = "";

            if (joke.text.includes("|")) {
                const [s, p] = joke.text.split("|");
                setup = s.trim();
                punchline = p ? p.trim() : "";
            }

            const li = document.createElement("li");
            li.classList.add("leaderboard-item");

            const setupSpan = document.createElement("span");
            setupSpan.classList.add("setup");
            setupSpan.textContent = setup;

            const punchlineSpan = document.createElement("span");
            punchlineSpan.classList.add("punchline");
            punchlineSpan.textContent = punchline;

            const ratingSpan = document.createElement("span");
            ratingSpan.classList.add("rating");
            ratingSpan.textContent = joke.rating;

            li.appendChild(setupSpan);
            li.appendChild(punchlineSpan);
            li.appendChild(ratingSpan);

            leaderboardList.appendChild(li);
            
        });           
    }
  });
