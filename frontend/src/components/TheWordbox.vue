<script>
export default {
    props: {
        wordProgress: Array
    }
}
</script>

<template>
    <div class="wordbox">
        <h1 class="word">{{ wordProgress.join(" ") }}</h1>
    </div>
</template>

<style scoped>
.wordbox {
    border: 1px solid white;
    width: 600px;
    height: 300px;
}

.word {
    font-size: 100px;
    text-align: center;
    margin-top: 100px;
    font-family: 'Courier New', Courier, monospace;
}
</style>