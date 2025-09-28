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
        });

        
    }
  });
