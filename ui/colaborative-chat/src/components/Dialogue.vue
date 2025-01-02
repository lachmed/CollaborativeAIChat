<script setup>
import { marked } from "marked";
import { computed } from "vue";

const props = defineProps(["message", "owner", "ownerId"]);

var message = marked(props.message);
var owner = props.owner;
var ownerId = props.ownerId;

const ownerType = computed(() => {
  if (owner == "Client") {
    return 0;
  } else if (owner == "AI") {
    return 1;
  } else if (owner == "Self") {
    return 2;
  }
});
</script>

<template>
  <div class="dial">
    <div class="question" v-if="ownerType == 2">
      <div>
        <img src="../assets/avatar_self.png" class="avatar" />
        <h6>{{ ownerId }}</h6>
      </div>
      <span class="text" v-html="message"></span>
    </div>

    <div class="answer" v-if="ownerType == 1">
      <div>
        <img src="../assets/avatar_ai.png" class="avatar" />
        <h6>{{ ownerId }}</h6>
      </div>
      <span class="text" v-html="message"></span>
    </div>

    <div class="answer" v-if="ownerType == 0">
      <div>
        <img src="../assets/avatar_client.png" class="avatar" />
        <h6>{{ ownerId }}</h6>
      </div>
      <span class="text" v-html="message"></span>
    </div>
  </div>
</template>

<style scoped>
.dial {
  padding: 0.2rem 0;
  border: 1px solid whitesmoke;
  margin-bottom: 1rem;
  border-radius: 1rem;
  overflow-wrap: break-word;
}

.avatar {
  max-width: 4rem;
  max-height: 4rem;
  border-radius: 25%;
}
.text {
  margin-left: 1rem;
  color: white;
  /* border: 1px solid red; */
}

.question,
.answer {
  display: flex;
  flex-direction: column;
  margin: 1rem 1rem 1rem 1rem;
  justify-content: baseline;
}

.question div,
.answer div {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 0.5rem;
}
</style>
