<script>
export default {
    props: {
        selectionState: {
            timestamp: Number,
            state: String
        }
    },

    data() {
        return {
            alphabet: "abcdefghijklmnopqrstuvwxyz".split("").map(letter => ({ letter, state: "inactive" })),
            currentSelected: "None",
            selectionDisabled: false
        }
    },

    methods: {
        handleConfirm() {
            this.$emit("selected", this.currentSelected)
        },

        handleSelectionState(state) {
            const index = this.alphabet.findIndex((alphabet) => alphabet.letter === this.currentSelected)

            if (state === "correct") {
                if (index !== -1) {
                    this.alphabet[index].state = "correct"
                }
            } else if (state === "incorrect") {
                if (index !== -1) {
                    this.alphabet[index].state = "incorrect"
                }
            } else if (state === "win") {
                this.selectionDisabled = true
            }
        }
    },

    watch: {
        selectionState: {
            handler(state) {
                this.handleSelectionState(state.state)
            },

            deep: true
        }
    }
}
</script>

<template>
    <div class="container">
        <div style="width: 100%; height: 100%">
            <button 
                v-for="({ letter, state }, i) in alphabet" 
                :key="i" 
                class="input-button" 
                :class="state"
                @click="this.currentSelected = letter"
            >
                {{ letter }}
            </button>

            <div class="textbox">
                <p>Selected: {{ currentSelected }}</p>
            </div>
        </div>

        <button 
            class="confirm-button" 
            @click="handleConfirm"
            :disabled="selectionDisabled"
        >CONFIRM SELECTION</button>
    </div>
</template>

<style scoped>
.inactive {
    background-color: #f8f8f8;
}

.inactive:hover {
    background-color: #e7e7e7;
}

.incorrect {
    background-color: #e34749;
}

.correct {
    background-color: #8bc34a;
}

button:disabled {
    background-color: #b5b6ba;
    cursor: not-allowed;
}

button:disabled:hover {
    background-color: #979797;
}


.container {
    width: 600px;
    height: 300px;

    border: 1px solid white;

    padding: 30px;
}

.input-button {
    width: 10%;
    aspect-ratio: 1;

    font: inherit;
    font-size: 20px;
    border: 1px solid black;
}

.textbox {
    width: 210px;
    height: 48px;
    display: inline-block;

    font: inherit;
    font-size: 20px;
    margin-left: 5px;   
    text-align: center;
}

.confirm-button {
    font: inherit;
    font-size: 20px;
    border: 1px solid black;
}

.confirm-button:hover {
    background-color: #e7e7e7;
}
</style>