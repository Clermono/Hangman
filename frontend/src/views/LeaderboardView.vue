<script>
export default {
    data() {
        return {
            leaderboard: null
        }
    },

    async mounted() {
        const URL = "https://hangman-backend-alpha.vercel.app/scorecards"

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
    },

    computed: {
        rankEmoji() {
            return (rank) => {
                if (rank === 1 || rank === 2 || rank === 3) {
                    return {
                        class: "emojiRank",
                        text: rank === 1 ? "🥇" : rank === 2 ? "🥈" : "🥉"
                    }
                } else {
                    return {
                        class: "textRank",
                        text: rank
                    }
                }
            }
        },

        rankColor() {
            return (rank) => {
                if (rank === 1) {
                    return "goldPlayer"
                } else if (rank === 2) {
                    return "silverPlayer"
                } else if (rank === 3) {
                    return "bronzePlayer"
                } else {
                    if (rank % 2 === 0) {
                        return "evenPlayer"
                    } else {
                        return "oddPlayer"
                    }
                }
            }
        }
    }
}
</script>

<template>
    <div class="container">
        <h1>Leaderboard</h1>

        <div :class="rankColor(index + 1)" class="player" v-for="(player, index) in leaderboard" :key="index">
            <span :class="rankEmoji(index + 1).class">{{ rankEmoji(index + 1).text }}</span>
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
    position: relative;
    width: 600px;
    height: 60px;
    color: #e0e0e0;
}

.textRank {
    position: absolute;
    left: 15px;
    font-size: 25px;
    margin-top: 10px;
    text-align: center;
}

.emojiRank {
    position: absolute;
    left: 7px;
    font-size: 25px;
    margin-top: 10px;
    text-align: center;
}

.playerName {
    position: absolute;
    left: 70px;
    font-size: 25px;
    margin-top: 10px;
}

.goldPlayer {
    background-color: #d4af37;
}

.silverPlayer {
    background-color: #b0b0b0;
}

.bronzePlayer {
    background-color: #cd7f32;
}

.evenPlayer {
    background-color: #484848;
}

.oddPlayer {
    background-color: #333333;
}

.playerScore {
    font-size: 25px;
    margin-left: auto;
    margin-right: 10px;
    margin-top: 10px;
}
</style>