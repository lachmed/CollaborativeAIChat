<script setup>
import { ref } from "vue";
import axios from "axios";

import Dialogue from "@/components/Dialogue.vue";

var formData = ref({
  text: "",
});

var messaging = ref([]);

var loading = ref(false);

async function fetchData(message) {
  try {
    const response = await axios.get(
      "http://127.0.0.1:5000/message?message=" + message
    );
    messaging.value.push({
      question: message,
      answer: response.data,
    });
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

function handleSubmit() {
  var question = formData.value.text;
  loading.value = true;
  formData.value.text = "";
  console.log(loading.value);
  // console.log(question);

  fetchData(question);

  // console.log(messaging.value);
  console.log(loading.value);
  loading.value = false;
}
</script>

<template>
  <div class="container" id="containerA">
    <div class="container" id="dialogue">
      <div v-if="loading">Generating...</div>
      <Dialogue
        v-for="dial in messaging"
        :question="dial['question']"
        :answer="dial['answer'].response"
      />
    </div>

    <form class="container" id="prompt" @submit.prevent="handleSubmit">
      <input type="text" placeholder="Chat here" v-model="formData.text" />
    </form>
  </div>
</template>

<style scoped>
/*
        medium devices styles
    */

@media (max-width: 992px) {
}

/*
    small devices styles
    */

@media (max-width: 576px) {
}

/* Large devices (default) */

@media (min-width: 992px) {
  #containerA {
    margin: 0;
    padding: 0;
    min-width: 100%;
    min-height: 100vh;
    background-color: rgb(19, 18, 21);
    color: white;
    /* border: 1px solid yellow; */
  }

  #prompt {
    /* border: 2px solid red; */
    position: fixed;
    bottom: 7%;
    left: 5%;
    height: 5rem;
    margin-left: auto;
    margin-right: auto;
    padding: 0;
    margin: 0;
    min-width: 90%;
  }

  #prompt input {
    min-width: 100%;
    min-height: 100%;
    border-radius: 5rem;
    padding: 0 10px;
    background-color: rgb(31, 31, 33);
    border: none;
    color: white;
    /* border: 1px solid salmon; */
  }

  #dialogue {
    max-height: 500px;
    overflow-y: scroll;
    scrollbar-color: #ccc transparent;
    scrollbar-width: thin;
  }
}
</style>
