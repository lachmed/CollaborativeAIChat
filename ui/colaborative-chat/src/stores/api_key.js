import { ref } from "vue";
import { defineStore } from "pinia";

export const useApiKeyStore = defineStore("api_key", () => {
  var apiKey = ref("");

  function setApiKey(key) {
    apiKey.value = key;
  }

  return { apiKey, setApiKey };
});
