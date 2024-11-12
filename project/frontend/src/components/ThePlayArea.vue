<script>
import TheWordbox from './TheWordbox.vue';
import TheInputs from './TheInputs.vue';

export default {
    components: {
        TheWordbox,
        TheInputs
    },

    data() {
        return {
            answer: "",
            wordProgress: ["_", "_", "_", "_", "_"],
            selectionState: {
                timestamp: 0,
                state: "inactive"
            }
        }
    },

    async mounted() {
        const url = "https://random-word-api.vercel.app/api?words=1&length=5"

        try {
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            this.answer = data[0]

            console.log(this.answer);
        } catch (error) {
            console.error(error);
        }
    },

    methods: {
        handleSelected(selected) {
            if (this.answer.includes(selected)) {
                this.selectionState = {
                    state: "correct",
                    timestamp: Date.now()
                }

                for (let i = 0; i < this.answer.length; i++) {
                    if (this.answer[i] === selected) {
                        this.wordProgress[i] = selected
                    }
                }

                if (!this.wordProgress.includes("_")) {
                    console.log(this.answer)
                    this.$emit("handleWin", this.answer);

                    this.selectionState = {
                        state: "win",
                        timestamp: Date.now()
                    }
                }

                console.log(this.wordProgress);
            } else {
                this.selectionState = {
                    state: "incorrect",
                    timestamp: Date.now()
                }

                this.$emit("incrementHangmanStatus")
            }
        }
    }
}
</script>

<template>
    <div>
        <TheWordbox 
            class="item wordbox"
            :wordProgress="wordProgress"
        ></TheWordbox>
        <TheInputs 
            class="item inputs"
            @selected="handleSelected($event)"
            :selectionState="selectionState"
        ></TheInputs>
    </div>
</template>

<style scoped>
.item {
    display: grid;
    grid-template-columns: 1fr;
}

.wordbox {
    margin-bottom: 40px;
}
</style>