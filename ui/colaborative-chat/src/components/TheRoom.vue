<script setup>
import { ref, onMounted, useTemplateRef, onUpdated } from "vue";
import Dialogue from "@/components/Dialogue.vue";

const props = defineProps(["roomId", "apiKey"]);
var messages = ref([
  // {
  //   message: "This is a test1 This is a test1 This is a test1",
  //   owner: "Client",
  // },
  // {
  //   message: "This is a test2",
  //   owner: "Client",
  // },
  // {
  //   message:
  //     "This is a test3 This is a test3This is a test3 This is a test3 This is a test3 This is a test3 This is a test3 This is a test3\
  //     This is a test3 This is a test3This is a test3 This is a test3 This is a test3 This is a test3 This is a test3 This is a test3",
  //   owner: "Self",
  // },
  // {
  //   message: "This is a test4",
  //   owner: "AI",
  // },
]);

// var messaging = computed(() => {
//   if (result.value != "") messages.value.push(result.value);
//   return messages;
// });

const text = ref("");
const connection = ref(null);
const p = ref("");
const result = ref("");

const loading = ref(false);

const id = ref("");

const dialogueRef = useTemplateRef("dialogue");
const containerA = useTemplateRef("containerA");
const bottomOfPanelRef = useTemplateRef("bottomOfPanelRef");

// console.log(
//   'localStorage.getItem("clientId"):',
//   localStorage.getItem("clientId")
// );

// console.log("id after check: ", id.value);

function manageConn() {
  console.log("Starting connection to WebSocket Server");
  connection.value = new WebSocket("ws://localhost:5000/chat");

  connection.value.onmessage = function (event) {
    // console.log(event);
    // console.log("ONMESSAGE___");

    result.value = JSON.parse(event.data);

    // console.log("BeforeUpdateMessaging_____");

    if (result.value.owner == "Client") {
      messages.value.push({
        message: result.value.client_message,
        owner: "Client",
        ownerId: result.value.ownerId,
        key: messages.value.length + 1,
      });
    } else if (result.value.owner == "AI") {
      loading.value = false;
      messages.value.push({
        message: result.value.client_message,
        owner: "Client",
        ownerId: result.value.clientOwnerId,
        key: messages.value.length + 1,
      });
      messages.value.push({
        message: result.value.ai_model_message,
        owner: "AI",
        ownerId: result.value.ownerId,
        key: messages.value.length + 1,
      });
    }

    // console.log("AfterUpdateMessaging_____");
    updateScroll();
  };

  connection.value.onopen = function (event) {
    id.value = "Client_" + Date.now();
    localStorage.setItem("clientId", id.value);

    // console.log(event);
    console.log("Successfully connected to the echo websocket server...");

    event.target.send(
      JSON.stringify({
        roomId: props.roomId,
        clientId: id.value,
        msg: "____BEGIN____",
        time: Date.now(),
        for: 0,
        apiKey: props.apiKey,
      })
    );
  };

  connection.value.onclose = function (event) {
    // console.log("Connection to websocket was closed");
    localStorage.removeItem("clientId");
  };

  connection.value.onerror = function (event) {
    console.log("there was an error connecting to the web socket");

    console.log(event);
  };
}

function sendMessage(reciepient) {
  var msg = {
    roomId: props.roomId,
    clientId: id.value,
    msg: text.value,
    time: Date.now(),
    for: reciepient,
  };

  if (reciepient != 1)
    messages.value.push({
      message: text.value,
      owner: "Self",
      ownerId: id.value,
      key: messages.value.length + 1,
    });

  if (reciepient == 1) {
    loading.value = true;
  }

  text.value = "";

  // containerA.value.scroll(0, 20000 * (messages.value.length + 1));
  updateScroll();
  connection.value.send(JSON.stringify(msg));
}

onMounted(() => {
  manageConn();
});

function copyLinkToClipBoard() {
  navigator.clipboard.writeText(window.location);
  alert("Copied To ClipBoard!");
}

function updateScroll() {
  // var aa = dialogueRef.value.getElementsByClassName("dial");
  // aa[aa.length - 1].scrollIntoView({
  //   behavior: "smooth",
  //   block: "end",
  //   inline: "nearest",
  // });
  console.log("HERE !!!");

  bottomOfPanelRef.value.scrollIntoView({
    behavior: "smooth",
    block: "center",
    inline: "nearest",
  });
}
</script>

<template>
  <div class="theroom">
    <div class="header">
      <h3>Room Id: {{ roomId }}</h3>
      <button class="btn btn-success" @click="copyLinkToClipBoard()">
        Invite
      </button>
    </div>

    <div class="container" id="containerA" ref="containerA">
      <div class="container" id="dialogue" ref="dialogue">
        <Dialogue
          v-for="dial in messages"
          :owner="dial['owner']"
          :message="dial['message']"
          :ownerId="dial['ownerId']"
          :key="dial['key']"
        />
        <Dialogue v-if="loading" owner="AI" message="..." ownerId="Google AI" />
        <div style="margin-top: 1rem" ref="bottomOfPanelRef"></div>
      </div>
    </div>

    <div class="controls">
      <input type="text" v-model="text" />
      <div class="btns">
        <button class="btn btn-success" @click="sendMessage(0)">
          Address Clients
        </button>
        <button class="btn btn-success" @click="sendMessage(1)">
          Address AI
        </button>
      </div>
    </div>

    <!--<p :ref="p">{{ result }}</p>-->
  </div>
</template>

<style lang="css" scoped>
.theroom {
  /* border: 1px solid yellow; */
  min-height: 100vh;
}

.header {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding: 1rem;
}

#containerA {
  min-height: 40rem;
  max-height: 40rem;
  overflow-y: scroll;
  scrollbar-color: #ccc transparent;
  scrollbar-width: thin;
  padding-bottom: 5rem;
}

.controls {
  display: grid;
  grid-template-columns: 1fr;
}
.controls input {
  width: 95%;
  margin-left: auto;
  margin-right: auto;
  height: 3rem;
  border-radius: 0.5rem;
}
.controls .btns {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.controls .btns button {
  margin: 0.5rem 1rem;
}
</style>
