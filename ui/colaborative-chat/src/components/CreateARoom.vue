<script setup>
import { RouterLink } from "vue-router";
import { ref, computed } from "vue";
import { useApiKeyStore } from "@/stores/api_key.js";

const name = ref("");
const Key = ref("");
const link = computed(() => {
  return "/room/" + name.value;
});

function sendAPIKey() {
  var apiKey = useApiKeyStore();
  apiKey.setApiKey(Key.value);
}

const full = computed(() => {
  if (name.value != "" && Key.value != "") {
    return true;
  } else return false;
});
</script>

<template>
  <div class="container">
    <label
      ><span>Room name</span><br />
      <input type="text" v-model="name" />
    </label>

    <label>
      <span>Google Ai API</span>
      <br />
      <input type="text" v-model="Key" />
    </label>

    <RouterLink
      v-if="full"
      @click="sendAPIKey()"
      class="btnStart btn btn-success"
      v-bind:to="link"
    >
      Start
    </RouterLink>
    <p class="btn btn-success" v-else>fill in the room name and api key</p>
  </div>

  <div class="tuto">
    <h3>Follow these easy steps to get your API key</h3>
    <iframe
      loading="lazy"
      class="tutoFrame"
      src="https://www.canva.com/design/DAGa9-imgzE/3RMrm6N7pH5O7MBMVV3Gvw/view?embed"
      allowfullscreen="allowfullscreen"
      allow="fullscreen"
    >
    </iframe>
    <a
      href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGa9-imgzE&#x2F;3RMrm6N7pH5O7MBMVV3Gvw&#x2F;view?utm_content=DAGa9-imgzE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link"
      target="_blank"
      rel="noopener"
    ></a>
  </div>
</template>

<style scoped>
div {
  height: 50vh;
  margin-top: 5rem;
  margin-bottom: 5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.btnStart {
  width: 20rem;
}

span {
  font-size: 2rem;
}

input {
  width: 30rem;
  border-radius: 1rem;
  height: 3rem;
  border: none;
}

.tuto {
  margin-top: 0;
  min-height: fit-content;
}

.tutoFrame {
  position: relative;
  width: 80%;
  height: 600px;
  max-height: 80vh;
  border: none;
  border-radius: 8px;
  padding: 0;
  margin: 0;
  overflow: hidden;
}

p {
  margin-top: 1rem;
}
</style>
