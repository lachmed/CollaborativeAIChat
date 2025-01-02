<script setup>
import { useRoute } from "vue-router";
import Room from "../components/TheRoom.vue";
import { useApiKeyStore } from "@/stores/api_key.js";

const route = useRoute();

const apiKey = useApiKeyStore();
const roomName = route.params.name;
</script>

<template>
  <Room v-bind:roomId="roomName" v-bind:apiKey="apiKey" />
</template>

<style scoped></style>
