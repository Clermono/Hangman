<script>
import TheHangman from '@/components/TheHangman.vue';
import ThePlayArea from '@/components/ThePlayArea.vue';
import Swal from 'sweetalert2';

export default {
    components: {
        TheHangman,
        ThePlayArea
    },

    data() {
        return {
            HangmanStatus: 0,
            playtime: {
                start: null,
                end: null
            }
        }
    },

    mounted() {
        this.playtime.start = Date.now();
    },

    methods: {
        incrementHangmanStatus() {
            this.HangmanStatus++

            if (this.HangmanStatus === 10) {
                Swal.fire({
                    title: "Oops...",
                    text: "You lost! Play again?",
                    icon: "error",
                    showCancelButton: true,
                    confirmButtonText: "Play again",
                    cancelButtonText: "No thanks",
                }).then((result) => {
                    if (result.isConfirmed) {
                        let timerInterval

                        Swal.fire({
                            title: "Page refresh alert!",
                            html: "I will refresh in <b></b> milliseconds.",
                            timer: 1500,
                            timerProgressBar: true,
                            didOpen: () => {
                                Swal.showLoading()
                                const timer = Swal.getPopup().querySelector("b")
                                timerInterval = setInterval(() => {
                                timer.textContent = `${Swal.getTimerLeft()}`
                                }, 100)
                            },
                            willClose: () => {
                                clearInterval(timerInterval)
                            }
                        }).then(() => {
                            window.location.reload()
                        })
                    }
                })
            }
        },

        gameScore() {
            this.playtime.end = Date.now();

            return 1000 - Math.floor((this.playtime.end - this.playtime.start) / 100) * (this.HangmanStatus + 1)
        },

        handleWin(answer) {
            Swal.fire({
                title: "Congratulations!",
                html: `You've successfully guessed <em>${answer}</em>! Save score to leaderboard?`,
                icon: "success",
                showCancelButton: true,
                cancelButtonText: "No, don't save",
                confirmButtonText: "Yes, save score",
            }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire({
                        title: "Enter your name",
                        input: "text",
                        inputAttributes: {
                            autocapitalize: "off",
                            autocorrect: "off",
                            spellcheck: false
                        },
                        inputValidator: (value) => {
                            if (!value) {
                                return "You need to enter your name!"
                            }
                        },
                        showCancelButton: true,
                        confirmButtonText: "Save my score"
                    }).then((result) => {
                        if (result.isConfirmed) {
                            const url = new URL("/scorecards", "https://hangman-backend-alpha.vercel.app")
                            console.log(url)
                            
                            const postData = async () => {
                                try {
                                    const response = await fetch(url, {
                                        method: "POST",
                                        headers: {
                                            'Accept': ["application/json"],
                                            'Content-Type': ["application/json"]
                                        },

                                        body: JSON.stringify({
                                            playerName: result.value,
                                            playerScore: this.gameScore(),
                                            playerStatistics: {
                                                word: answer,
                                                mistakes: this.HangmanStatus,
                                                time: this.playtime.end - this.playtime.start
                                            }
                                        })
                                    })

                                    if (!response.ok) {
                                        throw new Error(`HTTP error! status: ${response.status}`)
                                    }

                                    console.log(await response.json())
                                } catch (error) {
                                    console.error(error)
                                }
                            }

                            postData()
                        }
                    }).then(() => {
                        Swal.fire({
                            title: "Did you make it?",
                            text: "Check the leaderboard for your score!",
                            icon: "question",
                            showCancelButton: true,
                            confirmButtonText: "Go to leaderboard",
                            cancelButtonText: "No, thanks",
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.location.href = "/leaderboard"
                            } else {
                                window.location.reload()
                            }
                        })
                    })
                }
            })
        }
    }
}
</script>

<template>
    <div class="centered_container">
        <ThePlayArea 
            class="playarea" 
            @incrementHangmanStatus="incrementHangmanStatus"
            @handleWin="handleWin"
        ></ThePlayArea>
        <TheHangman :HangmanStatus="HangmanStatus"></TheHangman>
    </div>
</template>

<style scoped>
.centered_container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.playarea {
    margin-right: 40px;
}
</style>