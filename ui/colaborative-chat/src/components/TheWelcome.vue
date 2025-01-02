<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="container cont">
    <div class="intro">
      <h1>Welcome to Colaborative chat !</h1>
      <p>
        Create a new room to start chatting with your friend and an AI agent.
        You can talk with your friend(s) and both of you can ask an AI agent
        questions.
      </p>
      <RouterLink to="/Create">Create a new room</RouterLink>
    </div>
    <div class="img">
      <img src="../assets/chat_room.png" alt="" srcset="" />
    </div>
  </div>
</template>

<style scoped>
.cont {
  min-width: 90%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-top: 0;
  /* border: 1px solid white; */
}

.intro {
  width: 40%;
  margin-left: auto;
  margin-right: auto;
  /* border: 1px solid white; */
  margin: 0;
  padding: 0;
}

.img {
  width: 60%;
  height: 95%;
  /* border: 1px solid white; */
  margin: 0;
  padding: 0;
}
img {
  width: 90%;
  height: 80%;
  margin: 0;
  padding: 0;
}
</style>
