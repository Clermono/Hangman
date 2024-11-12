<script>
export default {
    data() {
        return {
            leaderboard: null 
        }
    },

    async mounted() {
        const URL = "http://localhost:8000/scorecards"

        try {
            const response = await fetch(URL, {
                headers: {
                    'Accept': ['application/json', 'text/plain']
                }
            })

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }

            const data = await response.json()
            this.leaderboard = data
            console.log(data)
        } catch (error) {
            console.error(error)
        }
    }
}
</script>

<template>
    <div class="container">
        <h1>Leaderboard</h1>

        <div class="player" v-for="(player, index) in leaderboard" :key="index">
            <span class="playerName">{{ player.playerName }}</span>
            <span class="playerScore">{{ player.playerScore }}</span>
        </div>
    </div>
</template>

<style scoped>
h1 {
    font-size: 50px;    
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    flex-wrap: wrap;
    height: 100vh;
}

.player {
    display: flex;
    border: 1px solid white;
    width: 600px;
    height: 60px;
}

.playerName {
    font-size: 25px;
    margin-left: 10px;
    margin-top: 10px;
}

.playerScore {
    font-size: 25px;
    margin-left: auto;
    margin-right: 10px;
    margin-top: 10px;
}
</style>