<script>
import { RouterLink, RouterView } from 'vue-router';

export default {
  components: {
    RouterLink,
    RouterView
  }
}
</script>

<template>
  <div class="container">
    <div class="textbox animate__animated animate__zoomIn">
      <h1>Enter New Game or View Leaderboard</h1>
    </div>

    <hr>

    <RouterLink class="button animate__animated animate__bounceInLeft" to="/game">Start New Game</RouterLink>
    <RouterLink class="button animate__animated animate__bounceInLeft"to="/leaderboard">View Leaderboard</RouterLink>
  </div>

  <RouterView />
</template>

<style scoped>
h1 {
  font-size: 40px;
}

hr {
  width: 600px;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 20px;
  height: 100vh;
}

.text-box {
  width: 300px;
  height: 100px;
  border: 2px solid black;
  display: flex;
  justify-content: center;
  align-items: center;
}

.button {
  width: 300px;
  height: 50px;
  border: 2px solid black;
  background-color: white;
  border-radius: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  text-decoration: none; /* Removes default link styling */
  color: black; /* Ensures the text color */
}
</style>


