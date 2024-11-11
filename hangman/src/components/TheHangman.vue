<script>
import hangman0 from '@/assets/hangman/0.jpg'
import hangman1 from '@/assets/hangman/1.jpg'
import hangman2 from '@/assets/hangman/2.jpg'
import hangman3 from '@/assets/hangman/3.jpg'
import hangman4 from '@/assets/hangman/4.jpg'
import hangman5 from '@/assets/hangman/5.jpg'
import hangman6 from '@/assets/hangman/6.jpg'
import hangman7 from '@/assets/hangman/7.jpg'
import hangman8 from '@/assets/hangman/8.jpg'
import hangman9 from '@/assets/hangman/9.jpg'
import hangman10 from '@/assets/hangman/10.jpg'

export default {
    props: {
        HangmanStatus: Number
    },

    data() {
        return {
            HangmanImages: [
                hangman0,
                hangman1,
                hangman2,
                hangman3,
                hangman4,
                hangman5,
                hangman6,
                hangman7,
                hangman8,
                hangman9,
                hangman10
            ]
        }
    }
}
</script>

<template>
    <div>
        <img :src="HangmanImages[HangmanStatus]" class="image">
    </div>
</template>

<style scoped>
.image {
    height: 640px;
    margin-top: 8px;
}
</style>
